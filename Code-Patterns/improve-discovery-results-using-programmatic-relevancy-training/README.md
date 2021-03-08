# API ベースの関連性トレーニングを使用して Watson Discovery の結果を改善する

### 追加のトレーニング詳細を提供して、検索結果を改善する

English version: https://developer.ibm.com/patterns/improve-discovery-results-using-programmatic-relevancy-training
  ソースコード: https://github.com/IBM/improve-discovery-results-using-api-based-relevancy-training

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2020-04-28

 
## 概要

IBM&reg; Watson&trade; Discovery サービスを利用すると、開発者はコグニティブ機能、検索機能、コンテンツ分析機能を備えたエンジンを迅速にアプリケーションに追加できます。このエンジンを使用すれば、非構造化データからパターン、傾向、洞察を引き出して、より効果的な意思決定を推進できます。場合によっては、検索結果を改善するために、さらに綿密なトレーニングを行わなければならないことがあります。Watson Discovery には、検索結果の精度を高めるための追加トレーニングを行う、関連性トレーニングという機能があります。このコード・パターンでは、Watson Discovery 内で関連性トレーニング API を使用して、検索結果を改善する方法を説明します。

## 説明

IBM Watson Discovery サービスを利用すると、開発者はコグニティブ機能、検索機能、コンテンツ分析機能を備えたエンジンを迅速にアプリケーションに追加できます。このエンジンを使用すれば、非構造化データからパターン、傾向、洞察を引き出して、より効果的な意思決定を推進できます。Watson Discovery では、データを取り込んで (変換、エンリッチ、クリーニング、正規化して) 保管し、クエリーを実行してデータから実用的な洞察を引き出すことができます。検索とクエリーを実行するには、コレクションに注入して永続させるコンテンツが必要です。Watson Discovery を利用したアプリケーション開発について詳しく学ぶには、 [コグニティブ・ディスカバリーのリファレンス・アーキテクチャー](https://www.ibm.com/cloud/architecture/architectures/cognitiveDiscoveryDomain)を調べてください。

関連性トレーニングは、正しい手法で使用すれば検索結果の精度を高めることができる、Watson Discovery に組み込まれた強力な機能です。この機能を使用して、特定の組織やサブジェクト・エリアとクエリー結果の関連性が強化されるように Watson Discovery をトレーニングすることができます。Watson Discovery インスタンスにトレーニング・データを渡すと、このサービスは Watson の機械学習手法を使用して、コンテンツと質問に含まれるシグナルを検出します。これらのシグナルを基に、クエリー結果を並び替えて最も関連性の高い結果を先頭に表示します。さらにトレーニング・データを追加するにつれ、サービス・インスタンスが返す結果の順序付けがより正確で洗練されたものになります。

関連性トレーニングを使用するかどうかは任意です。クエリーの結果がニーズを満たしている場合、それ以上のトレーニングは必要ありません。<!--トレーニング用の使用ケースを作成する方法の概要については、ブログ記事「[How to get the most out of relevancy training](https://developer.ibm.com/dwblog/2017/get-relevancy-training/)」をご覧ください。-->

Watson Discovery 内で関連性トレーニングを行うには、以下の 2 つの方法があります。

* ツールを使用する。詳細については、「[ツールを使用した結果関連性の改善](https://cloud.ibm.com/docs/discovery?topic=discovery-improving-result-relevance-with-the-tooling)」をご覧ください。
* API を使用する。Watson Discovery に、関連性トレーニングを行うための API が用意されています。

Watson Discovery インスタンスのかなりの数の質問に対して関連性トレーニングが必要だとすると、ツールを使用してトレーニングするよりも、プログラムで (API を使用して) トレーニングするほうが時間を大幅に短縮できます。また、API を使用する場合、ブラウザーからオンラインで Watson Discovery インスタンスに接続する必要もありません。

このコード・パターンでは、API を使用して関連性トレーニングを行う方法を説明します。

## フロー

![Discovery の関連性トレーニングで検索結果を改善するフロー図](../../images/improve-discovery-relevancy-training.png)

1. クライアント・アプリケーションが、関連性トレーニングを必要とするクエリーのそれぞれに対して、自然言語のクエリーを送信します。
1. Watson Discovery が、送信された自然言語のクエリーのそれぞれに対応する一連のドキュメントを返します。
1. クライアント・アプリケーションが各クエリーとそのクエリーに対応するドキュメントをローカル・マシン上の TSV ファイル内に保存します。
1. ユーザーがドキュメントに関連性スコアを割り当て、ファイルを保存します。
1. アプリケーションが、更新された関連性スコアを持つファイルにアクセスします。
1. クライアント・アプリケーションが更新された関連性スコアを使用して API を呼び出し、Watson Discovery コレクションを更新します。
1. クライアントが再度クエリーを実行すると、改善された結果が返されます。

## 手順

このパターンの詳細な手順については、[readme](https://github.com/IBM/improve-discovery-results-using-api-based-relevancy-training/blob/master/README.md) ファイルを参照してください。手順の概要は以下のとおりです。

1. IBM Watson 上で Cloud Discovery サービス・インスタンスを作成します。
1. リポジトリーのクローンを作成してコードを取得します。
1. ドキュメントにアノテーションを付けます。
1. 大規模な質問セットに対して関連性トレーニングを実行します。
