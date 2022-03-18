---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
draft: false
excerpt: This article describes how an SCC actually grants permissions to protected
  Linux functions.
menu_order: 2
meta_description: This article describes how an SCC actually grants permissions to
  protected Linux functions.
meta_keywords: security context constraint permissions, permissions for Linux functions
meta_title: How an SCC specifies permissions
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
subtitle: Controlling permissions to access protected Linux functionality
tags:
- security
- linux
time_to_read: 10 minutes
title: How an SCC specifies permissions
---

A Red Hat OpenShift cluster uses security context constraints (SCCs) to limit pod permissions to access protected Linux functionality. This article takes a closer look at exactly how an SCC grants permissions to a pod to access those protected functions.

This article assumes that you have a general understanding of how to deploy an application to an OpenShift cluster and how the cluster manages a workload.

## Overview of security context constraints

The key points from the [Overview of security context constraints](/learningpaths/secure-context-constraints-openshift/intro/) article include:

* By default, OpenShift isolates containers by limiting their access to protected functions in Linux. SCCs allow select pods to access some or all of the protected functions.
* When a developer creates an application that needs permissions to access protected functions, the deployer must create a deployment manifest that requests those permissions in its security context (SC), and the administrator must assign an SCC that grants those permissions.
  * The pod configures the container's Linux environment with the permissions requested by the SC and granted by the SCC. If the application attempts to perform a protected function that wasn't requested in the SC, the container will block the application from performing that function. The application will experience this as an error.
  * Custom SCCs should be developed using the [Principle of Least Privilege](https://redhat-connect.gitbook.io/best-practices-guide/principle-of-least-privilege) and grant as little access as possible.
* The administrator makes an SCC available by assigning it to a service account, ideally via a role.
* A manifest makes the SCC available to its pods by specifying the service account.
* Admission allows the cluster to deploy each pod specified by the manifest only if the SCC grants all of the permissions that the manifest requests.

With those highlights in mind, let's explore in detail just how this works.

## How an SCC specifies permissions

Up to this point, the generic term "permissions" has been used to describe what pods can request (via the deployment manifest) and what SCCs will allow. OpenShift specifies permissions in three different aspects: privileges, access control, and capabilities.

Each aspect has its own set of rules and syntax. The following sections detail some of the available fields and values that can be used -- from both the deployment manifest side (asking permission) and the SCC side (granting permission).

### Privileges  

Privileges describe the general authority the pod has when it's deployed. In an SCC or deployment manifest, a setting value of "true" means that the privilege is allowed.

Here are some example privileges in SCCs:

* `allowPrivilegedContainer` -- specifies whether a pod can run containers with privileged processes
* `allowPrivilegeEscalation` -- specifies if a child process can gain more privileges than its parent

The deployment manifest can request these privileges for a container. For example:

```
securityContext.privileged: true
```

_**IMPORTANT**: Although an SCC can allow running [privileged containers](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities) and escalation, doing so makes the host much less secure. A privileged container allows a process running in the container "nearly all the same access to the host as processes running outside containers on the host." Arguably, if a container can't protect the host by containing a process, this nullifies a significant advantage of using containers. Also see "[Should You Run Privileged Docker Containers?](https://phoenixnap.com/kb/docker-privileged#htoc-why-running-privileged-containers-is-not-secure)"_

### Access controls

Access controls manage the specific user ID and group ID values the pod runs as.

In the SCC, the list of fields for specifying access include:

* `runAsUser` specifies the allowable range of user IDs used for running all the containers in the pod.
* `supplementalGroups` specifies the allowable range of group IDs used for running all the containers in the pod.
* `fsGroup` specifies the allowable range of group IDs used for controlling pod storage volumes.
* `seLinuxContext` specifies the allowable values used for setting the SELinux context, which includes SELinux user, role, type, and level.

Access control settings in an SCC can specify the following values:

* `MustRunAs` and `MustRunAsRange` enforce the range of user ID values that a container can request, and also assigns a default value if needed.
* `RunAsAny` indicates that the user ID does not have to be within a range specified by the SCC or the project, thus allowing any ID to be requested. Note that this allows the root user (UID=0) to be specified, which is significantly less secure than a non-root user ID.
* `MustRunAsNonRoot` indicates that any non-root ID value (any user ID other than 0) can be requested. This is similar to `RunAsAny` but much more secure.

The deployment manifest can request access for a container or a pod using these fields:

* `securityContext.runAsUser` -- request to run under a specific user ID
* `securityContext.runAsGroup` -- request to run under a specific group ID
* `securityContext.fsGroup` -- request to run under a specific group ID for accessing storage volumes
* `securityContext.seLinuxOptions` -- request to run using a specific SELinux context set of labels

**What is SELinux?**

[Security-Enhanced Linux (SELinux)](https://www.redhat.com/en/topics/linux/what-is-selinux) is a Linux kernel module that provides additional access control security and offers the following benefits:

* **All processes and files are labeled:** SELinux policy rules define how processes interact with files, as well as how processes interact with each other. Access is only allowed if an SELinux policy rule exists that specifically allows it.
* **Fine-grained access control:** Stepping beyond traditional UNIX permissions that are controlled at user discretion and based on Linux user and group IDs, SELinux access decisions are based on all available information, such as an SELinux user, role, type, and, optionally, security level.
* **SELinux policy** is administratively defined and enforced system-wide.
* **Improved mitigation for privilege escalation attacks:** Processes run in namespaces, and are therefore separated from each other. SELinux policy rules define how processes access files and other processes.

### Capabilities

These settings control access to [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html), which are individual superuser privileges such as accessing system time or configuring network settings. These capabilities are assigned to individual containers running within the pod and take precedence over any pod settings.

Examples of capabilities include:

* `CHOWN` -- can change file ownership and group ownership
* `KILL` -- can send a signal to process without having a matching user ID
* `NET_BROADCAST` -- can broadcast and listen to multicast
* `NET_ADMIN` -- can configure interfaces, routing tables, multicast, admin of IP firewall, etc.
* `SYS_CHROOT` -- can use the `chroot` command
* `SYS_ADMIN` -- can set the domain and host names, run mount and unmount, lock/unlock shared memory, etc.
* `SYS_TIME` -- can manipulate the system clock
* `MKNOD` -- provides privileged aspects of `mknod()`
* `SETCAP` -- can set or remove capabilities on files

The full list of capabilities is specified in [include/linux/capability.h](https://github.com/torvalds/linux/blob/master/include/uapi/linux/capability.h).

An SCC grants capabilities using these fields:

* `defaultAddCapabilities` -- list of default capabilities automatically added to each container
* `requiredDropCapabilities` -- list of capabilities that are forbidden to run on each container
* `allowedCapabilities` -- list of container capabilities that are allowed to be requested by the deployment manifest

The deployment manifest can request capabilities for a container using these fields:

* `securityContext.capabilities.add`
* `securityContext.capabilities.drop`

Any SCC specifies permissions using these three aspects: privileges, access control, and capabilities. OpenShift includes several predefined SCCs. An administrator can add to them by implementing custom SCCs.

## Summary

Now that you've gotten an in-depth look at how a security context constraint grants permissions that enable a pod to access protected Linux functions, you're ready to move on to the next article in this learning path which explores [predefined and custom SCCs](/learningpaths/secure-context-constraints-openshift/openshift-predefined-scc/).