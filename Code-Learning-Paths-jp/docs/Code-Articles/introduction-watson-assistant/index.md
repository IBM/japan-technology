---
also_found_in:
- learningpaths/get-started-watson-assistant/
authors: ''
completed_date: '2019-08-06'
components:
- watson-assistant
display_in_listing: true
draft: false
excerpt: Watson Assistantの概要を知り、AIの力を使ってお客様をサービスリソースにつなぎ、お客様の関心を維持し、問題を解決するためにWatson
  Assistantがどのように役立つかを学びます。
last_updated: '2021-10-04'
meta_description: Watson Assistantの概要を知り、AIの力を使ってお客様をサービスリソースにつなぎ、お客様の関心を維持し、問題を解決するためにWatson
  Assistantがどのように役立つかを学びます。
meta_keywords: assistant, chatbot, watson, learning path, getting started, beginner,
  conversation, watson assistant
meta_title: Watson Assistantの紹介
primary_tag: artificial-intelligence
related_links:
- title: IBM Watson Assistant
  url: https://www.ibm.com/jp-ja/products/watson-assistant
- title: Watson Assistant on IBM Developer
  url: https://developer.ibm.com/components/watson-assistant/
subtitle: Watson Assistantサービスの基本を学ぶ
tags:
- conversation
- machine-learning
- deep-learning
title: Watson Assistantの紹介
---

## 概要

IBM Watson Assistant は、あらゆるメッセージング・プラットフォーム、アプリケーション、デバイス、チャネルにおいて、お客様に迅速で一貫性のある正確な回答を提供する、AI を搭載したバーチャル・エージェントです。AI と自然言語処理を使用して、Watson Assistant はお客様との会話から学習し、問題を最初に解決する能力を向上させるとともに、長い待ち時間や退屈な検索、役に立たないチャットボットに対する不満を解消します。

Watson Assistantを使えば、あらゆるアプリケーション、デバイス、チャネルに会話型インターフェースを構築することができます。ほとんどのバーチャルアシスタントは人間のインタラクションを模倣しようとしますが、Watson Assistantはナレッジベースから答えを検索するタイミング、明確な説明を求めるタイミング、そして人間に誘導するタイミングを把握しています。人間のパーソナルアシスタントのように、あなたが作ったアシスタントは、お客様がタスクを実行したり、質問に答えたりするのをサポートします。これを実現するために、アシスタントのアクションを定義します。

アクションとは、ユーザーのリクエストに応じてアシスタントに実行させたい個別の結果を表します。アクションは、特定の質問やリクエストに関するお客様とアシスタントとのやりとりを表します。このやりとりは、アクションを開始するユーザーの入力から始まります（例えば、「お金をおろしたい」など）。その後、アシスタントがより多くの情報を収集する際に追加のやり取りが行われ、アシスタントがリクエストを実行したり、お客様の質問に答えたりしたときに終了することがあります。

Watson Assistantを紹介するビデオはこちらです。

<iframe src="https://player.vimeo.com/video/590052149?h=05c4576022" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
<p><a href="https://vimeo.com/590052149">IBM Watson Assistant solves customer problems the first time</a> from <a href="https://vimeo.com/watsonassistant">Watson Assistant</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

## Why use Watson Assistant?

バーチャルアシスタント（チャットボット）は、よくあるギミック的なアプローチをはるかに超えています。ボットを使ってアポイントメントを設定したり、車を呼んだりすることができます。検索の代わりになるわけではありません。Amazon EchoやGoogle Homeは、仮想アシスタントの優れた例です。インターフェースがないので、しっかりと構造化された対話で話を進めることが不可欠です。

Watson Assistantが優れている例としては、顧客のセルフサービスと従業員のセルフサービスが挙げられます。Watson Assistantでは、次のような特徴があります。

* 一般的な質問には直接回答し、より複雑な質問にはより一般的な検索結果を参照するタイミングを把握します。
* バーチャルアシスタントでは対応できない問題は、人間のエージェントに引き継ぐ。新しい（2021年10月8日以降）Watson Assistantインスタンスは、Genesys、Nice inContact、Twilio、または自社のエージェントとシームレスに統合します。
* 電話番号と統合して、ユーザーがアシスタントと会話できるようにします。Watson Assistantが電話番号を生成するか、IntelePeer、Genesys、Twilioなどの既存のSIPプロバイダと統合します。
* Slack や Facebook Messenger などのエンドチャネルと直接統合することで、ユーザーにとって最も便利な場所でリクエストを処理することができます。
* ユーザーインタラクション内のデータを保存し、時間の経過とともにエクスペリエンスのガイドやパーソナライズに利用可能です。

## アーキテクチャ

