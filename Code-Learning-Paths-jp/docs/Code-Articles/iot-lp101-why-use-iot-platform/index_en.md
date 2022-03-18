---
abstract: This article explores the key capabilities of IoT platforms and considers
  the top general-purpose end-to-end IoT platforms. You'll learn why you should adopt
  an IoT platform to rapidly develop your IoT solutions and quickly get the most value
  from your IoT data.
also_found_in:
- learningpaths/iot-getting-started-iot-development/
authors: ''
completed_date: '2017-06-05'
draft: false
duration: 1 hour
excerpt: Explore the key capabilities of IoT platforms and examine the top general-purpose
  end-to-end IoT platforms.
ignore_prod: false
last_updated: '2020-01-31'
meta_description: Explore the key capabilities of IoT platforms and examine the top
  general-purpose end-to-end IoT platforms.
meta_keywords: IoT, IoT platforms
primary_tag: iot
related_content:
- slug: iot-getting-started-iot-development
  type: learningpaths
- slug: iot-next-steps-iot-development
  type: learningpaths
subtitle: A guide to help you understand why you should you use an IoT Platform
tags:
- iot
title: Streamlining the development of your IoT applications by using an IoT platform
---

<!-- <sidebar> <heading>Learning path: Getting started with IoT development</heading> <p>This article is part of the IoT 101 learning path, a quick-start guide for IoT developers.</p> <ul> <li> [IoT concepts and skills](/articles/iot-key-concepts-skills-get-started-iot)</li> <li>[IoT hardware guide](/articles/iot-lp101-best-hardware-devices-iot-project)</li> <li> [IoT networking guide](/articles/iot-lp101-connectivity-network-protocols/)</li> <li> IoT platforms (this article)</li> <li> [Tutorial: Build a smart doorbell](/tutorials/iot-lp101-get-started-develop-iot-home-automation/)</li></ul></sidebar> -->

Developing and deploying IoT systems is complex&mdash;it involves coordinating a diverse range of connected devices, networks, cloud services, and mobile and web applications.

IoT platforms provide middleware to connect and manage hardware devices and the data that they collect with user-facing mobile and web applications. These IoT platforms are typically designed to establish secure communication between devices, apps, and services. They also make it faster and easier to develop and deploy IoT applications. IoT platforms are designed to be scalable and reliable. For example, they implement fault tolerance so that your IoT systems will continue to operate in the face of device, network, or cloud service failures. By leveraging standards and providing well documented APIs and SDKs, IoT platforms enable you to integrate heterogeneous devices, apps, and services into your IoT system, providing you with the flexibility to customize and substitute components as requirements change.

The Internet of Things is evolving at a rapid pace, so you'll need to develop your IoT applications quickly and efficiently to minimize time to market and remain competitive. Although each IoT initiative comes with its own set of unique requirements, most IoT projects share some common requirements for the management of connected devices and the communication, storage, and analysis of the data that they generate. IoT platforms address these fundamental requirements by providing generic, customizable tools and services and also the [abstractions](https://developer.ibm.com/iotplatform/2017/01/17/iot-platform-vs-iot-infrastructure/) that you can build upon when you develop your custom IoT solutions.

By exploring the key capabilities of IoT platforms and considering the top general-purpose end-to-end IoT platforms, you will come to realize why you should adopt an IoT platform to rapidly develop your IoT solutions and quickly get the most value from your IoT data.

## IoT platform capabilities

Consider these key IoT platform capabilities:

* Device management
* Data communication protocols
* Data storage
* Rules and analytics
* Rapid application development and deployment
* Integration
* Security
* Cost of developing and maintaining the solutions that you build with the IoT platform.

The relative importance of each capability depends on requirements. For example, for a small-scale home automation system, device management is not a primary concern. There are few devices to manage. A home automation is mostly reactive. It is less important for the IoT platform to provide data storage and data analytics capabilities to store and analyze historical sensor readings. However, the IoT platform must support fast and reliable data communication protocols to ensure events that sensors detect are not missed and responded to in real time. And yet, for an industrial IoT application that involves thousands of sensors that monitor industrial equipment for failure, wear, and inferior performance, device management and analytics capabilities of the IoT platform is much more important.

### Device management

 <sidebar> <p>Read more about managing IoT devices in my article, "[Choosing the best hardware for your next IoT project](/articles/iot-lp101-best-hardware-devices-iot-project)."</p></sidebar>

 One of the core functions of an IoT platform is managing its devices. Device management occurs throughout the entire lifecycle of each IoT device. This includes provisioning of new devices, monitoring and maintaining operating devices, and eventually decommissioning devices at the end of their useful life. IoT platforms allow device registration management, configuration, and over-the-air updates. With the proper IoT Platform, you can receive alerts for the device status and monitor  device analytics and usage, and know its overall condition and health. IoT platforms may provide remote debugging  when things go wrong. IoT platforms may also allow asset management, including the ability to inventory and find connected devices and their metadata.

 It is also quite important for IoT platforms to be "device agnostic" and   integrate with existing Enterprise Resource Planning (ERP) systems.

### Data communication protocols

 <sidebar> <p>Read more about IoT networking protocols in my article, "[Connecting all the things in the Internet of Things](/articles/iot-lp101-connectivity-network-protocols)."</p></sidebar>

Secure and reliable communication between IoT devices, gateways, and cloud-based apps and services, are all essential to enable remote device management and their connections, in order to ensure proper and continuous data gathering and transmission. While some data may be stored and processed locally with edge analytics, much  data that is collected remotely using sensors and other IoT devices. Therefore cloud services and  apps upstream may be required for necessary aggregation, processing, and even visualization. Thousands of devices are often connected within a single IoT system, and many IoT platforms incorporate message broker services to enable devices and gateways to send and receive messages with low latency and at scale. These message broker services usually use standard communication protocols like MQTT, CoAP, or XMPP, while some platforms support web sockets for real-time communication.

