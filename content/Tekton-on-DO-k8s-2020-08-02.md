Title: Tekton CI/CD on DigitalOcean Kubernetes
Date: 2020-10-04
Category: devops
Tags: kubernetes, tekton, digitalocean


## Motivation

These days, I do much more operations, architecture and security than I do
feature development. This means I spend most of my days working with Kubernetes,
some service mesh, and as much automation as possible (it's all possible). While
I generally use AWS at work, I like to run my personal projects on
[DigitalOcean](https://digitalocean.com) or [Linode](https://linode.com), and I
have similar expectations for my personal projects as I have for my professional
projects: save me time and effort, automate all the things. Naturally, the ideal
and the actual are seldom the same. I always have room for improvement.

A critical component of modern web development is the implementation of
Continuous Integration (CI) and Continuous Deployment (CD). While I have in the
past had to manually deploy web applications, often on the weekend or other off
hours, this is no longer considered acceptable, and I agree. Manual deployments
are expensive and error prone. Deployments present an excellent opportunity for
automation. In recent years, the companies I've worked for have relied on
[Jenkins](https://www.jenkins.io/) for automated deployment. This is fine,
except for a few short-comings:

1. Every Jenkins installation is built to site. This means that from company to
   company, Jenkins setups seldom resemble one another.
1. Jenkins runs out of band. While your application may be Kubernetes-native,
   Jenkins most assuredly is not and requires a different architecture than the
   rest of your stack.
1. Jenkins is bossy. It requires god-like privileges to run in your environment,
   making it a prime candidate for attack and exploitation.

I have worked some with SaaS alternatives such as [Travis
CI](https://travis-ci.org/) and [CircleCI](https://circleci.com/), and these
may more than adequately suit your needs, particularly for small, personal sites
like mine. However, I'm not as enamored of SaaS as much of the industry seems
to be, and these services share some of Jenkins' drawbacks while introducing new
ones.

For my personal projects, as well as current professional projects, it has been
important to me to explore CI/CD alternatives that can be hosted on my own
Kubernetes clusters, and that are discrete and light-weight such that they can
be managed and understood by my team.

One such project is [Tekton](https://tekton.dev). Tekton is e project of the [CD
Foundation](https://cd.foundation/), and is a true Cloud Native CI/CD
application. Tekton presents a collection of useful primitives such as Tasks and
Pipelines, to be combined as needed. While Tekton is the foundation of larger
projects like Jenkins-X and Google Cloud Build, I wanted to give Tekton a try on
its own. Today I will be using Tekton to replace the otherwise half-done and
rickety process that deploys Letters. I also have in mind a Part II where I use
Tekton as the runner for a stunt hack - managing a pipeline of CTF exploits.

In order to perform the tasks in this article, you will need to have access to a
Kubernetes cluster. I've noted DigitalOcean and Linode, but GKS or EKS will
apply equally. Tekton is a Kubernetes Native application, so your cloud provider
should be irrelevant. You should also have the version of `kubectl` appropriate
to your cluster and a basic understanding of Kubernetes.

## Install Tekton Pipelines

There are excellent instructions in [Tekton's
documentation](https://tekton.dev/docs/getting-started/) on how to install
Tekton, so I'll consider that a prerequisite to this exercise. I consider the
installation of the Tekton dashboard and the `tkn` command line tool to be
optional. While the dashboard is spare compared to Jenkins or Travis, I do
believe it adds value. As for `tkn`, I'm just tired of installing everybody's
cli tools, and I don't appreciate the trend. Everything we do today can be done
using only `kubectl`.

## Set the stage

I wrote this article while setting up a new Tekton build pipeline for this site,
[Letters](https://letters.vexingworkshop.com). For this project I have chosen to
create a new namespace where I will keep all of my build related manifests for
this site. Here I define my manifest in a file called `namespace.yaml` and apply
it to my cluster.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: letters-ops
```

```shell
kubectl apply -f namespace.yaml
```

As my pipeline will have to publish the built Docker image to Docker Hub, we
will require authentication. I have chosen to use basic authentication, and for
this Tekton requires a secret and a service account that has access to this
secret. Be sure not to commit your secret manifest to your git repository!

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: basic-user-pass
  annotations:
    tekton.dev/docker-0: https://index.docker.io/v1/
type: kubernetes.io/basic-auth
stringData:
  username: redacted
  password: redacted
```

```shell
kubectl apply -f secret.yaml -n letters-ops
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-bot
secrets:
  - name: basic-user-pass
```

```shell
kubectl apply -f service-account.yaml -n letters-ops
```

With these resources in place, my Tekton pipeline will be able to authenticate
to Docker Hub and publish my image.

## Install catalog tasks

Tekton pipelines are at their most basic made up of a series of Tasks. Each task
may be made up of multiple steps that are run in order, while tasks are run in
order within a pipeline. Each task spawns a Kubernetes pod, with each step being
run within its own container.

While it is easy to create our own tasks for any purpose we can imagine, there
are many common tasks already assembled in the [Tekton Catalog on
Github](https://github.com/tektoncd/catalog). As Letters is simply built using a
static site generator, and already compiled in a multi-stage build container, I
have chosen not to write any custom tasks for now, but to use two that I've
found in the catalog.

Before we write our pipeline, we'll go ahead and clone the Tekton Catalog repo
and install tasks.

```shell
git clone https://github.com/tektoncd/catalog tekton-catalog
cd tekton-catalog
kubectl apply -f task/git-clone/0.2/git-clone.yaml -n letters-ops
kubectl apply -f task/kaniko/0.1/kaniko.yaml -n letters-ops
```

Note that I've chosen to install these tasks into my `letters-ops` namespace.
Now that we have all the pieces in place, let's write our pipeline.

## Build the pipeline

create pipeline
create pipelinerun
