---
authors: ''
check_date: '2021-12-18'
completed_date: '2020-12-18'
components:
- application-modernization
display_in_listing: true
draft: false
excerpt: IBM Mono2Microを使用してビジネス・アプリケーションを近代化し、モノリシックなJavaアプリケーションをAIの力でマイクロサービスに変換します。
ignore_prod: false
last_updated: '2020-12-18'
meta_description: IBM Mono2Microを使用してビジネス・アプリケーションを近代化し、モノリシックなJavaアプリケーションをAIの力でマイクロサービスに変換します。
meta_keywords: modernize, modernization, refactor, refactoring, application refactoring,
  app refactoring, microservice, microservices, mono2micro, ibm mono2micro, java
meta_title: IBM Mono2Microを使って、モノリシックなJavaアプリケーションをAIの力でマイクロサービス化する
primary_tag: java
related_content:
- slug: mono2micro-automate-application-refactoring-using-ai
  type: articles
- slug: advantages-of-using-ibm-mono2micro-to-automate-application-refactoring
  type: articles
- slug: challenges-and-patterns-for-modernizing-a-monolithic-application-into-microservices
  type: articles
related_links:
- title: IBM Mono2Micro
  url: http://ibm.biz/Mono2Micro
subtitle: IBM Mono2Microによるビジネスアプリケーションの近代化
tags:
- microservices
title: モノリシックなJavaアプリケーションをAIの力でマイクロサービス化する
---

<!--##############################

このチュートリアルは、 *[Introduction to IBM Mono2Micro](/series/intro-to-ibm-mono2micro/)* シリーズの一部です。

| レベル | トピック | タイプ |
| --- | --- | --- |

| 101 | [IBM Mono2Microを視覚的に紹介](/videos/introduction-to-mono2micro/) | 動画 | |
| 102 ｜ [IBM Mono2Micro を使用してアプリケーションのリファクタリングを自動化するメリットを理解する](/articles/Advantages-of-using-ibm-mono2micro-to-automate-application-refactoring/)| 記事 |
***| **201**｜**Use IBM Mono2Micro to transform monolithic Java applications into the microservices with the power of AI**｜**Tutorial**｜**Tutorial**｜***。

このシリーズでは、IBM Mono2Microの主な機能と、それを使ってモノリシックなJavaアプリケーションをマイクロサービスに変換する方法を学びます。-->

## はじめに

ビジネス・アプリケーションを近代化するための最良の方法の1つは、マイクロサービスにリファクタリングすることです。各マイクロサービスは、独立して機能強化と拡張が可能であり、敏捷性と提供速度の向上を実現します。また、マイクロサービスは、レガシーアプリケーションをクラウドに移行するための自然な方法でもあります。

Mono2Microは、新しい機械学習アルゴリズムと世界初のコード生成技術を用いたAIベースの半自動ツールセットで、Javaアプリケーションのコードやビジネスロジックを書き換えることなく、完全または部分的なマイクロサービスへのリファクタリングの旅を支援します。Mono2は、モノリシックなアプリケーションを静的および動的に分析し、モノリシックなアプリケーションを潜在的なマイクロサービスとなるクラス群に分割する方法を提案します。パーティション化に基づいて、Mono2Microはマイクロサービスの基礎コードとAPIを生成し、既存のモノリシックなJavaクラスと一緒に、実行中のマイクロサービスを実装してデプロイするために使用できるようにします。

![](images/1-mono2micro-overview.png)

次の図は、Mono2Microを使って、既存のモノリシック・アプリケーションのデータを収集し、AIアナライザ・ツールを実行して、アプリケーションを分割する異なる方法に関する2種類の推奨事項を生成するところまでを示したハイレベルなフロー図です。

![](images/2-high-level-flow.png)

