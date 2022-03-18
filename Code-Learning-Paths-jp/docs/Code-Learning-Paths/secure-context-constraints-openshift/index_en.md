---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
content_tags:
- hcbt
draft: false
excerpt: Learn to use security context constraints with your Red Hat OpenShift workloads.
meta_description: Learn to use security context constraints with your Red Hat OpenShift
  workloads.
meta_keywords: security context constraints, security in OpenShift
meta_title: 'Learning Path: Getting started with security context constraints on Red
  Hat OpenShift'
primary_tag: containers
related_content:
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
- slug: l-lpic1-104-5/
  type: tutorials
subtitle: Learn to use security context constraints with your Red Hat OpenShift workloads
tags:
- security
- linux
- hcbt
time_to_read: 2 hours
title: Get started with security context constraints on Red Hat OpenShift
---

This learning path is designed for anyone interested in getting up to speed on using security context contraints with Red Hat OpenShift. Security context constraints (SCCs) allow containerized applications to access protected Linux functionality.

This learning path consists of introductory and detailed articles and a step-by-step tutorial with hands-on demonstrations that show you how to create and use SCCs with OpenShift deployments.

## Outcomes

After completing this learning path, you will:

* Have a firm understanding of SCC concepts, including:
    * What is an SCC?
    * Deploying a secure pod
    * How a pod requests additional access
    * How an SCC specifies permissions
    * OpenShift's predefined SCCs
    * Creating a custom SCC
    * How a deployment specifies permissions
* Gain hands-on experience using SCCs, including:
    * Recognizing what SCC and security context is assigned to a workload
    * Using a default service account and default security context
    * Looking for SCC validation errors
    * Creating an SCC and assigning it to a service account
    * Using a security context that requests special permissions with an SCC that allows them