Title: Fixing My Broken Scuttlebutt Pub Server in Kubernetes
Date: 2019-09-02
Category: devops
Tags: ssb, p2p, kubernetes


## Poor planning and neglect

It wasn't that I wasn't warned, but I chose a too-small data volume for my
[scuttlebutt](https://www.scuttlebutt.nz) pub server and I let it fill up, thus
crashing my server (perhaps we can talk about that as a stability issue in ssb
later). As I'm frequently disenchanted with Scuttlebutt (I don't really have
any friends there) I've left the broken deployment sitting in my
kubernetes cluster for too long unaddressed, so it's time to either fix it
or tear it down. Let's try to fix it.

## Goals and intentions

I'm writing this post as I attempt to revive my broken pub. For starters, to
halt the endless `CrashLoopBackoff`, I've opted to delete my server's
deployment, leaving the persistent volume claim in place. One of the best things
about kubernetes, and to be honest one of the bigger mind-benders for me, is how
casual I can be about bringing up and tearing down resources. As long as I'm not
dealing with persistence (in this case my persistent volume), it's safe to tear
down a deployment knowing I can bring it back up into a prescribed state with a
single command. So it is understood upfront, my goal is not to resize this
volume - that is not currently supported by DigitalOcean - but to rescue the
necessary files from the existing volume that make up the identity of the pub
server.  As I understand it, this means the private key and the gossip.json
files.

## Step 1. - Deploy the "rescue" image

My plan as of this second is to define a rescue deployment, a simple container
where I can mount the volume, exec in and pull the files down to my local
machine for redeployment. I've decided to go with a vanilla Debian Buster image
and to name it `ssb-rescue`. This I'm putting in a kubernetes deployment that
looks like this:

```yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  name: ssb-rescue-deployment
  namespace: scuttlebutt
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ssb-rescue
  template:
    metadata:
      labels:
        app: ssb-rescue
    spec:
      containers:
        - name: ssb-rescue
          image: debian:buster
          imagePullPolicy: Always
          livenessProbe:
            exec:
              command:
                - "sh"
                - "true"
            initialDelaySeconds: 180
            periodSeconds: 300
```

My intention here is to deploy a single Debian container, deployed to the same
namespace as my scuttlebutt deployment, with a liveness probe of a periodic call
to `whoami` to keep the container from exiting. I've put this in a file called
`rescue.yaml` and, as I just made this up, let's give it a try:

```shell
$ kubectl apply -f rescue.yaml
deployment.apps/ssb-rescue-deployment created
$ kubectl get pods -n scuttlebutt
NAME                                     READY   STATUS             RESTARTS   AGE
ssb-rescue-deployment-68775dc5c4-wlslc   0/1     CrashLoopBackOff   1          13s
```

Well, crap. That didn't work at all. I reached out to a more experienced
friend who suggested I use a command to keep the container running. So I aded
this to my container definition:

```yaml
command: ["/bin/bash", "-c", "--"]
args: ["while true; do sleep 30; done;"]
```

Now, the container starts and runs just fine...

```shell
$ kubectl apply -f rescue.yaml
deployment.apps/ssb-rescue-deployment created
$ kubectl get pods -n scuttlebutt
NAME                                    READY   STATUS    RESTARTS   AGE
ssb-rescue-deployment-dcf487bcf-wkqxj   1/1     Running   0          3m54s
```

Perfect. Now I want to mount the old pub data volume to this container by adding
a `volumes` section to my deployment, and a `volumeMounts` section to my
container specification.

First I'll define the volume, using the name of the existing
PersistentVolumeClaim:

```yaml
volumes:
  - name: ssb-pub-volume
    persistentVolumeClaim:
      claimName: ssb-pvc
```

And then I'll add a volumeMount to the container spec:

```yaml
volumeMounts:
  - name: ssb-pub-volume
    mountPath: "/data/ssb-old"
```

Now I can `exec` into the pod and see the contents of the old volume, including the
files I want to move to the new volume.

```shell
$ kubectl exec -it <your pod name> -n scuttlebutt /bin/bash
root@pod:/# ls /data/ssb-old
blobs	    config  ebt    gossip.json	 lost+found	node_modules  secret
blobs_push  db	    flume  gossip.json~  manifest.json	oooo
```

Perfect! Now I'm ready to create a new volume with a (much) larger capacity onto
which I can move the pertinent files.

## Step 2. - Create and mount a new volume