すべてのデータを収集する方法については、「[モノリシックアプリケーションのデータ収集](#collecting-data-on-the-monolithic-application)」のセクションで詳しく説明しますが、基本的にデータは、コード分析から静的に収集され、インスツルメンテーションされたモノリシックアプリケーションをさまざまなユースケースシナリオで実行してコードベースをできるだけ多く活用することで動的に収集されます。

Mono2Microは、収集したデータに基づいて、パーティション間のクラスの包含依存性や絡み合い（言い換えれば、クラスがパーティション外のメソッドを呼び出すこと）が最小限になるようにモノリシッククラスをパーティション化してグループ化することを目的とした、*Natural Seams Partitioning*勧告を生成します。「データ依存性分析」とは、このようなJavaクラス間の依存性分析のことです。事実上、これは一枚岩のアプリケーションを自然な継ぎ目に沿って、最小限の混乱で分割します。

Mono2Microは、ユースケース・データとランタイム・ログ・トレースに基づき、クラス・コンテインメントの依存性とメソッド・コールを考慮せずに、*ビジネス・ロジック・パーティショニング*も生成します。このパーティショニングは、パーティション間のより多くの絡み合いと依存性を提示するかもしれませんが、最終的には、モノリシック・アプリケーションを機能とビジネス・ロジックの能力に沿って分割する、より有用なパーティショニングを提供します。

このチュートリアルでは、DayTraderと呼ばれるオンライン株式取引システムをエミュレートしたオープンソースのモノリシックJava EEベンチマーク・アプリケーションを使用して、モノリシック・アプリケーションから始まり、同じアプリケーションのデプロイされコンテナ化されたマイクロサービス・バージョンに至るまで、Mono2Microツールセット全体を最後まで順を追って説明します。

## 前提条件

[Mono2Micro](http://ibm.biz/Mono2Micro)のページにアクセスして、以下のものをダウンロードすることをお勧めします。

* ユーザーガイド
* データコレクタツール
* `Mono2Micro-example.zip` ファイルには、このチュートリアルで説明するすべてのコードとファイルが含まれています（それぞれの詳細については、`README` に記載されています）。

   * Monolithのソースコード。モノリスのソースコード： `./daytrader/monolith` です。
*   * Monolith アプリケーションデータ。*モノリスのソースコード： `./daytrader/monolith` * モノリスのアプリケーションデータ： `./daytrader/application-data/`
   * Mono2Micro分析（AI分析ツールによる初期推奨）：`./daytrader/mono2micro-analysis/`
   * Mono2Micro分析(さらに手作業でカスタマイズ): `./daytrader/mono2micro-analysis-custom/`.
   * Mono2Microで生成されたコードをベースに、デプロイ可能なマイクロサービスのソースコードを作成します。`./daytrader/microservices/`

    **Note:** `Mono2Micro-example.zip` ファイルのダウンロードに問題がある場合は、[直接ダウンロード](http://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/mono2micro/Mono2Micro-Example.zip)することもできます。

このチュートリアルでは、お使いのマシンにMono2Microコンテナとツールがすでにインストールされていることを前提としています。このチュートリアルでは、Mono2Micro のコンテナとツールがインストールされていることを前提としていますが、各ツールの実行やファイルの編集・生成は任意です。生成されたすべてのファイルと、.zip ファイルに含まれるコードを確認しながら進めることができます。

## モノリシック・アプリケーションのデータの収集

Mono2Micro を使用してリファクタリング プロセスを開始するための最初のステップは、静的および動的解析のためにモノリシック アプリケーションの Java ソース コードを準備することです（少なくとも、マイクロサービスにリファクタリングする予定のモノリシック アプリケーションの部分またはモジュールのソース コード）。DayTrader アプリの場合、EAR モジュール、EJB モジュール、Web モジュール、およびその他の補助ファイルで構成される、ソースファイルの完全なセットがすでに 1 つのディレクトリツリーに用意されています。この記事では、`/m2m/`の親ディレクトリに`Mono2Micro-example.zip`が展開されていると仮定します。monolithのソースファイルのツリーは、`/m2m/daytrader/monolith/`ディレクトリにあります。

まず、静的なデータ収集の段階として、Mono2Microの**Bluejay**ツールを実行して、Javaのソースコードを解析し、インスツルメントを行い、解析結果を2つのJSONファイルに出力してみましょう。解析を実行するには、以下のコマンドを実行します。


その後、Bluejayが実行され、親ディレクトリに入力ソースディレクトリのミラーコピーを`-klu`という拡張子で作成します。例えば、`/m2m/daytrader/monolith-klu/`では、ディレクトリツリー全体の中にある全てのJavaファイルがインスツルメンテーションされ、各メソッドのエントリーとエグジットの時間がログに記録されます（これについては後ほど詳しく説明します）。ソースのインストルメント化に加えて、`/m2m/daytrader/monolith-klu/`では、2つのJSONファイル `refTable.json` と `symTable.json` が生成されます。これらのファイルには、メソッドのシグネチャ、クラスの変数や型、クラスの包含依存関係（あるクラスが別のクラスをインスタンス変数の型やメソッドの戻り値・引数の型として使用している場合）、クラスの継承、パッケージの依存関係、ソースファイルの位置など、各Javaクラスに関する様々な詳細やメタデータが記録されています。この静的解析により、モノリシックアプリケーションのJavaコードの詳細な概要が収集され、Mono2MicroのAIアナライザツールは、モノリシックアプリケーションをどのように分割するかについての推奨事項を提供することになります。さらに、この情報はMono2Microのコード生成ツールでも使用され、各パーティションをマイクロサービスとして実装するための基盤と配管のコードを生成します。

前述のように、Bluejayは、静的解析から2つのテーブル.jsonファイルを生成するとともに、ソースツリー全体のすべてのJavaファイルを計測し、各メソッドにロギングステートメントを注入して、メソッドが入力された時間と終了した時間を正確に記録します。さらに、スレッドIDも記録します。このスレッドIDは、後にMono2MicroのAI解析ツールがトレースデータの壊れた断片をつなぎ合わせるために使用します。このバージョンのソースコードを使用して、モノリシックアプリケーションのインスツルメンテッドバージョンを構築・実行し、アプリケーション全体で様々なユーザーシナリオを実行することで、可能な限り多くのコードを実行し、AI分析に備えて追加のデータを動的に収集することができます。`m2m/daytrader/monolith-klu/`のソースを使用して、インスツルメンテッド・デイ・トレーダー・アプリを構築・実行するには、オリジナルのモノリシック・アプリケーションにすでに使用されているのと同じ[build process](https://github.com/WASdev/sample.daytrader7/blob/master/docs/Using-cmd-line.md)を使用することができます。

データ収集の次の段階に入る前に、モノリシックコードでのインスツルメンテーションの例を見てみましょう。`/m2m/dayatrader/monolith-klu/daytrader-ee7-ejb/src/main/java/com/ibm/websphere/samples/daytrader/TradeAction.java`にあるTradeActionクラスを見てみると、エントリーとエグジットの時間を記録するステートメントがどのように注入されているかがよくわかります。

<プロジェクト xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent> (親)
        <groupId>net.wasdev.maven.parent</groupId>
        <artifactId>java7-parent</artifactId>
        <バージョン>1.3</バージョン>
    </parent>

    <groupId>net.washdev.wlp.sample</groupId> </groupId
    <artifactId>daytrader7</artifactId>
    <packaging>pom</packaging>
    <バージョン>1.0-SNAPSHOT</バージョン>。
    <name>WAS Liberty Sample - Java EE7 Benchmark Sample</name>

    <license>
        <license>
            <name>The Apache Software License, Version 2.0</name>
            <url>https://raw.github.com/WASdev/sample.async.jaxrs/master/LICENSE</url>
            <配布先>repo</配布先
        </license>
    </license>

    <modules>
        <モジュール>cardinal-utils</モジュール
        <module>daytrader-ee7-ejb</module>
        <module>daytrader-ee7-web</module>（デイトレーダー・イーセブン・ウェブ
        <モジュール>daytrader-ee7</モジュール
    </modules>

</project

`partition-2`、`partition-3`、`web`の各パーティションでは、追加設定に違いがあることに注意してください。これは、EJBモジュールのソースフォルダに実際のEJBが含まれておらず、代わりにプロキシのみが含まれているためです。これは、EJBモジュールのソースフォルダに実際のEJBが含まれておらず、代わりにプロキシのみが含まれているためで、このようなマークを付けてはいけません。

`/m2m/daytrader/microservices/daytrader-partition2/daytrader-ee7/pom.xml`:

########################################
# ビルドイメージ
########################################
FROM maven:3.6-jdk-8-slim as build

作業ディレクトリ /app
COPY .

RUN mvn clean
RUN mvnインストール

########################################
# プロダクションイメージ
########################################
FROM open-liberty:microProfile2-java8-ibm

# ビルドファイルの追加
COPY --from=build --chown=1001:0 /app/daytrader-ee7/target/daytrader-ee7-1.0-SNAPSHOT.ear /config/apps/daytrader-ee7.ear
COPY --from=build --chown=1001:0 /app/daytrader-ee7/src/main/liberty/config/ /config/
COPY --from=build --chown=1001:0 /app/daytrader-ee7/src/main/liberty/resources/db2jcc4.jar /liberty/usr/shared/resources/db2jars/

docker compose yamlの内容は、ご自身の都合に合わせて検討していただければと思いますが、重要なポイントをいくつかご紹介します。

* 各パーティションには、他のパーティションにあるJAX-RS WebサービスのエンドポイントURLを指定する環境変数が渡されます。Cardinalが生成したコードは、プロキシコードでこれらの環境変数を使用してJAX-RSサービスを呼び出します。
* JAX-RSでは、URLにアンダースコアを含むことができません。これは、最初にパーティションをマイクロサービスとして実行しようとしたときに直面した問題で、デバッグに多くの時間を費やしました。
* URLの`daytrader`の部分は、Java EEアプリケーションのコンテキストルートであり、`rest`の部分は、各`JAXRSConfiguration`がパーティションごとに指定するものと一致しています。
* すべてのパーティションが相互に通信できるように、Dockerネットワークが設定されています。
* すべてのパーティションは、Docker環境の内部ではポート9080を使用しますが、外部のホストマシンに対しては別のポートで公開します。
* このスキームをベースにして、各コンテナがKubernetesのサービスとして動作するクラスタ上にKubernetesのデプロイメントをセットアップすることができます。

パーティションを最初に実行して初めて解決する典型的な問題は、ダミーのクラスメソッドがいつ、どのようにヒットしているかを発見することです（詳細は前のセクションを参照）。私の場合は、これにより、`TradeDirect`と`FinancialUtils`を外部向けのサービスクラスとして指定しました。Cardinalでコードを生成し直し、新しいコードをパーティションにコピーすると、この問題は解決しました。

また、パーティションを実行する際の最初のデバッグでは、「web」パーティションの一部の.jspコードが、プロキシされているモノリスクラスのパブリックフィールドを直接参照していたため、失敗するという問題がありました。そこで、通常のモノリスJavaクラスで行っていたのと同様に、フィールドの直接参照を、そのフィールドのゲッター/セッターを使用するように変更することで解決しました。通常、Mono2Microでモノリスをリファクタリングする前に、他のクラスのパブリックフィールドを直接参照するすべてのJavaコード（.javaおよび.jspファイル）をゲッターおよびセッターメソッドを使用するように変更するのがベストです。

今回抽出した例では、パーティションをマイクロサービスとして実行するために、以下のコマンドを実行します（詳細は`Mono2Micro-example.zip`のREADMEを参照してください）。

`cd /m2m/daytrader/microservices`。

`./run_db2_container.sh` (DB2のセットアップが終了し、サービスが開始されるまで数分待ちます。セットアップに失敗した場合、スクリプトは10分後にタイムアウトします)。

`docker-compose up -d` を実行します。

`docker-compose logs -f` (すべてのコンテナからのログを監視し、LibertyがそれぞれのコンテナでDayTraderアプリケーションを起動するまで待ちます。)

デフォルトでは、生成されたコードはパフォーマンスを最適化するために最小限のロギングとトレースを使用し、エラーのみを表示します。Mono2Mircoで生成されたコードのロギングとトレースのレベルを変更し、マイクロサービス内およびマイクロサービス間のコードフローで何が起こっているかについてより多くの情報を確認するには、各パーティションの `cardinal-utils` モジュール内にある `com.ibm.cardinal.util.CardinalLogger` Javaソースファイルで、`DEFAULT_LOG_LEVEL変数` の値を `Level.FINE` に変更します。これは、マイクロサービスを最初に実行し、マイクロサービスやアプリケーション・サーバーの起動時やアプリケーションの実行後に現れる可能性のある問題のデバッグを開始する際に強く推奨されます。また、この詳細なトレースは、パーティション間で行われている様々な通信を示しており、モノリスコードとMono2Microが生成したコードの間の実行の流れを確認する上で興味深いものとなります。

最後に、ブラウザで [http://localhost:9080/daytrader/](http://localhost:9080/daytrader/) に移動してアプリケーションを開くと、マイクロサービスとして動作するリファクタリングされた DayTrader アプリケーションを使用することができます!

## Conclusion

このチュートリアルでは、Java EE のモノリシックなアプリケーションから始まり、AI 駆動の Mono2Micro ツールを使用してアプリケーションを分析し、潜在的なマイクロサービスのために分割できるさまざまな方法を提案するという、完全なエンドツーエンドのフローを示すことを試みました。Mono2MicroのUIを使ってパーティショニングの操作やカスタマイズを行い、独自のコード生成ツールを使ってマイクロサービスの基盤となるコードの大部分を生成し、モノリシックなJavaクラスは書き換えずにそのまま残します。一枚岩のアプリケーションのJava以外の部分をさらに手作業でリファクタリングすると、一枚岩のアプリケーションとまったく同じ機能を提供するマイクロサービスのセットがコンテナにデプロイされます。

Mono2Microチームと私は、アプリケーションのモダナイゼーションを加速させるこの革新的なソフトウェアツールセットのリリースに興奮しています。近い将来、より多くの資料をお届けできることを楽しみにしています。