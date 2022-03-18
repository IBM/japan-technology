---
authors: ''
check_date: '2021-11-15'
completed_date: '2020-12-09'
components:
- kafka
display_in_listing: true
draft: false
excerpt: このチュートリアルでは、IBM Event Streams の Java サンプル・アプリケーションを確認します。クライアント・コードの書き方を見て、Apache
  Kafka からメッセージを生成したり消費したりする方法を学びます。
ignore_prod: false
meta_description: このチュートリアルでは、IBM Event Streams の Java サンプル・アプリケーションを確認します。クライアント・コードの書き方を見て、Apache
  Kafka からメッセージを生成したり消費したりする方法を学びます。
meta_keywords: IBM Event Streams, Apache Kafka, producer, consumer
meta_title: IBM Event StreamsのJavaサンプル・アプリケーションを実際に体験することができます。
primary_tag: kafka
related_content:
- slug: get-started-with-apache-kafka
  type: tutorials
- slug: apache-kafkas-producer-api-and-consumer-api
  type: tutorials
subtitle: コードを確認し、Apache Kafkaからメッセージを生成・消費するクライアントコードの書き方を学ぶことができます。
title: IBM Event StreamsのJavaサンプル・アプリケーションを実際に体験することができます。
type: tutorial
---

<!-- <sidebar> <heading>Learning path:IBM Event Streams Developer Essentials Badge</heading> <p>この記事は、IBM Event Streams Developer Essentialsのラーニングパスとバッジの一部です。</p> <ul><li>[IBM Event Streams fundamentals](/articles/event-streams-fundamentals)</li><li>[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals)</li><li>[Deploying and using a basic Kafka instance](/tutorials/deploying-and-using-a-basic-kafka-)</li><li>[Get hands on experience](/tutorials/event-streams-hands-on-java-sample)</li><li>[Take on the coding challenge](/tutorials/event-streams-badge-event-streams-dev-challenge)</li><li>[Debug your app](/articles/event-streams-dev-cheat-sheet)</li></ul></sidebar> -->

