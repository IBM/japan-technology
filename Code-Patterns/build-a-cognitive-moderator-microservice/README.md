# 自然言語を理解して怒りの感情を検出し、露骨な画像を削除するチャットボット・モデレーターを作成する

### ディスカッションを管理するために、Watson のサービスを利用してチャット・チャネル内で交換されるメッセージと画像を処理する

English version: https://developer.ibm.com/patterns/build-a-cognitive-moderator-microservice
  ソースコード: https://github.com/IBM/cognitive-moderator-service

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-10-03

 
## 概要

怒りをあらわにしたメッセージや不適切なメッセージ、そして露骨な画像をモニタリングするチャットボットを作成する方法を学んでください。このコード・パターンでは、モニタリング・チャットボットを作成する方法を説明します。作成したチャットボットは、Slack などのチャット・ルームや、レビューを投稿できる Web サイト内で使用できます。

## 説明

無礼な態度、怒りをあらわにしたメッセージや不適切なメッセージ、露骨な画像。これらはすべて、ソーシャル・メディア・プラットフォームの中で毎日のように目にするものです。こうした問題のあるメッセージや画像をフィルタリングして排除するには、メッセージと画像をモニタリングするチャットボットを作成するという方法があります。モニタリング・チャットボットを Slack などのチャット・ルームやレビューを投稿できる Web サイト内で使用すれば、露骨な画像や不適切なテキストを削除できます。

このコード・パターンで作成するチャットボットは、IBM&reg; Cloud Functions と Watson&trade; サービスを利用します。このチャットボットのフローを Watson Visual Recognition と Watson Natural Language Understanding を利用して拡張し、露骨な画像を識別して削除したり、怒りをあらわにしたメッセージや不適切なメッセージを検出したりできるようにします。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* IBM Cloud Functions を介して Slack を統合したチャットボットを作成する
* Watson Visual Recognition を利用して、露骨な画像を検出する (ベータ版)
* Watson Natural Understanding を利用して、会話の中での感情を検出する
* Watson Natural Language Understanding を利用して、エンティティーを検出する

## フロー

![フロー](../../images/flow-cognitive-moderator.png)

1. ユーザーが Slack アプリを操作して、テキストを送信するか、画像をアップロードします。
1. ボットが Slack 内で使用されているテキストまたは画像を IBM Cloud Functions API に渡します。IBM Function に対して API 呼び出しが行われます。すると、IBM Function が Watson Visual Recognition または Watson Natural Language Processing から返されたレスポンスに応じてテキストまたは画像を分類します。
1. アップロードされた画像は、Watson Visual Recognition がデフォルトの分類子と明示的分類子を使用して分類します。
1. テキストが Slack コミュニケーションの一部として送信された場合は、Watson Natural Language Processing がそのテキストを分類します。
1. IBM Cloud Functions にレスポンスが返されます。その結果、テキストが無礼なものであれば、ボットが [Slack のメッセージ投稿 API](https://api.slack.com/methods/chat.postMessage) を使用して、Slack ユーザーに礼儀正しくするようメッセージを送信します。露骨だとみなされる画像が使用されている場合、IBM Cloud Functions が [Slack のファイル削除 API](https://api.slack.com/methods/files.delete) を使用して、その画像を削除します。

## 手順

詳細な手順については、[README](https://github.com/IBM/cognitive-moderator-service/blob/master/README.md) ファイルを参照してください。手順の概要は以下のとおりです。

1. GitHub リポジトリーを複製します。
1. IBM Cloud を使用して Watson Visual Recognition サービスと Natural Language Understanding サービスのインスタンスを作成します。
1. ワークスペース用の Slack アプリとボットを作成します。
1. IBM Function を IBM Cloud にデプロイします。
1. Slack を使用してテストします。
