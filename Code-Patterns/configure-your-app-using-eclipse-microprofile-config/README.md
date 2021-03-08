# Eclipse MicroProfile Config を使用してアプリを構成する

### システム・プロパティーや環境変数などを使用して容易にアプリケーションを構成する

English version: https://developer.ibm.com/patterns/configure-your-app-using-eclipse-microprofile-config
  ソースコード: https://github.com/IBM/java-microprofile-config

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-08-30

 ## 概要

Eclipse MicroProfile Config を使用すると、アプリケーションを再パッケージ化しなくても、さまざまなソースのアプリケーション構成データに変更を加えることができます。このリポジトリー内にあるアプリケーションでは、[Open Liberty](https://openliberty.io/) 上での [Eclipse MicroProfile Config API](http://microprofile.io/project/eclipse/microprofile-config) の機能をデモンストレーションします。このコードには、依存性注入によって動的構成データを受け取り、コンバーターでそのデータを必要な型に変換する方法が含まれています。

## 説明

ほとんどのアプリケーションは、実行環境に基づいてセットアップしなければなりません。アプリケーション自体を再パッケージ化しなくても済むようにするには、アプリケーションの外部から構成データに変更を加えられるようにする必要があります。

構成データは設定されている場所も形式もさまざまに異なります。例えば、システム・プロパティー、システム環境変数、プロパティー・ファイル/リソース、XML ファイル/リソースに設定されていたり、さらにはデータ・ソースにあったりするといった具合です。Eclipse MicroProfile Config では、これらのデータのソースを ConfigSource と呼んでいます。複数の ConfigSource 内に同じ構成プロパティーが定義されている場合もあることから、優先順位に基づいて、プロパティー値に使用する ConfigSource を判断できるようになっています。

また、構成の設定値が動的に変更される場合もあります。その場合、アプリケーションを再起動することなく、アプリケーションが最新の値にアクセスできるようにしなければなりません。この機能は、特に、クラウド環境内で実行されるマイクロサービスにとって非常に重要ですが、このような構成設定値の動的更新も、Eclipse MicroProfile Config はサポートしています。

Eclipse MicroProfile は、マイクロサービス・アーキテクチャー用に Enterprise Java™ テクノロジーを最適化する基本のプラットフォーム定義であり、さまざまな Eclipse MicroProfile Config ランタイムにアプリケーションを移植可能にします。

## フロー

![フロー](../../images/Configure-your-application-with-Eclipse-MicroProfile-Config-arch-flow.png)

1. ユーザーが Open Liberty サーバーに対して REST リクエストを実行します。
2. JAX-RS がリクエストをアプリケーションに転送します。
3. アプリケーションが MicroProfile Config API を使用して、Open Liberty サーバーに構成データをリクエストします。
4. Open Liberty がさまざまな構成ソースから構成データを検索します。
5. Open Liberty サーバーが構成データを必要な型に変換するようコンバーターに指示します。
6. アプリケーションが JAX-RS リクエストに対し、JSON 形式の結果を返して応答します。
7. Open Liberty がレスポンスをユーザーに送信します。

## 手順

Find the detailed steps for this pattern in the [README](https://github.com/IBM/java-microprofile-config).
