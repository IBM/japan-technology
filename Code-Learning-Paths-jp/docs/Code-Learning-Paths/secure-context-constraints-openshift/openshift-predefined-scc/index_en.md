---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
draft: false
excerpt: This article describes what's included in Red Hat OpenShift's predefined
  security context constraints and also shows you how to customize an SCC.
menu_order: 3
meta_description: This article describes what's included in Red Hat OpenShift's predefined
  security context constraints and also shows you how to customize an SCC.
meta_keywords: custom security context constraint, predefined SCCs
meta_title: Predefined security context constraints vs. custom SCCs
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
subtitle: What's included in predefined SCCs and how to customize them
tags:
- security
- linux
time_to_read: 10 minutes
title: Predefined vs. custom SCCs
---

This article describes what's included in Red Hat OpenShift's predefined security context constraints (SCCs) and also shows you how to customize an SCC.

An SCC is either predefined or custom. A predefined SCC is built into the cluster when the cluster is created. An administrator creates a custom SCC, which is then unique to that cluster. The administrator should not modify a predefined SCC, but should instead create or modify a custom SCC. Any SCC is global to its cluster, so any SCC can be assigned to any service account, regardless of the project the service account is in.

## OpenShift's predefined SCCs

Each OpenShift cluster contains eight predefined SCCs, each specifying a set of permissions. This table from "[Managing SCCs in OpenShift](https://www.openshift.com/blog/managing-sccs-in-openshift)" lists and explains the predefined SCCs. (Note that "UID" is a user ID and "GID" is a group ID.)

