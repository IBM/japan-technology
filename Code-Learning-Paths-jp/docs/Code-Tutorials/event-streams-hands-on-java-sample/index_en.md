---
authors: ''
check_date: '2021-11-15'
completed_date: '2020-12-09'
components:
- kafka
display_in_listing: true
draft: false
excerpt: In this tutorial, we review an IBM Event Streams Java sample application.
  We look at how to write client code, so that you learn how to produce and consume
  messages from Apache Kafka.
ignore_prod: false
meta_description: In this tutorial, we review an IBM Event Streams Java sample application.
  We look at how to write client code, so that you learn how to produce and consume
  messages from Apache Kafka.
meta_keywords: IBM Event Streams, Apache Kafka, producer, consumer
meta_title: Get hands on experience with an IBM Event Streams Java sample application
primary_tag: kafka
related_content:
- slug: get-started-with-apache-kafka
  type: tutorials
- slug: apache-kafkas-producer-api-and-consumer-api
  type: tutorials
subtitle: Review the code and learn how to write client code that produces and consumes
  messages from Apache Kafka
title: Get hands on experience with an IBM Event Streams Java sample application
type: tutorial
---

<!-- <sidebar> <heading>Learning path: IBM Event Streams Developer Essentials Badge</heading> <p>This article is part of the IBM Event Streams Developer Essentials learning path and badge.</p> <ul><li>[IBM Event Streams fundamentals](/articles/event-streams-fundamentals)</li><li>[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals)</li><li>[Deploying and using a basic Kafka instance](/tutorials/deploying-and-using-a-basic-kafka-instance)</li><li>[Get hands on experience](/tutorials/event-streams-hands-on-java-sample)</li><li>[Take on the coding challenge](/tutorials/event-streams-badge-event-streams-dev-challenge)</li><li>[Debug your app](/articles/event-streams-dev-cheat-sheet)</li></ul></sidebar> -->

