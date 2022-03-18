---
authors: ''
check_date: '2022-06-30'
completed_date: '2021-06-30'
components:
- openshift
- kubernetes
- devops
display_in_listing: true
draft: false
excerpt: Use the open source Cloud-Native Toolkit's build pipeline to create images
  that pass Red Hat Certification.
meta_description: Use the open source Cloud-Native Toolkit's build pipeline to create
  images that pass Red Hat Certification.
meta_keywords: universal application images, cloud-native toolkit
primary_tag: containers
related_content:
- slug: introduction-to-kubernetes-operators
  type: articles
- slug: how-operators-extend-kubernetes-functionality
  type: articles
subtitle: Use the Cloud-Native Toolkit's build pipeline to create images for Red Hat
  Certification
title: Build images with the Cloud-Native Toolkit
---

Building [universal application images](/learningpaths/universal-application-image) that meet all the requirements needed to run well in Kubernetes and Red Hat OpenShift can feel overwhelming. Using the open source Cloud-Native Toolkit makes it easier to create well-built images.

The [Cloud-Native Toolkit](https://cloudnativetoolkit.dev/) includes a number of image-building best practices, tools, and learning materials along  with a repeatable and maintainable process. You can use the toolkit throughout the entire software development lifecycle (SDLC) to develop complete applications -- including the ability to build universal application images for Red Hat Container Certification. The toolkit can run in any Kubernetes or OpenShift cluster, on IBM Cloud, or elsewhere.

## Prerequisites

To complete the tutorials in this learning path, a cluster administrator needs to install the Cloud-Native Toolkit on a Red Hat OpenShift cluster. This only needs to be done once on a cluster, and then multiple projects can use it.

- [Install the Cloud-Native Toolkit](/learningpaths/build-images-cloud-native-toolkit/install-toolkit)

## Steps and outcomes

### 1. Start with the starter kits

To get a feel for how to use the Cloud-Native Toolkit, start with the first tutorial: [Use the Cloud-Native Toolkit starter kits](/learningpaths/build-images-cloud-native-toolkit/starter-kits)

This tutorial will help you:

   * Learn how to use the Cloud-Native Toolkit
   * Create and run CI pipelines
   * Build a cloud-native application that's deployed as a container

### 2. Use an existing application with the Cloud-Native Toolkit to build an image

If you have an existing application in a single repo that you want to containerize using the Cloud-Native Toolkit, follow the instructions in the tutorial 
[Use Cloud-Native Toolkit on an existing application](/learningpaths/build-images-cloud-native-toolkit/existing-application), which will guide you to:

   * Use the Cloud-Native Toolkit with an existing application
   * Learn how to prepare your GitHub repo to run in a CI pipeline
   * Learn how to modify the pipeline tasks to accommodate your application
   * Prepare the container image for OpenShift certification

### 3. Use an application from multiple repos

If you have a more complex application that spans multiple repos, read the advanced tutorial [Build an OpenShift certifiable image from a complex application](/learningpaths/build-images-cloud-native-toolkit/poly-repo/) to learn how to:

   * Use the Cloud-Native Toolkit on a real-world open source application
   * Modify the pipeline tasks to work with multiple GitHub repos
   * Add and use parameters to modify pipeline actions
   * Use semantic versioning for image releases
   * Prepare the container image for OpenShift certification