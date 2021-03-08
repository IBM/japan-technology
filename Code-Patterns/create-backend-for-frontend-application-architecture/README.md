# フロントエンドのためのバックエンド・アプリケーション・アーキテクチャーを作成する

### フロントエンドのコードをバックエンドのコードに動的に結び付ける Node.js、Swift、または Java アプリケーションを構築する

English version: https://developer.ibm.com/patterns/create-backend-for-frontend-application-architecture
  ソースコード: https://github.com/IBM/nodejs-backend-for-frontend

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-12-13  

 ## 概要

BFF (Backend for Frontend) というアーキテクチャーを使用すると、クライアント対応のモバイル・アプリまたは Web アプリのためのバックエンドを作成できます。BFF は、複数のクライアントを使用してアプリケーションをサポートすると同時に、システム全体をモノリス・システムではなく疎結合された状態に移行させます。このコード・パターンでは、対応するモバイル・アプリや Web アプリのエクスペリエンスに影響を与えずに、チームが反復型開発でより迅速にアプリの機能を開発し、モバイル・アプリのためのックエンドを管理できるようお手伝いします。

## 説明

マイクロサービス・アーキテクチャーを使用すると、チームが迅速なペースで反復型開発を実践するのにも、高速スケーリングのためのテクノロジーを開発するのにも役立ちます。BFF (Backend for Frontend) アーキテクチャーは、こうしたマイクロサービスを念頭に構築された一種のパターンです。このパターンで主要なコンポーネントとなるのは、アプリケーションのフロントエンドをバックエンドに接続するアプリケーションです。この BFF コード・パターンでは、BFF の主要なコンポーネントを IBM のベスト・プラクティスに従って作成できます。

このコード・パターンを完了すると、次の方法を理解できるようになります。

* Backend for Frontend (BFF) アーキテクチャー・パターンを構築する
* Node.js、Swift、または Java アプリケーションを生成する
* Kubernetes、Cloud Foundry または DevOps パイプラインへのデプロイを目的としたファイルを使用してアプリケーションを生成する
* モニタリングと分散トレースを目的としたファイルを使用してアプリケーションを生成する
* プロビジョニングされたサービスに接続する

このコード・パターンでは、IBM の BFF アプリ開発のベスト・プラクティスを採用したクラウド・ネイティブ・プログラミング・モデルにも簡単に従えるようになっています。テスト・ケース、ヘルス・チェック、メトリックなどは、プログラミング言語ごとに確認できます。

コード・パターンの上部にある「**Build on IBM Cloud (IBM Cloud 上で構築)**」をクリックすると、IBM Cloud サービスを動的にプロビジョニングすることができます。プロビジョニングしたサービスは、皆さんが生成するアプリケーション内で自動的に初期化されます。管理された MongoDB サービス、Watson サービス、または自動テストを追加して、DevOps パイプラインをカスタマイズしてください。

## フロー

![BFF アプリケーションのアーキテクチャー図](../../images/backend-for-frontend-arch-diagram2.png)

1. Node.js、Java、または Swift などの言語に対応可能なユーザー・エクスペリエンス・プラットフォーム (Mobile and Web Apps など) がそれぞれに固有のバックエンドと通信し、必要とされる適切な API やサービス・リクエストを収集します。
2. 各 Backend for Frontend がフロントエンドからのリクエストに必要なサービスを呼び出します。

## 手順

詳細な手順については、README ファイルを参照してください。

* [Node.js](https://github.com/IBM/nodejs-backend-for-frontend)
* [Java](https://github.com/IBM/java-liberty-backend-for-frontend)
* [Spring](https://github.com/IBM/spring-backend-for-frontend)
* [Swift](https://github.com/IBM/swift-backend-for-frontend)
