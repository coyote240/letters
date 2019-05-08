# Securing Kubeless Functions with Auth0 and JWT

Of late I have had a professional interest in Functions as a Service. While I
was slow to jump on the bandwagon, there has been an increasing need for one-off
web capabilities on the teams I work with...

Right away the need to secure our web hooks became apparent...

* Kubernetes
* Kubeless
* Ingress-Nginx
* Auth0

## Install Kubeless

## Define a Function

This project will require two functions to demonstrate:

1. A function to be protected
1. A function to perform the auth-url validation

Create a namespace for the project

* write
* deploy
  * https://kubeless.io/docs/advanced-function-deployment/
* trigger
* modify trigger
  * nginx.ingress.kubernetes.io/auth-url: https://auth-service...

## Configure Auth0

## Configure External Auth Service
