---
authors: ''
check_date: '2022-09-01'
completed_date: '2021-11-01'
components:
- open-liberty
- websphere-hybrid-edition
draft: true
excerpt: サンプル・アプリケーションのモダナイゼーションの次のステップとして、ランタイムのモダナイゼーションを行います。まず、WebSphere Libertyの使用に移行し、次にOpen
  Libertyの使用に移行します。
menu_order: 14
meta_description: サンプル・アプリケーションのモダナイゼーションの次のステップとして、ランタイムのモダナイゼーションを行います。まず、WebSphere
  Libertyの使用に移行し、次にOpen Libertyの使用に移行します。
meta_keywords: application modernization
meta_title: アプリのランタイムの近代化
primary_tag: application-modernization
subtitle: アプリケーションサーバーからアプリケーションランタイムへの切り替え
tags:
- java
- containers
- microservices
time_to_read: 15 minutes
title: アプリのランタイムの近代化
---

アプリケーション・モダナイゼーションの第2ステップでは、WebSphereアプリケーションをLibertyアプリケーションに変換します。WebSphere Libertyは、オープンソースのOpen Libertyプロジェクトに基づいて構築されており、高速でダイナミック、かつ使いやすいJakarta EEとMicroProfileのアプリケーション・サーバーです。Libertyは、（前回のチュートリアルで有効にしたばかりの）コンテナ化されたワークロードのためのより効率的なランタイムで、クラウド・ネイティブなマイクロサービス・ベースのアプリケーションに最適化されています。

ここでは、アプリケーションを近代化するために赤ちゃんのようなステップを踏んでいるので、まずWebSphere Libertyを使用するようにアプリを移行します。  WebSphere Liberty上で実行するためのコードの変更には、WebSphere Application Serverの移行ツール、Migration Toolkit for Application Binaries（非公式にはバイナリスキャナとして知られている）とWebSphere Application Server Migration Toolkit（ソーススキャナとしても知られている）の両方を使用します。変更しなければならないのは数行のコードだけです。特に、EJBのコードを更新する必要があります。

そして、次のステップは、Open Libertyを使用するように移行することです。<a href="https://developer.ibm.com/articles/6-reasons-why-open-liberty-is-an-ideal-choice-for-developing-and-deploying-microservices/" target="_blank" rel="noopener noreferrer">_use Open Liberty_</a>に移行することで、活発なオープンソース・コミュニティに参加し、最新の新機能をいち早く手に入れることができ、ライセンス費用も少なくて済む可能性があります。  Open Libertyに移行する際には、ホットコードの置き換えや最新のツールを使ったデバッグを活用することで、開発者の生産性を高めるためにアプリを再構築します。

## 前提条件

このラーニングパスのチュートリアルで使用している [サンプル例](/learningpaths/get-started-application-modernization/modernizing-apps-step-by-step/architecture-sample-app/) を確認しておいてください。

次に、まだやっていなければ、サンプルアプリケーションの完全なソースコードを取得するために、リポジトリをクローンします。


## ステップ

1. WebSphere Libertyへの移行
2.オープンリバティへの移行

### ステップ1：WebSphere Libertyへの移行

ランタイムの近代化は WebSphere Liberty への移行から始めます。既存のプロジェクト構造はそのままで、EARファイルのzipファイルを含む4つのサブプロジェクトがあります。  まず、Dockerfileとpom.xmlファイルを更新することで、ランタイムの定義と構成を行います。モノリスをコンテナ化したときにTransformation Adviserから生成されたファイル(/learningpaths/get-started-application-modernization/modernizing-apps-step-by-step/containerize-app/)から始めることもできますが、Dockerfileを手動で定義するだけでも十分に簡単です。

### Step 1a:アプリケーションのランタイムの定義と設定

WebSphere Liberty のイメージには、さまざまな長所と短所を持つものがあります。それらはいくつかの方法で差別化されています。JVM、JDKバージョン、Javaバージョン、UBIイメージ、などです。DockerHubでこれらのイメージのタグをチェックしてみてください。

