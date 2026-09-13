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
excerpt: このチュートリアルでは、IBM Event Streams on IBM Cloud サービスを使用して Kafka インスタンスをデプロイし、サンプル・アプリケーションの
  1 つを接続して実行することがいかに簡単かを紹介しています。
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
subtitle: IBM CloudのIBM Event Streamsを使用してKafkaインスタンスをデプロイし、最初のKafkaアプリを接続して使用します。
tags:
- messaging
title: 基本的なKafkaインスタンスのデプロイと使用
---

Apache Kafkaをすぐに使い始めるためには、Kafkaインスタンスをデプロイし、サンプルのKafkaアプリケーションを接続して実行できるようにする必要があります。

確かに[ダウンロードしてローカル・システムにApache Kafkaインスタンスをインストールする](https://kafka.apache.org/quickstart)こともできますが、[IBM Event Streams on IBM Cloudサービス](https://cloud.ibm.com/catalog/services/event-streams?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)は、完全に管理されたApache Kafkaインスタンスです。  

このチュートリアルでは、IBM Event Streams on IBM Cloud サービスを使用して Kafka インスタンスをデプロイし、サンプル・アプリケーションの 1 つを接続して実行することがいかに簡単であるかを紹介します。

## 前提条件

* [Apache Kafka] に関する一般的な知識(/learningpaths/develop-kafka-apps/introduction/intro-to-kafka/)
* [IBM Cloud アカウント](https://cloud.ibm.com/registration?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)
* [サンプルアプリケーション](https://github.com/ibm-messaging/event-streams-samples)については、以下もインストールしておく必要があります。「Git」「Gradle」「Java 8 以上」がインストールされていること。

## ステップ

<sidebar>IBM Event Streams Liteプランでは、使用できるパーティションが1つに限られているため、本番使用には適していません。ドキュメントで[異なるプランを確認する](https://cloud.ibm.com/docs/EventStreams?topic=eventstreams-plan_choose)ことができます。</sidebar>

このチュートリアルでは、Kafka インスタンスに、Event Streams on IBM Cloud を使用します。

Kafka インスタンスをデプロイし、Kafka アプリを接続して使用するには、以下の手順を実行する必要があります。

1. マネージド Kafka インスタンスをデプロイするには、Event Streams on IBM Cloud サービス・インスタンスを作成します。

2.マネージドKafkaインスタンスでKafkaアプリを接続して使用するには、以下が必要です。

    * トピックの作成
    * クレデンシャルの作成
    * サンプルアプリの Github リポジトリをクローンします。
    * コンシューマ・アプリの実行
    * プロデュースするアプリの実行

3.トピックの削除

これらの手順は、次のビデオで紹介されています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/XyNy7TcfJOc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

これらの手順は、[IBM Event Streams for IBM Cloud getting started tutorial](https://cloud.ibm.com/docs/EventStreams?topic=eventstreams-getting_started)にも詳しく書かれています。

## まとめ

おめでとうございます。これで、IBM Event Streams on Cloud のインスタンスの作成と、最初のサンプル Kafka アプリケーションの実行に成功しました。

一般に、継続的な開発のためには、IBM Event Streams on Cloud の標準インスタンスに対して実行する必要があります。このチュートリアルで作成した Lite インスタンスを Standard インスタンスにアップグレードすることができます。