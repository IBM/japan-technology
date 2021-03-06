# API Connect と Secure Gateway を使用してハイブリッド・クラウドを作成する

### オンプレミスのアプリケーションとサービスをハイブリッド・クラウドまで拡張する

English version: https://developer.ibm.com/patterns/create-hybrid-cloud-api-connect-secure-gateway
  
ソースコード: https://github.com/IBM/Hybrid-Cloud-Applications-and-Services

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-10-18

 ## 概要

ハイブリッド・クラウドは、プライベート・クラウドとパブリック・クラウドの要素を融合させて、両方のクラウドにまたがってアプリとサービスを実行する選択肢と柔軟性を提供します。簡単に言えば、ハイブリッド・モデルは主としてプライベート・クラウドであり、必要に応じてパブリック・クラウドを利用できるというモデルです。このコード・パターンでは、オンプレミスとパブリック・クラウドの間でアプリケーションとサービスを公開し合う方法を説明します。

## 説明

次世代のアプリケーションには、プライベート・クラウドとパブリック・クラウドの両方にまたがるマルチクラウドおよびハイブリッドのデプロイメントが必要になります。この新しいクラウドの世界で開発者と企業に必要となってくるのは、オフサイトのパブリック・クラウド上でホストされている基幹システムのアプリケーションからデータ (例えば、顧客データ) にアクセスする方法です。アプリケーションがオンサイトでホストされているとしても、開発者には、API を介して外部に機能を公開する何らかの方法が必要になります。

このコード・パターンでは、トランスポート・プロトコル、そしてセキュアなトンネル経由の接続を作成できる API ゲートウェイを使用して、プライベート・クラウドのアプリケーションと API を企業ファイアウォールの外部に公開します。その上で、アプリケーションをパブリック・クラウドに移動し、オンサイトのリソース (データベースなど) にも引き続きアクセスできるようにします。

ハイブリッドへの移行は、これまでになく容易になっています。私たちがハイブリッドに移行するためにとった以下の方法を学んでください。

* オンプレミス環境をパブリック・クラウドに接続するトンネルを作成する
* WebSphere Liberty (オンプレミスの場合) または Cloud Foundry (パブリック・クラウドの場合) を使用してサンプル・アプリケーションを作成し、実行する
* CouchDB と Docker を使用して、アプリケーションをオンプレミスのデータベースに接続させる
* API ゲートウェイ・フレームワークを使用してアプリケーション API を公開して使用可能にする

## フロー

![フロー](./images/arch-hybridcloud-journey.png)

## 手順

1. オンプレミス環境をパブリック・クラウドに接続します。
1. シナリオ 1: プライベート・クラウド内のアプリケーションに、外部からパブリック・クラウドを介してアクセスできるようにします。
1. シナリオ 2: パブリック・クラウド内のアプリケーションが、プライベート・クラウド内のリソースに接続できるようにします。
1. アプリケーション API をカタログに登録し、API Connect を使用して一般公開します。
