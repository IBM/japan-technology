---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
draft: false
excerpt: This article describes how an administrator makes a security context constraint
  available to a deployment.
menu_order: 4
meta_description: This article describes how an administrator makes a security context
  constraint available to a deployment.
meta_keywords: custom security context constraint, predefined SCCs
meta_title: Make a security context constraint available to a deployment
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
subtitle: Steps to make a security context constraint available to a deployment
tags:
- security
- linux
time_to_read: 10 minutes
title: Make SCCs available
---

So far, this learning path has described key security context constraints (SCCs), their permissions, and the difference between predefined and custom SCCs. This article describes how an administrator can make an SCC available to a deployment. The key resource is the *service account*, which can have SCCs assigned to it (directly or indirectly via a role or group). Once the SCCs are assigned, a deployment can easily specify that service account to gain access to its SCCs.

## Role-based access control (RBAC)

A service account is one of the resource types that are configured using a Red Hat OpenShift cluster's role-based access control (RBAC). This section assumes that you are already familiar with RBAC resources and how they work -- such as user accounts and service accounts, roles and bindings, and how administrators use them to manage permissions and access. For reference, see these pages in the OpenShift documentation:

* [Using RBAC to define and apply permissions](https://docs.openshift.com/container-platform/4.6/authentication/using-rbac.html)
* [Understanding and creating service accounts](https://docs.openshift.com/container-platform/4.6/authentication/understanding-and-creating-service-accounts.html)

A few tips to keep in mind about the scope of RBAC objects:

* A user account is global to the entire cluster.
* A service account is scoped to a single project; for example, each project has its own default service account.
* A role can be a local role that's limited to a project (i.e. a `Role`) or a cluster role that's global to a cluster (i.e. a `ClusterRole`).
* An SCC is global to a cluster.

A user must be a cluster administrator to create the cluster-wide RBAC objects. Each project's administrators (including the cluster admins) creates the project-level RBAC objects.

## Service accounts

A _service account_ allows a component running in a cluster to directly access the cluster's API. It is similar to a user account but is scoped to a single project and does not have to share a regular user's credentials. A deployment accesses an SCC via a service account so that it has access to the SCC regardless of which user deployed it.

Each service account's username is derived from its project and name:

```bash
system:serviceaccount:<project>:<name>
```

Use the following command to create a new service account in the current project:

```bash
oc create sa my-custom-sa
```

_**Important:** Each project includes a service account named `default`; the SCC assigned to it is the `restricted` SCC, which means that all deployments get assigned the `restricted` SCC by default. Do not modify the `default` service account, such as by assigning additional SCCs to it. This would change the defaults for all deployments deployed to that project. Rather, create a new service account and assign SCCs to that._

## Assign SCCs to service accounts

The easiest way to give a service account access to an SCC is to assign the SCC directly to the service account.

Here is the command to assign your custom SCC to your service account:

```bash
oc adm policy add-scc-to-user my-custom-scc -z my-custom-sa
```

Note the `-z` flag, which tells the command that `my-custom-sa` is the name of a service account, not a user.

The service account now has direct access to the SCC.

_**Note:** The preferred approach is to associate an SCC with a service account via an RBAC role: Create a role, assign the SCC to that role, and bind the service account to the role. See [Role-based access to security context constraints](https://docs.openshift.com/container-platform/4.7/authentication/managing-security-context-constraints.html#role-based-access-to-ssc_configuring-internal-oauth) for more details on how to accomplish this._

Now that the SCC is assigned to a service account, how will the cluster use the SCC to control what can be deployed?

## Admission

_[Admission control](https://docs.openshift.com/container-platform/4.6/authentication/managing-security-context-constraints.html#admission_configuring-internal-oauth)_ with SCCs allows for control over the creation of resources based on the capabilities granted to a user. The cluster uses it to decide whether to create a resource by comparing the permissions requested by the pod with those granted by the SCC.

What happens when a pod has access to multiple SCCs? This occurs when more than one SCC is assigned to the pod's user and service account, as well as the groups and roles they belong to.

Admission compares the pod's security context to each SCC until a match is found. If no one SCC grants all the permissions requested, the pod is rejected.

## Prioritization

SCCs have a priority field that affects the ordering when a pod request is validated. A higher-priority SCC is moved to the front of the set when sorting.

Here is an SCC that sets its priority to 11:

```yaml
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: scc-priority-sample
# PRIORITY FIELD
priority: 11
...
```

When the complete set of available SCCs is determined, they are ordered by:

1. Highest priority first -- nil is considered a 0 priority (lowest).
1. If priorities are equal, the SCCs are sorted from most restrictive to least restrictive.
1. If both priorities and restrictions are equal, the SCCs are sorted alphabetically.

Note that admission control compares the security context to all of the SCCs (in priority order) until a match is found or until none is found. Prioritization only changes the order that the SCCs are considered; it does not change the approval outcome.

## Summary

Now that you know how admins make SCCs available to deployments, you're ready to learn how SCCs are actually used in practice -- specifically, the next article shows you [how deployments specify permissions and how the SCC admission process works](/learningpaths/secure-context-constraints-openshift/deployment-specify-permissions/).