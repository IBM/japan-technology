---
authors: ''
check_date: '2021-09-02'
completed_date: '2019-01-31'
components:
- kubernetes
draft: false
excerpt: Why you should care about containers and how they interact with microservices
  and the cloud.
last_updated: '2020-09-24'
menu_order: 1
meta_description: What are containers, why you should care about them, and how they
  interact with microservices and the cloud.
meta_keywords: what are containers, what is container orchestration
meta_title: What are containers and why should you care? What is a Docker container?
primary_tag: containers
subtitle: Why you should care about containers as a developer
tags:
- microservices
title: What are containers and why do you need them?
---

*"Awww, come on guys, it's so simple. Maybe you need a refresher course. ... It's all ball bearings nowadays." - Fletch, 1985 movie*

Sadly, it is not all about ball bearings nowadays. It's all about containers. If you heard about containers, but are not sure what they are, you've come to the right place. This blog post addresses the following questions:

* Why should I care about containers?
* What are containers?
* Are containers the same as microservices?
* What is an example of a microservices application?
* What is a Docker container?
* What are container orchestration and Kubernetes?
* What is the difference between containers and virtual machine images?
* How can I get started with containers?
* How can IBM Cloud Paks help?
* Where can I run my containers?
* What is Red Hat OpenShift on IBM Cloud?

## Why should I care about containers?

Across organizations, there is a spectrum of container adoption. Many people are just learning about containers. Some companies are further along in their journey. If you're at all considering containerization, it's time to join the fun where you can see real business results:

* **Faster time to market:** New applications and services are what keep your competitive edge. Organizations are able to speed up delivery of new services with development and operational agility.
* **Deployment velocity:** Move quicker from development to deployment. Containerization breaks down barriers for DevOps teams to accelerate deployment times and frequency.
* **IT infrastructure reduction:** Reduce your costs by increasing your application workload density, getting better utilization of your server compute density, and reducing software licensing costs.
* **IT operational efficiency:** Gain more operational efficiency by streamlining and automating the management of diverse applications and infrastructure into a single operating model.
* **Gain freedom of choice:** Package, ship, and run applications on any public or private cloud.

## What are containers?

The best analogy for understanding containers is a shipping container. That's why the majority of all container articles and blog posts show a photo of a shipping container. We're sure you've seen the transport of those big steel shipping containers. (We've also seen some people use them to build houses and swimming pools.) The shipping industry standardized on a consistent size container. Now, the same container can move from a ship to a train to a truck without unloading the cargo. The container contents do not matter.

Just like a shipping container, a software container is a standardized package of software. Everything needed for the software to run is inside the container. The software code, runtime, system tools, system libraries, and settings are all inside a single container.

## Are containers the same thing as microservices?

Once you start diving into containers, it's impossible to avoid reading about microservices. (No, microservices are not those tiny cars you step on in the dark. Those are Micro Machines. Maybe we're dating ourselves?) Microservices is an architectural style. A microservices architecture structures an application by using as a collection of loosely coupled services, which deliver specific business capabilities. Containers help make it happen.

## What is an example of a microservices application?

More than ten years ago, Netflix was one of the first companies to begin using containers extensively. They rewrote the applications that ran their entire video service by using a microservices architecture. In 2017, <a href="https://medium.com/refraction-tech-everything/how-netflix-works-the-hugely-simplified-complex-stuff-that-happens-every-time-you-hit-play-3a40c9be254b/" target="_blank" rel="noopener noreferrer nofollow">Netflix estimated</a> that it employed around 700 microservices to control each of the many functions that make up its service. Let's look at a few (not all 700):

1. **Video selection**: A microservice, in a container, provides your phone, tablet, computer, or TV with the video file to play and at a video quality based on your internet speed.
1. **Viewing history:** One microservice remembers what shows you watch.
1. **Program recommendations:** A microservice takes a look at your viewing history and uses analytics to recommend movies.
1. **Main menu:** One microservice provides the names and images of these movies shown on your main menu.
1. **Billing**: Another microservice deducts the monthly fee from your credit card.

Netflix members <a href="https://research.netflix.com/business-area/streaming/" target="_blank" rel="noopener noreferrer nofollow">stream more than 140 million hours</a> of content every day, with <a href="https://www.nytimes.com/2020/04/21/business/media/netflix-q1-2020-earnings-nflx.html/" target="_blank" rel="noopener noreferrer nofollow">182.8 million subscribers</a> in 190 countries. At this scale, providing entertainment in a matter of a few seconds puts their application to the test. So, yes, containers work for small and the largest of companies.

## What is a Docker container?

Now that you understand what a container is, it's time to introduce you to Docker. (We are not referring to the comfortable Casual Friday pants made by *Dockers*.) Docker is the name of an open source containerization platform that you can use to create and run containers. Docker isn't new, in fact it's been around since 2008. There are other container options, but most believe Docker *won* the container war. (Some of you may remember the Blu-ray vs. HD-DVD standards battle years ago, where Blu-ray was triumphant. Docker is like Blu-ray using this analogy.) Docker allows you to package, ship, and run applications on any public or private cloud. Being able to run applications anywhere helps you avoid vendor lock-in and move to a new environment anytime.

## What are container orchestration and Kubernetes?

