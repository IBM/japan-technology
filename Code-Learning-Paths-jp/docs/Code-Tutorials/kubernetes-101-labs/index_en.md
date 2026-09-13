---
also_found_in:
- learningpaths/get-started-containers/
authors: ''
check_date: '2021-06-30'
completed_date: '2018-12-09'
components:
- docker
- kubernetes
draft: false
excerpt: Learn how to build a Docker image and deploy it to a Kubernetes cluster,
  control application deployments, add AI services, and secure and monitor your cluster.
last_updated: '2021-01-16'
meta_description: Learn how to build a Docker image and deploy it to a Kubernetes
  cluster, control application deployments, add AI services, and secure and monitor
  your cluster.
meta_keywords: kubernetes 101, kubernetes labs, kubernetes training, kubernetes exercises
meta_title: 'Kubernetes 101: Labs designed to help you understand Kubernetes'
primary_tag: containers
related_content:
- slug: kubernetes-learning-path
  type: series
- slug: get-started-containers
  type: learningpaths
subtitle: How to build a Docker container image and deploy an app to a Kubernetes
  cluster
time_to_read: 3 hours
title: 'Kubernetes 101: Labs designed to help you understand Kubernetes'
---

Do you want to learn about Kubernetes, but are completely overwhelmed with the amount of articles and blog posts about the topic? You've heard about it and seen it in others' code, but what does it actually do? How does it help your containers? Is Kubernetes a type of container? This set of labs clears up confusion and helps you get comfortable with Kubernetes. They are designed with you, the developer, in mind.

When you complete the labs, you gain the following:

* A full understanding of Kubernetes core concepts
* Knowledge on how to build a Docker image and deploy an application on Kubernetes in the IBM Cloud Kubernetes Service
* Controlled application deployments, while minimizing your time with infrastructure management
* Skills to add AI services to extend your app
* More secure clusters and apps, as well as an understanding of how to monitor them

Completing all the exercises in these labs takes approximately 3 hours. Try a few exercises to get started.

## Prerequisites

These labs uses a free Kubernetes cluster with either a Pay-As-You-Go or a Subscription account for IBM Cloud. To get started, register for an <a href="https://cloud.ibm.com/registration/?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg" target="_blank" rel="noopener noreferrer">IBM Cloud account</a>. Then, follow <a href="https://ibm.github.io/workshop-setup/PAYASYOUGO/" target="_blank" rel="noopener noreferrer">this guide</a> to upgrade to a Pay-As-You-Go account.

## Labs

* <a href="https://ibm.github.io/kube101/Lab0/" target="_blank" rel="noopener noreferrer">__Lab 0. Access a Kubernetes cluster__</a>  
For the hands-on labs, you need a Kubernetes cluster. This lab explains options to create a cluster, including the IBM Cloud Kubernetes Service, a hosted trial environment, and configuring Kubernetes to run on your local workstation. It also provides a walkthrough for installing IBM Cloud command-line tools and the Kubernetes CLI, and downloading the sample Guestbook application for the labs.

* <a href="https://ibm.github.io/kube101/Lab1/" target="_blank" rel="noopener noreferrer">__Lab 1. Deploy your first application__</a>  
Deploy a simple Guestbook application written in Go to a Kubernetes cluster hosted within the IBM Cloud Kubernetes Service.

* <a href="https://ibm.github.io/kube101/Lab2/" target="_blank" rel="noopener noreferrer">__Lab 2. Scale and update deployments__</a>  
Learn how to update the number of instances in a deployment and how to safely roll out an update of your application on Kubernetes.

* <a href="https://ibm.github.io/kube101/Lab3/" target="_blank" rel="noopener noreferrer">__Lab 3. Build multitier applications__</a>  
Learn how to deploy the same Guestbook application with configuration files instead of the `kubectl` command-line helper functions. The configuration file mechanism allows you to have more fine-grained control over all of resources created within the Kubernetes cluster.