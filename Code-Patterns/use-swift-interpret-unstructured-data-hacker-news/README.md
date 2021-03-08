# Swift を使用して Hacker News の非構造化データを解釈する

### ひとひねり利かせたコグニティブ API を使用して、Hacker News 上の技術動向について洞察を得る

English version: https://developer.ibm.com/patterns/use-swift-interpret-unstructured-data-hacker-news
  ソースコード: https://github.com/IBM/Hackernews-NLU

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated:     2018-06-18

 
## 概要

大量の非構造化データ・ソースから洞察を得るのは次第に簡単になってきています。それは、機械学習テクノロジーのおかげです。このコード・パターンで、自然言語サービスを Swift ベースのアプリケーションから呼び出して Hacker News の記事からデータ・ポイント (概念、エンティティー、カテゴリー、キーワード、センチメント、感情など) を抽出する方法を学んでください。

## 説明

「自然言語処理 (NLP) は、人間の言語に対するコンピューターの理解力と処理能力を埋め合わせる分野であり、ニュースを収集するには可能性に満ち溢れています」。これは、Anthony Pesce 氏が「Natural Language Process in the kitchen.」の中で語った言葉です。開発者は NLP を使用することで、知識を整理して構造化し、固有表現抽出、関係の抽出、センチメント分析、音声認識といったタスクを実行することができます。大量の非構造化データから必要な情報を迅速に抽出しなければならない医療、法律をはじめとする多くの分野では、NLP のアプリケーションが使用されています。

通常、私たちが目にするアプリケーションで使用されている NLP API は Python または Node.js NLP で作成されていますが、このコード・パターンではひとひねり利かせて、Swift ベースのアプリケーション内に組み込んだ機械学習機能を紹介します。このアプリケーションでは Watson&trade; Natural Language Understanding API を使用して、Hacker News の非構造化テキストを解釈し、最新の技術動向と開発者たちの間で話題になっている主な分野を識別します。このコード・パターンから、Swift アプリケーションからでも簡単に Watson サービスを呼び出せることがわかるはずです。

## フロー

![フロー](../../images/hackernews-arch-1.png)

1. アプリケーションを IBM Cloud&reg; にデプロイします。
1. アプリケーションが Hacker News API からデータをロードします。
1. ユーザーがブラウザーを使用してアプリケーション UI を操作します。
1. ユーザーが何らかのアクションを実行すると、UI がサーバー・アプリケーション API を呼び出します。呼び出された API は Watson NLU サービスを利用して該当するニュース記事を分析します。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the [README](https://github.com/IBM/Hackernews-NLU/blob/master/README.md).
