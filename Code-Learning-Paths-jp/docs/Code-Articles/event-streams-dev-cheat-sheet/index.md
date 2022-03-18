---
authors: ''
check_date: '2021-11-15'
completed_date: '2020-12-09'
components:
- kafka
display_in_listing: true
draft: false
excerpt: この記事では、イベントストリームを使ったアプリケーションの実装、デバッグ、運用のためのトップヒントを紹介します。
ignore_prod: false
meta_description: この記事では、イベントストリームを使ったアプリケーションの実装、デバッグ、運用のためのトップヒントを紹介します。
meta_keywords: kafka, tips and tricks, debugging, event streams
meta_title: IBM Event Streams cheat sheet for developers
primary_tag: kafka
related_content:
- slug: get-started-with-apache-kafka
  type: tutorials
subtitle: IBMイベント・ストリームの一般的なエラーを簡単にデバッグするためのヒントとコツ
tags:
- messaging
title: IBM Event Streams cheat sheet for developers
---

<!-- <sidebar> <heading>Learning path:IBM Event Streams Developer Essentials Badge</heading> <p>この記事は、IBM Event Streams Developer Essentialsのラーニングパスとバッジの一部です。</p> <ul><li>[IBM Event Streams fundamentals](/articles/event-streams-fundamentals)</li><li>[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals)</li><li>[Deploying and using a basic Kafka instance](/tutorials/deploying-and-using-a-basic-kafka-)</li><li>[Get hands on experience](/tutorials/event-streams-hands-on-java-sample)</li><li>[Take on the coding challenge](/tutorials/event-streams-badge-event-streams-dev-challenge)</li><li>[Debug your app](/articles/event-streams-dev-cheat-sheet)</li></ul></sidebar> -->

この記事では、イベントストリームを使ったアプリケーションの実装、デバッグ、運用のためのトップヒントを紹介しています。

## Sysdigモニタリングの有効化

Event Streamsは[IBM Cloud Monitoring with Sysdig](https://cloud.ibm.com/docs/Monitoring-with-Sysdig?topic=Sysdig-getting-started#getting-started)をサポートしています。Sysdigは、アプリケーションやサービス、プラットフォームのパフォーマンスや健全性を運用面で可視化するために、さまざまな指標を監視することができます。Sysdigは、管理者、DevOpsチーム、開発者に、モニタリングやトラブルシューティング、アラートの定義、カスタム・ダッシュボードのデザインなどの高度な機能を備えたフルスタック・テレメトリを提供します。

監視できるメトリクスの詳細については、ドキュメントの[Monitoring Event Streams metrics using IBM Cloud Monitoring with Sysdig](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-metrics)を参照してください。

## クライアントの動作と診断

ほとんどのKafkaクライアントは、ログやメトリクスを生成します。アプリケーションを実行する際、問題が発生した場合に問題の調査に役立つことが多いため、ログやメトリクスを取得することは重要です。

例えば、Javaクライアントの場合。

* ログ。ログの設定はlog4jで行います。最小限の推奨設定ファイルは

    そして、アプリケーションの起動時に、以下のJVM引数を渡します。


* メトリクスデフォルトでは、メトリクスはJMX経由で出力されます。また、`metric.reporter`を設定することで、メトリクスパイプライン用のカスタムレポーターを構成することができます。

## 接続問題のデバッグ

接続の問題をデバッグする場合は、以下の手順で行うことをお勧めします。

1. Kafkaクライアントに設定されているブートストラップサーバーを確認する。
2.セキュリティプロトコルがSASLおよびSSLに設定されていることを確認する。
3.SASLに設定されているパスワードを確認する。
4.ServiceIDに[正しいIAM権限](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-security#default_settings)が設定されていることを確認します。
5.5. [最大接続クライアント数](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-metrics#ibm_eventstreams_kafka_recommended_max_connected_clients_percent)に達していないことを確認する。

詳細は、ドキュメントの[Troubleshooting section](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-troubleshooting)を参照してください。

## Event Streams サンプルリポジトリを使用する

[Event Streams sample GitHub repository](https://github.com/ibm-messaging/event-streams-samples)には、Java、Node.js、Pythonなどの複数の言語でKafkaアプリケーションを構築するためのベストプラクティスを示すサンプルアプリが含まれています。

このリポジトリには、以下を行うための手順とDockerイメージも含まれています。

* [Run Kafka Connect](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-connect)。このサンプルには、`ibmcom/eventstreams-kafkaconnect`というDockerイメージの構築に必要なアーティファクトが含まれています。このイメージには、Kafka Connectランタイムと[IBM Cloud Object Storage sink connector](https://github.com/ibm-messaging/kafka-connect-ibmcos-sink)と[IBM MQ source connector](https://github.com/ibm-messaging/kafka-connect-mq-source)が含まれており、Kubernetes上で実行する方法も説明されています。

* [Run MirrorMaker](https://github.com/ibm-messaging/event-streams-samples/tree/master/kafka-mirrormaker)を参照してください。  このリポジトリには、`ibmcom/eventstreams-kafkamirrormaker`というDockerイメージの構築に必要なアーティファクトが含まれています。このイメージにはKafka Mirror Makerが含まれており、クラスター間でのデータのレプリケーションに使用できます。

## イベントストリームのCLIを使う

Event Streams CLIは、クラスターの詳細を素早く簡単に収集することができます。サポートしています。

- トピックの作成、一覧表示、更新、および削除。
- コンシューマ・グループのリストアップ、削除、およびリセット。
- クラスタの説明。

詳細については、[Event Streams CLI reference](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-cli_reference)を参照してください。

## イベントストリームの必須収集情報

Event Streamsチームのサポートを受けたい場合、チケットを開く際には、以下の情報を提供するのがベストです。

* 使用しているEvent StreamsサービスのCRN IDは何ですか？この ID は、サービスをクリックした後に IBM Cloud コンソールの完全な URL を貼り付けるか、以下の CLI コマンドの出力を貼り付けることで提供できます。


* 問題が最初に発生したのはいつですか（具体的な時間、日付、タイムゾーン）？この問題が発生する前、アプリはどのくらいの期間実行されていましたか？
* 問題はまだ発生していますか？それを再現できますか？
* あなたのアプリケーションはどのKafkaクライアントを使用していますか？そのバージョンの詳細は何ですか？
* クライアントの構成の詳細は何ですか？プロデューサとコンシューマの設定を知る必要がありますので、プロデューサまたはコンシューマの作成に渡したデフォルト以外のオプションをすべて列挙してください。
* 問題を示すアプリケーションログの断片はありますか？
* 表示されている問題は何ですか？どのトピック、クライアントID、グループID、トランザクションIDが影響を受けますか？
* 問題はサービスにどのような影響を与えていますか？

詳しくは、[Reporting a problem to the Event Streams team](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-report_problem_enterprise)をご覧ください。

## まとめと次のステップ

これらのヒントをすべて活用すれば、プロのようにEvent Streamsのインスタンスとアプリケーションを管理することができるはずです。また、何か問題が発生しても、すぐにデバッグすることができるでしょう。

Event Streamsのドキュメントの中には、[FAQセクション](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-faqs)があり、ユーザーからの最も一般的な質問をカバーしています。質問があるときは、いつでもこのセクションをご覧になることをお勧めします。

クイズに答えて IBM Event Streams Developer Essentials バッジを取得する準備ができたら、[IBM Event Streams Developer Essentials バッジ](/learningpaths/ibm-event-streams-badge/summary/)ページに戻って、クイズをクリックしてください!