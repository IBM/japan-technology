# Watson Natural Language Classification のテクノロジーを利用したサポート・チケットの分類

### Watson Natural Language Classification サービスを利用して、消費者からのクレームに対応するためのさまざまなサポート・チケットを分類するアプリを構築する

English version: https://developer.ibm.com/patterns/watson-studio-nlc-technical-support-ticket-categorization
  ソースコード: 'https://github.com/IBM/support-ticket-classification'

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: '2018-11-27'

 
## 概要

このコード・パターンでは、消費者からのクレームに対応するためのさまざまなサポート・チケットを分類するアプリを構築します。アプリを構築するために利用するサービスは、IBM Watson Natural Language Classifier です。このサービスで、消費者からのクレーム・データセットを使用するモデルをトレーニングします。このデータセットは、商業目的でなければ無料で使用できます。商業目的で使用する場合は、明示的な許可を得る必要があります。Watson Developer Cloud Node.js SDK を使用すれば、カスタム Natural Language Classifier モデルを Web UI で迅速、簡単に作成できます。作成したモデルはブラウザーから実行することができます。

## 説明

消費者保護局は、金融商品や金融サービスに関する消費者からのクレームを毎週数千件も受け取り、それらのクレームをさまざまな企業に送信して対応にあたらせます。これだけ大量のクレームが送信されるとなると、企業がそのそれぞれを手作業で調べて該当するカテゴリーに分類するのは難しく、実際的でもありません。適切なチームが対応して適切に解決するまでには、おおよそ 15 日もかかります。こうした手作業による手法では、クレームを効率的にルーティングすることはできません。

一方、サポート・チケットの知識とサンプルがあれば、AI ツールを利用して、サポート・チケットの内容がどのような性質のものであるかを判断できます。そのような AI ツールとして利用するには、IBM Watson Natural Language Classifier が最適です。トレーニング・データを提供すると、どのサポート・チケットがどのカテゴリーに属するかを判断するために必要なすべての情報が Natural Language Classifier サービスから返されてきます。トレーニング・データとして提供するクレームは、GUI を使用して CSV 形式でアップロードできるので、モデルを簡単に作成できます。モデルを作成した後は、Watson Developer Cloud SDK を使用して、このサービスをアプリケーションに統合することができます。

このようなデータの分類は、市場での傾向と問題を識別するのに役立つため、企業の監督、国の消費者保護法の施行、規則の策定を行う上で、より効果的な成果を上げられるようになります。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* Web UI を使用して Watson Natural Language Classifier モデルを作成する
* Natural Language Classifier モデルを使用して消費者サポート・チケットのテキストの集合を分類する Node.js アプリを作成する
* Watson Developer Cloud SDK for Node.js を使用する

## フロー

![フロー](../../images/flow-support-ticket-classification.png)

1. Natural Language Classifier インターフェースとやり取りしてモデルをトレーニングします。
2. [消費者からのクレームに対応するためのサポート・チケット・データセット](https://github.ibm.com/riyamaro/support-ticket-classification/tree/master/docs/training_data)をトレーニング・データとして Natural Language Classifier にロードします。
3. テスト・データを含む Excel ファイル (.csv 拡張子を使用) を分類対象としてアップロードします。
4. アプリケーションが Watson Natural Language Classifier サービスを利用して、サポート・チケットの集合を住宅ローン関連、銀行取引関連、融資関連、クレジット・カード関連のカテゴリー別に分類します。

## 手順

このパターンの詳細な手順については、[README](https://github.com/IBM/support-ticket-classification/blob/master/README.md) ファイルを参照してください。手順の概要は以下のとおりです。

1. GitHub リポジトリーを複製します。
1. IBM Cloud を使用して、Watson Natural Language Classifier サービス・インスタンスを作成します。
1. Natural Language Classifier モデルをトレーニングします。
1. 資格情報を構成します。
1. アプリケーションを実行します。
