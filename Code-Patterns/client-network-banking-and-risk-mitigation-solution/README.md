# クライアント・ネットワーク・バンキング

### 'IBM Cloud、Watson サービス、オープンソース・テクノロジーを利用して顧客情報を分析し、顧客に投資する前に早期警告を受けられるようにする'

English version: https://developer.ibm.com/patterns/client-network-banking-and-risk-mitigation-solution
  ソースコード: 'https://github.com/IBM/banking-risk-mitigation-nlu-studio'

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-09-18

 
_**Note: This pattern is part of a composite pattern.** These are code patterns that can be stand-alone applications or might be a continuation of another code pattern. This composite pattern consists of:_

* [Watson のテキスト分類を拡張する](https://developer.ibm.com/jp/patterns/extend-watson-text-classification/)
* [さまざまなソースからのドキュメントを互いに関連付ける](https://developer.ibm.com/jp/patterns/watson-document-correlation/)
* Client network banking (このパターン)

## 概要

信用リスク・マネジメント・プロセスでは、まず始めに顧客を知ることが非常に重要なベスト・プラクティスとされています。それは、以降のすべてのステップは、顧客に関する情報を基に進められていくためです。このプロセスを成功させるためには、適正かつ正確で、時宜を得た情報を基に業務を行う必要があります。けれども、クライアント・ネットワーク情報は各種のソースに散らばっています。このコード・パターンは、クライアント・ネットワークとして知られる、1 つの場所で照合されたリアルタイムの顧客情報を取得するためのものです。このパターンで対象としているのは、銀行で顧客への投資を担当する顧客関係の管理者です。

## 説明

銀行の顧客関係の管理者は、顧客への投資を担当します。投資顧問にとって、顧客に投資する上で最も重要となる考慮事項の 1 つは、リスク評価です。顧客の環境で何らかの変化が生じた場合、どのようなリスクがあるかを評価しなければなりません。さらに、エコシステムやクライアント・ネットワーク内で発生するイベント (経営体制の変更、経営陣の不履行、株価の暴落、信用格付け、ストライキなど) によっても投資に影響が及びます。

このコード・パターンは、クライアント・ネットワークとして知られる、1 つの場所で照合されたリアルタイムの顧客情報を取得するためのものです。この情報は、あらゆる組織に影響する極めて重要なイベントに応じたものとなっています。つまり、人気の高いニュース・サイトからリアルタイムのニュースを取得し、Watson Natural Language Understanding の助けを借りて、そのニュースによって影響を受ける顧客を抽出します。サンプル・アプリケーションでは、IBM Cloud、Watson サービス、Python Flask、Python NLTK を利用して、顧客に関する洞察を引き出す方法を具体的に説明します。

## フロー

![フロー](../../images/flow-client-network-banking-and-risk-mitigation-solution.png)

1. ユーザーがアプリの UI を操作して、特定のイベントまたは顧客に関連する情報を要求します。
1. Web アプリの UI が Python-Flask サーバーとやり取りして、要求された情報を、該当する API から受け取ります。
1. Flask API が人気の高いオンライン・ニュース・ポータルからリアルタイムのニュースを収集します。
1. 収集されたデータが NLU Studio に送信され、重要なエンティティーが抽出されます。
1. JSON 構成ファイルが Flask アプリに送信され、NLU 上で取得された結果がさらに絞り込まれます。
1. 収集されたすべての情報が対話式 UI にプッシュされます。

## 手順

詳細な手順については、[README](https://github.com/IBM/banking-risk-mitigation-nlu-studio/blob/master/README.md) ファイルを参照してください。手順の概要は以下のとおりです。

1. リポジトリーを複製します。
1. IBM Cloud サービス・インスタンスを作成します。
1. IBM Cloud 上でアプリケーションをセットアップします。
1. ローカル・ホスト上でアプリケーションをセットアップします。
1. Python アプリケーションを実行します。
