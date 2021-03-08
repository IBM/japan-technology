# Watson Machine Learning と Jupyter Notebook を利用してデータ分析、モデルの作成、デプロイを行う

### IBM Cloud Pak for Data 上で Watson Machine Learning と Jupyter Notebook を利用してカスタマー・チャーンを予測する

English version: https://developer.ibm.com/patterns/data-analysis-model-building-and-deploying-with-wml
  ソースコード: https://github.com/IBM/telco-customer-churn-on-icp4d

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-10-04

 
**このコード・パターンは[ラーニング・パス「IBM Cloud Pak for Data 入門」](https://developer.ibm.com/jp/series/cloud-pak-for-data-learning-path/)を構成するコンテンツになっています**。

| レベル | トピック | タイプ |
 
## 概要

このコード・パターンでは IBM Cloud Pak&reg; for Data を使用して、Telco Customer Churn データセットに基づいてビジネス問題を解決し、カスタマー・チャーンを予測するデータ・サイエンス・パイプライン全体を見ていきます。IBM Cloud Pak for Data はクラウド・ベースのインタラクティブなコラボレーション環境です。データ・サイエンティストと開発者、そしてデータ・サイエンスに関心を持つ人々がツールを使用して共同で作業し、データから引き出した洞察を共通、収集するために利用できるだけでなく、機械学習モデルと深層学習モデルを作成してデプロイすることもできます。

## 説明

カスタマー・チャーン (顧客が企業との取引関係を終わらせること) は、ビジネスの収益を左右する最も基本的な要因の 1 つです。この問題を解決するためには、どの顧客が忠実で、どの顧客にチャーンのリスクがあるかを把握し、チャーンの決定に影響する要因を顧客の観点から理解しなければなりません。そこで、このコード・パターンでは機械学習モデルを作成し、そのモデルを使用してチャーンのリスクがある顧客を予測する方法を説明します。ここで取り上げるのは完全なデータ・サイエンス・プロジェクトであり、このプロジェクトで作成したモデルによる調査結果は、規範的分析やターゲットを絞ったマーケティングに使用できます。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* [Jupyter Notebook](https://jupyter.org/) を使用してデータをロード、視覚化、分析する
* Jupyter Notebook を [IBM Cloud Pak for Data](https://www.ibm.com/jp-ja/analytics/cloud-pak-for-data) 内で実行する
* IBM Cloud Pak for Data 上で [Spark MLib](https://spark.apache.org/mllib/) を使用して機械学習モデルを作成、テスト、デプロイする
* IBM Cloud Pak for Data を使用して、選択した機械学習モデルを本番環境にデプロイする
* クライアントとインターフェースをとるフロントエンド・アプリケーションを作成し、デプロイしたモデルの使用を開始する

## フロー

![フロー](../../images/datanalarch.png)

1. ユーザーが Jupyter Notebook を IBM Cloud Pak for Data platform にロードします。
1. [Telco Customer Churn データセット](https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv)を GitHub から直接 Jupyter Notebook にロードします。または、[ラーニング・パス「IBM Cloud Pak for Data 入門」](https://developer.ibm.com/jp/series/cloud-pak-for-data-learning-path/)の[データ仮想化チュートリアル](https://developer.ibm.com/jp/tutorials/virtualizing-db2-warehouse-data-with-data-virtualization/)の手順に従った後、仮想化されたデータとしてロードすることもできます。
1. データを前処理し、機械学習モデルを作成して IBM Cloud Pak for Data 上の Watson&reg; Machine Learning に保存します。
1. 選択した機械学習モデルを IBM Cloud Pak for Data プラットフォーム上の本番環境にデプロイし、採点エンドポイントを取得します。
1. フロントエンド・アプリケーションを使用して、モデルを基に信用度を予測します。

## 手順

このコード・パターンに取り組む準備はできましたか？このアプリケーションを起動して使用する方法について詳しくは、[README](https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/README.md) ファイルを参照してください。

## まとめ

このコード・パターンでは IBM Cloud Pak for Data を使用して、Telco Customer Churn データセットに基づいてビジネス問題を解決し、カスタマー・チャーンを予測するデータ・サイエンス・パイプライン全体を詳しく調べる方法を説明しました。このコード・パターンは[ラーニング・パス「IBM Cloud Pak for Data 入門」](https://developer.ibm.com/jp/series/cloud-pak-for-data-learning-path/)の一部です。  このシリーズで引き続き IBM Cloud Pak for Data の詳細を学ぶには、次のコード・パターン [Watson OpenScale でモデルをモニタリングする](https://developer.ibm.com/jp/patterns/watson-openscale-with-watson-machine-learning-engine-on-icp4d) をご覧ください。