There is another critical concept that needs an introduction: orchestration. If you have one container, it is easy to manage. However, as you create more containers, it is crucial to manage them. If you don't, you likely descend into chaos. (Chaos is not good.) Kubernetes saves you from the aforementioned chaos. (Fun fact: Kubernetes is a Greek word meaning helmsman or pilot.) Kubernetes is an open source system that pilots or orchestrates your fancy containerized applications. Think of Kubernetes as the crane that moves and controls your containers.

As we previously mentioned, Kubernetes orchestrates your containers. What does that really mean, though? Kubernetes scales your application up or down. Kubernetes rolls out changes and upgrades to your application. If something goes wrong, Kubernetes rolls back the change and restarts the containers that failed, replaces containers when nodes die, and kills off containers that don't respond to your health check. This management saves resources without sacrificing availability and provides auto load-balancing.

## What is the difference between containers and virtual machine images?

As the name suggests, a virtual machine (VM) is software that emulates a computer system. With a VM, your team can run what appear to be multiple machines on a single computer. If you need to run software on a different type of hardware or operating system, a VM provides that option without using additional hardware.

The primary difference between a container and a VM is that with a VM, the team creates virtual environments – containing operations systems – where different types of software can run. A container, however, isolates the software from the environment and the operating system, enabling it to run almost anywhere.

## How to get started with containers

The best way to start is to start – with one container. There are plenty of benefits with containerizing your applications, but the question is where to start? Or, rather, how to start? Here are three ways:

1. **Migrate and expand:** *Lift-and-shift* is the process of containerizing an on-premises application to lift it (usually from a data center) and then shift it somewhere else, which is usually a public or private cloud. Note that <a href="https://www.ibm.com/cloud/learn/lift-and-shift/" target="_blank" rel="noopener noreferrer">lift and shift</a> is not refactoring or breaking apart your application. It is putting all, or most, of the application into a single container.
2. **Application modernization:** A more aggressive approach is to take your monolithic application and refactor it into microservices containers. This method is moving from one development approach to another.
3. **New development:** Some organizations choose to start all new development by using containers.

## How IBM Cloud Paks help

Beyond containers and Kubernetes, enterprises need to orchestrate their production topology and to provide management, security, and governance for their applications. Enter IBM Cloud Paks.

IBM Cloud Paks are enterprise-ready, containerized software solutions that give an open, faster, and more secure way to move core business applications to any cloud. Each IBM Cloud Pak runs on Red Hat OpenShift on IBM Cloud and Red Hat Enterprise Linux, and includes containerized IBM middleware and common software services for development and management, on top of a common integration layer. The <a href="https://developer.ibm.com/videos/cloud-paks-openshift-explained/" target="_blank" rel="noopener noreferrer">IBM Cloud Paks explained</a> video provides a good overview of the architecture.

Learn more about the <a href="https://www.ibm.com/cloud/paks/" target="_blank" rel="noopener noreferrer">available Cloud Pak solutions</a> for applications, data, integration, automation, multicloud management, and security.

## Where can I run my containers?

Remember, Docker and IBM Cloud Paks allow you to package, ship, and run applications on any public or private cloud. Most organizations today do not lock in with one cloud vendor. This approach a good practice. Eighty-five percent of companies <a href="https://www.ibm.com/thought-leadership/institute-business-value/report/multicloud/" target="_blank" rel="noopener noreferrer">already operate in multicloud environments</a> and the majority of these environments are comprised of multiple hybrid clouds.

There are three different types of cloud environments to consider:

1. **Public cloud:** A public cloud is a multi-tenant environment, but is fully managed and provides usage-based pricing. IBM Cloud, AWS, and Azure are public clouds. You can run your IBM Cloud Paks in any of these clouds.
2. **Dedicated cloud:** A dedicated cloud provides the benefits of a public cloud with dedicated infrastructure. A dedicated cloud meets many industry regulatory requirements. Also, you are not sharing compute capabilities with others.
3. **Private cloud:** A private cloud provides you the benefits of cloud computing, but behind your firewall. Red Hat OpenShift on IBM Cloud is a comprehensive service that offers fully managed OpenShift clusters on the scalable and reliable IBM Cloud platform. You get the keys, but it runs in a secure IBM data center.

## What is Red Hat OpenShift on IBM Cloud?

Containers, Docker, Cloud Paks, and Kubernetes. Yes to all? Red Hat OpenShift on IBM Cloud brings it all together for you, so you can focus on developing and managing your applications. Check out the <a href="https://developer.ibm.com/videos/red-hat-openshift-on-ibm-cloud-video/" target="_blank" rel="noopener noreferrer">guided tour of Red Hat OpenShift on IBM Cloud</a> video to learn how the service manages OpenShift clusters for you. It is directly integrated into the same Kubernetes service that maintains 25 billion on-demand forecasts daily at The Weather Company. That is a lot.

<a href="https://www.ibm.com/cloud/openshift" target="_blank" rel="noopener noreferrer">Get the details</a> of capabilities such as dashboards with a native OpenShift experience, continuous availability with multi-zone clusters, and moving workloads and data more securely. And learn the <a href="https://developer.ibm.com/videos/kubernetes-plus-openshift-video/" target="_blank" rel="noopener noreferrer">difference between Kubernetes and OpenShift</a> in this video.

## Summary

Containers are building blocks for the future. More than a new "bright shiny object," they are here to stay. From delivering applications more quickly, to supercharging development to deployment, to reducing infrastructure and software costs, containers provide both small and large organizations with real business results.