# IoT ダッシュボードを使用して、ブロックチェーン・ネットワークから送信されたデータを分析する

### Watson IoT Platform と Node-RED を使用して、ブロックチェーン・ネットワークから送信された IoT データを分析する IoT アプリケーションと IoT ダッシュボードを作成する

English version: https://developer.ibm.com/patterns/iot-dashboards-analyze-data-blockchain-network
  ソースコード: https://github.com/IBM/Using-IOT-toProcess-BlockchainAnalytics

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-05-01

 
## 概要

このパターンで作成する IBM Cloud IoT アプリは、ブロックチェーン・アプリケーションから受信したデータを Cloudant データベースに挿入し、イベントを Watson IoT Platform に送信します。Watson IoT Platform に送信されたデータは、Node-RED アプリケーション内で分析されてから、Node-RED ダッシュボードまたは IBM Cloud IoT アプリの Watson IoT Platform ダッシュボードに POST リクエストで送信されます。どちらのダッシュボードを使うかは、目的に合わせて決めてください。

## 説明

Hyperledger ネットワークにアクセスせずにブロックチェーン・ネットワーク内で行われる一連のトランザクションを理解する方法として、トランザクションに関するデータを表示して分析する IoT アプリと IoT ダッシュボードを作成することができます。具体的には、このパターンで作成する IoT アプリはユーザーを編成して、トランザクションから値を受信します。ユーザーはデバイスとして登録されます。IoT アプリは生成された値 (ステップなど) を取り、これらの登録ユーザーすべてにわたる値とトランザクションの合計を表示します。さらに、この IoT アプリは受信したブロックチェーンのブロックを解析し、データベース内の既存のユーザーであるかどうかに応じて、ユーザーとそのデータをフィルタリングします。ユーザーが既存のユーザーであれば、そのユーザーのデータがダッシュボードに渡されて、ダッシュボード上で出力が表示されます。これらのトランザクションのすべては、Cloudant データベースに記録されます。

## フロー

![フロー](../../images/blockchain-iot-analytics-arch-diagram.png)

1. Hyperledger ブロックチェーン・ネットワークから、ブロックが JSON オブジェクトとして送信されます。送信されるブロックは、ユーザーとそのデータです。
1. ブロックチェーンのトランザクション (新規ユーザーの作成、ユーザーの検証、ステップに基づく fitcoin の生成) とユーザー・データが IBM Cloud 内の IBM Cloud データベースに格納されます。Watson IoT Platform 内では、ユーザーがデバイスとして登録されます。
1. Watson IoT Platform ダッシュボードまたは Node-RED ダッシュボードのいずれかを使用して、IoT データを表示および分析します。

## 手順

このパターンの詳細な手順については、[README](https://github.com/IBM/Using-IOT-toProcess-BlockchainAnalytics/blob/master/README.md) を参照してください。手順の概要は以下のとおりです。

1. IoT アプリを作成します。Cloudant サービスと Internet of Things サービスをあらかじめ作成し、IBM Cloud アプリのインスタンスにバインドしておく必要があります。
1. JSON ファイルを Node-RED にインポートします。
1. Node-RED ダッシュボードを作成します (インポートによって自動的に作成されなかった場合)。Watson IoT Platform ダッシュボードではなく Node-RED ダッシュボードを使用することも、この 2 つを同時に使用することもできます。
