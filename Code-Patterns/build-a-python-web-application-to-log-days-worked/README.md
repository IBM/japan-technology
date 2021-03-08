# Python Flask アプリケーションを Kubernetes 内にデプロイする

### 勤務日と勤務形態をログに記録する

English version: https://developer.ibm.com/patterns/build-a-python-web-application-to-log-days-worked
  ソースコード: https://github.com/IBM/worklog

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-11-06

 
## 概要

このコード・パターンでは、Docker コンテナー内の MongoDB をマイクロサービスとして統合する Python Flask アプリケーションを作成します。これらのコンテナーは Kubernetes 内にデプロイします。

## 説明

このコード・パターンでは、Flask、MongoDB、Kubernetes を使用して Work Log Web アプリケーションを作成します。Work Log は、仕事に関連付けられたさまざまなタイプの日々を記録するために使用するアプリケーションです。ログには次のタイプ別に日々を記録します。

* オフィス勤務
* 遠隔勤務
* 休暇
* 休日
* 病欠

このコード・パターンを完了すると、以下の方法がわかるようになります。

* Python Flask アプリケーションを作成する
* MongoDB を Python アプリケーションに統合する
* マイクロサービスを Kubernetes 上にデプロイして実行する

## フロー

![フロー](../../images/architecture.png)

1. ユーザーが App UI を操作して、最初にアカウントを作成します。ユーザーはそのアカウントにログインするか、アカウントのパスワードをリセットします。ログインした後、ユーザーは自分の仕事のログ・データを表示、追加、編集できます。
1. ユーザーが操作する App UI の機能は、React によって処理されます。API 呼び出しは、React から開始されます。
1. Kubernetes 上の Flask API マイクロサービス内で、API 呼び出しがその目的に応じて処理されます。
1. API 呼び出しによって、MongoDB 内でデータが保管、収集、変更されます。
1. API 呼び出しからのレスポンスが、App UI によって適切に処理されます。

## 組み込まれているコンポーネント

* [IBM Cloud Container Service](https://cloud.ibm.com/docs/containers/container_index.html): IBM Bluemix Container Service を利用すると、IBM Cloud 上の Kubernetes クラスターに含まれる Docker コンテナー内で可用性の高いアプリを管理できます。
* [Swagger](https://swagger.io/): OpenAPI 仕様に対応するための API 開発者向けツールからなるフレームワークです。Swagger により、API ライフサイクル全体にわたる開発が可能になります。

## 主要なテクノロジー

* [コンテナー・オーケストレーション](https://www.ibm.com/cloud/container-service): コンテナー化されたアプリケーションのデプロイ、スケーリング、管理を自動化します。
* [マイクロサービス](https://www.ibm.com/developerworks/community/blogs/5things/entry/5_things_to_know_about_microservices?lang=en): マイクロサービスとは、クラウド内で最新式のアプリケーションを組み立てるためにビルティング・ブロックとして疎結合される、軽量のプロトコルを使用した一連のサービスのことです。
* [Python](https://www.python.org/): Python をプログラミング言語として使用すると、より迅速にプログラムを作成し、より効率的にシステムを統合できます。
* [Flask](http://flask.pocoo.org/): API を作成するための Python 対応マイクロフレームワークです。
* [React](https://reactjs.org/): ユーザー・インターフェースを作成するための JavaScript ライブラリーです。
* [MongoDB](https://www.mongodb.com/): ドキュメント指向の NoSQL データベースです。

## ブログ

この Web アプリケーションの作成方法を詳しく説明している[ブログ投稿](https://developer.ibm.com/blogs/my-journey-to-creating-my-first-web-application/)を読んでください。
