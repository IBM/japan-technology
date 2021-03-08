# 過去の購入行動に基づいて追加購入を促す、機械学習レコメンデーション・エンジンを作成する

### IBM Watson Studio で Jupyter Notebook を使用してレコメンデーション・エンジンを作成する

English version: https://developer.ibm.com/patterns/./build-a-product-recommendation-engine-with-watson-machine-learning
  ソースコード: 'https://github.com/IBM/product-recommendation-with-watson-ml'

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: '2020-02-18'

 
## 概要

商品をオンラインで販売する Web サイトのほとんどは、顧客が興味を持ちそうな商品のリストを提示します。推奨する商品が適切なものであればあるほど、顧客が購入する可能性が高くなり、売上高が増えることになります。けれども、こうした商品推奨はどのように作成されているのでしょうか？このコード・パターンでは、いずれもオープンソースの Jupyter Notebook、Apache Spark を使用して、顧客データを基にレコメンデーション・エンジンを作成する方法を説明します。作成したレコメンデーション・エンジンに Watson Studio と Watson Machine Learning を統合すれば、レコメンデーション・モデルを探索してテストするための対話式ダッシュボードを簡単に作成できます。

## 説明

商品推奨を作成するのに最も手っ取り早い方法は、あらゆる顧客の購入データを使用することです。このデータがあれば、同様の商品を購入した顧客のグループ (クラスター) を作成できます。それぞれのクラスターに含まれる顧客は、他のクラスターに含まれる顧客に比べ、互いに似ている点が数多くあります。

このコード・パターンでは、過去の購入データを使用して、Spark と Watson Machine Learning を利用したレコメンデーション・エンジンを作成します。続いて買い物カゴの中身の内容に基づいた推奨する商品のリストを作成します。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* Jupyter Notebook を IBM Watson Studio 内で使用する
* SparkML と Watson Machine Learning を使用して、顧客の購入履歴に基づいて推奨する商品を提示するためのレコメンデーション・モデルを作成する

## フロー

![フロー](./images/flow-product-recommendation-with-watson-ml.png)

1. IBM Watson Studio にログインします。
1. 用意されているノートブックを Watson Studio にロードします。
1. 顧客データをノートブックにロードして変換します。
1. SparkML を使用して k 平均法クラスタリング・モデルを作成します。
1. 作成したモデルを Watson Machine Learning にデプロイします。
1. ノートブック内で作成されたモデルを、Watson Machine Learning API を使用してテストし、比較します。

## 手順

詳細な手順については、[README](https://github.com/IBM/product-recommendation-with-watson-ml/blob/master/README.md) ファイルを参照してください。手順の概要は以下のとおりです。

1. Watson Studio に登録します。
1. プロジェクトを作成してサービスを追加します。
1. ノートブックを作成します。
1. 顧客データを Jupyter Notebook にロードします。
1. Watson Machine Learning サービスを追加します。
