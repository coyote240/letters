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
like mine. However, I'm not as enamoured of SaaS as much of the industry seems
to be, and these services share some of Jenkins' drawbacks while introducing new
ones.

For my personal projects, as well as current professional projects, it has been
important to me to explore CI/CD alternatives that can be hosted on my own
Kubernetes clusters, and that are discrete and light-weight such that they can
be managed and understood by my team.

One such project is [Tekton](https://tekton.dev). Tekton is e project of the [CD
Foundation](https://cd.foundation/), and is a true Cloud Native CI/CD
application. Tektop presents a collection of useful primitives such as Tasks and
Pipelines, to be combined as needed. While Tekton is the foundation of larger
projects like Jenkins-X and Google Cloud Build, I wanted to give Tekton a try on
its own. Today I will be using Tekton to replace the otherwise half-done and
rickety process that deploys Letters. I also have in mind a Part II where I use
Tekton as the runner for a stunt hack - managing a pipeline of CTF exploits.

## Requirements

install tekton pipeline
create namespace
install catalog tasks
create pipeline
create pipelinerun