| **SCC name** | **Description** | **Comments** |
|--------------|-----------------|--------------|
| **restricted** | Denies access to all host features and requires pods to be run with a UID and SELinux context from the set that the cluster assigns to the project. | This is the most secure SCC and is always used by default. Will work for most typical stateless workloads. |
| **nonroot** | Provides all the same features as the **restricted** SCC, but allows users to run with any non-root UID. | Suitable for applications that need predictable non-root UIDs, but can function with all the other limitations set by the **restricted** SCC. |
| **anyuid** | Same as **restricted**, but allows users to run with any UID and GID. | Potentially very risy as it allows running as root user outside the container. If used, SELinux controls can play an important role in adding a layer of protection. It's also a good idea to use **seccomp** to filter out undesired system calls. |
| **hostmount-anyuid** | Provides all the features of the **restricted** SCC, but allows host mounts and any UID by a pod.  This is primarily used by the persistent volume recycler, a trusted workload that is an essential infrastructure piece to the cluster. | This SCC should only be used by the persistent volume recycler. Same warnings as with **anyuid**, but hostmount-anyuid goes further by allowing the mounting of host volumes. *Warning:* This SCC allows host file system access as any UID, including UID 0. Grant with caution. |
| **hostnetwork** | Allows the use of host networking and host ports, but still requires pods to be run with a UID and SELinux context that are assigned to the project. | This SCC allows the pod to "see and use" the host network stack directly. Requiring the pod run with a non-zero UID and preassigned SELinux context can add some security. |
| **node-exporter** | Used only for the [Prometheus Node Exporter](https://prometheus.io/docs/guides/node-exporter/). (Prometheus is a popular Kubernetes monitoring tool.) | This SCC should only be used by Prometheus. It is designed specifically for Prometheus to retrieve metrics from the cluster. It allows access to the host network, host PIDS, and host volumes, but not the host IPC. It also allows **anyuid**. Applications should *not* use this SCC. |
| **hostaccess** | Allows access to _all_ host project namespaces, but still requires pods to be run with a UID and SELinux context that are assigned to the project. | Access to all host namespaces is dangerous, even though it does restrict UID and SELinux. This should only be used for necessary trusted workloads. |
| **privileged** | Allows access to all privileged and host features, as well as the ability to run as any user, group, or fsGroup, and with any SELinux context. This is the most relaxed SCC policy. | This SCC allows a pod to control everything in the host and worker nodes, as well as other containers. Only trusted workloads should use this. There is a case to be made that this should _never_ be used in production, as it allows the pod to completely control the host. |
<br>

_**IMPORTANT:** Do not modify the predefined SCCs. Customizing the predefined SCCs can lead to issues when OpenShift is upgraded. Instead, create new custom SCCs._

Now that you've gotten an overview of the predefined SCCs, let's examine a predefined SCC in detail.

### Examining the restricted SCC

The `restricted` SCC is the default SCC because it is assigned to each project's `default` service account. Therefore, a `restricted` SCC is the one used by all of the deployments that do not specify a service account, making it the most commonly used SCC. Let's examine it in detail.

You can view an SCC by running either of the following OpenShift CLI commands:

```bash
oc get scc <scc name> -o yaml
oc describe scc/<scc name>
```

Here is a snippet of what the YAML for the `restricted` SCC looks like (with comment lines added for clarity):

```yaml
$ oc get scc restricted  -o yaml
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: restricted
...
# Privileges
allowPrivilegedContainer: false
allowHostNetwork: false
allowHostPID: false
...
# Capabilities
allowedCapabilities: null
defaultAddCapabilities: null
requiredDropCapabilities:
- KILL
- MKNOD
- SETUID
- SETGID
...
# Access Control
fsGroup:
  type: MustRunAs
runAsUser:
  type: MustRunAsRange
seLinuxContext:
  type: MustRunAs
supplementalGroups:
  type: RunAsAny
...
```

Note how locked down this SCC is -- it doesn't allow any special privileges or capabilities. However, it does allow any supplemental group ID to be specified, which enables pods to access the shared resources that are owned by a group.

In addition to the predefined SCCs that are built into a cluster, the administrator can also add custom SCCs.

## Creating a custom SCC

When determining which SCC to assign, it is important to remember that less is better. If a pod requires permission A, don't select an SCC that provides permissions A, B, and C.

If none of the predefined SCCs provides exactly the permissions an application requires, the administrator can create a custom one.

One way to create a custom SCC is to use a YAML file, such as the following:

```yaml
apiVersion: v1
kind: SecurityContextConstraints
metadata:
  name: my-custom-scc
# Privileges
allowPrivilegedContainer: false
# Access Control
runAsUser:
  type: MustRunAsRange
  uidRangeMin: 1000
  uidRangeMax: 2000
seLinuxContext:
  type: RunAsAny
fsGroup:
  type: MustRunAs
  ranges:
  - min: 5000
    max: 6000
supplementalGroups:
  type: MustRunAs
  ranges:
  - min: 5000
    max: 6000
# Capabilities
defaultAddCapabilities:
  - CHOWN
  - SYS_TIME
requiredDropCapabilities:
  - MKNOD
allowedCapabilites:
  - NET_ADMIN  
```

_**NOTE**: Note that the SCC fields `fsGroup` and `supplementalGroups` are set to `MustRunAs` -- which typically would indicate setting a value, but in fact a range is specified._

You can save this SCC definition in a file named `my-custom-scc.yaml` and create the SCC with this command:

```bash
oc create -f my-custom-scc.yaml
```

To view the created SCC, use the command:

```bash
oc get scc my-custom-scc -o yaml
```

You can also view the SCC with the `describe` command:

```bash
$ oc describe scc/my-custom-scc
Name:                           my-custom-scc
Priority:                       <none>
Access:
  Users:                        <none>
  Groups:                       <none>
Settings:
  Allow Privileged:             false
  Allow Privilege Escalation:   true
  Default Add Capabilities:     CHOWN,SYS_TIME
  Required Drop Capabilities:   MKNOD
  Allowed Capabilities:         <none>
  Allowed Seccomp Profiles:     <none>
  Allowed Volume Types:         awsElasticBlockStore,azureDisk,azureFile,cephFS,cinder,configMap,csi,downwardAPI,emptyDir,fc,flexVolume,flocker,gcePersistentDisk,gitRepo,glusterfs,iscsi,nfs,persistentVolumeClaim,photonPersistentDisk,portworxVolume,projected,quobyte,rbd,scaleIO,secret,storageOS,vsphere
  Allowed Flexvolumes:          <all>
  Allowed Unsafe Sysctls:       <none>
  Forbidden Sysctls:            <none>
  Allow Host Network:           false
  Allow Host Ports:             false
  Allow Host PID:               false
  Allow Host IPC:               false
  Read Only Root Filesystem:    false
  Run As User Strategy: MustRunAsRange
    UID:                        <none>
    UID Range Min:              1000
    UID Range Max:              2000
  SELinux Context Strategy: RunAsAny
    User:                       <none>
    Role:                       <none>
    Type:                       <none>
    Level:                      <none>
  FSGroup Strategy: MustRunAs
    Ranges:                     5000-6000
  Supplemental Groups Strategy: MustRunAs
    Ranges:                     5000-6000
```

A quick note on some of the permissions specified in the SCC:

### SELinux

How the `seLinuxOptions` values are used depends on the value of the `seLinuxContext.type` field:

* **`MustRunAs`** -- Requires `seLinuxContext.seLinuxOptions` to be set, either in the SCC or in the project's configuration. These values are then validated against the `seLinuxOptions` that are requested in the deployment manifest.
* **`RunAsAny`** -- Means no default values are provided, which allows any `seLinuxOptions` to be specified in the deployment manifest.

### seccomp

[`seccomp`](https://man7.org/linux/man-pages/man2/seccomp.2.html), short for "Secure Computing state," is a Linux kernel security feature. When enabled, `seccomp` prevents the container from making a majority of system calls, eliminating most common vulnerabilities. `seccomp` is maintained by a whitelist profile that can be added to for custom use and is unique to each base image profile.

## Summary

With you newly acquired understanding of predefined SCCs and custom SCCs, you're ready to learn the steps for [making an SCC available to a deployment](/learningpaths/secure-context-constraints-openshift/scc-availability/) in the next article in this learning path.