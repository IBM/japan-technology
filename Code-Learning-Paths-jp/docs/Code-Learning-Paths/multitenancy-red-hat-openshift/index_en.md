---
authors: ''
check_date: '2022-08-30'
completed_date: '2021-08-31'
components:
- openshift
- kubernetes
display_in_listing: true
draft: false
excerpt: This learning path is designed for anyone interested in quickly setting up
  a multitenant environment with Red Hat OpenShift.
meta_description: This learning path is designed for anyone interested in quickly
  setting up a multitenant environment with Red Hat OpenShift.
meta_keywords: multitenancy OpenShift, multitenant environments, RBAC, network isolation,
  resource isolation
primary_tag: containers
related_content:
- slug: build-images-cloud-native-toolkit
  type: learningpaths
- slug: secure-context-constraints-openshift
  type: learningpaths
subtitle: Learn how to set up a mulitenant environment on Red Hat OpenShift
tags:
- security
- devops
title: Get started with multitenancy on OpenShift
---

This learning path is designed for anyone interested in quickly setting up a multitenant environment with Red Hat OpenShift. This learning path consists of introductory article explaining what multitenancy is, its benefits, and various aspects you need to know about a multitenant environment. The learning path also includes detailed, step-by-step tutorials for the different aspects of multitenancy listed below:

* Role-based access control to OpenShift projects
* Isolating network for tenants
* Isolating resources for tenants

Let's look more closely at what each piece contains.

### Article: Introduction to Multitenancy on Red Hat OpenShift

This article introduces core concepts related to multitenancy, including:

* Defining multitenancy
* Benefits of mutitenancy
* Options to achieve multitenancy
* Configuring OpenShift containers for multitenancy on IBM Cloud

<button-link><text>Read the article</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/introduction</url>
</button-link>

### Tutorial: Role-based access control

Upon completion of this tutorial, you will learn how to:

* Create users
* Create role bindings
* Impersonate user and deploy application
* Create and deploy the pod
* Switch to another user

<button-link><text>Complete the tutorial</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/rbac</url>
</button-link>

### Tutorial: Secure your applications deployed on OpenShift using network isolation

Upon completion of this tutorial, you will learn how to:
* Create a project in OpenShift and deploy a web application that runs on Open Liberty using odo
* Configure multitenant isolation by using network policies for a project
* Test the multitenant mode configuration

<button-link><text>Complete the tutorial</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/network-isolation</url>
</button-link>

### Tutorial: Secure your applications deployed on OpenShift using resource isolation

Upon completion of this tutorial, you will learn to:

* Observe the performance of two different applications when deployed in the same project
* Observe the performance of two different applications when deployed in two different projects
* Assign resource quotas (CPU, Memory) to the projects and again observe the performance of the applications

<button-link><text>Complete the tutorial</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/resource-isolation</url>
</button-link>