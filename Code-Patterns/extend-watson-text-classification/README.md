# Watson のテキスト分類を拡張する

### Python NLTK ツールキットと IBM DSX を使って、望ましいテキスト分類結果を得る

English version: https://developer.ibm.com/patterns/extend-watson-text-classification
  ソースコード: https://github.com/IBM/watson-document-classifier

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-06-28

 
## 概要

Watson Natural Language Understanding で正確な結果を得るためには、多数のドキュメントによるトレーニングが必要です。けれども新しい主題領域においては、多数のトレーニング用ドキュメントを作成する時間が限られています。そのようなシナリオでは、このコード・パターンで提案する手法に従って、単純な入力構成 JSON ファイル (ドメイン・エキスパートが作成可能) を使用することで、Natural Language Understanding から得られる結果の精度を向上させることができます。この手法により、トレーニング用ドキュメントを用意しなくても正確な結果が得られるようになります。

## 説明

Watson Natural Language Understanding (NLU) サービスでトレーニングに使用できる履歴データがない場合、今回紹介するコード・パターンで説明するように、IBM Watson Studio を利用することでテキスト分類結果の精度を向上させることができます。このパターンでは、IBM Watson Studio で、ドメイン・エキスパートによって作成された構成 JSON ドキュメントを入力として取ります。構成 JSON ドキュメントに変更を加えることによって、テキストの内容からより正確な結果と洞察を得られるようになります。

このコード・パターンをひと通り完了することで、以下を行う方法を把握できます。

* Watson Studio 内で Jupyter Notebook を作成して実行する
* Watson Studio Object Storage を利用してデータと構成ファイルにアクセスする
* NLU API を使用して、Jupyter Notebooks 内のドキュメントからメタデータを抽出する
* 単純化された Python 関数を使用して、非構造化データを抽出してフォーマット化する
* 構成ファイルを使用して、構成可能な階層型分類文法を作成する
* 構成ファイルに含まれる文法上の分類と正規表現パターンの組み合わせを使用して、単語のトークンをクラスに分類する
* 処理後の出力 JSON を Watson Studio Object Storage に保管する

## フロー

![フロー](../../images/Watson-Text-Classifier-arch-flow-1.png)

1. 分析を必要とするドキュメントを IBM Cloud Object Storage に保管します。
1. Python コードにより、Object Storage からドキュメントの内容と構成 JSON を取得します。
1. ドキュメントの内容を Watson NLU に送信します。これにより、レスポンスが返されます。
1. Python Natural Language Toolkit (NLTK) モジュールを使用してドキュメントを構文解析し、タグ・パターンに基づいてキーワード、POS タグ、チャンクを生成します。
1. 構成 JSON を読み取り、ドメイン固有のキーワードと属性を分類します。
1. NLU からのレスポンスを、Python コードによる結果で増補します。
1. 最終的なドキュメントの分類と属性を Object Storage 内に保管し、今後も使用および処理できるようにします。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the [README](https://github.com/IBM/watson-document-classifier/blob/master/README.md).
