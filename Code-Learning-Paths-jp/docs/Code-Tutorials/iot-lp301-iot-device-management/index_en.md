---
abstract: In this article, discover how the IoT device management protocols and features
  help you address many IoT device management challenges, including scalability and
  availability among others.
authors: ''
completed_date: '2017-12-22'
draft: false
excerpt: Learn how IoT device management protocols and features help you address many
  device management challenges, including scalability and availability.
ignore_prod: false
last_updated: '2020-03-26'
meta_description: Learn how IoT device management protocols and features help you
  address many device management challenges, including scalability and availability.
meta_keywords: IoT, devices, device management
primary_tag: iot
related_content:
- slug: iot-lp101-getting-started
  type: series
subtitle: A guide to selecting IoT device management protocols and features that solve
  your IoT device management challenges
tags:
- iot
title: Managing your IoT devices
type: tutorial
---

<!-- <sidebar> <heading>Learning path: Building skills in IoT development</heading> <p>This tutorial is part of the IoT 201 learning path, an developer guide for IoT.</p> <ul> <li> [IoT architectures](/articles/iot-lp201-iot-architectures/)</li><li> [IoT security challenges](/articles/iot-top-10-iot-security-challenges/)</li> <li>[IoT data analytics](/tutorials/iot-lp301-iot-manage-data) </li><li> IoT device management (this article)</li> <li> [Tutorial: Build a door monitoring system](/tutorials/iot-lp201-build-door-monitoring-system)</li></ul></sidebar> -->

Any complex IoT system might contain a lot of devices, and must include device management capabilities in its architecture. IoT devices are often deployed in hostile environments. They need to be monitored actively, and when they fail, they might need to be retired or updated so that they can continue to operate in those environments.

Device management helps to protect devices and their data by making it easier to secure and monitor the devices. Device management capabilities allow IoT developers to control IoT devices by performing operations such as resetting the devices to factory defaults or applying updates to patch security issues or fix bugs.

Because the devices might communicate with different protocols and data formats, the complexity of IoT systems increases with increase in the number of devices, which makes managing IoT devices even more critical and challenging.

## Device management challenges

The key challenges involved with managing and maintaining IoT devices include security, interoperability, constrained devices, scalability, and availability.

### Security

Security is an important consideration across all layers of your IoT system. Device management services can make it easier to manage the security IoT devices themselves by providing secure device registration and authentication services and by supporting encrypted machine-to-machine (M2M) communication. This typically includes incorporating standard security measures like SSL, access tokens, etc. at all the layers of your architecture. Read more in our [Top 10 IoT Security Challenges](/learningpaths/iot-next-steps-iot-development/iot-security/) article and how implementing device management services in your IoT system can address many of these security challenges.

### Interoperability

The devices deployed within an IoT system now and into the future might be of different classes, be produced by a range of manufacturers, and use a range of communication protocols. Device management tools must support managing all of the devices consistently to maintain interoperability across heterogeneous devices. Look for device management services that support standard device management protocols, or which implement protocols and APIs to provide abstractions for managing devices generically in bulk. For long term support, try to follow reference IoT architectures, and adhere to industry standard data transfer protocols like MQTT or more higher-level device-management oriented protocols like LMW2M, OMA-DM and TR-069.

### Constrained devices

IoT devices are often constrained, which means they have limited power, memory, processing capability, or connectivity. (Read more about IoT devices in this [IoT hardware guide](/articles/iot-lp101-best-hardware-devices-iot-project/).) These constraints affect whether the device is capable of being managed remotely, and how effectively it can apply remote operations. If a device is powered by a battery, it is vital that the device be able to communicate with the device manager and perform updates or operations without exhausting the power available. If the power supply is exhausted and then an operation such as a factory reset or firmware update is interrupted, it could result in bricking the device.

Lightweight device management protocols (the ones with less resource overhead) like <a href="https://en.wikipedia.org/wiki/OMA_LWM2M" target="_blank" rel="noopener noreferrer nofollow">_LWM-2M_</a> can be a good choice, as they are designed to be efficient and minimize the amount of processing that needs to be performed by the device itself. These lightweight device management protocols require less bandwidth and frequency of communication between the device and the upstream management services, hence conserving resources like computation power and battery. The disadvantage with lightweight protocols can be that you may have to depend on proprietary implementation for some advanced device management capabilities and measures like handling data transfer errors, reliability, and security.