* <a href="https://hub.docker.com/r/ibmcom/websphere-liberty" target="_blank" rel="noopener noreferrer nofollow">_ibmcom/websphere-liberty_</a>
* <a href=" https://hub.docker.com/_/websphere-liberty " target="_blank" rel="noopener noreferrer nofollow">_websphere-liberty_</a>

ここでは、私のサンプルアプリケーションの<a href="https://github.com/IBM/application-modernization-javaee-quarkus/blob/master/monolith-websphere-liberty/Dockerfile" target="_blank" rel="noopener noreferrer">_Dockerfile_</a>をご紹介します。


最後の行（`RUN configure.sh`）は、キャッシングなどの最適化を実行するため、開発環境では無視して構いません。この行をコメントアウトすることで、イメージの構築やコンテナの再起動がより速くなります。

次のステップでは、pom.xmlファイルを定義する必要があります。実際には、ここでは異なるpom.xmlファイルを定義します。昔のJavaプロジェクトでは、さまざまなアーティファクトを生成するために、さまざまな<a href="https://github.com/IBM/application-modernization-javaee-quarkus/tree/master/monolith-websphere-liberty" target="_blank" rel="noopener noreferrer">_sub-projects_</a>を使用していました。`.ear`、`.war`、`.jar`といったファイルです。

`pom.xml`では、Java EEまたは現在のJakarta EEへの依存を宣言する必要があります。多くの場合、これで必要な依存関係のほとんどをカバーできます。


次に、<a href="https://github.com/IBM/application-modernization-javaee-quarkus/blob/master/monolith-websphere-liberty/liberty/server.xml" target="_blank" rel="noopener noreferrer">_WebSphere Liberty server configuration_ (the server.xml file)</a>を定義する必要があります。このファイルには、どの機能を使用するか、データベースへのアクセス方法、HTTPエンドポイントなどが記述されています。  ここでは、私が使用したものを紹介します。


### Step 1b:必要なコードの変更

<sidebar>
「<a href="https://developer.ibm.com/learningpaths/app-mod-liberty/" target="_blank" rel="noopener noreferrer">_Modernizing your applications to use WebSphere Liberty_</a>」のラーニング・パスを完了し、WebSphere ユーザーが利用できるすべての移行ツールについて詳しく学びます。
</sidebar>

ここでは、WebSphere Application Server Migration Toolkit を使用してコードの変更を行います。

WebSphere Application Server Migration Toolkitの使用方法については、次のビデオをご覧ください。

<iframe width="480" height="270" src="https://www.ustream.tv/embed/recorded/130909621" scrolling="no" allowfullscreen webkitallowfullscreen frameborder="0" style="border:0 none transparent;"></iframe>。

<!--デモが必要な方はこちらをご利用ください。
<iframe width="480" height="270" src="https://www.ustream.tv/embed/recorded/130909625" scrolling="no" allowfullscreen webkitallowfullscreen frameborder="0" style="border:0 none transparent;"></iframe> -->

以下の手順で、<a href="https://www.ibm.com/support/pages/websphere-application-server-migration-toolkit" target="_blank" rel="noopener noreferrer nofollow">_WebSphere Application Server Migration Toolkit_</a>をEclipseにインストールします。

その後、`was-to-lib`という名前のSoftware Analyzer Configurationを作成します。

![Software Analyzer Configurationの作成](images/software-analyzer-config.png)

次に、「Rules」タブから「WebSphere Application Server Version Migration」を選択します。

![Create a Software Analyzer Configuration](images/rules-was-version-migration.png)

ルールセットの構成ダイアログで、ソースアプリケーションサーバーとターゲットアプリケーションサーバーを選択します。

![Create a Software Analyzer Configuration](images/source-target-app-server.png)を参照してください。

この例では、3つのコード変更を行う必要があります。結果は、「Software Analyzer Configuration」ビューの特に「Java Code Review」タブに表示されます。

