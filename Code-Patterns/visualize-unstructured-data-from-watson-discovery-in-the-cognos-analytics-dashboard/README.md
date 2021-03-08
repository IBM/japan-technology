# Cognos Analytics ダッシュボードを作成する

### Watson Discovery で非構造化データから引き出した洞察を Cognos Analytics ダッシュボード内で視覚化する

English version: https://developer.ibm.com/patterns/visualize-unstructured-data-from-watson-discovery-in-the-cognos-analytics-dashboard
  ソースコード: https://github.com/IBM/cognos-analytics-using-unstructured-data

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2020-06-04

 ## 概要

この開発者コード・パターンでは、製品レビューと顧客アンケートからなる非構造化データを Watson Discovery で処理してから Cognos Analytics にインポートします。顧客データを基に、アンケート対象の製品に対する感情を分析し、分析結果を Cognos&reg; Analytics ダッシュボードに表示できます。

## 説明

企業が顧客の意見を参考にしてビジネスの成果を上げるには、AI を活用し、カスタマー・フィードバックで述べられている意見、感情、コンセプト、キーワードから実用的な洞察を引き出す必要があります。顧客が製品や企業について共有したいと思う意見の大半は、すぐに見つかります。例えば、公開フォーラム、ブログ、ソーシャル・メディアへの投稿、カスタマー・サービス担当者とのチャットのログなどです。こうした情報を利用する上での従来からの課題は、データが構造化されていないことにあります。けれども最近では、AI と Watson&trade; Discovery のようなサービスを利用して、データを集約して増補し、顧客に関する重要な洞察を浮き彫りにできるようになっています。このコード・パターンでは、製品のパフォーマンス分析を目的に、Watson Discovery で処理した非構造化データを Cognos Analytics に取り込んで視覚化する方法を説明します。

製品レビューと顧客アンケートからなる非構造化データを Watson Discovery で処理して Cognos Analytics にインポートします。顧客データを基に、アンケート対象の製品に対する感情を分析し、分析結果を Cognos Analytics ダッシュボードに表示できます。Cognos Analytics と Discovery を組み合わせることで、企業は以下の目的を果たすことができます。

* 顧客のフィードバックに基づいて、傾向についての早期警告を受ける。
* 顧客インタラクションの増加に早い段階で介入して対処する。
* 製品とマーケティングのターゲットを適切な顧客に絞る。
* 収益増加と顧客による採用を促進するために投資すべきビジネス分野を把握する。
* 顧客離れの根本原因を突き止める。
* NPS やその他の顧客満足度メトリックを改善するための措置を識別する。

このコード・パターンでは、製品を地元の市場で販売している小規模なコーヒー製造業者のデータを処理する例を取り上げます。このデータには、各種のコーヒーに対するレビューと格付けが含まれています。

## フロー

![フロー図](../../images/flow.png)

1. 製品レビューのデータを Watson Discovery にロードして増補します。増補されたデータには、感情分析とキーワード・ディスカバリーの結果が含まれます。
1. ユーザーが Cognos Analytics を実行します。
1. データ・ファイルを直接 Cognos Analytics にロードします。

## 手順

このパターンの詳しい手順については、[README](https://github.com/IBM/cognos-analytics-using-unstructured-data/blob/master/README.md) ファイルを参照してください。手順の概要は以下のとおりです。

1. リポジトリーのクローンを作成します。
1. Watson Discovery サービス・インスタンスを作成します。
1. Watson Discovery サービス・インスタンスを構成します。
1. サービス資格情報を環境ファイルに追加します。
1. データを生成するスクリプトを実行します。
1. Cognos Analytics 内でデータ・モジュールを作成します。
1. Cognos Analytics ダッシュボードを作成します。
1. 視覚化をダッシュボードに追加します。
1. データ・モジュールを更新します。
1. 製品レビューが売上に与える影響を視覚化します。

このパターンを「[売上高データと在庫レベルを視覚化する Cognos Analytics ダッシュボードを作成する](https://developer.ibm.com/jp/patterns/visualize-customer-insights-with-business-data-for-product-performance-analysis)」パターンと併せて使用して、[AI で非構造化データを分析して製品のパフォーマンスを把握する](https://developer.ibm.com/articles/leverage-the-voice-of-the-customer-using-watson-discovery-to-show-business-results-in-cognos-analytics)ためのソリューションを完成させてください。
