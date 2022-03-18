---
authors: ''
check_date: '2022-08-21'
completed_date: '2021-08-21'
components:
- openshift
- kubernetes
draft: false
excerpt: Learn what mulitenancy is, how it's achieved, and how to make it work in
  Red Hat OpenShift
menu_order: 1
meta_description: 4 areas to focus on when moving images from Kubernetes to OpenShift
meta_keywords: Kubernetes operators, migration, migrate to openshift
meta_title: Introduction to multitenancy
primary_tag: containers
subtitle: Learn what mulitenancy is, how it's achieved, and how to make it work in
  Red Hat OpenShift
tags:
- containers
title: Introduction to multitenancy
---

A Red Hat OpenShift cluster is often used to host workloads from a single tenant (or, customer) who owns the cluster. However, multiple workloads from different tenants can also be run in the same cluster. In this case, you must isolate those workloads from one another so that the tenants cannot interfere with each other. This article explains how to isolate workloads in OpenShift so that they can be used by multiple tenants.

## What is multitenancy?

_Software multitenancy_ refers to a software architecture where a single software instance serves multiple users or groups, also called tenants. <!--EM: reworded this b/c I didn't want to straight copy the wikipedia definition--even though it's a good one. I also wanted to define "tenants" in the first sentence.-->

Many times, an existing software solution is designed for a single tenant. In this case, you can achieve multitenancy by provisioning a separate instance of the software for every tenant while also isolating each tenant. Tenants refers to a single user, group of users, or an organization.

In multitenancy, every tenant needs to be isolated from and invisible to each other to protect the tenant's data privacy and security.
 
### Benefits of sharing workloads

In many companies, different departments (such as Human Resources and Finance) use their own set of workloads that run on shared software and hardware <!--EM: Not sure if software is the right term here-->. For instance, a company might have multiple departments running their workloads on a WebSphere Application Server with a DB2 server.

A dedicated hardware and software setup for every workload would be expensive, hard to maintain, and impractical. <!--EM: I deleted most of that paragraph and just summarized it b/c it felt like extra, not necessary content-->

In a shared computing environment, multiple workloads share capacity. So, workloads are able to acquire capacity when needed and release it when the capacity is not needed. This is possible because in companies, the usage of every application varies during different times day, months, and years.

<!--EM: Is this something developers care about? Just curious b/c I know it's important but is it important on a developer site?
A shared computing environment has benefits for workloads in the same infrastructure, including:

- Lower costs: Multiple workloads run on shared infrastructure. Resource utilization is higher, giving a higher return on investment. Customers pay for just the capacity they're using, not for capacity that is sitting idle.
- Scalability: Workloads can opt to scale up on-demand or scale down if required. If the environment has too little capacity or too much for all of the applications, the infrastructure providers can add or remove infrastructure.
- Maintenance: Because the infrastructure provider needs to provide less capacity overall, there is less hardware and software to maintain.-->

The key to this shared computing environment being valuable to all tenants is for the environment to support multitenancy. That is, the environment needs to keep the workloads related to compute, network, and other hardware resource for each tenant isolated from the other tenants' workloads.

New virtualization and containerization techniques make it possible to provide complete isolation for the tenants on a shared hardware infrastructure. The software as a service (SaaS) model makes software available to a user without the user having to install or manage it themselves. A SaaS service can be used by multiple tenants, as long as the tenants are isolated from each other.

A multitenant SaaS service uses shared computing resources efficiently, enables multiple tenants to use the service while being isolated from each other, and makes the service consumer more productive because the service provider is responsible for managing the service and its computing environment.

## Approaches to achieving multitenancy

There are a couple of approaches to achieving multitenancy using OpenShift:

1. Multitenant service -- In this ideal solution, a service is implemented such that a single instance can support multiple tenants. <!--EM: why is this here? And I don't understand the sentence after it as it relates to OpenShift ---- But multitenant applications are difficult to implement, and modifying an existing application to make it multitenant can be even more difficult. In any case, if a workload isn't implemented to support multiple tenants, deploying it to OpenShift won't change that.-->