最初に必要な変更は、「org.codehaus.jackson」の使用を置き換えることです。Eclipse の 'Help' ビューには、変更する必要がある内容が簡単に記載されています。

![Software Analyzer Configurationの作成](images/code-change1.png)

次に必要な変更は、「com.ibm.json」をJava EEのオープンソース・パッケージで置き換えることです。

![Create a Software Analyzer Configuration](images/code-change2.png)

3つ目の変更点はEJBの検索です(最新のLibertyバージョンではもう必要ないかもしれません)。

![Create a Software Analyzer Configuration](images/code-change3.png)

### Step 2: Open Liberty への移行

WebSphere Liberty上でサンプルアプリが動作するようになったので、次のベビーステップとして、Open Liberty上で動作するように移行してみましょう。  Open Libertyへの移行の一環として、アプリの構造をシンプルにして、よりクラウドネイティブなアプリにしていきます。

Open Libertyを使用するメリットについては、こちらのビデオをご覧ください。

<iframe width="480" height="270" src="https://www.ustream.tv/embed/recorded/130909633" scrolling="no" allowfullscreen webkitallowfullscreen frameborder="0" style="border:0 none transparent;"></iframe>。

### Step 2a:アプリケーションのランタイムの定義と設定

WebSphere LibertyはOpen Libertyをベースにしているため、必要な変更点はそれほど多くありませんが、いくつかの違いがあります。

まず、変更が必要なのはDockerfileです。<a href=" https://github.com/IBM/application-modernization-javaee-quarkus/blob/master/monolith-websphere-liberty/Dockerfile.multistage" target="_blank" rel="noopener noreferrer">_WebSphere Liberty Dockerfile_</a>は、<a href=" https://github.com/IBM/application-modernization-javaee-quarkus/blob/master/monolith-open-liberty-cloud-native/Dockerfile.multistage" target="_blank" rel="noopener noreferrer">_Open Liberty version_</a>と似ているので、手動で作成する必要があります。


Javaアプリケーションの場合、私は常に多段の`Dockerfile`を使用して、どこでコードをビルドしても、Mavenのビルドが常に同じ結果を返すようにしています。これにより、JVM、Mavenのバージョン、JDKのバージョンなどが異なる場合の問題が解消されます。

正しいOpen Libertyのイメージを選ぶには、<a href="https://github.com/OpenLiberty/ci.docker#container-images" target="_blank" rel="noopener noreferrer nofollow">_Open Liberty documentation_</a>をチェックしてください。DockerHubには様々なOpen Libertyプロジェクトがありますが、推奨されるイメージはDocker Officialイメージ（<a href="https://hub.docker.com/_/open-liberty" target="_blank" rel="noopener noreferrer nofollow">_open-libty_</a>）ではなく、Universal Base Image (UBI) (<a href="https://hub.docker.com/r/openliberty/open-liberty" target="_blank" rel="noopener noreferrer nofollow">_openliberty/open-libty_</a>)になります。

オープンリバティを使い始めるには、`full`というタグのついたイメージから始めるのがいいでしょう。これらのイメージにはフルランタイムが含まれているので、サイズは大きくなりますが、最初は使いやすいでしょう。その後、`slim`バージョンを使用したり、'features.sh'スクリプトを実行して必要な機能だけを取り出したりすることで、イメージを最適化することができます。

また、最後の行（`RUN configure.sh`）をコメントアウトすることで、イメージの構築とコンテナの再起動がより高速になります。

次に、手動で単一の<a href="https://github.com/IBM/application-modernization-javaee-quarkus/blob/master/monolith-open-liberty-cloud-native/pom.xml" target="_blank" rel="noopener noreferrer">_pom.xml_</a>ファイルを作成し、ファイル内のいくつかの依存関係を変更する必要があります。移行をできるだけ簡単にするために、`umbrella`の依存関係であるJakartaとMicroProfileを使い、最新のバージョンを選ぶようにします。また、`pom.xml`ファイルでJavaのコンパイルバージョンを変更することもできます。

