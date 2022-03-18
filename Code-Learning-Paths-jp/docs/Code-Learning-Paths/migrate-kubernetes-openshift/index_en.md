---
authors: ''
check_date: '2022-08-30'
completed_date: '2021-08-10'
components:
- openshift
- kubernetes
- devops
display_in_listing: true
draft: false
excerpt: This guide walks you through how to migrate your existing Kubernetes service
  to run well in OpenShift.
meta_description: This guide walks you through how to migrate your existing Kubernetes
  service to run well in OpenShift.
meta_keywords: migrate Kubernetes to OpenShift, openshift migration, SCCs
primary_tag: containers
related_content:
- slug: build-images-cloud-native-toolkit
  type: learningpaths
- slug: secure-context-constraints-openshift
  type: learningpaths
subtitle: Learn how to modify your Kubernetes service to run on Red Hat OpenShift
title: Migrate a service from Kubernetes to OpenShift
---

When you build an application service that can deploy in a Kubernetes cluster, you offer great flexibility to users who host your service. Anywhere a cluster is hosted, a service can also be hosted. A Red Hat OpenShift cluster offers all of the capabilities of Kubernetes, plus greater security and vendor support. While Kubernetes and OpenShift are highly compatible in most respects, a service that runs properly in Kubernetes does not always run the exact same way in OpenShift.

This guide is for you if you need to package your services to deploy and run properly in both Kuberentes and OpenShift clusters. Specifically, it guides you through how to migrate your existing Kubernetes service to run well in OpenShift. By adding this flexibility, you increase your marketplace of potential customers from those who only use Kubernetes to also include those who use OpenShift.

### Skill level

To follow along with this guide, you should be an experienced Kubernetes and Red Hat OpenShift user.

### Time to read

This learning path will take about 2 hours to complete.

## Why you should consider using Openshift

OpenShift is built on Kubernetes and runs on Red Hat Enterprise Linux (RHEL) technologies with additional features that make it valuable for hosting enterprise applications. OpenShift and Red Hat Enterprise Linux include vendor support from Red Hat, with more explicitly defined SLAs and security features than the community support that comes with open source projects like Linux and Kubernetes. Containers designed for OpenShift include RHEL libraries that run a more fully integrated stack with the RHEL kernel than Kubernetes does.

## Migrating from Kubernetes to OpenShift

When migrating your application or service from Kubernetes to OpenShift, there are two main issues you need to be aware of:  

1. Container image: The process used to build the image for Kubernetes often needs to be refined for OpenShift.

1. Protected Linux functionality: The feature the cluster uses to authorize containers to access protected Linux functionality is different in OpenShift than the one in Kubernetes.

Let's explore these issues in a little more detail.

### Container image migration

OpenShift runs containers more securely than Kubernetes does, and these security constraints can cause errors when a container and its application try to run. Red Hat not only provides support for OpenShift but also for containers running in OpenShift, but only if the containers' images are built to meet Red Hat certification specifications. 

For a container to run securely in OpenShift and be eligible for Red Hat's support, the image build process needs to be changes to meet OpenShift requirements. When packaging an application as a container and implementing the deployment manifest for deploying it into clusters, there are four main areas you need to be concerned about.

<button-link><text>Read the article</text><url>/learningpaths/migrate-kubernetes-openshift/migrate-images</url>
</button-link>

### Protected Linux functionality migration

Many applications do not require access to protected Linux functionality. For those that do, both Kubernetes and OpenShift enable pods to specify security contexts that configure the containers with access to Linux functionality that is otherwise blocked by default. However, to prevent rogue containers from granting themselves access they shouldn't have, the cluster has to authorize the access the security context wants to grant. 

Kubernetes authorizes access using one feature, a pod security policy (PSP). OpenShift authorizes access using a different feature, a security context constraint (SCC). Therefore, PSPs that work in Kubernetes will not work in OpenShift; the PSPs need to be converted into SCCs with the corresponding permissions.

This difference is a concern for the cluster administrator, since they configure the cluster with the PSPs and SCCs so that they are available for the pod deployments to use.

<button-link><text>Read the article</text><url>migrate-kubernetes-psp-openshift-scc</url>
</button-link>