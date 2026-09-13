---
authors: ''
check_date: '2021-11-15'
completed_date: '2020-12-09'
components:
- kafka
display_in_listing: true
draft: false
excerpt: In this tutorial, you'll actually build a small application. First, however,
  you will first run a small binary application. This application will produce some
  records to a topic. Then, your challenge is to write a consumer application that
  will consume records from the topic and will recover the secret message that is
  put inside one of the records.
ignore_prod: false
meta_description: In this tutorial, you'll actually build a small application. First,
  however, you will first run a small binary application. This application will produce
  some records to a topic. Then, your challenge is to write a consumer application
  that will consume records from the topic and will recover the secret message that
  is put inside one of the records.
meta_keywords: kafka, event streams, producer, consumer, messaging
meta_title: Take the IBM Event Streams Java app coding challenge
primary_tag: kafka
related_content:
- slug: get-started-with-apache-kafka
  type: tutorials
- slug: apache-kafkas-producer-api-and-consumer-api
  type: tutorials
subtitle: Develop a small binary application with IBM Event Streams
tags:
- messaging
title: Take the IBM Event Streams Java app coding challenge
---

<!-- <sidebar> <heading>Learning path: IBM Event Streams Developer Essentials Badge</heading> <p>This article is part of the IBM Event Streams Developer Essentials learning path and badge.</p> <ul><li>[IBM Event Streams fundamentals](/articles/event-streams-fundamentals)</li><li>[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals)</li><li>[Deploying and using a basic Kafka instance](/tutorials/deploying-and-using-a-basic-kafka-instance)</li><li>[Get hands on experience](/tutorials/event-streams-hands-on-java-sample)</li><li>[Take on the coding challenge](/tutorials/event-streams-badge-event-streams-dev-challenge)</li><li>[Debug your app](/articles/event-streams-dev-cheat-sheet)</li></ul></sidebar> -->

In the previous tutorial, "[Get hands on experience with an IBM Event Streams Java sample application](/learningpaths/ibm-event-streams-badge/hands-on-event-streams-app/)," we reviewed the logic of the Event Streams Java sample and you played around with changing it up.  In this tutorial, you'll actually build a small application.

In this tutorial, you will first run a small binary application. This application will produce some records to a topic. Then, your challenge is to write a consumer application that will consume records from the topic and that will recover the secret message put inside one of the records.

## Prerequisites

To complete this challenge, you'll need the following in your local environment:

- [Gradle](https://gradle.org/)
- [JDK](https://adoptopenjdk.net/)
- [Eclipse](https://www.eclipse.org/downloads/packages/) or [IntelliJ IDEA](https://www.jetbrains.com/idea/download/)
- [Docker](https://www.docker.com/get-started)

## The challenge

The challenge is to produce messages by running the producer binary application provided and modify the consumer application to find the secret message.

The producer application will create a topic called `event-streams-coding-challenge` and send records, one of which is the secret message. The next step will be to edit the example `App.java` application and add a poll loop in order to keep consuming records until it finds the secret message. The secret message is the value of the record that has the following key: `coding-challenge`.

Follow these steps to complete the challenge:

1. Download the challenge code, which is stored in the [ibm-messaging/eventstreams-badge-sample](https://github.com/ibm-messaging/eventstreams-badge-sample) GitHub repository.

    Go to our [ibm-messaging/eventstreams-badge-sample](https://github.com/ibm-messaging/eventstreams-badge-sample) repository in GitHub, and click the clone or download button. You can choose to Clone with SSH, Use HTTPS, or Download a ZIP with the code. If you download a .ZIP file, unzip the repository.

2. Run the producer application by providing the broker address and API key found from your Event Streams Service credentials.

    ```
    java -jar coding-challenge-setup.jar <kafka_broker_sasl> <api_key>
    ```

    Ensure you see "`Congratulations! You have successfully set up the topic for the coding challenge.`" in the output to confirm the secret message was correctly written to the topic.

    Now it's time to try to recover the secret message!

3. Set up a project for the sample consumer application.

    First, navigate to the `coding-challenge-consumer` directory:

    ```
    cd coding-challenge-consumer
    ```

    Then, create a project for your preferred IDE: `gradle eclipse` or `gradle idea`.

    Finally, import the consumer project into your IDE.

4. In the IDE, open `App.java` and modify the code where you see `TODO` comments.

    There are 4 `TODO` comments that highlight Consumer logic that is required to complete the challenge.

    ```
    // TODO Move position to beginning of partition
    // TODO: Add consumer poll loop
    // TODO: Find the record whose key is equal to KEY ("coding-challenge")
    // TODO: Print the record value to discover the secret message
    ```

5. After you have finished modifying the consumer code, build the application.

    ```
    gradle clean && gradle build
    ```

6. Run the consumer application.

    ```
    java -jar ./build/libs/coding-challenge-consumer.jar <kafka_broker_sasl> <api_key>
    ```

If your code does not work, don't panic! Just return to step 4, and rerun steps 5 and 6 after you've made changes.  

If you get stuck, review the explanations of the Event Streams sample in [Get hands on experience with Event Streams Java sample](/tutorials/event-streams-hands-on-java-sample/) as it contains all the logic required to complete the challenge.

# Summary and next steps

Congratulations! You’ve successfully written your first Kafka application and completed the coding challenge. Be sure that you’ve checked out the [Event Streams cheat sheet](/learningpaths/ibm-event-streams-badge/event-streams-developer-cheat-sheet/), because it’s packed full of ninja moves that every Event Streams user should know.