次に、手動で作成する<a href="https://github.com/IBM/application-modernization-javaee-quarkus/blob/master/monolith-open-liberty-cloud-native/src/main/liberty/config/server.xml" target="_blank" rel="noopener noreferrer">_server.xmlファイル_</a>に、Open Libertyが使用する機能を定義する必要があります。  server.xmlでは、再び「アンブレラ」機能を使用します。MicroProfile reactive featureはMicroProfile coreに含まれていないため、別途定義する必要があります。


### Step 2b:必要なコードを変更する

最近の開発者は、最新のフレームワークを使ってコードを書く際に、特定の機能を利用することに慣れています。例えば、次のようなことが考えられます。

* ホットコードの置き換え
* コンテナでのデバッグを含む、デバッグ
* エラー、警告、オートコンプリートなどのIDEサポート

Open Libertyがこのような機能を提供していること、特にdevモードが気に入っています。

* Open Liberty を開発モードで起動するには、<a href="https://github.com/OpenLiberty/ci.maven/blob/master/docs/dev.md#dev" target="_blank" rel="noopener noreferrer nofollow">_mvn_liberty:dev_</a> とします。
* Open Liberty をコンテナ対応の dev モードで起動するには、このコマンドを使用します。  <a href="https://github.com/OpenLiberty/ci.maven/blob/master/docs/dev.md#devc-container-mode" target="_blank" rel="noopener noreferrer nofollow">_mvn_liberty:devc_</a>

残念ながら、この機能はマルチモジュールを使用するいくつかのレガシープロジェクトでは動作しません。これらのプロジェクトには、複数のサブプロジェクトが存在し、ear、jar、warファイルなどの異なるアーティファクトを生成していることがよくあります。これらのサブプロジェクトは、相互に依存関係を持つ独自のpom.xmlファイルを持っています。このようなタイプのプロジェクトでは、devモードは機能しません。

Open Libertyの開発モードで生産性向上ツールを使用するために、私はプロジェクトの構造を変更しました。

* <a href="https://github.com/IBM/application-modernization-javaee-quarkus/tree/master/monolith-open-liberty" target="_blank" rel="noopener noreferrer">_複数のモジュールを持つ元のコード_</a>
* <a href="https://github.com/IBM/application-modernization-javaee-quarkus/tree/master/monolith-open-liberty-cloud-native" target="_blank" rel="noopener noreferrer">_Modernized code with one project_</a>

要約すると、以下のような変更が必要でした。

* 新しいOpen Libertyプロジェクトを作成し、その中にすべてのサブプロジェクトのソースコードをコピーします。
* すべてのpom.xmlファイルをマージする
* 設定ファイル（server.xml、persistence.xmlなど）を引き継ぐ。
* Dockerfileのパスを更新する

左側のプロジェクト構造は、元のマルチモジュール構造を示し、右側は簡略化した新しい構造を示しています。

![簡易プロジェクト構造](images/simplified-project-structure.png)

コードを単純化するために、EJB（Enterprise Java Beans）をCDI（Contexts and Dependency Injection）に置き換えました。例えば、これは元々のEJBのコードです。

これがCDIを使った変換後のコードです。

トランザクションを処理するには、Java/Jakarta EE標準のJava Transaction API (JTA)の一部である`@Transactional`を使用できます。最も簡単な方法は、メソッドにこのアノテーションを使用することです。

さらにコントロールが必要な場合は、トランザクションを手動で管理することもできます。


## まとめと次のステップ

このチュートリアルでは、サンプルアプリケーションの近代化の次のステップとして、ランタイムの近代化を行いました。まず、WebSphere Liberty を使用するように移行し、次に、Open Liberty を使用するように移行しました。

アプリケーションのモダナイゼーションの次のステップは、モノリシックなアプリをマイクロサービスにリファクタリングすることです。