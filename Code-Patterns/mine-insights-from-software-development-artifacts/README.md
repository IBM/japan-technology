# ソフトウェア開発成果物から洞察をマイニングする

### 十分な情報に基づいた意思決定を支援するために、非構造化データを分析して洞察力を生み出す網羅的なアナリティクス・ソリューションを構築する

English version: https://developer.ibm.com/patterns/mine-insights-from-software-development-artifacts
  ソースコード: https://github.com/IBM/engineering-insights-composite-pattern

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-01-17

 
<!--
_**Note: This pattern is part of a composite pattern.** These are code patterns that can be stand-alone applications or might be a continuation of another code pattern. This composite pattern consists of:_

* [Watson のテキスト分類を拡張する](https://developer.ibm.com/jp/patterns/extend-watson-text-classification)
* [さまざまなソースからのドキュメントを互いに関連付ける](https://developer.ibm.com/jp/patterns/watson-document-correlation)
* [相互に関連するデータを保管し、グラフを生成して洞察を引き出す](https://developer.ibm.com/jp/patterns/store-graph-and-derive-insights-from-interconnected-data)
* [データ・サイエンスのワークフローを、Node-RED を使用して編成する](https://developer.ibm.com/jp/patterns/orchestrate-data-science-workflows-using-node-red)
* ソフトウェア開発成果物から洞察をマイニングする (このパターン)
-->

## 概要

開発ライフサイクル、金融、医療、ソーシャル・メディアなどのどのドメインをとっても、生成される非構造化テキスト・コンテンツは膨大な量に上ります。このようなドキュメント・ソースにわたる非構造化テキスト・コンテンツを分析して情報を互いに関連付ければ、貴重な洞察力を生み出すことが可能になります。このパターンでは、十分な情報に基づいた意思決定を支援するための洞察力を生み出す網羅的なアナリティクス・ソリューションを、Watson(tm) Natural Language Understanding、Python Natural Language Toolkit、OrientDB、Node-RED、そして IBM Watson Studio を利用して構築します。

## 説明

このパターン・シリーズでは、以下の一連のコード・パターンを使用して、さまざまなデータ・ソースの非構造化テキスト・コンテンツから洞察を引き出します。これらのコード・パターンの対象読者は、このような洞察力を可能にするソリューションの構築において有利なスタートを切りたいと目指している開発者です。

パターン・シリーズのそれぞれのコード・パターンで、IBM Cloud、Watson サービス、Python NLTK、OrientDB、IBM Watson Studio を利用して洞察を引き出す方法を説明します。

* [Watson のテキスト分類を拡張する](https://developer.ibm.com/jp/patterns/extend-watson-text-classification)
* [さまざまなソースからのドキュメントを互いに関連付ける](https://developer.ibm.com/jp/patterns/watson-document-correlation)
* [相互に関連するデータを保管し、グラフを生成して洞察を引き出す](https://developer.ibm.com/jp/patterns/store-graph-and-derive-insights-from-interconnected-data)
* [データ・サイエンスのワークフローを、Node-RED を使用して編成する](https://developer.ibm.com/jp/patterns/orchestrate-data-science-workflows-using-node-red)
* ソフトウェア開発成果物から洞察をマイニングする (このパターン)

## フロー

![フロー](../../images/engineering-insights-composite-pattern-arch-flow.png)

1. カスタム Python コードを使用して、複数のドキュメントから、分析して相互に関連付ける対象となる非構造化テキスト・データを抽出します。
2. コード・パターン「[Watson のテキスト分類を拡張する](https://github.com/IBM/watson-document-classifier)」に従って、テキストを分類し、タグを付けます。
3. 「[ドキュメントを相互に関連付ける](https://github.com/IBM/watson-document-co-relation)」に従って、テキストを相互に関連付けます。
4. 「[相互に関連するデータを保管し、グラフを生成して洞察を引き出す](https://github.com/IBM/graph-db-insights)」に従って、ドキュメントのデータと相関関係を OrientDB データベース内に保管します。
5. 「[Node-RED を使用してデータ・サイエンスのワークフローを編成する](https://github.com/IBM/node-red-dsx-workflow)」に従って、IBM Watson Studio 上のアナリティクス・ソリューションを呼び出し、視覚化します。
