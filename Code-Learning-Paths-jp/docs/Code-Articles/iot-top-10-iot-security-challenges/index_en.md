---
abstract: Explore the security challenges facing IoT developers today, from device
  security, to network security, to application security, and more.
authors: ''
completed_date: '2017-11-17'
draft: false
excerpt: Explore the security challenges facing IoT developers today, from device
  security, to network security, to application security, and more.
ignore_prod: false
last_updated: '2020-03-26'
meta_description: Explore the security challenges facing IoT developers today, from
  device security, to network security, to application security, and more.
meta_keywords: iot, security
meta_title: 'IoT Security Issues: Top 10 Challenges'
primary_tag: iot
related_content:
- slug: iot-anatomy-iot-malware-attack
  type: articles
subtitle: From device security, to network security, to application security, and
  more
tags:
- iot
- security
title: Top 10 IoT security challenges
---

<!-- <sidebar> <heading>Learning path: Building skills in IoT development</heading> <p>This tutorial is part of the IoT 201 learning path, an developer guide for IoT.</p> <ul> <li> [IoT architectures](/articles/iot-lp201-iot-architectures/)</li><li> IoT security challenges (this article)</li> <li>[IoT data analytics](/tutorials/iot-lp301-iot-manage-data) </li><li> [IoT device management](/tutorials/iot-lp301-device-management)</li> <li> [Tutorial: Build a door monitoring system](/tutorials/iot-lp201-build-door-monitoring-system)</li></ul></sidebar> -->

