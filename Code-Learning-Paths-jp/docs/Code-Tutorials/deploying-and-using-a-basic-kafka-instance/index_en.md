---
also_found_in:
- learningpaths/develop-kafka-apps/
- learningpaths/ibm-event-streams-badge/
authors: ''
check_date: '2021-05-31'
completed_date: '2020-06-04'
components:
- kafka
display_in_listing: true
draft: false
excerpt: In this tutorial, we’ll show you just how easy it is to deploy a Kafka instance
  using IBM Event Streams on IBM Cloud service and then connect and run one of the
  sample applications.
ignore_prod: false
last_updated: '2020-12-09'
primary_tag: kafka
related_content:
- slug: an-introduction-to-apache-kafka
  type: articles
- slug: running-a-compliant-kafka-service
  type: articles
related_links:
- title: Apache Kafka Documentation
  url: https://kafka.apache.org/documentation/
- title: Apache Kafka Quickstart
  url: https://kafka.apache.org/quickstart
subtitle: Use IBM Event Streams on IBM Cloud to deploy a Kafka instance and connect
  and use your first Kafka app
tags:
- messaging
title: Deploying and using a basic Kafka instance
---

To get started quickly using Apache Kafka, you need to deploy a Kafka instance and be able to connect and run a sample Kafka application.

While you can certainly [download and install an Apache Kafka instance on your local system](https://kafka.apache.org/quickstart), the [IBM Event Streams on IBM Cloud service](https://cloud.ibm.com/catalog/services/event-streams?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg) is a fully managed Apache Kafka instance.  

In this tutorial, we’ll show you just how easy it is to deploy a Kafka instance using IBM Event Streams on IBM Cloud service and then connect and run one of the sample applications.

## Prerequisites

* General knowledge about [Apache Kafka](/learningpaths/develop-kafka-apps/introduction/intro-to-kafka/)
* [IBM Cloud account](https://cloud.ibm.com/registration?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)
* For the [sample application](https://github.com/ibm-messaging/event-streams-samples), you must also have installed: Git, Gradle, and Java 8 or higher.

## Steps

<sidebar>Because the IBM Event Streams Lite plan limits you to using a single partition, it is not suitable for production use. You can [review the different plans](https://cloud.ibm.com/docs/EventStreams?topic=eventstreams-plan_choose) in the documentation.</sidebar>

For this tutorial, for our Kafka instance, we use the Event Streams on IBM Cloud.

To deploy a Kafka instance and connect and use a Kafka app, you’ll need to complete these steps:

1. To deploy a managed Kafka instance, create an Event Streams on IBM Cloud service instance.

2. To connect and use a Kafka app in your managed Kafka instance, you need to:

    * Create a topic
    * Create credentials
    * Clone the Github repo for the sample app
    * Run the consuming app
    * Run the producing app

3. Delete the topic

These steps are demonstrated for you in the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/XyNy7TcfJOc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

These steps are also detailed in the [IBM Event Streams for IBM Cloud getting started tutorial](https://cloud.ibm.com/docs/EventStreams?topic=eventstreams-getting_started).

## Summary

Congratulations! You have now successfully created an instance of IBM Event Streams on Cloud and run your first sample Kafka application.

In general, for ongoing development, you will need to run against a standard instance of IBM Event Streams on Cloud. You can upgrade the Lite instance you created in this tutorial to a Standard instance.