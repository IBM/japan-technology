---
authors: ''
check_date: 2022-08-04
completed_date: '2021-08-04'
display_in_listing: true
draft: false
excerpt: Learn what you need to change in your Kubernetes' pod security policies (PSPs)
  to convert them to Red Hat OpenShift's secure context constraints.
meta_description: Learn what you need to change in your Kubernetes' pod security policies
  (PSPs) to convert them to Red Hat OpenShift's secure context constraints.
meta_keywords: kubernetes pod security policies, Kubernetes PSPs, OpenShift SCCs,
  OpenShift secure context constraints
meta_title: Migrate your Kubernetes pod security policies to OpenShift security context
  constraints
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: universal-application-image
  type: learningpaths
subtitle: Security updates to make when moving your workloads from Kubernetes to Red
  Hat OpenShift
tags:
- security
title: Migrate your Kubernetes pod security policies to OpenShift security context
  constraints
---

Red Hat OpenShift is a Kubernetes-based container platform. Typically, any containerized applications that deploys and runs properly in a Kubernetes cluster will also deploy and run properly in an OpenShift cluster. However, one difference between Kubernetes and OpenShift is how the cluster allows the pod to modify the container's security context.

* Kubernetes has a feature called Pod Security Policies (PSPs) for granting permissions to modify the security context.
* OpenShift has a similar but different feature called Security Context Constraints (SCCs).

The application deploys the same in both types of clusters, so the deployment manifest doesn't need to change. But the OpenShift cluster is configured differently, with SCCs instead of PSPs, and the RBAC artifacts need to connect to these new SCC artifacts for granting access.

This article shows cluster administrators how to migrate cluster security policies from Kubernetes to OpenShift. Cluster administrators are in charge of configuring and deploying PSPs and SCCs. Specifically, the article explains how to convert PSPs to SCCs, and how to update the RBAC artifacts to use the SCCs instead of the PSPs.

## Before you start

The learning path [Get started with security context constraints on Red Hat OpenShift](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift) covers exactly how to build and use SCCs with OpenShift. If you're not familiar with SCCs, you should read the learning path first.

## Defining Pod Security Policies, Security Context Constraints, and RBAC

Before discussing _how_ to migrate Pod Security Policies in Kubernetes to Security Context Constraints in OpenShift, let's take a look at what each security mechanism does.

### Pod Security Policies (PSPs) in Kubernetes

A container in a Kubernetes cluster restricts its application's access to the host network, volumes, or other assets. This is to prevent the application from making changes that could affect the Linux environment and other containers. When an application needs access to protected Linux functions, the pod can configure this access. For the pod to run (that is, for the cluster to admit the pod), the cluster must allow the access the pod has configured.

