---
authors: ''
check_date: '2022-07-25'
completed_date: '2021-07-27'
display_in_listing: true
draft: false
excerpt: When migrating your images from Kubernetes to OpenShift, watch out for these
  4 areas to change.
meta_description: When migrating your images from Kubernetes to OpenShift, watch out
  for these 4 areas to change.
meta_keywords: Kubernetes images, OpenShift images, Kubernetes to OpenShift migration
meta_title: Migrate your Kubernetes images to Red Hat OpenShift
primary_tag: containers
subtitle: 4 areas to focus on when moving images from Kubernetes to OpenShift
tags:
- containers
title: Migrate your Kubernetes images to Red Hat OpenShift
---

Red Hat OpenShift is a Kubernetes-based container platform. Typically, any containerized applications that deploys and runs properly in a Kubernetes cluster will also deploy and run properly in an OpenShift cluster. However, OpenShift includes some default security settings that require you to change how your container image is built in order to deploy to OpenShift.

This article shows you how to alter your Kubernetes container image to run on OpenShift as well as how to verify whether your container image requires modification before migration. This article is most meaningful for those who design and build container images.

## Before you start

The learning path [Design, build, and deploy universal application images](https://developer.ibm.com/learningpaths/universal-application-image) covers exactly how to build images that run well in Kubernetes and OpenShift. 

This article highlights four of the areas covered in the original learning path that give people the most trouble when trying to adapt Kubernetes images to run on OpenShift. These include:

* Building OCI-compliant container images
* Running processes without root user access in container images
* Building container images with the base image as Red Hat Enterprise Linux or a Universal Base Image
* Storing images in an integrated image registry or in an external image registry

## Build an OCI-compliant container image

<sidebar>
    <p><b>CRI and OCI-compliance</b></p><br/>
    <p>A container runtime takes a container image and runs the application defined in the image. Originally in Kubernetes, the individual nodes of the cluster used Docker's runtime to run containers. To accommodate more container runtimes, Kubernetes created an abstraction between Kubernetes and the container runtime called the [Container Runtime Interface](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/) (CRI). CRI helps to use a wide variety of container runtimes without the need to recompile.</p><br/>
    <p>CRI-compliant runtimes are also OCI-compliant and therefore can run OCI-compliant images.</p>
    </sidebar>
    
Before you can understand _how_ to build OCI-compliant container images, you must first understand how the Open Container Initiative (OCI) relates to OpenShift.

The [Open Container Initiative (OCI)](https://opencontainers.org/) was created to ensure that all container runtimes can run images produced by any build tool. OCI has published specifications for container image formats and for runtimes. Container images should comply with the [OCI Image Format Specification](https://github.com/opencontainers/image-spec/blob/master/spec.md) so that they will be able to run in any container runtime that is compliant with the [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec/blob/master/spec.md). The OCI does not replace Docker; the Docker Engine is OCI-compliant.

OpenShift Container Platform v4 has replaced the Docker container engine with CRI-O, which is a lightweight container engine focused on OCI-compatible runtimes and container images.

### Migrate OCI-compliant images to OpenShift

To migrate your images to OpenShift, you need to make sure your container image is OCI-compliant so that it'll run in OCI-compliant container runtimes such as the one in CRI-O. To produce OCI-compliant images, use image build tools that produce OCI-compliant images. While you can use Docker to build images, the tools [Buildah, Podman, and Skopeo](https://www.redhat.com/en/blog/say-hello-buildah-podman-and-skopeo) help to build, run, and manage OCI-compliant images, independent of the container runtime. 

Read the "Build universal application images" article for [instructions on building OCI-compliant images](https://developer.ibm.com/learningpaths/universal-application-image/build-image/#1-use-oci-compliant-tools).

## Build images with no processes running with root access

By default, image build tools use root to build an image which will also run as root (where `uid=0`), unless the Dockerfile specifies a different user. By default, OpenShift runs containers using an arbitrarily assigned non-root user ID. An image that performs actions which succeed because the user is root, such as accessing files that cannot be accessed by other users, will not be able to perform these actions in OpenShift.

### Example showing how root access affects processes

To show you how root access affects common processes, let's look at an example of deleting a file inside the root directory of a base operating system file system. The following example shows an Ubuntu OS.

The following Dockerfile has instructions to delete the `/etc/passwd` file (related to base OS `ubuntu`) which needs root user access.

```
docker
FROM ubuntu:18.04

RUN echo "echo 'Starting Shell Script...'" > shell.sh
RUN echo "rm /etc/passwd && echo '-> execution of rm command successful.' 
|| '-> execution of rm command failed.'" >> shell.sh
RUN echo "echo 'Ending Shell Script...'" >> shell.sh
RUN chmod +x shell.sh

CMD [ "sh", "shell.sh" ]
```

The container image is built from the Dockerfile and stored in a registry like the IBM Cloud Container Registry.

**Deploy on Kubernetes**

When deploying this Dockerfile on Kubernetes, you get these results:

The pod status is **Completed** which shows that the execution is completed.

```
$ kubectl get pods
NAME                READY   STATUS             RESTARTS   AGE
root-app            0/1     Completed          0          4s
```

The pod log shows the `/etc/passwd` file has been deleted successfully.

```
$ kubectl logs root-app
Starting Shell Script...
-> execution of rm command successful.
Ending Shell Script...
```

**Deploy on OpenShift**

When deploying the image on OpenShift using the `oc new-app` command you get these results:

You receive a warning message: **Image "`us.icr.io/test-namespace/root-app:v1`" runs as the 'root' user which may not be permitted by your cluster administrator**.

```
$ oc new-app us.icr.io/test-namespace/root-app:v1
--> Found Docker image 811f173 (46 hours old) from us.icr.io for "us.icr.io/ksoc/root-app:v10"

    * An image stream tag will be created as "root-app:v10" that will track this image
    * This image will be deployed in deployment config "root-app"
    * The image does not expose any ports - if you want to load balance or send traffic to this component
    you will need to create a service with 'oc expose dc/root-app --port=[port]' later
    * WARNING: Image "us.icr.io/test-namespace/root-app:v1" runs as the 'root' user which may not be permitted by your cluster administrator

--> Creating resources ...
     deploymentconfig.apps.openshift.io "root-app" created
--> Success
      Run 'oc status' to view your app.
```

The pod status is ***CrashLoopBackOff*** which shows that the container has crashed.

 ```
 oc get pods
 NAME                READY   STATUS             RESTARTS   AGE
 root-app-1-lljqm    0/1     CrashLoopBackOff   1          5s
 ```

The pod log shows that the `delete` command failed to execute on OpenShift Container Platform because its default settings don't allow processes with root access to run inside an image.

 ```
 $ oc logs root-app-1-lljqm
 Starting Shell Script...
 rm: cannot remove '/etc/passwd': Permission denied
 shell.sh: 2: shell.sh: -> execution of rm command failed.: not found
 Ending Shell Script...
```

### How to address root access permissions during migration

Before migration, you need to assess whether your container image requires root access and modify the image not to run as root.

If the image does not require any root user access, the best practice is to specify a `USER` who is non-root in your Dockerfile as shown.

```dockerfile
FROM <base-image>
..
..
USER <user-id>
..
..
CMD [.., ...]
```

The learning path [Best practices for designing a universal application image](https://developer.ibm.com/learningpaths/universal-application-image/design-universal-image/#2-design-the-image-to-run-as-a-non-root-user-id) explains more about how to design an image to run as a non-root user ID.

If your application truly needs to perform root-access operations, follow the instructions in the [SCC learning path](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift/), specifically `RunAsAny` in the section about [access control](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift/scc-permissions/#access-controls).

## Build images using Red Hat Universal Base Images (UBI)

As explained in "[Design, build, and deploy universal application images](https://developer.ibm.com/learningpaths/universal-application-image/#image-structure)," container images are made up of three main parts -- Linux libraries, language runtime, and application. These layers includes all the required language runtimes, interpreters, libraries, and your application. 

Build an application image on a base image that already includes the Linux libraries and ideally the language runtime as well. Then you just need to add your application, which will run in the language runtime. Choosing the base image has a major impact on how secure, efficient, and upgradeable your container is in the future.

You can run images built on a variety of Linux distributions on OpenShift (similar to Kubernetes), but these images may have compatibility problems when run in OpenShift and will not be supported by Red Hat.

If you plan to create an image that will be deployed on OpenShift, and you want to maximize compatibility with the container host and have Red Hat support your image, you need to build your image from a [Red Hat Universal Base Image (UBI)](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image). UBIs are supported by Red Hat, offer great security, performance and life cycles, and are listed in the [Red Hat Container Catalog](https://catalog.redhat.com/software/containers/explore). 

Read more about [how to build images using a UBI](https://developer.ibm.com/learningpaths/universal-application-image/design-universal-image/#1-build-your-uai-from-a-ubi).

## Integrated image registry or an external image registry

After building the image, you need to push the image to an image registry. An image registry is a content server that can store and serve container images. Kubernetes requires an external image registry. In Kubernetes, you can use any public image registry like Docker Hub or set up a private registry and access the images from there.

An OpenShift cluster includes an integrated image registry or you can use external image registries as well. Two advantages of the integrated image registry is that it is the default destination for images after they are built and includes [image notification support](https://docs.openshift.com/container-platform/4.6/registry/registry-options.html). An advantage of an external registry is that multiple clusters can share the registry and therefore share its images.

For example, the command `oc new-app` makes use of the integrated image registry by default. It builds the image using a source code repository (in the case of s2i build), pushes the image into the integrated image registry, and deploys the app using the image.

### Image registry considerations for migration

To migrate your workload from Kubernetes to OpenShift, you need to pick whether you want to use an external or internal registry.

If you decide to work with an external registry, you can use any OCI-compliant registry, such as the [IBM Cloud Container Registry](https://cloud.ibm.com/docs/Registry?topic=Registry-registry_overview) or the [Quay registry](https://www.redhat.com/en/technologies/cloud-computing/quay). These provide many useful features out of the box like security scanning, high availability, and more. If the image registry is private, ensure that you have the required permissions to access it, usually configured in a pull secret. Otherwise, the pod will fail with an `ImagePullBackOff` status.

If your team does not already have an external image registry, then the integrated image registry is a quick way to get started. It gives you the ability to provision new image repositories on the fly and provides a great experience because of an entirely integrated computing environment.

## Summary

This article highlights a few things to be aware of when you migrate your images from Kubernetes to OpenShift. If you are building new images to deploy on OpenShift, check out our learning path: [Design, build, and deploy universal application images](https://developer.ibm.com/learningpaths/universal-application-image/).

## Conclusion

You have learned that if the container image is not OCI compliant or if it runs any process as a root user then the container image will not work on OpenShift. You need to take corrective actions as explained in the article. You should use UBI as the base image to achieve support from Red Hat. Also, you can plan to use the integrated image registry for your pre-production scenarios to get the benefit of its integration with OpenShift.