### Data storage

With billions of connected devices generating data at an unprecedented rate, where to store the vast quantities of data is another consideration in selecting an IoT platform. Data lakes store data in a variety of formats, including raw, semi-structured, or structured. These data lakes are often built on top of NoSQL or Hadoop technologies for maximum flexibility and scalability. Data lakes and other data stores are highly available, support concurrent reads and writes, and include configurable indexes to improve performance when your IoT app accesses and queries data.

### Rules and Analytics

Once the data is reliably stored, you must be able to analyze it. Many IoT platforms offer analytics capabilities that include real-time and batch processing. A rules engine performs real-time data analytics for actionable insights. Rules encoding the conditions trigger actions. Some platforms provide turnkey analytics applications. Other platforms offer flexibility to customize reports, analytics, dashboards, and data visualizations.

### Rapid application development and deployment

Speed of development and delivery of purpose-built applications is a key concern for an IoT platform. Select an IoT platform that provides code boilerplate generation tools, templates or widgets for rapid development, and tools to streamline and automate deployment.

### Integration

Interoperability is another important consideration. A wide variety of connected devices and IoT-related services exist. Billions more will be online in the coming years. Rapidly future-proofing your IoT system is essential. IoT platforms achieve this interoperability by adopting standards and  providing additional layers of abstraction and normalization over the underlying technologies. For example, your applications are less likely to break if you upgrade your IoT devices as required to use a sensor with a higher resolution when integrating with other platforms, devices, web services, tools, and applications through SDKs and APIs - with REST APIs being particularly common.

### Security

Security is an integral part of the design of any IoT solution. Security includes securing devices and networks along with cloud and application-level security. Choose an IoT platform that provides authentication and authorization services, preferably with integration, to existing systems that are used for identity management like LDAP. Consider adopting standards such as X.509 for device authentication. For secure communication, adopt a standard like TLS for encrypting content and ensuring data integrity. IoT platforms might also implement role-based access control for users, devices, gateways, and services, as well as providing security monitoring and auditing tools.

### Cost

Speeding up development of IoT solutions is one of the main benefits of adopting an IoT platform, however an IoT platform can also help to reduce development costs. Ongoing costs, like subscription fees for accessing a hosted IoT platform or hosting costs for a self-hosted platform, will typically be less than the cost of developing and maintaining custom-made in-house solutions. Many IoT platforms offer free trial periods or low usage tiers that you can use to get started with almost no upfront expenditure but be sure to factor in how those costs will change after the initial trial is over.

## Comparing IoT platforms

There are hundreds of IoT platforms available from a range of vendors. Some platforms are highly specialized, for example, only catering to one market vertical like GE Predix ([https://www.predix.io/)](https://www.predix.io/)), a PaaS IoT platform aimed specifically at Industrial IoT. Other IoT platforms are focused on providing only a subset of the functions that might be required for your IoT system, rather than an end-to-end IoT platform solution, for example, Cisco and SAS Edge-to-Enterprise IoT Analytics Platform, which is focused on IoT analytics only. As a result, you might choose to adopt more than one IoT platform.

As a starting point, here are five popular general-purpose end-to-end IoT platforms that are suitable for a wide range of applications:

<!-- USED GENERIC IOT PROD LINK -->
* **[IBM Watson IoT](https://www.ibm.com/cloud/internet-of-things)** <br/>
  Built on top of the IBM Cloud platform, IBM Watson IoT is a mature, developer-friendly IoT platform with strengths in real-time analytics and cognitive computing. The platform also supports device management, authentication and authorization, secure data storage and communication, standard communication protocols like MQTT and HTTPS, rules, REST APIs and SDKs.
* **[Amazon Web Services IoT](https://aws.amazon.com/iot-platform/how-it-works/)** <br/> AWS IoT is a highly scalable IoT platform. It includes an SDK, authentication and authorization, device registry, a device gateway that communicates with devices using MQTT, WebSockets or HTTP, and a rules engine that integrates with existing AWS services like DynamoDB. An interesting feature of AWS IoT is “device shadows,” which is a persistent virtual version of each device including the last known state of the device.
* **[Microsoft Azure IoT Suite](https://www.microsoft.com/en-au/internet-of-things/azure-iot-suite)** <br/> The Microsoft Azure IoT Suite is another comprehensive IoT platform, which includes support for device management and device twins (like device shadowing) by using Azure IoT Hub, standard communication protocols including MQTT, AMQP, and HTTP, secure storage, rules, and analytics engines supporting predictive analysis and data visualization.
* **[ThingWorx](https://www.thingworx.com/)** <br/>  PTC ThingWorx is an enterprise IoT platform that supports model-driven rapid application development. Features include device management, application modeling, support for standard protocols including MQTT, AMQP, XMPP, CoAP, and WebSockets and predictive analytics, as well as REST APIs and SDKs to support integration.
* **[Kaa](https://www.kaaproject.org/)** <br/> Kaa is a free open source IoT platform that is published under an Apache 2.0 license, which allows the platform to be self-hosted. Kaa includes REST APIs and SDKs for Java, C++, and C, with features for device management, data collection, configuration management, notifications, load balancing, and data analysis.

## Summary

With so many different IoT platforms to choose from, selecting a platform may seem daunting. Consider your requirements against the capabilities of each platform to select the best match for your business. Adopting the right IoT platform can simplify, accelerate, and streamline the development of your next IoT project. With the right IoT platform, you can focus on unique requirements deliver the most value to your customers in the least time.