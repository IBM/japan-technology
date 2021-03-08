# コグニティブ・ニュース検索アプリを作成する

### Node.js と Watson Discovery サービスを利用して、ニュースを検索してトレンディング・トピックを分析するコグニティブ Web アプリを構築する

English version: https://developer.ibm.com/patterns/create-a-cognitive-news-search-app

ソースコード: https://github.com/IBM/watson-discovery-news/

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-06-28

 ## 概要

ニュース・データをエンリッチすると、アプリケーションによって、動的に現在のイベントを相互に関連付ける機能の迅速化に役立ちます。このコード・パターンでは、JavaScript、Node.js、Watson Discovery サービスを利用して、ニュース・マイニング Web アプリケーションを構築する方法を説明します。Watson Node.js SDK を使用して、最新のニュースを検索して傾向を検出する独自のニュース・アプリを構築してください。このアプリには、さらに Slack などの他のアプリケーションも統合します。

## 説明

大量のデータが存在する Web に、毎日さらにデータが作成され続けています。組織はこの絶え間なく生成され続けるデータを利用して、情報に対する理解を深め、戦略を計画し、機会を見いだすことができれば、成功をつかむことができます。したがって、組織が大量のデータを利用できるよう支援できる開発者は、不可欠の存在となるはずです。

Watson Discovery サービスを使用すると、開発者は、コグニティブ検索とコンテンツ・アナリティクス対応のクラウド・ネイティブのアプリケーションを作成できます。しかも Watson Discovery 内では、事前にエンリッチされたデータ・コレクションとして、Watson Discovery News を使用することができます。Watson Discovery News は、毎日約 300,000 件のニュース記事とブログを追加して継続的に更新される、すぐに使える最新ニュースのデータ・セットです。

このコード・パターンでは、この大量のデータ・セットを利用して洞察をマイニングする方法を説明するために、Watson Discovery サービスを使用し、Watson Node.js SDK を使ってニュース・マイニング Web アプリケーションを構築します。Watson Discovery News の具体的な使用ケースとして、次の 2 つを取り上げます。

* **検索**: 特定のトピックまたはサブジェクトに最も関連性の高い最新の記事をクエリーします。ニュース・コレクションは自然言語処理によって事前にエンリッチされるため、キーワードやカテゴリーに基づくクエリーだけでなく、概念、センチメント、関係を基準にしたクエリーによってよりリッチな検索結果を得ることができます。
* **ニュースのトレンディング・トピック**: 過去 24 時間にわたってよく取り上げられているトピックを特定します。一般的なトピックでも、業界やカテゴリーに固有のトピックでも特定することができます。

このコード・パターンに従って、アプリ開発やサービスのスキルを磨いてください。このコード・パターンを完了すると、以下の方法がわかるようになります。

* Watson Discovery を使い、Node.js を使用してニュース・マイニング Web アプリケーションを作成する
* ニュースを検索してトレンディング・トピックを検出するなど、基本的な Watson Discovery 機能を使用する
* RSS ニュース・フィード・ジェネレーターを作成して、トレンディング・トピックのニュースを任意の RSS リーダーにプッシュする
* Slack の検索機能にアクセスする SlackBot を作成する

## フロー

![フロー](./images/cognitive-news-search-arch-1.png)

1. ユーザーが API の UI を操作して関連するニュース・コンテンツをリクエストします。
1. アプリがユーザー・リクエストを Watson Discovery News に送信します。
1. Watson Discovery Service は継続的に Web をクロールして Discovery News コレクションを更新します。
1. Watson Discovery Service が Slack 検索リクエストに応答します。
1. Watson Discovery Service がニュース記事を RSS リーダーに入力します。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the [README](https://github.com/IBM/watson-discovery-news/blob/master/README.md).