サンプルアプリケーションを実際に体験するために、[`event-streams-samples`](https://github.com/ibm-messaging/event-streams-samples)リポジトリにあるJava Consoleサンプルを確認します。

このチュートリアルでは、特に[Local Development sample](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/docs/Local.md)に注目します。

クライアントコードの書き方を見ていくので、Apache Kafkaからメッセージを生成・消費する方法を学ぶことができます。

## 前提条件

- [Apache Kafka](/learningpaths/ibm-event-streams-badge/kafka-fundamentals/)に関する一般的な知識。
- [IBM Cloud アカウント](https://cloud.ibm.com/registration?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)
- また、[サンプルアプリケーション](https://github.com/ibm-messaging/event-streams-samples)については、インストールされている必要があります。Git、Gradle、およびJava 8以上をインストールしていること。
- [イベント・ストリーム・インスタンスの作成とサンプル・アプリケーションの実行](/learningpaths/ibm-event-streams-badge/deploy-kafka-instance/)の手順を完了しました。

## Javaサンプルの概要

このチュートリアルでは、サンプルのコードのすべての行を説明するつもりはありませんが、サンプルのコードの構造を説明する価値はあります。

このコードは、GitHub レポの [`event-streams-samples`](https://github.com/ibm-messaging/event-streams-samples) 内の [kafka-java-console-sample](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples) フォルダにあります。

### メインのメソッドです。EventStreamsConsoleSample.java (イベントストリームズコンソールサンプル)

[EventStreamsConsoleSample.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/EventStreamsConsoleSample.java)ファイルにはメインメソッドが含まれています。次のような処理を行います。

- コマンドラインの引数を解析し、検証します。
- サンプルが対象とするトピックが存在するかどうかを確認し、存在しない場合は作成します。
- 異なるスレッドでクライアントを起動します。サンプルでは、プロデューサ、コンシューマ、またはその両方を同時に実行できます。これらのクライアントは起動され、ユーザーがキャンセルする（Ctrl-Cを使用）まで実行されます。

### プロデューサー

プロデューサーは、メッセージのストリームをKafkaのトピックにパブリッシュするアプリケーションです。プロデューサーについては、「[Apache Kafkaの基礎知識](/articles/event-streams-kafka-fundamentals/)」の記事でご紹介しました。

#### プロデューサー設定プロパティ

このサンプルでは、プロデューサー構成は[EventStreamsConsoleSample.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/EventStreamsConsoleSample.java)の`getProducerConfigs()`メソッドで構築されており、すべてのクライアントで使用されるいくつかの共通の構成をベースに、少数のプロデューサー固有の構成プロパティを設定しています。

これらの構成プロパティは注目すべきものです。

* シリアライザ (およびデシリアライザ)


    これらは、生成されるメッセージのキーと値に使用されるシリアライザーです。サンプルでは、シンプルな文字列が両方に使用されているので、Kafkaが提供するStringSerializerが必要なものを提供します。コンシューマにはマッチするデシリアライザが必要であることに注意してください。

* 謝辞 (`acks`)


`    acks`が`all`に設定されていると，プロデューサーは同期しているすべてのレプリカがメッセージを受け取ったことを要求します．リーダーは、同期しているすべてのレプリカがメッセージを安全に書き込んだことを確認してから、確認応答を送信します。これは最も耐久性のあるオプションですが、その代償としてレイテンシーが増加します。

重要なプロデューサー構成設定については、[Event Streams on IBM Cloud documentation](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-producing_messages#config_settings)を参照してください。すべてのプロデューサー構成の完全なドキュメントについては、[Apache Kafka documentation](http://kafka.apache.org/documentation.html#producerconfigs)を参照してください。しかし、注意していただきたいのは、変更したくなるような構成オプションがたくさんあるということです。アプリケーションの動作に慣れるまでは、いくつかの設定にとどめておくことをお勧めします。

#### `ProducerRunnable.java` を参照してください。

[ProducerRunnable.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/ProducerRunnable.java)はRunnableを実装しているため、独自のスレッドで実行されます。

コンストラクタは、与えられた設定に基づいて `KafkaProducer` の新しいインスタンスを作成します。


`run()`関数は、実際の作業が行われる場所です。スレッドは`while`ループで実行され、`closing`変数を介してアプリケーションがシャットダウンしているかどうかをチェックしていることに気づくでしょう。

生成されるメッセージを表すために `ProducerRecord` が構築されます。コメントには、サンプルアプリケーションがデフォルトのパーティショナーを使用していることが書かれています。


他のケースでは、自分でパーティションを決定するようにコントロールしたい場合もあるでしょう。その例は、Kafka [javadoc](https://kafka.apache.org/26/javadoc/org/apache/kafka/clients/producer/ProducerRecord.html#ProducerRecord-java.lang.String-java.lang.Integer-K-V-)で見ることができます。

このサンプルでは、`ProducerRecord`を非同期に送信し、すぐにブロックして確認応答を待っています。これは、サンプルでのデモ目的には十分ですが、パフォーマンスに影響するため、現実のアプリケーションで必要とされる動作ではないと思われます。アプリケーションの要件を検討する際には、メッセージを送信して確認応答を処理する際に、プロデューサーがどのように動作するかを考慮する必要があります。


### コンシューマー

コンシューマは、1つ以上のトピックからメッセージを読み込んで処理します。コンシューマについては、「[Apache Kafkaの基礎知識](/articles/event-streams-kafka-fundamentals/)」の記事でご紹介しました。

#### コンシューマーの設定

このサンプルでは、コンシューマの設定は[EventStreamsConsoleSample.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/EventStreamsConsoleSample.java)の`getConsumerConfigs()`メソッドで構築されています。このメソッドは、すべてのクライアントで使用される共通のコンフィグレーションをベースに構築されています。また、key, valueのデシリアライザなど、プロデューサに類似した構成を持っています。しかし、このメソッドは、次のような少数のコンシューマ固有の構成プロパティを設定します。

* `group.id` です。


`    group.id` プロパティは、このコンシューマーが所属するコンシューマーグループを制御します。必要に応じて、既存のグループに参加したり、新しいグループを作成したりします。

* `auto.offset.reset`


`    auto.offset.reset` プロパティは、このコンシューマの現在のオフセットがサーバに存在しなくなった場合や、初期のオフセットが存在しない場合にどうするかを決定します。`latest`は、現在のオフセットが自動的にパーティション上の最新のオフセットに設定されることを意味し、つまり、コンシューマーは最新のレコードから消費することになります。

重要なコンシューマー構成設定については、[Event Streams on IBM Cloud documentation](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-consuming_messages#configuring_consumer_properties)で詳しく説明しています。すべてのコンシューマー構成の完全なドキュメントについては、[Apache Kafka documentation](https://kafka.apache.org/documentation/#consumerconfigs)を参照してください。しかし、変更したくなるような構成オプションがたくさんあることに注意してください。アプリケーションの動作に慣れるまでは、いくつかの設定にとどめておくことをお勧めします。

#### ConsumerRunnable.java

producer同様、[ConsumerRunnable.java](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/src/main/java/com/eventstreams/samples/ConsumerRunnable.java)はRunnableを実装しているため、独自のスレッドで実行されます。

コンストラクタは、与えられた設定に基づいて `KafkaConsumer` の新しいインスタンスを作成します。


繰り返しになりますが、プロデューサーと同様に、ほとんどのロジックは `run()` 関数の中にあり、アプリケーションがシャットダウンされているかどうかを識別するロジックも含まれています。

コンシューマは利用可能な`ConsumerRecords`があるかどうかをポーリングします。これはコレクションであり、利用可能なすべてのメッセージが返されます。3秒以内に何も受信しなかった場合、コンシューマは`poll()`を終了し、消費されたメッセージがなかったことを記録します。


コンシューマーが何らかのメッセージを受信した場合，サンプルアプリケーションでは，単に各メッセージをループし，それぞれのメッセージの内容を表示します．


## Time to get creative?

Javaサンプルとクライアントの動作について理解したところで、コードを少しいじってみましょう。  [コードをダウンロード](https://github.com/ibm-messaging/event-streams-samples)して、[`kafka-java-console-sample`](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-java-console-sample)フォルダに移動し、[docs](https://github.com/ibm-messaging/event-streams-samples/blob/master/kafka-java-console-sample/docs/Local.md)を探索して、コードで遊ぶ準備をしましょう。

<button-link> <text>Get the code</text> <url>https://github.com/ibm-messaging/event-streams-samples</url></button-link>

まずは、クライアントを独立して起動したり停止したりする実験をしてみましょう。メッセージの消費を一定期間停止してから再び開始するとどうなるでしょうか？

クライアントのコードを変更してみてはいかがでしょうか？コンシューマが読み込んだ各メッセージに対して長時間の処理を行っていたらどうなるでしょうか？sleepを追加してこれを再現し、何が起こるか見てみましょう。

クライアントの設定を見直して、それぞれがどのような効果を持つかを確認してください。
 - [プロデューサー構成](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-producing_messages#config_settings)
 - [コンシューマの設定](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-consuming_messages#configuring_consumer_properties)

## まとめと次のステップ

このチュートリアルでは、Javaのサンプルアプリケーションを使って、その機能を説明しました。また、サンプルコードで遊んでいただき、プロデューサとコンシューマのコードがどのように動作するかについて理解を深めていただければ幸いです。

これで、[IBM Event Streams coding challenge](/learningpaths/ibm-event-streams-badge/event-streams-coding-challenge/)に挑戦し、コンシューマーアプリケーションを書く準備ができました。

あるいは、[Debug your application](/learningpaths/ibm-event-streams-badge/event-streams-developer-heat-sheet/)の方法を学ぶ準備ができているかもしれません。