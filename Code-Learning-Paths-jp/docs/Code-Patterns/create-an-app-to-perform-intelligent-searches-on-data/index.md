---
also_found_in:
- learningpaths/get-started-watson-discovery/
authors: ''
completed_date: '2018-02-21'
components:
- watson-discovery
demo:
- button_title: View the demo
  type: youtube
  url_or_id: 5EEmQwcjUa4
draft: false
excerpt: Watson Discovery Service のデータを照会および操作する Web アプリケーションの動作例をご覧ください。このウェブアプリケーションには、独自の
  Watson Discovery Service アプリケーションを開発するための出発点として使用できる複数の UI コンポーネントが含まれています。
github:
- button_title: Get the code
  url: https://github.com/IBM/watson-discovery-ui
last_updated: '2020-03-05'
meta_description: Watson Discovery Service のデータを照会および操作する Web アプリケーションの動作例をご覧ください。このウェブアプリケーションには、独自の
  Watson Discovery Service アプリケーションを開発するための出発点として使用できる複数の UI コンポーネントが含まれています。
meta_keywords: node.js, Watson Discovery
meta_title: データをインテリジェントに検索するアプリの作成
primary_tag: artificial-intelligence
pta:
- cognitive, data, and analytics
pwg:
- watson discovery
related_links:
- title: Overview of the IBM Watson Discovery service
  url: https://www.ibm.com/watson/services/discovery/Extract value from unstructured
    data by converting, normalizing, enriching it.
- description: Download the Watson Node SDK.
  title: Watson Node.js SDK
  url: https://github.com/watson-developer-cloud/node-sdk
- description: Learn how this code pattern fits into the Cognitive discovery Reference
    Architecture.
  title: Architecture center
  url: https://www.ibm.com/cloud/garage/architectures/cognitiveDiscoveryDomain/0_1
- description: Unlock new intelligence from vast quantities of structured and unstructured
    data and develop deep, predictive insights.
  title: Cognitive for intelligence and insights from data
  url: https://www.ibm.com/cloud/garage/architectures/cognitiveArchitecture
- description: Try an app to filter and sort Airbnb Review Data for Ausin, TX
  title: Try the app
  url: https://watson-discovery-ui-demo.mybluemix.net/
runtimes:
- sdk-for-node-js
service-id: wdui
services:
- discovery
subtitle: Node.jsとWatson Discoveryを使用して、充実したデータを抽出・視覚化するウェブアプリを開発する。
tags:
- node-js
title: データをインテリジェントに検索するアプリの作成
type: default
---

**注意：**このコードパターンは Watson Discovery V1 を使用しており、Discovery V2 では使用できません。しかし、Discovery の機能を学ぶために使用することは可能です。将来的には、Discovery V2 で動作するようにコードパターンを更新する予定です。

## まとめ

サイトの標準的な検索では、人が調べたいと思うにはあまりにも多くの結果が返されることがあります。しかし、より関連性の高い検索結果を返すために強化されたデータを照会および操作するすぐに使える UI コンポーネントを使用して、IBM Watson Discovery インスタンスの検索インターフェースをすばやく構築することができます。このコードパターンでは、Airbnb の物件で公開されているレビューを使用して、個々の UI コンポーネントを使用してインサイトを視覚化する方法を示します。このコードパターンは、データセットを簡単に切り替えて、独自のユースケースに適応させることができます。

## 説明

充実したデータを照会・操作することで、より洞察力のある検索インターフェースを構築することができます。このコードパターンでは、Watson Discovery Service 上に構築された Node.js アプリを提供しています。このパターンでは、すぐに使える個々の UI コンポーネントを使用して、Discovery 分析エンジンによって提供される充実したデータを抽出して視覚化する方法を示します。

Watson Discovery Service を使用する主な利点は、データに認知的な豊かさと洞察を提供する強力な分析エンジンです。このコードパターンのアプリでは、フィルター、リスト、グラフを使用してこれらのエンリッチメントを表示する方法の例を示しています。主なエンリッチメントは以下の通りです。

* エンティティ。人物、企業、組織、都市など
* カテゴリー。カテゴリー：データを最大5段階のカテゴリーの階層に分類
* 概念。概念：データの中では必ずしも参照されていない一般的な概念の識別
* キーワード。キーワード：データのインデックスや検索に使用される重要なトピック
* センチメント。センチメント：各ドキュメントの全体的なポジティブまたはネガティブなセンチメント

本アプリでは、フィルタリスト、タグクラウド、センチメントグラフなどの標準的な検索UIコンポーネントに加え、パッセージやハイライト機能などのより複雑なディスカバリーオプションも使用しています。この2つの機能により、アプリはクエリに基づいてデータ内の最も関連性の高いスニペットを識別し、検索しているデータを返す可能性が高くなります。

このコードパターンを完了すると、以下の方法を知ることができます。

* Watson Discovery Service でデータをロードしてエンリッチする。
* Watson Discovery Service でデータをクエリして操作する。
* Watson Discovery Service で作成された充実したデータを表現する UI コンポーネントを作成する。
* Watson Discovery Service のデータとエンリッチメントを機能させるために、一般的な JavaScript 技術を使用して完全な Web アプリを構築する。

## フロー

![フロー](images/Discovery-ui.png)

1. AirbnbのレビューのJSONファイルをDiscoveryコレクションに追加します。
1. アプリUIを使用して、バックエンドサーバーと対話します。フロントエンドのアプリUIはReactを使用して検索結果をレンダリングし、バックエンドがサーバーサイドレンダリングに使用するすべてのビューを再利用できます。フロントエンドはsemantic-ui-reactコンポーネントを使用しており、レスポンシブに対応しています。
1. Discovery は入力を処理してバックエンド・サーバに転送し、バックエンド・サーバはブラウザに表示されるビューのサーバサイド・レンダリングを担当します。バックエンドサーバーは Express を使用して記述されており、express-react-views エンジンを使用して React を使用して記述されたビューをレンダリングします。
1. バックエンド・サーバーは、ユーザーのリクエストを Watson Discovery Service に送ります。プロキシサーバーとして機能し、フロントエンドからのクエリを Watson Discovery Service API に転送する一方で、機密性の高い API キーをユーザーには隠します。

##指示

このコードパターンを使用する準備はできましたか？このアプリケーションの実行と使用を開始する方法の完全な詳細は、<a href="https://github.com/IBM/watson-discovery-ui/blob/master/README.md" target="_blank" rel="noopener noreferrer">README</a>に記載されています。