---
authors: ''
check_date: '2021-11-15'
completed_date: '2020-12-09'
components:
- kafka
display_in_listing: true
draft: false
excerpt: このチュートリアルでは、実際に小さなアプリケーションを作ってみます。しかし、まず最初に、小さなバイナリ・アプリケーションを実行します。このアプリケーションは、あるトピックにいくつかのレコードを生成します。次に、トピックからのレコードを消費するコンシューマ・アプリケーションを書き、レコードの中に入れられた秘密のメッセージを復元することが課題です。
ignore_prod: false
meta_description: このチュートリアルでは、実際に小さなアプリケーションを作ってみます。しかし、まず最初に、小さなバイナリ・アプリケーションを実行します。このアプリケーションは、あるトピックにいくつかのレコードを生成します。次に、トピックからのレコードを消費するコンシューマ・アプリケーションを書き、レコードの中に入れられた秘密のメッセージを復元することが課題です。
meta_keywords: kafka, event streams, producer, consumer, messaging
meta_title: IBM Event Streams Javaアプリのコーディングチャレンジに参加する
primary_tag: kafka
related_content:
- slug: get-started-with-apache-kafka
  type: tutorials
- slug: apache-kafkas-producer-api-and-consumer-api
  type: tutorials
subtitle: IBM Event Streamsを使った小さなバイナリアプリケーションの開発
tags:
- messaging
title: IBM Event Streams Javaアプリのコーディングチャレンジに参加する
---

<!-- <sidebar> <heading>Learning path:IBM Event Streams Developer Essentials Badge</heading> <p>この記事は、IBM Event Streams Developer Essentialsのラーニングパスとバッジの一部です。</p> <ul><li>[IBM Event Streams fundamentals](/articles/event-streams-fundamentals)</li><li>[Apache Kafka fundamentals](/articles/event-streams-kafka-fundamentals)</li><li>[Deploying and using a basic Kafka instance](/tutorials/deploying-and-using-a-basic-kafka-)</li><li>[Get hands on experience](/tutorials/event-streams-hands-on-java-sample)</li><li>[Take on the coding challenge](/tutorials/event-streams-badge-event-streams-dev-challenge)</li><li>[Debug your app](/articles/event-streams-dev-cheat-sheet)</li></ul></sidebar> -->

前回のチュートリアル「[Get hands on experience with an IBM Event Streams Java sample application](/learningpaths/ibm-event-streams-badge/hands-on-event-streams-app/)」では、Event Streams Java サンプルのロジックを確認し、それを変更して遊んでみました。  このチュートリアルでは、実際に小さなアプリケーションを作ってみましょう。

このチュートリアルでは、まず、小さなバイナリ・アプリケーションを実行します。このアプリケーションは、あるトピックに対するいくつかのレコードを生成します。次に、トピックからのレコードを消費するコンシューマ・アプリケーションを書き、レコードの中に入れられた秘密のメッセージを復元することが課題です。

## 前提条件

この課題を達成するには、ローカル環境に以下のものが必要となります。

- [Gradle](https://gradle.org/)
- [JDK](https://adoptopenjdk.net/)
- [Eclipse](https://www.eclipse.org/downloads/packages/) または [IntelliJ IDEA](https://www.jetbrains.com/idea/download/)
- [Docker](https://www.docker.com/get-started)

## 課題

用意されたプロデューサー・バイナリ・アプリケーションを実行してメッセージを生成し、コンシューマー・アプリケーションを修正して秘密のメッセージを見つけることが課題です。

プロデューサアプリケーションは `event-streams-coding-challenge` という名前のトピックを作成し、秘密のメッセージを含むレコードを送信します。次のステップでは、サンプルアプリケーションの `App.java` を編集して、秘密のメッセージを見つけるまでレコードを消費し続けるためのポーリングループを追加します。秘密のメッセージは、次のキーを持つレコードの値です: `coding-challenge`.

以下の手順でチャレンジを完了させます。

1. チャレンジコードをダウンロードします。このコードは [ibm-messaging/eventstreams-badge-sample](https://github.com/ibm-messaging/eventstreams-badge-sample) の GitHub リポジトリに格納されています。

    GitHubの[ibm-messaging/eventstreams-badge-sample](https://github.com/ibm-messaging/eventstreams-badge-sample)リポジトリにアクセスして、cloneまたはdownloadボタンをクリックします。「Clone with SSH」、「Use HTTPS」、「Download a ZIP with the code」のいずれかを選択できます。.ZIPファイルをダウンロードした場合は、リポジトリを解凍します。

2.Event Streams Serviceの認証情報から得たブローカーアドレスとAPIキーを入力して、プロデューサーアプリケーションを実行します。


    出力に「`Congratulations!You have successfully set up the topic for the coding challenge.`" が出力され、秘密のメッセージが正しくトピックに書き込まれたことを確認します。

    さて、いよいよ秘密のメッセージを復元してみましょう。

3.サンプルのコンシューマ・アプリケーションのプロジェクトを設定します。

    まず，`coding-challenge-consumer`ディレクトリに移動します．


    次に、お好みの IDE である `gradle eclipse` または `gradle idea` 用のプロジェクトを作成します。

    最後に、お使いの IDE に consumer プロジェクトをインポートします。

4.4. IDE で `App.java` を開き、`TODO` コメントが表示されている部分のコードを修正します。

    4 つの `TODO` コメントがあり、課題を達成するために必要な Consumer ロジックが強調されています。


5.コンシューマコードの修正が終わったら、アプリケーションをビルドします。


6.コンシューマ・アプリケーションを実行します。


もし、コードがうまくいかなくても、慌てないでください。ステップ4に戻って、変更を加えた後にステップ5と6を再実行すればいいのです。  

行き詰まったら、[Get hands on experience with Event Streams Java sample](/tutorials/event-streams-hands-on-java-sample/)のイベント・ストリーム・サンプルの説明を確認してください。このサンプルには、課題を完了するために必要なロジックがすべて含まれています。

# まとめと次のステップ

おめでとうございます。あなたは初めてのKafkaアプリケーションを書き、コーディングチャレンジを完了しました。[Event Streamsチートシート](/learningpaths/ibm-event-streams-badge/event-streams-developer-cheat-sheet/)をチェックしたことを確認してください。なぜなら、イベントストリームのユーザーが知っておくべき忍者の動きが満載だからです。