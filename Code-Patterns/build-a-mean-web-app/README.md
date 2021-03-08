# MEAN Web アプリを構築する

### MongoDB、Express、AngularJS、Node.js スタックを使用してクラウド・ネイティブの Web アプリケーションを作成、デプロイする

English version: https://developer.ibm.com/patterns/build-a-mean-web-app
  ソースコード: https://github.com/IBM/MEAN-app

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-11-07

 ## 概要

この開発者パターンで紹介するコードは、MongoDB、Express.js、AngularJS、Node.js (MEAN) スタックを使用して事前構成された Web アプリを作成するためのものです。作成したアプリケーションは、IBM Cloud サービスを利用してホストします。その上で、IBM Cloud Developer Tools CLI を使用してアプリケーションをローカルで実行してテストしてから、Kubernetes または Cloud Foundry にデプロイします。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* MongoDB、Express.js、AngularJS、Node.js を使用するアプリケーションを構築する
* App Metrics を使用して、モニタリングと分散トレースに対応するアプリケーションを作成する
* IBM Cloud Developer Tools CLI を使用してアプリケーションをデプロイするか、Kubernetes または Cloud Foundry を使用してネイティブにデプロイする

## フロー

![フロー](../../images/mean-architecture.png)

1. ユーザーがブラウザーで AngularJS Web アプリを表示します。
1. AngularJS フロントエンドと Express バックエンドはどちらも Node.js で作成されています。この 2 つのコンポーネントが RESTful API を介して通信します。
1. バックエンドの Express アプリケーションは Mongo データベースを使用してデータを保管、取得します。
1. バックエンドの結果がフロントエンドに返されます。
1. フロントエンドの結果は、人間が読んで理解できる形式でユーザーに表示されます。

## 手順

このパターンに取り組む準備はできましたか？詳細な手順については、[README](https://github.com/IBM/mean-app/blob/master/README.md) を参照してください。
