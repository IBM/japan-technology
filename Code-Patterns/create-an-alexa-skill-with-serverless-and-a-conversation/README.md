# サーバーレスと会話を使って Alexa スキルを作成する

### Alexa と Watson を使用して天気について話し合い、会話を組み立てるか、ライブラリーから会話を選択する

English version: https://developer.ibm.com/patterns/create-an-alexa-skill-with-serverless-and-a-conversation
  ソースコード: https://github.com/IBM/alexa-skill-watson-conversation

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-07-16

 
## 概要

このコード・パターンでは、Apache OpenWhisk サーバーレス・フレームワークを介して Watson&trade; Assistant を利用することによって、Alexa スキルを作成します。Alexa は、Amazon Echo のような製品を背後で支える音声サービスです。この Alexa に Watson Assistant を統合するために、(Apache OpenWhisk ベースの) IBM Cloud Functions を使用します。さまざまなインテントの間でコンテキストを受け渡す方法をデモンストレーションするようにサンプル会話が付属しています。このコード・パターンは、Bot Asset Exchange (BAE) の会話を試すためにも利用できます。

## 説明

多くのワークフローでは、複数のテクノロジーを利用するのが一般的なことになっています。このコード・パターンはその一例として、Amazon Alexa スキルに Watson Assistant を統合する方法を説明するために作成されています。このコード・パターンではチャットボットや人工知能にフォーカスしている開発者を対象に、Watson を使用して作成された会話を Alexa ユーザーが利用できるようにする方法を説明します。

このコード・パターンでは、Apache OpenWhisk サーバーレス・フレームワークを介して Watson Assistant を利用することによって、Alexa スキルを作成します。Alexa は、Amazon Echo のような製品を背後で支える音声サービスです。この Alexa に Watson Assistant を統合するために、(Apache OpenWhisk ベースの) IBM Cloud Functions を使用します。付属のサンプル会話を使って、さまざまなインテントの間でコンテキストを受け渡して天気情報を検索する方法をデモンストレーションします。このコード・パターンは、Bot Asset Exchange (BAE) の会話を試すためにも利用できます。

私たちが交わす会話の状態を記憶して、外部アクションをリクエストできるようにするために、Redis を使用して、サーバーレス関数の呼び出しから次の呼び出しまで状態を保存することにしました。また、天気予報を取得する外部アクションも作成しました。この仕組みを拡張すれば、任意の Watson Assistant を使用することも、独自のアクション・コードを追加することもできます。

このコード・パターンをひととおり完了すると、以下の方法がわかるようになります。

* IBM Cloud Functions サーバーレス・プラットフォーム内で OpenWhisk アクションを作成する
* Redis を使用して、あるイベントから次のイベントまで、セッションでの会話のコンテキストを保管する
* BAE または JSON ファイルから会話をインポートする
* Node.js を使用して、Watson との会話を呼び出す
* The Weather Channel データ・サービスを使用して場所や天気予報を検索する
* 何千万人ものユーザーを魅了する Alexa スキルを作成する

## フロー

![フロー](../../images/Create-an-Alexa-skill-with-serverless-and-a-conversation.png)

1. ユーザーが「Alexa、Watson に ... を聞いて」と話しかけます。
2. Alexa が入力テキストを使用して IBM Cloud Functions を呼び出します。
3. 該当するアクションによって、Redis から会話のコンテキストが取得されます (存在する場合)。
4. Watson Assistant からのレスポンスがアクションに返されます。
5. The Weather Company データ・サービスが天気予報に関する情報を提供します (該当する場合)
6. レスポンスのコンテキストが Redis 内に保管されます。
7. レスポンスのテキストが Alexa に送信されます。
8. Alexa がユーザーに応答します。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the README.