To get some hands on experience with a sample application, we are going to review the Java Console sample in the [`event-streams-samples`](https://github.com/ibm-messaging/event-streams-samples) repository.

In this tutorial, we focus specifically on the [Local Development sample](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/docs/Local.md).

We will look at how to write client code, so that you learn how to produce and consume messages from Apache Kafka.

## Prerequisites

- General knowledge about [Apache Kafka](/learningpaths/ibm-event-streams-badge/kafka-fundamentals/)
- [IBM Cloud account](https://cloud.ibm.com/registration?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)
- For the [sample application](https://github.com/ibm-messaging/event-streams-samples), you must also have installed: Git, Gradle, and Java 8 or higher.
- Completed the steps for [creating an Event Streams instance and running a sample application](/learningpaths/ibm-event-streams-badge/deploy-kafka-instance/).

## Overview of the Java sample

We are not going to walk through every line of code in the sample in this tutorial, but it is worth explaining the structure of the code in the sample.

The code can be found in the [kafka-java-console-sample](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples) folder in the [`event-streams-samples`](https://github.com/ibm-messaging/event-streams-samples) GitHub repo.

### Main method: EventStreamsConsoleSample.java

The [EventStreamsConsoleSample.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/EventStreamsConsoleSample.java) file contains the main method. It does the following:

- Parses and validates the command line arguments.
- Checks that the topic that the sample is working against exists, and creates it if it does not exist.
- Starts the clients on different threads. The sample can either run a producer, a consumer, or both at once. They are started and will run until the user cancels them (using Ctrl-C).

### Producer

A producer is an application that publishes streams of messages to Kafka topics. You learned all about producers in our "[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals/)" article.

#### Producer Configuration properties

For this sample, the producer configuration is built in [EventStreamsConsoleSample.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/EventStreamsConsoleSample.java) in the `getProducerConfigs()` method, which builds on some common configuration that is used across all clients and sets a small number of producer-specific configuration properties.

These configuration properties are worth noting:

* Serializers (and deserializers)

    ```
    configs.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName()); // key.serializer

    configs.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName()); // value.serializer
    ```

    These are the serializers used for the message key and value that is produced. In the sample, a simple string is used for both so the Kafka-provided StringSerializer gives us what we need. Note the consumer must have matching deserializers.

* Acknowledgements (`acks`)

    ```
    configs.put(ProducerConfig.ACKS_CONFIG, "all"); // acks
    ```

    With `acks` set to `all` the producer requires all in sync replicas to have received the message. The leader will send acknowledgement only when all in sync replicas have confirmed the message has been safely written. This is the most durable option, however this is at the cost of increased latency.

Read more about important producer configuration settings in the [Event Streams on IBM Cloud documentation](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-producing_messages#config_settings). For the complete documentation of all producer configuration see the [Apache Kafka documentation](http://kafka.apache.org/documentation.html#producerconfigs). But, be warned, there are loads of configuration options that you might be tempted to change. We suggest that you stick to a few until you are comfortable with the behavior of the application.

#### `ProducerRunnable.java`

[ProducerRunnable.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/ProducerRunnable.java) implements Runnable and is therefore run in its own thread.

The constructor creates a new instance of `KafkaProducer` based on the provided configuration.

```
// Create a Kafka producer with the provided client configuration
kafkaProducer = new KafkaProducer<>(producerConfigs);
```

The `run()` function is where the actual work is done. You will notice that the thread runs in a `while` loop, checking whether the application is shutting down via the `closing` variable.

A `ProducerRecord` is constructed to represent the message to be produced. In the comment, it notes that the sample application uses the default partitioner.

```
// If a partition is not specified, the client will use the default partitioner to choose one.
ProducerRecord<String, String> record = new ProducerRecord<>(topic,key,message);
```

In other cases, you may want to be in control of determining the partition yourself, which you can see an example of in the Kafka [javadoc](https://kafka.apache.org/26/javadoc/org/apache/kafka/clients/producer/ProducerRecord.html#ProducerRecord-java.lang.String-java.lang.Integer-K-V-).

In the sample, the `ProducerRecord` is sent asynchronously, then immediately blocks waiting for the acknowledgement. This is sufficient for demonstration purposes in the sample, however it is unlikely to be the required behavior in a real world application because of the performance implications. When looking at the requirements for your application, you should consider how you want your producer to behave when sending messages and processing the acknowledgement.

```
// Send record asynchronously
Future<RecordMetadata> future = kafkaProducer.send(record);

// Synchronously wait for a response from Event Streams / Kafka on every message produced.
// For high throughput the future should be handled asynchronously.
RecordMetadata recordMetadata = future.get(5000, TimeUnit.MILLISECONDS);
```

### Consumer

A consumer reads messages from one or more topics and processes them. You learned all about consumers in our "[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals/)" article.

#### Consumer Configuration

For this sample, the consumer configuration is built in [EventStreamsConsoleSample.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/EventStreamsConsoleSample.java) in the `getConsumerConfigs()` method. This method builds on some common configuration that is used across all clients. It also has similar configuration to the producer, such as the deserializer for key, value. However, the method does set a small number of consumer-specific configuration properties, such as:

* `group.id`

    ```
    configs.put(ConsumerConfig.GROUP_ID_CONFIG, "kafka-java-console-sample-group"); // group.id
    ```

    The `group.id` property controls the consumer group which this consumer is part of. It will either join an existing group or create a new one as required.

* `auto.offset.reset`

    ```
    configs.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "latest"); // auto.offset.reset
    ```

    The `auto.offset.reset` property determines what to do when the current offset for this consumer is no longer present on the server, or there is no initial offset. `latest` means that the current offset is automatically set to the latest offset on the partition, that is the consumer will consume from the latest records.

Read more about important consumer configuration settings in the [Event Streams on IBM Cloud documentation](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-consuming_messages#configuring_consumer_properties). For full documentation of all consumer configuration see the [Apache Kafka documentation](https://kafka.apache.org/documentation/#consumerconfigs). But, be warned though that there are loads of configuration options that you might be tempted to change. We suggest that you stick to a few until you are comfortable with the behavior of the application.

#### ConsumerRunnable.java

Like the producer, [ConsumerRunnable.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/ConsumerRunnable.java) implements Runnable and is therefore run in its own thread.

The constructor create a new instance of `KafkaConsumer` based on the provided configuration.

```
// Create a Kafka consumer with the provided client configuration
kafkaConsumer = new KafkaConsumer<>(consumerConfigs);
```

Again, like the producer, most of the logic is inside the `run()` function with logic to identify if the application is being shutdown.

The consumer polls to see if there are any `ConsumerRecords` available. This is a collection and all available messages will be returned. If nothing is received within 3 seconds, the consumer finishes the `poll()` and logs that there were no messages consumed.

```
// Poll on the Kafka consumer, waiting up to 3 secs if there's nothing to consume.
ConsumerRecords<String, String> records = kafkaConsumer.poll(Duration.ofMillis(3000L));

if (records.isEmpty()) {
    logger.info("No messages consumed");
}
```

If the consumer did receive some messages, the sample application simply loops over each message and prints the contents of each one.

```
for (ConsumerRecord<String, String> record : records) {
    logger.info("Message consumed: {}", record);
}
```

## Time to get creative?!

Now that you understand more about the Java sample and how the clients work, it is time to play around with the code a bit.  [Download the code](https://github.com/ibm-messaging/event-streams-samples), and navigate into the [`kafka-java-console-sample`](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-java-console-sample) folder, explore the [docs](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/docs/Local.md), and get ready to play with the code.

<button-link> <text>Get the code</text> <url>https://github.com/ibm-messaging/event-streams-samples</url></button-link>

Start by experimenting with starting and stopping the clients independently. What happens if you stop consuming messages for a period then start again?

How about you try modifying the client code? What would happen if the consumer was doing some lengthy processing of each message it reads? You could recreate this by adding a sleep to see what happens?

Review the configuration of the clients to see what effects each of these have on the clients:
 - [Producer Configuration](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-producing_messages#config_settings)
 - [Consumer Configuration](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-consuming_messages#configuring_consumer_properties)

## Summary and next steps

In this tutorial, we walked through the Java sample application and learned what it does. Hopefully, you also played around with the sample code and gained more understanding about how producer and consumer code works.

You're now ready to take on the [IBM Event Streams coding challenge](/learningpaths/ibm-event-streams-badge/event-streams-coding-challenge/) and write a consumer app.

Or, perhaps you're ready to learn how to [debug your application](/learningpaths/ibm-event-streams-badge/event-streams-developer-cheat-sheet/).