So far, I'm feeling pretty good about this. Like I said, I'm kinda making this
up as I go along, and I'm thus far chuffed that it's working out. Since this is
all done using kubernetes manifests, all of our work is saved in files that can
be committed to source control. Since I already had my pub server's manifests in
[source control](https://github.com/coyote240/ssb-pub), this seems like a good
time to commit.

Now that we have a usable Debian deployed, I have an easy way to copy files from
the old volume to the new volume. Next we need to create that new volume. My
previous volume was only 5GB, so I've decided to multiply that by 10 to 50GB,
which at current pricing on DigitalOcean will be $5 a month. Not bad, and
hopefully I'll learn something about pruning scuttlebutt databases by the time I
fill this one up.

I've already been down this road once before, so the basics of creating the
volume in kubernetes on DigitalOcean is solved. I do just want to update the
volume storage size, so I'll copy the old definition and make that one change.
I'll do this in a file called `volume.yaml`.

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: ssb-pvc-extended
  namespace: scuttlebutt
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: do-block-storage
```

I can apply this file, and that is all that is neded to create the new storage
volume.

```shell
$ kubectl apply -f volume.yaml
persistentvolumeclaim/ssb-pvc-extended created
$ kubectl get pvc -n scuttlebutt
NAME               STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       AGE
ssb-pvc            Bound    pvc-bdc11612-a0ba-11e9-bb99-de33b94a578b   5Gi        RWO            do-block-storage   57d
ssb-pvc-extended   Bound    pvc-94bca086-cde2-11e9-a30b-4671334a8dc3   50Gi       RWO            do-block-storage   4s
```

Here you can see the older, smaller volume as well as the newer, larger volume.
This I will add to my deployment just as I did the older volume, mounting the
volume at `/data/ssb-new`. Just like before I define the volume:

```yaml
volumes:
  - name: ssb-pub-volume-new
    persistentVolumeClaim:
      claimName: ssb-pvc-extended
```

And then I add a volumeMount to the container spec:

```yaml
volumeMounts:
  - name: ssb-pub-volume-new
    mountPath: "/data/ssb-new"
```

This should be all it takes to mount the newly created volume. I'll update my
cluster by once again applying my manifest, then we should see the new, empty
volume in place.

```shell
$ kubectl apply -f rescue.yaml
deployment.apps/ssb-rescue-deployment configured
$ kubectl get pods -n scuttlebutt
NAME                                     READY   STATUS    RESTARTS   AGE
ssb-rescue-deployment-7bcfd9c466-vk57x   1/1     Running   0          91s
$ kubectl exec -it ssb-rescue-deployment-7bcfd9c466-vk57x -n scuttlebutt /bin/bash
root@pub: /# ls /data
ssb-new ssb-old
```

## Step 3. - Copy files!

After all of that work, this hardly seems like a step at all! Now that both
volumes are mounted on our handy rescue server, it's just a matter of copying
relevant files from one volume to the other.

```shell
$ cp /data/ssb-old/secret /data/ssb-new/
$ cp /data/ssb-old/gossip.json /data/ssb-new/
```

Whew! Ok, now...

## Step 4. - Bring up the pub server

Ok, so before I redeploy my pub server, I'm going to need to take down my rescue
server deployment. This is easy enough by issueing a delete command against the
deployment.

```shell
$ kubectl delete deployment ssb-rescue-deployment -n scuttlebutt
deployment.extensions "ssb-rescue-deployment" deleted
```

To be clear, I'm going to leave the old volume in place until I'm confident that
the new volume is working and that my pub server is back up and humming along.
This way if my assumptions regarding exactly which files need to be moved to the
new volume are incorrect, I can try again.

To use the new volume, I only need to update my existing pub server deployment
manifest. In my case, this only means pointing my persistentVolumeClaim to the
new claim.

```yaml
volumes:
  - name: ssb-pub-volume
    persistentVolumeClaim:
      claimName: ssb-pvc-extended
```

And now the spooky part, let's try bringing the pub server back up.

```shell
$ kubectl apply -f deployment.yaml
namespace/scuttlebutt unchanged
service/ssb-pub unchanged
persistentvolumeclaim/ssb-pvc unchanged
configmap/ssb-config unchanged
deployment.apps/ssb-pub-deployment created
```

As you can see, the bulk of my configuration hasn't changed. At the beginning of
this exercise I deleted my deployment which brought down the server pod, but the
remaining elements remained in place. I can now look and see that my pod is
running.

```shell
$ kubectl get pods -n scuttlebutt
NAME                                 READY   STATUS    RESTARTS   AGE
ssb-pub-deployment-f7965fbff-tn572   1/1     Running   0          77s
```

Right away I see my pod is back up and running, and [Patchwork](), my
scuttlebutt client, is reporting the same! After a few minutes waiting, I can
see my pub is rebuilding its database and is beginning to relay messages. If I
understand the protocol correctly, the pub is going to take some time to rebuild
its database by requesting messages from me and its one other follower.

## Success!

I look forward to seeing my pub settle into itself over the next few hours, but
overall I feel pretty good about this exercise. I intend to leave the old volume
in place for a few days just to make sure I didn't miss anything before deleting
it. If I learn anything new in the process, I'll be sure to share it here.

Ĝis la revido, kaj feliĉa kodumado!
