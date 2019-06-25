Title: Evaluating API Gateways
Date: 2019-06-25
Category: devops 
Tags: kubernetes
Status: draft


Lately I've been tasked with evaluating proxies and ingress controllers to act
as an API gateway into our environment. There are numerous reasons why one might
want to put a proxy in front of a web application. Perhaps you are working with
a third-party app that doesn't provide the authentication mechanisms you
require, or whose security stance is not as rigorous as yours. Or you may want
logging and rate-limiting to be handled uniformly across your catalog.

There are many such applications available, both open source and enterprise -
often both. During my evaluation, I have a number of criteria that I want an
application to meet.

1. It must be Kubernetes native. This means it must be deployable as a
   containerized application, and configurable in Kubernetes via yaml.
   Configuration-as-code is a virtue.
1. It must be able to proxy to applications both within and without Kubernetes.
   While we strive to run everything in containers, not everything can... yet.
   The proxy we choose must be able to service both.
1. It must be extensible. Whether via an existing corpus of plugins or a plugin
   API that is pleasant to use, there are business needs that will certainly
   require some glue code to implement. Which leads us to...
1. Developer ergonomics matter. If the API sucks, the application sucks, that
   simple. If I can't get developers to work on my project, it doesn't really
   matter what it's built on.

For the purposes of my evaluation, we reduced our selection of proxies to three:

1. [Ingress-NGINX](https://kubernetes.github.io/ingress-nginx/) - A basic but
   powerful, open source ingress controller. This is the controller that many
   teams start with, and there is plenty of existing skill on our team to
   support it.
1. [Kong](https://konghq.com) - Available as both open source and enterprise...
1. [Ambassador](https://getambassador.com)