### Scalability

As more devices are added to the system, device management services need to scale to handle larger numbers of devices that are registering and communicating with the device management service. Device management services need to be able to handle the increased number of routine device management operations that will need to be performed at any given time.

For instance, a complex IoT system might have thousands of devices of different kinds (sensors, actuators) connected over different networks in different geographical areas of the world. Since some of these devices may be interdependent, some of the system updates will have to be done in a synchronized manner. In such cases, it becomes impossible to monitor and manage the devices manually. You need high-level functionalities like remote controlling in groups, changing device state remotely, provisioning new devices, device-discovery, and so on. Thus, automation becomes key to scaling device management for IoT.


### Availability

Device management services must be aware of the device as well as network context in order to ensure availability. Device management includes monitoring the current state of devices to prevent incidents like reboot of a device while it is in the middle of an update, or applying updates to a device which is low on battery. It also includes broader awareness of the state of the network, awareness of the device’s status and available power, or what the current device usage looks like before performing maintenance operations. Device management services should support synchronizing management for operations like firmware updates and system reset to prevent any deadlocks and minimize disruption.

## Device management protocols

Many of these device management challenges can be addressed by adopting standard device management protocols or by making use of device management services provided by an IoT platform. (Read more about [why you might need to use an IoT platform](/articles/iot-lp101-why-use-iot-platform/) in your IoT solutions in my previous IBM Developer article.)

IoT devices typically perform machine-to-machine (M2M) communication over lightweight connectivity protocols like <a href="https://en.wikipedia.org/wiki/XMPP" target="_blank" rel="noopener noreferrer nofollow">_XMPP_</a> (an XML-based chat protocol), <a href="https://en.wikipedia.org/wiki/Constrained_Application_Protocol" target="_blank" rel="noopener noreferrer nofollow">_CoAP_</a> (Constrained Application Protocol), or <a href="https://mqtt.org/" target="_blank" rel="noopener noreferrer nofollow">_MQTT_</a> (MQ Telemetry Transport). Read more about IoT communication protocols in this [connectivity and network protocols guide](/articles/iot-lp101-connectivity-network-protocols/).

Device management protocols operate over the top of these general connectivity protocols, to support device registration, authentication, querying device capabilities, and performing operations consistently across devices.

Standardized device management protocols that have been applied to IoT devices from the broadband and mobile industries include TR-069, OMA DM and LWM2M:

* **TR-069.** The BroadBand Forum's <a href="https://www.broadband-forum.org/wp-content/uploads/2018/11/TR-069.pdf" target="_blank" rel="noopener noreferrer nofollow">_TR-069 Customer Premises Equipment (CPE) WAN Management Protocol (CWMP)_</a> was originally developed in 2004, based on SOAP, for managing broadband equipment including modems, routers, gateways, and home devices including set-top boxes. This protocol has been applied within IoT smart home applications.
* **TR-369 (USP)**. The <a href="https://usp.technology/" target="_blank" rel="noopener noreferrer nofollow">_TR-369 User Services Platform protocol_</a> is an expanded version of TR-069 that is more oriented towards IoT. According to their site, it's a natural evolution of TR-069, and uses an expanded version of the Device:2 Data Model to represent device operations (firmware upgrades, reboots, etc.), network interfaces, and service functions (IoT functions, VoIP, etc.).
* **OMA DM.** The <a href="https://openmobilealliance.org/wp/Overviews/dm_overview.html" target="_blank" rel="noopener noreferrer nofollow">_Open Mobile Alliance Device Management (OMA DM)_</a> specification was the predecessor of LWM2M, developed for mobile phones, PDAs, and tablets, and was first released in 2003. It is designed for constrained devices that have limited bandwidth, and supports M2M communication over a range of protocols including HTTP, WAP, or SMS. It can be applied to IoT devices to support provisioning, configuration, firmware updates, and fault management. However, it is not as lightweight as LWM2M.
* **LWM2M.** OMA's <a href="https://www.openmobilealliance.org/wp/Overviews/lightweightm2m_overview.html" target="_blank" rel="noopener noreferrer nofollow">_Lightweight Machine to Machine (LWM2M)_</a> protocol is designed to manage devices communicating over cellular networks, for example, within a sensor network. LWM2M is usually implemented over CoAP. There are a number of open source implementations of clients and servers that support the LWM2M protocol, including <a href="https://www.mbed.com/en/" target="_blank" rel="noopener noreferrer nofollow">_ARM mbed_</a> and Eclipse <a href="https://projects.eclipse.org/projects/iot.leshan" target="_blank" rel="noopener noreferrer nofollow">_Leshan_</a> and <a href="https://www.eclipse.org/wakaama/" target="_blank" rel="noopener noreferrer nofollow">_Wakaama_</a>.

