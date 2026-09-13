---
authors: ''
check_date: '2022-09-01'
completed_date: '2021-11-01'
components:
- open-liberty
- websphere-hybrid-edition
draft: true
excerpt: Understand the architecture of the legacy sample application, and understand
  the architecture of the modernized sample application.
menu_order: 12
meta_description: Understand the architecture of the legacy sample application, and
  understand the architecture of the modernized sample application.
meta_keywords: application modernization
meta_title: Overview of the sample app
primary_tag: application-modernization
subtitle: Application modernization from Java EE in 2010 to cloud-native in 2021
tags:
- java
- containers
- microservices
time_to_read: 15 minutes
title: Overview of the sample app
---

To help you learn how to modernize your applications, I’ve published a <a href="https://github.com/IBM/application-modernization-javaee-quarkus/" target="_blank" rel="noopener noreferrer">_sample application_</a> that will let you modernize a legacy Java EE application with cloud-native technologies that uses modern Java runtimes.  Whereas the legacy app was deployed to WebSphere Application Server traditional, the modernized app is built with Open Liberty (a Jakarta EE and MicroProfile compatible implementation) and deployed and operated on Red Hat OpenShift, the enterprise distribution of Kubernetes.

This sample application, a simple e-commerce app, will help you apply the [application modernization strategies](/learningpaths/get-started-application-modernization/intro-app-mod/strategies/) and [realize the benefits](/learningpaths/get-started-application-modernization/intro-app-mod/benefits/) of modernizing your applications.

<iframe width="480" height="270" src="https://www.ustream.tv/embed/recorded/130909606" scrolling="no" allowfullscreen webkitallowfullscreen frameborder="0" style="border: 0 none transparent;"></iframe>

## Architecture of legacy application

The sample application was built back in 2008 using a typical 3-tier architecture.

It was a Java EE 6 app that ran on WebSphere Application Server traditional, version 8.5.5, and was deployed to 2 virtual machines.

It was built with EJBs and REST APIs, using the <a href="https://kgb1001001.github.io/cloudadoptionpatterns/Microservices/Backend-For-Frontend/" target="_blank" rel="noopener noreferrer nofollow">_Backends for Frontends_</a> pattern not the <a href="https://en.wikipedia.org/wiki/Representational_state_transfer" target="_blank" rel="noopener noreferrer nofollow">_RESTful API pattern_</a>.  

The sample application essentially had 3 monoliths: a monolithic Db2 database, a monolithic backend (WebSphere Application Server), and a monolithic frontend (built with the Dojo toolkit).  The following architecture diagram shows this 3-tier architecture of the 3 monoliths running in the virtual machines.

![Architecture of legacy sample app](images/legacy-app-arch.png)

In this sample e-commerce app, you can navigate through products in a catalog using a set of categories. Then, you can select a product and add it to your shopping cart.

![UI of the legacy sample app](images/legacy-app-ui.png)

## Architecture of modernized app

I started to modernize the sample application back in the summer of 2020.  

The modernized app is a cloud-native, microservices-based application that uses Open J9 and Open Liberty (Jakarta EE, MicroProfile). A version using Quarkus is also available.

It is deployed to Red Hat OpenShift in multiple containers:  Quarkus or Open Liberty backend, Quarkus Catalog service, micro frontends (navigator, catalog, account, order, shell, and messaging), remaining monolith DB (Db2), Kafka, and Postgres (catalog DB).  The following simplified architecture diagram shows the micro frontends, the microservices, and the remaining monolith running in containers deployed on Red Hat OpenShift.

![Architecture of the modernized app](images/mod-app-arch.png)

The new modernized web application supports the same functionality as the legacy one. For this application modernization effort, the goal was not to improve the UI but instead to modularize the UI to be able to update micro-frontends independently from each other.

![UI of the modernized app](images/mod-app-ui.png)

The following illustration shows the breakdown of the micro-frontends.

![Micro-frontends of the modernized app](images/mod-app-ui.png)

## Results of the modernized app

If we look at the modernized app running in Red Hat OpenShift Container Platform, you can see that you can deploy new functionality separately from each other.  For example, let’s say that you want to add ratings to the products.  You don’t have to touch the remaining monolith and just change everything in the different components:

- Database of catalog service (Postgres)
- Catalog microservice
- Catalog micro frontend

![Results of modernizing app in Red Hat OpenShift Container Platform](images/app-mod-results.png)


## Summary and next steps

Now that you have an understanding of the architecture of the legacy sample application, and an understanding of the architecture of the modernized sample application, watch the following video to review a typical application modernization journey of modernizing just your runtime, modernizing your runtime and operations, or modernizing your architecture, runtime, and operations:

<iframe width="480" height="270" src="https://www.ustream.tv/embed/recorded/130909635" scrolling="no" allowfullscreen webkitallowfullscreen frameborder="0" style="border: 0 none transparent;"></iframe>

Then, you can complete these tutorials in this learning path that show you how to take baby steps in modernizing your legacy applications:

* Containerize your application
* Modernize your application runtimes
* Refactor your monoliths to microservices using the Strangler pattern
* Separate the frontend and develop micro frontends <link to tutorial>

<!-- ADD THIS BACK WHEN YOU ADD THESE TUTORIALS   
    * Build loosely coupled event-drive microservices <link to tutorial>
    * Build a reactive microservices application <link to tutorial> -->