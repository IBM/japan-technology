# 新着ニュースのアラートを送るアプリを作成する

### 最新のニュース記事をマイニングして、製品、ブランド、または価格変動に関するカスタム・アラートを送信する

English version: https://developer.ibm.com/patterns/create-cognitive-news-alerting-app
ソースコード: https://github.com/IBM/watson-discovery-news-alerting

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-06-22

 ## 概要

人工知能 API を使用した Web UI を作成することに興味を持つ、JavaScript と Node.js を使い慣れている開発者を対象に作成されたこのパターンでは、Watson Node.js SDK を使用して最新のニュース記事をマイニングし、Watson Discovery Service を利用して製品またはブランドに関するアラートを送信する方法を説明します。このパターンに従って、ニュースで取り上げられている特定の製品またはブランドに関するカスタム・アラートを e-メールで送信するニュース・アプリを Node.js で作成する方法を学んでください。このアプリは、ブランドに対するセンチメントと関連製品、さらに株価の変動に関するアラートもユーザーに送信します。

## 説明

このコード・パターンでは、Watson Discovery サービスを利用して Watson Discovery News にアクセスする Node.js Web アプリケーションを作成します。Watson Discovery News は、Watson Discovery Service に付随して提供されているデータ・コレクションです。主に英語のニュース・コンテンツからなるデータ・セットであり、毎日約 300,000 件の記事とブログを追加して常に更新されます。

このコード・パターンでフォーカスするのは、Watson Discovery サービスを利用して市場での製品ライフサイクルをモニターし、市場内で製品のスタンスが変化した時点でインテリジェントにアラートを送ることです。こうすることにより、製品またはブランドに関する情報とその製品/ブランドが市場でどのように受け止められているかに関するアラートを、ユーザーに定期的に e-メールで送信することができます。アラートによるトラッキングは、以下の分野に対してセットアップできます。

* 製品
* ブランド
* 関連する製品およびブランド
* 製品に対する肯定的または否定的センチメント
* 株価

フロントエンドで Watson Discovery News の検索に使用する管理インターフェースと、カスタマイズ可能なクエリーに関連するアラートを定期的に送信するバックエンド・サービスを作成するために必要となるステップを説明していきます。

## フロー

![フロー](../../images/news-architecture.png)

1. ユーザーがアプリの UI を使用してバックエンド・サーバーとやり取りします。フロントエンドのアプリ UI が検索結果をレンダリングします。この UI は、バックエンドで使用するすべてのビューを再利用してサーバー・サイドのレンダリングを行います。フロントエンドは watson-react-components を使用していて、レスポンシブなものとなっています。
1. ユーザー入力が処理されて、バックエンド・サーバーにルーティングされます。バックエンド・サーバーの役目は、ブラウザー上に表示するビューをレンダリングすることです。Express Node.js Web アプリケーション・フレームワークを使用して作成されたバックエンド・サーバーは、React JavaScript コンポーネント・エンジンを使用して作成されたビューをレンダリングするために、express-react-views エンジンを使用します。
1. バックエンド・サーバーが、サブスクリプション情報を Cloudant&reg; NoSQL データベース内に保管して、製品をトラッキングできるようにします。
1. バックエンド・サーバーがユーザー・リクエストを Watson Discovery Service に送信します。バックエンド・サーバーはプロキシー・サーバーとして機能し、フロントエンドからのクエリーを、機密性の高い API キーをユーザーから隠した状態で Watson Discovery Service API に転送します。
1. Watson Discovery サービスが Watson Discovery News コレクションに対し、製品に関する記事のクエリーを実行します。
1. バックエンド・サーバーは定期的な更新を e-メール・アドレスに送信します。

## 手順

Ready to put this code pattern to use? Find the detailed steps for this pattern in the [README](https://github.com/IBM/watson-discovery-news-alerting/blob/master/README.md).
