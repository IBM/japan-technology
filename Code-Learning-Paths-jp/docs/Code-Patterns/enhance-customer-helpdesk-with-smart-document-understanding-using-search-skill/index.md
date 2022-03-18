---
also_found_in:
- learningpaths/get-started-watson-discovery/
authors: ''
completed_date: '2020-03-05'
components:
- watson-discovery
- watson-assistant
- cloud-pak-for-data
- ibm-cloud-functions
demo:
- button_title: Watch the demo
  type: demo
  url_or_id: https://youtu.be/Jpr3wVH3FVA
draft: false
excerpt: 検索スキル「Watson Assistant」と「Watson Discovery」を使って、チャットボットを構築します。
github:
- button_title: Get the code
  url: https://github.com/IBM/watson-assistant-with-search-skill
last_updated: '2021-09-21'
meta_description: 検索スキル「Watson Assistant」と「Watson Discovery」を使って、チャットボットを構築します。
meta_keywords: watson, chatbot, smart document understanding, watson assistant, search
  skill
meta_title: Watson Assistantの検索スキルを利用した「Smart Document Understanding」によるカスタマーヘルプデスクの強化
primary_tag: artificial-intelligence
subtitle: 検索スキル「Watson Assistant」と「Watson Discovery」を使ったチャットボットの構築
tags:
- node-js
title: Watson Assistantの検索スキルを利用した「Smart Document Understanding」によるカスタマーヘルプデスクの強化
type: default
---

## まとめ

この開発者コードパターンでは、典型的なカスタマーケアのチャットボット体験を使用していますが、ダイアログは事前に定義された応答に頼るのではなく、追加の情報源として他の IBM&reg; Watson&trade; サービスを呼び出すことができるフックを提供しています。このケースでは、Watson Discovery にアップロードされているオーナーズマニュアルです。

**注：** このコードパターンには、<a href="https://www.ibm.com/jp-ja/cloud" target="_blank" rel="noopener noreferrer">IBM Cloud</a>と、<a href="https://www.ibm.com/jp-ja/products/cloud-pak-for-data" target="_blank" rel="noopener noreferrer">IBM Cloud Pak for Data</a>を備えた任意のクラウドの両方で動作する Watson サービスにアクセスするための手順が含まれています。

## 説明

一般的なカスタマーケアのチャットボットは、店舗の場所や営業時間、道順などの簡単な質問に答えることができ、場合によっては予約を取ることもできます。質問があらかじめ決められた質問セットの範囲外になると、一般的には、その質問は有効ではないと顧客に伝えるか、実際の人間と話すことを提案するという選択肢があります。

今回のコードパターンでは、もう一つの選択肢を用意しています。お客様からの質問がデバイスの操作に関するものであれば、Watson Assistantの検索スキル機能を使って、デバイスの取扱説明書があらかじめ登録されているWatson Discoveryサービスに質問を渡します。これにより、「カスタマーサポートにお問い合わせください」ではなく、お客様の問題を解決するためにオーナーズマニュアルの関連セクションを返すことができるのです。

さらに一歩進んで、Watson Discovery の Smart Document Understanding 機能を使用して、オーナーズマニュアルのどのテキストが重要で、どのテキストが重要でないかを学習させます。これにより、クエリから返される答えが改善されます。

まとめると、このコードパターンは

* Watson Assistant でカスタマーケアのダイアログスキルを作成する。
* Smart Document Understanding を使用して、強化された Watson Discovery コレクションを構築する。
* Watson Assistant の検索スキルを作成して、アシスタントダイアログが Watson Discovery にクエリを投稿できるようにする

## フロー

![SDU with Search Skill flow](images/enhance-customer-helpdesks-smart-document-understanding-assistant-search-skill.png)

1. Watson Discovery SDU を使用してドキュメントをアノテーションします。
1. ユーザーはアプリUIを通じてバックエンドサーバーと対話する。フロントエンドのアプリUIは、ユーザーと会話をするチャットボットです。
1. ユーザーとバックエンドサーバー間の対話は、Watson Assistantのダイアログスキルを使って調整されます。
1. ユーザーが製品操作に関する質問をした場合、Watson Assistantの検索スキルを使って、Watson Discoveryサービスに検索クエリを発行する。

##指示

詳細な手順は、<a href="https://github.com/IBM/watson-assistant-with-search-skill/blob/master/README.md" target="_blank" rel="noopener noreferrer">Readme</a>ファイルに記載されています。この手順では、以下の方法を説明します。

1. リポジトリをクローンする。
1. Watson サービスを作成します。
1. Watson Discovery を構成します。
1. Watson Assistant サービスを構成します。
1. Watson サービスの認証情報を環境ファイルに追加します。
1. アプリケーションを実行します。