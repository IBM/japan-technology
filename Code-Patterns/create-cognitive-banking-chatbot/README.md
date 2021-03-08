# バンキング・チャットボットを作成する

### Node.js と Watson を使用して感情を検出し、エンティティーを識別し、回答を見つける

English version: https://developer.ibm.com/patterns/create-cognitive-banking-chatbot
ソースコード: https://github.com/IBM/watson-banking-chatbot

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-08-06

 ## 概要

人工知能の機能を備えた Web UI チャットボットの作成に興味を持つ、JavaScript と Node.js を使い慣れた開発者向けに作成されたこのコード・パターンでは、IBM Watson Node.js SDK を利用して、会話によるやり取り、怒りの感情の検出、自然言語の理解、回答のディスカバリーに対応するための機能をアプリケーションに組み込みます。回答のディスカバリーでは、一連の FAQ ドキュメントから答えを見つけます。架空の金融機関として作成されたこのアプリは、会話に外部ビジネス・データを盛り込んで応答する方法を示す例として、単純なバンキング・サービス・コードを呼び出します。

## 説明

このコード・パターンでは、Node.js と IBM Watson™ Assistant を利用してチャットボットを作成します。そしてフローを拡張するために、Watson Natural Language Understanding を利用してエンティティーを識別し、Watson Tone Analyzer を利用して顧客の感情を検出します。FAQ については、Watson Discovery サービスの呼び出しでパッセージ取得機能を使用して、一連のドキュメントから回答を取得します。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* Watson Assistant と Node.js を利用して、Web UI を介して会話するチャットボットを作成する
* Watson Discovery のパッセージ取得機能を使用して、FAQ ドキュメントから回答を検出する
* Watson Tone Analyzer を利用して、会話から感情を検出する
* Watson Natural Language Understanding を利用して、エンティティーを検出する

## フロー

![フロー](../../images/Create-a-banking-chatbot.png)

1. 一連の FAQ ドキュメントを Watson Discovery コレクションに追加します。
1. ユーザーがアプリの UI を介してチャットボットとやり取りします。
1. Tone Analyzer を使用してユーザー入力が処理されて、怒りの感情が検出されます。怒りスコアがコンテキストに追加されます。
1. Natural Language Understanding を使用してユーザー入力が処理されます。検出されたエンティティーとキーワード (ロケーションなど) でコンテキストがエンリッチされます。
1. 入力とエンリッチされたコンテキストが Watson Assistant に送信されて、インテント、エンティティー、対話パスが認識されます。Watson Assistant が返答またはアクション、あるいはその両方で応答します。
1. 必要に応じて、要求されたアクションをアプリが実行します。これには、バンキング・サービスから追加情報を検出して返答に追加するアクション、Discovery を利用して FAQ ドキュメントから検出した回答で応答するアクションなどが含まれます。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the [README.md](https://github.com/IBM/watson-banking-chatbot/blob/master/README.md) file.