As more and more IoT devices make their way into the world, deployed in uncontrolled, complex, and often hostile environments, securing IoT systems presents a number of unique challenges. According to [Eclipse IoT Working Group’s 2017 IoT developer survey](https://ianskerrett.wordpress.com/2017/04/19/iot-developer-trends-2017-edition/), security is the top concern for IoT developers.

Follow along as we describe my top ten challenges for IoT security:

1. Secure constrained devices
1. Authorize and authenticate devices
1. Manage device updates
1. Secure communication
1. Ensure data privacy and integrity
1. Secure web, mobile, and cloud applications
1. Ensure high availability
1. Prevent incidents by detecting vulnerabilities
1. Manage vulnerabilities
1. Predict and preempt security issues

## 1 Secure constrained devices

Many IoT devices have limited amounts of storage, memory, and processing capability and they often need to be able to operate on lower power, for example, when running on batteries.

Security approaches that rely heavily on encryption are not a good fit for these constrained devices, because they are not capable of performing complex encryption and decryption quickly enough to be able to transmit data securely in real-time.

These devices are often vulnerable to side-channel attacks, such as [power analysis attacks](https://en.wikipedia.org/wiki/Power_analysis), that can be used to reverse engineer these algorithms. Instead, constrained devices typically only employ fast, [lightweight encryption algorithms](https://www.researchgate.net/publication/329072888_A_Survey_of_Lightweight_Cryptographic_Algorithms_for_IoT-Based_Applications_Proceedings_of_ICSICCS-2018).

IoT systems should make use of multiple layers of defense, for example, segregating devices onto separate networks and using firewalls, to compensate for these device limitations.


## 2 Authorize and authenticate devices

With so many devices offering potential points of entry within an IoT system, device authentication and authorization is critical for securing IoT systems.

Devices must establish their identity before they can access gateways and upstream services and apps. However, there are many IoT devices that fall down when it comes to device authentication, for example, by using weak basic password authentication or using passwords unchanged from their default values.

Adopting an [IoT Platform](/articles/iot-lp101-why-use-iot-platform/) that provides security by default helps to resolve these issues, for example by enabling two factor authentication (2FA) and enforcing the use of strong passwords or certificates. IoT Platforms also provide device authorization services used to determine which services, apps, or resources that each device has access to throughout the system.

## 3 Manage device updates

Applying updates, including security patches, to firmware or software that runs on IoT devices and gateways presents a number of challenges. For example, you need to keep track of which updates are available, apply them synchronously across distributed environments with heterogeneous devices that communicate through a range of different networking protocols. You have to implement a graceful rollback-strategy in case the update fails.

Not all devices support over-the-air updates, or updates without downtime, so devices might need to be physically accessed or temporarily pulled from production to apply updates. Also, updates might not be available for all devices, particularly older devices or those devices that are no longer supported by their manufacturer.

Even when updates are available, the owners of a device might opt out of applying an update, so maintaining backward-compatibility is important. As part of your device management, you need to keep track of the versions that are deployed on each device and which devices are candidates for retirement after updates are no longer available.

Device manager systems often support pushing out updates automatically to devices as well as managing rollbacks if the update process fails. They can also help to ensure that only legitimate updates are applied, for example through the use of digital signing.

## 4 Secure communication

Once the devices themselves are secured, the next IoT security challenge is to ensure that communication across the network between devices and cloud services or apps is secure.

Many IoT devices don’t encrypt messages before sending them over the network. However, best practice is to use transport encryption and to adopt standards like TLS. Using separate networks to isolate devices also helps with establishing secure, private communication, so that data transmitted remains confidential. Common measures include using Firewalls, restricting physical access to gateway devices, using randomly generated one-time-password, and turn off the OS features that aren't required by the device.

## 5 Ensure data privacy and integrity

It is also important that wherever the data ends up after it has been transmitted across the network, it is stored and processed securely. Implementing data privacy includes redacting or anonymizing sensitive data before it is stored or using data separation to decouple personally identifiable information from IoT data payloads. Data that is no longer required should be disposed of securely, and if data is stored, maintaining compliance with legal and regulatory frameworks is also an important challenge. There has been an increased interest in developing systems that enable [federated machine learning](https://en.wikipedia.org/wiki/Federated_learning), where the data stays local to the device and the machine learning work happens at edge, with only the learnings/insights being shared with the cloud. The essence of such systems is that the algorithm should come to the data instead of the conventional methods where all the data goes to the algorithm.

Ensuring data integrity, which may involve employing checksums or digital signatures to ensure data has not been modified. Blockchain – as a decentralized distributed ledger for IoT data – offers a scalable and resilient approach for ensuring the integrity of IoT data.

Read more about [what blockchain means for IoT](https://www.ibm.com/blogs/internet-of-things/watson-iot-blockchain/) in this blog post.

## 6 Secure web, mobile, and cloud applications

Web, mobile, and cloud apps and services are used to manage, access, and process IoT devices and data, so they must also be secured as part of a multi-layered approach to IoT security. All the standard practices to secure mobile and web apps should be followed.

When developing IoT applications, be sure to apply secure engineering practices to avoid vulnerabilities such as the [OWASP top 10 vulnerabilities](https://owasp.org/www-project-top-ten/). Just like devices, apps should also support secure authentication, both for the apps themselves and the users of the applications, by providing options such as 2FA and secure password recovery options.

## 7 Ensure high availability

As we come to rely more on IoT within our day-to-day lives, IoT developers must consider the availability of IoT data and the web and mobile apps that rely on that data as well as our access to the physical things managed by IoT systems. The potential for disruption as a result of connectivity outages or device failures, or arising as a result of attacks like  [denial of service attacks](/articles/iot-anatomy-iot-malware-attack/), is more than just inconvenience. In some applications, the impact of the lack of availability could mean loss of revenue, damage to equipment, or even loss of life.

For example, in connected cities, IoT infrastructure is responsible for essential services such as traffic control, and in healthcare, IoT devices include pacemakers and insulin pumps. To ensure high availability, IoT devices must be protected against cyber-attacks as well as physical tampering. IoT systems must include redundancy to eliminate single points of failure, and should also be designed to be resilient and fault tolerant, so that they can adapt and recover quickly when problems do arise. Since most IoT systems are distributed in nature, an important thing to keep in mind is the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) (A distributed computer system can have at most two properties out of high availability, consistency, and tolerance to network partition).

## 8 Prevent incidents by detecting vulnerabilities

Despite best efforts, security vulnerabilities and breaches are inevitable. How do you know if your IoT system has been compromised? In large scale IoT systems, the complexity of the system in terms of the number of devices connected, and the variety of devices, apps, services, and communication protocols involved, can make it difficult to identify when an incident has occurred. Strategies for detecting vulnerabilities and breaches include monitoring network communications and activity logs for anomalies, engaging in penetration testing and ethical hacking to expose vulnerabilities, and applying [security intelligence and analytics](https://www.ibm.com/security/security-intelligence/) to identify and notify when incidents occur.

Read more about how to [protect your IoT devices from malware attacks](/articles//iot-anatomy-iot-malware-attack/).

## 9 Manage vulnerabilities

The complexity of IoT systems also makes it challenging to assess the repercussions of a vulnerability or the extent of a breach in order to manage its impact. Challenges include identifying which devices were affected, what data or services were accessed or compromised and which users were impacted, and then taking immediate actions to resolve the situation.

Device managers maintain a register of devices, which can be used to temporarily disable or isolate affected devices until they can be patched. This feature is particularly important for key devices (such as gateway devices) in order to limit their potential to cause harm or disruption, such as by flooding the system with fake data if they have been compromised. Actions can be applied automatically using a rules engine with rules based on vulnerability management policies.


## 10 Predict and preempt security issues

A longer-term IoT security challenge is to apply security intelligence not only for detecting and mitigating issues as they occur, but also to predict and proactively protect against potential security threats. [Threat modeling](https://owasp.org/www-community/Threat_Modeling) is one approach used to predict security issues. Other approaches include applying monitoring and analytics tools to correlate events and visualize unfolding threats in real-time, as well as applying AI to adaptively adjust security strategies applied based on the effectiveness of previous actions. The essence is to minimize human intervention and offload as much work as possible to algorithms since continuous manual examination is almost impossible.

## Conclusion

Adopting a multi-layered security-by-design approach to IoT development is essential for securely managing devices, data, and mobile and cloud-based IoT apps and services, as well as dealing with threats or issues as they arise. Repercussions of neglecting security in IoT systems can lead to system failures, loss of capital, and even damage.

Incorporating security by default – where security features are configured at their most secure settings at all times, including before, during, and after development enables you to maintain data privacy and integrity, while delivering highly available IoT data, apps, and services.