If a service is not multitenant, then each tenant will need its own service instance. How can those instances be isolated from each other for multitenancy? There are a couple of options:

2. Multiple clusters -- The highest isolation between service instances is to deploy each in a separate cluster. Then each cluster can be installed on separate hardware, separate networks, even separate data centers or regions located thousand of miles apart. The downside to this is that having a separate cluster for each service instance would be expensive with extremely low utilization and create many clusters to manage.

3. Single shared cluster -- A more economical and practical approach is to deploy multiple service instances within the same cluster. Compared to multiple clusters, a single cluster is less expensive, easier to manage, and better utilized. However, the workloads in a cluster share the same resources and network, so their isolation is limited. The container isolation between workloads in a cluster is appropriate for a single tenant or multiple tenants who trust each other, but not sufficient for multiple tenants where one tenant should not even know the other tenants' workloads exist.

So A cluster can handle multiple workloads. How can they be isolated?

## Isolating workloads in OpenShift

To understand how isolation works in OpenShift, first let's quickly review how OpenShift is set up.
An OpenShift cluster is a collection of [projects](https://docs.openshift.com/container-platform/4.7/applications/projects/working-with-projects.html), which are based on Kubernetes [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/). A project is like a virtual cluster, logically separating its resources from those in other projects, so that multiple projects work like multiple virtual clusters all within a single physical cluster.

Projects provide several advantages:

1. Name scope -- Each project has its own name scope, so two resources of the same kind can have the same unique name as long as they're in separate projects.

1. User community -- The cluster users (such as application developers and deployers) who can access a project is controlled via cluster [RBAC](https://docs.openshift.com/container-platform/4.7/authentication/using-rbac.html). This makes it easy for a cluster administrator to isolate different projects in the same cluster by putting the users for different teams in different projects.

1. Resource quota -- The cluster administrator can configure each project with resource limits. This way, a project cannot use too much of the cluster's resources, so each project should get some resources.

1. Configuration scope -- Some cluster configuration can be specified on a per-project basis. Configuration that would normally be global to the cluster can be scoped to a project so that projects can be configured independently.

Projects group resources, but, by default, they do not isolate workloads. However, you can configure projects to isolate workloads. By creating a project per tenant and configuring each one for isolation, the workloads for a tenant in one project are isolated from those for a tenant in another project.

A cluster administrator configures project isolation in two main aspects:

1. Network isolation

1. Resource isolation

Let's explore those aspects in a little more detail.

### Network isolation

You configure an OpenShift project using Kubernetes network policies to prevent network connections between its pods and pods in other projects. Effectively, the pods in one project cannot see the pods in other projects on the network. It's as if they don't exist on the network. This ensures that network traffic is allowed between pods within the project but not between pods in different projects, thereby providing network isolation between projects.

Learn how to achieve network isolation by applying network policies on your project. [Read the tutorial]( https://github.ibm.com/TT-ISV-org/multitenancy/tree/master/Network-Isolation-Tutorial).

### Resource isolation
In a multitenant environment, the resource usage of one tenant's workloads should not impact the performance or resource availability for other tenants' workloads. You can configure OpenShift project with resource quotas for compute resources such as CPU and memory. This ensures that the workloads in one tenant's project cannot exceed its resource limits, thereby reserving resources for the workloads running in other tenants' projects.

Learn how to configure project resource quotas for CPU and memory and achieve resource isolation between tenants. [Read the tutorial]( https://github.ibm.com/TT-ISV-org/multitenancy/tree/master/Resource-Isolation-Tutorial) . 


## Summary
In this article, you saw the need and benefits of multitenant deployment of applications. You can use OpenShift projects to separate tenants, and use network policies and resource quotas to achieve isolation for multitenancy, thereby achieving multitenancy in a container environment.
  
## Related resources
- [What is Multitenancy?](https://www.redhat.com/en/topics/cloud-computing/what-is-multitenancy)