A Kubernetes cluster uses PSPs to specify which permissions a pod can enable on a container. According to the [Kubernetes docs](https://kubernetes.io/docs/concepts/policy/pod-security-policy/): "The `PodSecurityPolicy` objects define a set of conditions that a pod must run in order to be accepted into the system, as well as defaults for the related fields." As optional admission controllers, PSPs serve to restrict what can run on a Kubernetes cluster.

### Security Context Constraints (SCCs) in OpenShift

OpenShift has stricter security policies than Kubernetes. OpenShift uses Security Context Constraints (SCCs) to enable containerized applications to access protected Linux functionality. An SCC is defined in a cluster and enables an administrator to control permissions for pods.

Similarly to how [Role Based Access Controls](https://docs.openshift.com/container-platform/4.6/authentication/managing-security-context-constraints.html#role-based-access-to-ssc_configuring-internal-oauth) (RBAC) manages users' access to a cluster's resources, an SCC manages pods' access to Linux functions.

The learning path [Get started with security context constraints on Red Hat OpenShift](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift/) gives you a thorough introduction on what SCCs are and how to use them.

### Role Based Access Control (RBAC)

An SCC is associated with a security account, either directly or, ideally, via an RBAC role. You use RBAC to authorize the use of policies and security constraints. RBAC infrastructure is implemented through Role, ClusterRole, RoleBinding, and ClusterRoleBinding. First, a Role or ClusterRole needs to grant access to use the desired policies. Then, the (Cluster)Role is bound to the authorized user(s).

To learn more about RBAC in Kubernetes and OpenShift, and how it incorporates PSPs and SCCs:

  - [RBAC in Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
  - [Using RBAC for PSP](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#via-rbac)
  - [RBAC in OpenShift](https://docs.openshift.com/container-platform/4.6/authentication/using-rbac.html)
  - [Using RBAC for SCC](https://docs.openshift.com/container-platform/4.6/authentication/managing-security-context-constraints.html#role-based-access-to-ssc_configuring-internal-oauth)

With this background information to reference, see what it takes to migrate policies from Kubernetes to OpenShift.

## Migrate security policies from Kubernetes to OpenShift

To migrate security policies from Kubernetes to OpenShift, you must ensure that all of the control aspects in a Pod Security Policy are migrated to the Security Context Constraints. Cluster administrators define both PSPs and SCCs.

First, you need to identify the PSPs that are available in your Kubernetes cluster. You can use this command to get the list of PSPs.

```
$ kubectl get psp
```

A Kubernetes cluster does not include any built-in PSPs by default. This example adds a PSP called `my-custom-psp`. Then the command shows it in the list (and it's the only item in the list):

```
$ kubectl get psp
NAME                        PRIV    CAPS                                                                                                                  SELINUX    RUNASUSER          FSGROUP     SUPGROUP    READONLYROOTFS   VOLUMES
my-custom-psp               false                                                                                                                         RunAsAny   MustRunAs          MustRunAs   MustRunAs   false            persistentVolumeClaim,secret,emptyDir

$
```

To see the configuration of `my-custom-psp`, run this command:

```
$ kubectl get psp my-custom-psp -o yaml
```

The command displays the PSP:

```
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: my-custom-psp
  selfLink: /apis/policy/v1beta1/podsecuritypolicies/my-custom-psp
  ...
spec:
  privileged: false
  fsGroup:
    ranges:
    - max: 6000
      min: 5000
    rule: MustRunAs
  runAsUser:
    ranges:
    - max: 2000
      min: 1000
    rule: MustRunAs
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    ranges:
    - max: 6000
      min: 5000
    rule: MustRunAs
  volumes:
  - persistentVolumeClaim
  - secret
  - emptyDir
```

In this policy, some of the controls are:

- `privileged` is set to "false". This policy does not allow deployment of pods having privileged access.
- `fsGroup` and `supplementalGroups` are given limits to a certain range of group IDs.
- The policy allows access to certain volumes: `persistentVolumeClaim`, `secret`, and `emptyDir`.

### Convert a PSP to an SCC

The controls should be migrated to OpenShift's SCCs. The following table shows a mapping of security control fields between Kubernetes and OpenShift. Essentially, when building your OpenShift SCC file, you will update your PSP file by replacing the PSP control field names on the left with the corresponding SCC control field name on the right, where applicable.

| Control aspect | PSP field name | SCC field name |
| --- | --- | --- |
| Running of privileged containers | privileged | allowPrivilegedContainer |
| Usage of host namespaces | hostPID, hostIPC | allowHostPID, allowHostIPC |
| Usage of host networking and ports | hostNetwork, hostPorts | allowHostNetwork, allowHostPorts |
| Usage of volume types | volumes | volumes |
| Usage of the host filesystem | allowedHostPaths | (see note) |
| Allow specific FlexVolume drivers | allowedFlexVolumes | allowedFlexVolumes |
| Allocating an FSGroup that owns the pod's volumes | fsGroup | fsGroup |
| Requiring the use of a read only root file system | readOnlyRootFilesystem | readOnlyRootFilesystem |
| The user and group IDs of the container | runAsUser, runAsGroup, supplementalGroups | runAsUser, fsGroup, supplementalGroups |
| Restricting escalation to root privileges | allowPrivilegeEscalation, defaultAllowPrivilegeEscalation | allowPrivilegeEscalation, defaultAllowPrivilegeEscalation |
| Linux capabilities | defaultAddCapabilities, requiredDropCapabilities, allowedCapabilities | defaultAddCapabilities, requiredDropCapabilities, allowedCapabilities |
| The SELinux context of the container | seLinux | seLinuxContext |
| The Allowed Proc Mount types for the container | allowedProcMountTypes | (see note) |
| The AppArmor profile used by containers | annotations | annotations |
| The seccomp profile used by containers | annotations | annotations |
| The sysctl profile used by containers | forbiddenSysctls, allowedUnsafeSysctls | forbiddenSysctls, allowedUnsafeSysctls |


> NOTE: `allowedHostPaths`: There is no equivalent of `allowedHostPaths` in SCC. In SCC, it is handled in a different way as explained in the [Red Hat Customer Portal](https://access.redhat.com/solutions/5314051)

> NOTE: `allowedProcMountTypes`: There is no equivalent of `allowedProcMountTypes` in SCC.

For more details about control aspects and their field names, see [What is a Pod Security Policy?](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#what-is-a-pod-security-policy) in the Kubernetes docs and [SecurityContextConstraints](https://docs.openshift.com/container-platform/4.7/rest_api/security_apis/securitycontextconstraints-security-openshift-io-v1.html#specification) in the OpenShift docs.

There could be some variations in names and the way the controls are represented. As the table above shows, `privileged` in PSP is `allowPrivilegedContainer` in SCC, `hostNetwork` in PSP is `allowHostNetwork` in SCC, and so on.

### Specify control aspect values

There are variations in details of a control aspect as well. For example, `RunAsUser` controls are represented in different ways.

In PSP:

```
    runAsUser:
      rule: MustRunAs
      ranges:
      - min: 1000
        max: 2000
```

In SCC:

```
runAsUser:
  type: MustRunAsRange
  uidRangeMin: 1000
  uidRangeMax: 2000
```

You should go through the [SCC learning path](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift) thoroughly to understand how all the controls are represented in SCCs and how they are different from PSP.

### What a converted PSP looks like

When the previous PSP manifest example is adapted to an SCC manifest file, it looks like this:

```
apiVersion: v1
kind: SecurityContextConstraints
metadata:
  name: scc-tutorial-scc
allowPrivilegedContainer: false
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
```

You can save that SCC to a file and then deploy it to a cluster using the command:

```
oc create -f <scc_manifest_file_name.yaml>
```

You now know what it takes to prepare an SCC configuration file from an existing PSP. The next step is to migrate the RBAC artifacts: the Role (and/or ClusterRole) and RoleBinding (and/or ClusterRoleBinding).

### RBAC migration

Roles and RoleBindings help in mapping which user has access to which policies.

1. Before you can migrate your security policies to OpenShift, you must identify roles that use specific pod security policies. Use `kubectl get roles -n <namespace>` to get the list of roles, and use `kubectl get role <role_name> -o yaml -n <namespace>` to get YAML output of a particular role.

    An example role YAML output is shown below:

    ```
    $ kubectl get role use-example-psp -n myproject -o yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      creationTimestamp: "2021-03-16T03:48:35Z"
      managedFields:
      - apiVersion: rbac.authorization.k8s.io/v1
        fieldsType: FieldsV1
        fieldsV1:
          f:rules: {}
        manager: kubectl-create
        operation: Update
        time: "2021-03-16T03:48:35Z"
      name: use-example-psp
      namespace: myproject
      resourceVersion: "16574"
      selfLink: /apis/rbac.authorization.k8s.io/v1/namespaces/myproject/roles/use-example-psp
      uid: a227f47d-1981-4ad5-aad9-28ef167b73c2
    rules:
    - apiGroups:
    - extensions
    resourceNames:
    - example-psp
    resources:
    - podsecuritypolicies
    verbs:
    - use
    ```

    Notice that this role maps the resource `podsecuritypolicies` to the action `use`.

    For all the roles that use `podsecuritypolicies`, you need to create a corresponding role in OpenShift.

1. The next step is to identify RoleBindings which map roles to users and service accounts. When migrating security policies from Kubernetes to OpenShift, you will migrate RoleBindings the same way that you migrate Roles.  

1. If there are ClusterRoles that use the security policies, then ClusterRoles and ClusterRoleBindings should be migrated too.

    > NOTE: You should ensure that users, groups, and service accounts specified in SCC and (Cluster)RoleBinding exist. If the users and groups don't exist, then you should do one of the following:
    > - Edit the Role to include the appropriate user, group, or service account.
    > - Create required users, groups, or service accounts in OpenShift so that they can be used in SCC and ClusterRoleBindings.

Once all these manifest files (SCC, (Cluster)Role and (Cluster)RoleBinding) are created, you can apply these to your cluster so that the SCCs are implemented and your application deployments are secure.

## Mapping of predefined PSPs in Kubernetes to predefined SCCs in OpenShift

Generally, to grant permissions to the application pods in the cluster, an administrator should define custom PSPs rather than use a predefined (that is, default) PSP from a vendor. To migrate the application, the administrator should convert the definitions for those custom PSPs into definitions for corresponding custom SCCs, as described above. However, if an application uses a vendor's predefined PSPs, how should the administrator translate those into corresponding predefined SCCs?

For starters, a Kubernetes cluster does not include any built-in PSPs by default, so there are no predefined PSPs to convert into SCCs. OpenShift does define nine [default SCCs](https://docs.openshift.com/container-platform/4.7/authentication/managing-security-context-constraints.html#security-context-constraints-about_configuring-internal-oauth), which are:

- anyuid
- hostaccess
- hostmount-anyuid
- hostnetwork
- node-exporter
- nonroot
- privileged
- restricted
- pipelines-scc

See [OpenShift’s predefined SCCs](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift/openshift-predefined-scc/#openshift-s-predefined-sccs) for more details.

OpenShift’s predefined SCCs are mostly for use by the tools Red Hat builds into a cluster. User applications can also use the predefined SCCs, but unless one is an exact match for the privileges an application needs, by the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), a more secure approach is to define a custom SCC with only the privileges that the application requires.

### Predefined PSPs and SCCs in IBM Cloud Kubernetes Service

If migrating an application from an [IBM Cloud Kubernetes Service](https://cloud.ibm.com/docs/containers) (IKS) cluster to a [Red Hat OpenShift on IBM Cloud](https://cloud.ibm.com/docs/openshift) cluster, IBM builds in some of its own predefined PSPs and SCCs. An IBM-hosted Kubernetes cluster includes these [additional PSPs](https://cloud.ibm.com/docs/containers?topic=containers-psp#ibm_psp):

- ibm-anyuid-hostaccess-psp
- ibm-anyuid-hostpath-psp
- ibm-anyuid-psp
- ibm-privileged-psp
- ibm-restricted-psp

An IBM hosted OpenShift cluster includes these  [additional SCCs](https://cloud.ibm.com/docs/openshift?topic=openshift-openshift_scc#ibm_sccs):

- ibm-anyuid-hostaccess-scc
- ibm-anyuid-hostpath-scc
- ibm-anyuid-scc
- ibm-privileged-scc
- ibm-restricted-scc

As you can see, there's a one-to-one correspondence between IBM's predefined PSPs and SCCs. The only difference is the "psp" or "scc" suffix on the end of the name. If your application uses one of IBM's predefined PSPs, when migrating it to OpenShift, change the RBAC resource to specify the resource with the "scc" name instead of the one with the "psp" name.

### Predefined PSP in Amazon Elastic Kubernetes Service

Amazon Elastic Kubernetes Service (EKS) adds [a single predefined PSP](https://docs.aws.amazon.com/eks/latest/userguide/pod-security-policy.html) to its Kubernetes clusters, `eks.privileged`. This policy has no restrictions, so it places no limits on the privileges that can be enabled in a container. Red Hat OpenShift Service on AWS (ROSA) does not add any predefined SCCs to its OpenShift clusters. To migrate an application that requires the `eks.privileged` PSP, update its RBAC to use the `privileged` SCC that's predefined by Red Hat.

### Predefined PSP in Azure Kubernetes Service

Similarly, Azure Kubernetes Service (AKS) adds a single [default AKS policy](https://docs.microsoft.com/en-us/azure/aks/use-pod-security-policies#default-aks-policies) named `privileged`, which AKS applies to any authenticated user in the cluster. Because this policy has no restrictions, any user in the cluster can deploy containers with no limits on the privileges that can be enabled. Azure Red Hat OpenShift does not add any predefined SCCs to the ones Red Hat already includes, but one of the ones predefined by Red Hat is the `privileged` SCC. Therefore, if an application uses Azure's `privileged` PSP, update its RBAC to use the `privileged` SCC predefined by Red Hat.

## Summary

Stateful workloads often use persistent volumes, network capabilities, and users and groups. These resources are protected both in Kubernetes and OpenShift using PSPs and SCCs. By following the process above, you should be able to migrate security control aspects for these resources from Kubernetes to OpenShift.