---
authors: ''
check_date: '2021-11-15'
completed_date: '2020-12-09'
components:
- kafka
display_in_listing: true
draft: false
excerpt: In this article, we present some top tips for implementing, debugging, and
  operating applications with Event Streams.
ignore_prod: false
meta_description: In this article, we present some top tips for implementing, debugging,
  and operating applications with Event Streams.
meta_keywords: kafka, tips and tricks, debugging, event streams
meta_title: IBM Event Streams cheat sheet for developers
primary_tag: kafka
related_content:
- slug: get-started-with-apache-kafka
  type: tutorials
subtitle: Tips and tricks for easy debugging of common IBM Event Streams Errors
tags:
- messaging
title: IBM Event Streams cheat sheet for developers
---

<!-- <sidebar> <heading>Learning path: IBM Event Streams Developer Essentials Badge</heading> <p>This article is part of the IBM Event Streams Developer Essentials learning path and badge.</p> <ul><li>[IBM Event Streams fundamentals](/articles/event-streams-fundamentals)</li><li>[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals)</li><li>[Deploying and using a basic Kafka instance](/tutorials/deploying-and-using-a-basic-kafka-instance)</li><li>[Get hands on experience](/tutorials/event-streams-hands-on-java-sample)</li><li>[Take on the coding challenge](/tutorials/event-streams-badge-event-streams-dev-challenge)</li><li>[Debug your app](/articles/event-streams-dev-cheat-sheet)</li></ul></sidebar> -->

In this article, we present some top tips for implementing, debugging, and operating applications with Event Streams.

## Enable Sysdig Monitoring

Event Streams supports [IBM Cloud Monitoring with Sysdig](https://cloud.ibm.com/docs/Monitoring-with-Sysdig?topic=Sysdig-getting-started#getting-started). You can use Sysdig to monitor a number of metrics to gain operational visibility into the performance and health of your applications, services, and platforms. It offers administrators, DevOps teams, and developers full stack telemetry with advanced features to monitor and troubleshoot, define alerts, and design custom dashboards.

For more details on the metrics you can monitor, see [Monitoring Event Streams metrics using IBM Cloud Monitoring with Sysdig](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-metrics) in the documentation.

## Client Behavior and Diagnostics

Most Kafka clients generate logs and metrics. When running applications, it's important to capture logs and metrics as they often help investigate an issue, if an issue happens.

For example, for the Java client:

* logs. Logs are configured via log4j. The minimal recommended configuration file is:

    ```
    log4j.rootLogger=INFO, stdout, kafkaAppender

    log4j.appender.stdout=org.apache.log4j.ConsoleAppender
    log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
    log4j.appender.stdout.layout.ConversionPattern=[%d] %p %m (%c)%n
    ```
    Then pass the following JVM argument when starting the application:

    ```
    -Dlog4j.configuration=file:<PATH_TO_LOG4J_PROPERTIES_FILE>
    ```

* metrics: By default, metrics are emitted via JMX. You can also set `metric.reporters` to configure custom reporters for your metrics pipeline.

## Debug connection problems

When debugging connection issues, we recommend to follow the following steps:

1. Verify bootstrap servers configured in the Kafka client.
2. Verify the security protocol is set to SASL and SSL.
3. Verify the password configured for SASL.
4. Verify the ServiceID has the [correct IAM permissions](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-security#default_settings).
5. Verify the [maximum number of connected clients](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-metrics#ibm_eventstreams_kafka_recommended_max_connected_clients_percent) is not reached.

For more details, see the [Troubleshooting section](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-troubleshooting) in the documentation.

## Use the Event Streams sample repository

The [Event Streams sample GitHub repository](https://github.com/ibm-messaging/event-streams-samples) contains sample apps that demonstrate best practices for building Kafka applications in multiple languages, including Java, Node.js, and Python.

This repository also contains instructions and Docker images to do the following:

* [Run Kafka Connect](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-connect). This sample contains the artifacts required to build the `ibmcom/eventstreams-kafkaconnect` Docker image. This image contains the Kafka Connect runtime and the [IBM Cloud Object Storage sink connector](https://github.com/ibm-messaging/kafka-connect-ibmcos-sink) and the [IBM MQ source connector](https://github.com/ibm-messaging/kafka-connect-mq-source) as well as instructions how to run it on Kubernetes.

* [Run MirrorMaker](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-mirrormaker).  This repository contains the artifacts required to build the `ibmcom/eventstreams-kafkamirrormaker` Docker image. This image contains Kafka Mirror Maker and can be used to replicate data between clusters.

## Use the Event Streams CLI

The Event Streams CLI is a quick and easy way to gather details about your cluster. It supports:

- Creating, listing, updating, and deleting topics.
- Listing, deleting, and resetting consumer groups.
- Describing the cluster.

For more details, see the [Event Streams CLI reference](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-cli_reference).

## Event Streams Must-Gather Information

If you'd like help from the Event Streams team, when opening a ticket, it's best to provide the following information:

* What is the CRN ID of the Event Streams service you are using? You can provide this ID by pasting the full IBM Cloud console URL after clicking on the service, or by pasting the output from the following CLI command:

    ```
    ibmcloud resource service-instance NAME
    ```

* When did the problem first occur (specifically time, date, and timezone)? How long was your app running before this?
* Is the problem still occurring? Can you replicate it?
* Which Kafka client is your application using? What are the version details?
* What are your client configuration details? We need to know your producer and consumer settings, so please list any non-default options you have passed to your producer or consumer creation.
* Do you have application log snippets that display the problem?
* What is the issue you are seeing? Which topics, client IDs, group IDs, and transaction IDs are affected?
* What impact is the problem having on your service?

For more details, see [Reporting a problem to the Event Streams team](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-report_problem_enterprise).

## Summary and next steps

Using all these tips, you should be able to manage your Event Streams instances and applications like a pro. And, if any issues happen, you will be able to debug them quickly!

There is an [FAQs section](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-faqs) in the Event Streams documentation that covers some of the most common questions users ask. We recommend you to check it out whenever you have a question.

If you’re all done and ready to take the quiz and earn your IBM Event Streams Developer Essentials badge, go back to the [IBM Event Streams Developer Essentials badge](/learningpaths/ibm-event-streams-badge/summary/) page, and click through to the quiz!