IoT device management is an area of active standardization, so this area remains quite fragmented. Many [IoT reference architectures](/learningpaths/iot-next-steps-iot-development/iot-architectures/) describe device management features, and most IoT platforms, such as the IBM Watson IoT Platform, implement custom device management services that have been tailored to the requirements of managing IoT devices for use with the specific platform.

<!-- Commented this out because this service is no longer available? -->
<!-- The [IBM Watson IoT Platform Device Management protocol](https://cloud.ibm.com/docs/services/IoT/devices/device_mgmt) is a lightweight device management protocol that operates over MQTT. The IBM Watson IoT platform supports both managed and unmanaged devices. Managed devices run a device management agent, which includes the logic for connecting to and communicating with the Watson IoT Platform's device management service. -->

## Device management features

IoT platforms typically provide APIs and dashboards for their device management. These dashboards and APIs can be used to manage device registration, trigger remote operations, and to monitor, search for, or filter devices (for example, by manufacturer or serial number).

Whether you are considering adopting device management provided by an IoT platform, a standalone service (for example an Eclipse <a href="https://projects.eclipse.org/projects/iot.leshan" target="_blank" rel="noopener noreferrer nofollow">_Leshan_</a> server), that implements a standard device management protocol, or a combination of device management services, key features to look for include:

* **Provisioning.** When a new device is added to the system, the device should securely register itself with the device management service, as well as registering the metadata for the device. Registering the device provides it with identity and credentials.
* **Authentication.** Authentication services establish the identity of devices. The device uses the identity created initially during the provisioning process, so that whenever it communicates with other devices, apps or services, the other party can be assured that the device is a trusted, authentic device.
* **Configuration.** Device management services typically support applying new configurations to IoT devices directly or by broadcasting new configurations to update devices in bulk, as well as managing device configuration dependencies.
* **Monitoring & diagnostics.** Device management services are also responsible for keeping track of device logs and metadata, for example, a service might track device capabilities, firmware version, the usual location of the device, device ID and status. Device management services often expose this information, along with error and connectivity logs through dashboards or APIs to use for monitoring health and status as well as for diagnostics and remote debugging. The logs and status can also be used to generate alerts, for example, if the device has not produced any data for a certain period of time.
* **Scheduling remote operations.** Many device management services support scheduling remote operations, including device reboot, enabling or disabling the device, performing a factory reset and triggering a new firmware download and update through over the air updates. Being able to perform these maintenance operations remotely without manual intervention, helps to save time and money throughout the life of the device, as well as helping to avoid mistakes and minimize device downtime throughout the process. It also removes the need to manually retrieve or update devices installed in locations that are difficult to access physically.
* **Automation.** Automation becomes a necessity when the number and range of devices deployed within an IoT system starts to scale. Automation helps to simplify applying remote operations in bulk, for example to rapidly perform a firmware update on multiple devices to address a security vulnerability. Depending on the device, these updates might be applied through specialized device management protocols, however for Linux-based devices, Open Source orchestration tools like Kubernetes can be used to deploy [Docker containers](/articles/iot-docker-containers/) containing firmware, applications or operating environments across multiple devices.
* **Retirement.** Devices eventually fail, or are superseded when they come to the end of their service life. Device management services should support decommissioning devices securely, including revoking any tokens and identities associated with the device so that it is no longer able to communicate with other devices, apps or services within the system.

## Conclusion

Device management services help to automate the management of IoT devices throughout their lifecycle – including provisioning, authentication, configuration, maintenance operations, monitoring, and eventually decommissioning. Device management is a critical component for any scalable, secure and interoperable IoT solution.