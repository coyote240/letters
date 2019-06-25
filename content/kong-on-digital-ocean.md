Title: Installing Kong w/ Ingress on Kubernetes in DigitalOcean
Date: 2019-06-25
Category: devops 
Tags: kubernetes, digitalocean, kong


Lately I've been tasked with evaluating API gateway platforms for our
organization. Among the proxies I'm looking at is [Kong](https://konghq.com),
and to get a better look at it as an option I'm going to be installing it, as
well as it's ingress controller component, into a new kubernetes cluster on my
own [DigitalOcean](https://digitalocean.com) account.

While we don't host our applications or clusters on DigitalOcean, I do use it
for my own projects and research, for its ease of use and relatively low cost.
For that reason, I'll be setting up Kong on DigitalOcean for the purpose of
this article.

## Get right with DigitalOcean

Before we get started, let's get ourselves setup with DigitalOcean's
command-line tool, `doctl`. `doctl` is pretty powerful, and we'll be able to use
it for a number of tasks, but today we'll just get setup with an API key and to
manage kubernetes config files automatically. You may use your package manager
of choice to install `doctl`. As I'm on a mac:

```shell
$ brew install doctl
```

For `doctl` to work with your DigitalOcean account, it will need a Personal
Access Token, which you can generate by [following these
instructions](https://www.digitalocean.com/docs/api/create-personal-access-token/).
With your token in hand, initialize your `doctl` configuration like so:

```shell
$ doctl auth init

 DigitalOcean access token: <your token here>
 Validating token: OK 
```

This step will create the files and directories needed to store your
credentials. On my mac, these were created at `~/.config/doctl/config.yaml`. You
should now be set up to use `doctl` to manage your DigitalOcean account.

## Create a Cluster

Since I'm creating this cluster for demo purposes only, I'm going to go pretty
light on the resources. Here we'll create a cluster with a single, very small
worker node in San Francisco.

```shell
$ doctl k8s cluster create kong-demo \
    --region sfo2 \
    --count 1 \
    --size s-1vcpu-2gb
```

After several minutes, `doctl` will report that the cluster has been created and
is running, it will have added the cluster credentials to my kubernetes config
file, and it will have set my current context to the newly created cluster. It
will also display a table showing you the id, name, region etc. of the cluster
you just created. You can see this info again any time by typing:

```shell
$ doctl k8s cluster list
```

As I said before, this is a very small cluster. It would not be adequate for
running production loads, but it is good enough for casual websites or, today,
to run a demo. With the cluster created, we still have a bit more setup to do
before we can install Kong.

## Install helm and tiller

The shop where I work is all in on Kubernetes and Helm. If there's a helm chart
to be had, you'd better believe we're going to want to use it. Moreso, if you
can deploy your own project using a helm chart all the better. Configuration as
code is key.

The installation instructions for Kong provide guidance for both `kubectl` and
`helm` deployments. We're going to use the `helm` deployment, so let's get our
tooling set up for that. As we're working on a new cluster, we'll need to
install both `helm` and `tiller`, the server-side component.

Again, since I'm on a mac, I'll install `helm` using homebrew:

```shell
$ brew install helm
```

We can initialize helm and install tiller into our cluster with one command, so
let's first make sure we're pointed to the correct cluster.

```shell
$ kubectl config current-context

do-sfo2-kong-demo
```

Great, that's the cluster we just created. Now we can proceed with a default
installation.

First we'll create a tiller service account and bind it to the cluster-admin
role:

```shell
$ kubectl -n kube-system create serviceaccount tiller

serviceaccount/tiller created

$ kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller

clusterrolebinding.rbac.authorization.k8s.io/tiller created
```

Then we can initialize helm, installing tiller.  We'll set the `--history-max`
flag as recommended by helm's installation instrucions.

```shell
$ helm init --service-account tiller --history-max 200
```

For me, that only took a couple of seconds. I can verify the installation by
typing `helm version` which, much like `kubectl version` will show you version
info for both the client and the server.

## Install Kong Ingress Controller

Ok, now on to the main event!

This demo is for a product evaluation and there are a few criteria that have to
be met. First, we must be able to commit our configurations to source control.
As I said earlier, configuration-as-code is key! This means that Kong's typical
web API configuration does not meet this criteria. Fortunately, Kong has
introduced a declarative interface, allowing us to configure Kong via yaml. This
feature _does_ meet our criteria and allows us to proceed.

Second, we want our applications, where possible, to be Kubernetes native. While
I cannot say that Kong is k8s native, it's [ingress controller
project](https://github.com/Kong/kubernetes-ingress-controller) provides what
looks like a good k8s/yaml interface to most if not all of Kong's functionality.
While I need a proxy, primarily, to be able to configure it as an ingress and
services is very attractive as it draws from our in-house skillset.

To enable the declarative interface as well as the ingress controller, we'll
call `helm` with a couple of flags set:

```shell
$ helm install stable/kong --set ingressController.enabled=true \
                           --set postgresql.enabled=false \
                           --set env.database=off
```

This outputs quite a bit of information about the CRDs, services, etc created. I
can confirm by checking on a couple of resource types myself:

```shell
$ kubectl get pods,deployments,services

NAME                                  READY   STATUS    RESTARTS   AGE
pod/kong-demo-kong-5bf8d9cfdf-z9gt7   2/2     Running   2          10m

NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.extensions/kong-demo-kong   1/1     1            1           10m

NAME                           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/kong-demo-kong-admin   NodePort    10.245.152.233   <none>        8444:32230/TCP               10m
service/kong-demo-kong-proxy   NodePort    10.245.81.54     <none>        80:31695/TCP,443:31092/TCP   10m
service/kubernetes             ClusterIP   10.245.0.1       <none>        443/TCP                      149m
```

## What's next?

Well, this gets me far enough to start experimenting. Next up I'll want to see
how Kong handles proxying to applications running both inside and outside
Kubernetes. Also, and this is very important to me, what is the Kong plugin
landscape like? How easy is it to develop plugins? How do the available
annotations compare to those provided by Ingress-NGINX?

So many questions!

Ĝis la revido, kaj feliĉa kodumado!
