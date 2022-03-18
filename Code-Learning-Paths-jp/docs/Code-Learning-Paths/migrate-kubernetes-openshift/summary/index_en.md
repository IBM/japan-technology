---
authors: ''
completed_date: '2021-08-10'
components:
- openshift
- kubernetes
- devops
draft: false
excerpt: This guide walks you through how to migrate your service from Kubernetes
  to OpenShift, with a focus on how to modify your image and your security policies
  to comply with OpenShift standards.
menu_order: 5
meta_description: This guide walks you through how to migrate your service from Kubernetes
  to OpenShift, with a focus on how to modify your image and your security policies
  to comply with OpenShift standards.
meta_keywords: migrate Kubernetes to OpenShift, openshift migration, SCCs
meta_title: Summary, next steps, and additional resources for IoT development
primary_tag: containers
subtitle: Summary, next steps, and additional resources
title: Summary
---

If an application deploys and runs properly in Kubernetes, to migrate it to OpenShift:
1. Migrate its container images
1. Migrate its PSPs to SCCs

This will go a long way to help the application deploy and run properly in OpenShift as well. Once it does, you can proceed with making it self managing, getting it certified, and adding it to service catalogs like Red Hat Marketplace, as described in "[Make your solution run as a service and add it to service catalogs](https://developer.ibm.com/articles/a-guide-to-turning-your-solution-into-a-service-on-kubernetes-and-adding-it-to-service-catalogs/)."