次の図は、すべての実装に共通する Watson Assistant のアーキテクチャを示しています。このアーキテクチャは、Watson Assistantを展開する際に使用される典型的なアプローチです。

* ユーザーは、これらの統合ポイントの 1 つ以上を通じてアシスタントと対話します。

    * 既存のウェブサイトで実行されるウェブチャットのコードスニペット

    * WhatsAppとTwilio、Slack、Facebook Messengerなど、既存のサードパーティメッセージングプラットフォームに直接公開されるバーチャルアシスタント

    * ユーザーが電話でアクセスする音声アシスタント

    * モバイルアプリや音声インターフェースを備えたロボットなど、お客様が開発するカスタムアプリケーション

* 音声アシスタントは、ユーザーの入力を受け取り、それをダイアログスキルに送ります。

* ダイアログスキルは、ユーザーの入力をさらに解釈し、会話の流れを指示します。ダイアログは、ユーザーに代わって応答したり、トランザクションを実行したりするために必要な情報を収集します。

* ダイアログスキルで答えられない質問は、サーチスキルに送られ、目的に応じて設定した企業のナレッジベースを検索して、関連する答えを見つけます。

![Assistant architecture](https://cloud.ibm.com/docs-content/v1/content/07a736e5918d8c2d1dca127f22a26923060e7653/services/assistant/images/arch-overview-search.png)



## 用語

このセクションでは、アプリケーションで Watson Assistant を使用するための学習パスに沿って、知っておく必要のある用語を説明します。

| 用語 | 定義 |
| --- | --- |
| [アシスタント](https://cloud.ibm.com/docs/services/assistant?topic=assistant-assistants) | お客様の問題を解決するための最適なパスにリクエストを誘導します。アシスタントが一般的な質問に直接回答したり、より複雑なものにはより一般的な検索結果を参照できるように、スキルを追加します。|
| アクション|特定の質問やリクエストに関するお客様とアシスタントとのやりとりを含みます。|
| ステップ|アクションでは、アクションのきっかけとなった最初のお客様の入力に続く、会話の順番を定義します。|
| [ウェブチャット](https://cloud.ibm.com/docs/assistant?topic=assistant-web-chat-basics) | ウェブチャットは、あなたのウェブサイトにすぐに埋め込むことができるコードスニペットです。|
| [電話統合](https://cloud.ibm.com/docs/assistant?topic=assistant-deploy-phone) | アシスタントに自動的に接続される作業用の電話番号です。また、ご希望であれば、既存のセッション開始プロトコル(SIP)を設定することで、アシスタントを既存のインフラに接続することも可能です。|

## Watson Assistant はどこで利用できますか？

Watson Assistantは、パブリッククラウドとプライベートクラウドの両方で利用できます。

* **パブリック・クラウド**。Watson Assistant は [IBM Cloud](https://cloud.ibm.com/catalog/services/watson-assistant?cm_sp=ibmdev-_-developer-articles-_-cloudreg)で利用できます。Watson Assistant ["Getting started tutorial"](https://cloud.ibm.com/docs/services/assistant?topic=assistant-getting-started)では、サービスの設定に関する追加情報を提供しています。

* **プライベート・クラウド**。Watson Assistant は、[IBM Cloud Pak for Data](https://www.ibm.com/jp-ja/products/cloud-pak-for-data)を使用して、オンプレミスまたはマネージドの IBM プライベート・クラウドからも利用できます。

## SDK

様々なAIサービスをサポートするいくつかのSDKが用意されています。それらは以下のリストに限定されるものではありません。

* [Node SDK](https://github.com/watson-developer-cloud/node-sdk)
* [Python SDK](https://github.com/watson-developer-cloud/python-sdk)
* [Swift SDK](https://github.com/watson-developer-cloud/swift-sdk)
* [Java SDK](https://github.com/watson-developer-cloud/java-sdk)
* [Go SDK](https://github.com/watson-developer-cloud/go-sdk)
* [Ruby SDK](https://github.com/watson-developer-cloud/ruby-sdk)
* [.NET SDK](https://github.com/watson-developer-cloud/dotnet-standard-sdk)
* [Salesforce SDK](https://github.com/watson-developer-cloud/salesforce-sdk)

## API

[Watson Assistant V1 API](https://cloud.ibm.com/apidocs/assistant)をご利用いただけますが、アプリでは[Watson [Assistant V2 API](https://cloud.ibm.com/apidocs/assistant-v2)のご利用をお勧めします。

## 結論

本記事では、Watson Assistant の紹介を行いました。サービスの概要を説明し、そのアーキテクチャや用語・概念を解説しました。機能や価格など、Watson Assistant の概要を知るには、<a href="https://www.ibm.com/jp-ja/cloud/watson-assistant" target="_blank" rel="noopener noreferrer">Watson Assistant 製品ページ</a>をご覧ください。