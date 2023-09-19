# Watson Assistant/Discovery/OpenAIの連携

## はじめに 

Watson Assistantは、人間の言語を理解し、業界の語彙、貴社独自の社内用語も学習できる仮想アシスタントであり、既存の電話や対話型音声応答システムにも統合可能です。また、Facebookメッセンジャー・アプリ、Webサイトのチャット・ウィンドウ、電話などの手段を問わず、どのタッチ・ポイントでも同レベルのサービスを提供することができ、顧客のセルフ・サービスの要望にも応えます。さらに、AI検索ツールのWatson Discoveryを使って、最新の情報や社内ドキュメントから必要な情報を引き出すことができ、人の介入を必要とする問い合わせを減らせます。誰でも使いやすく、初めから賢く、短期および長期目標をサポートできるように設計されています。  

　WatsonDiscoveryでは、質問文に関連するするドキュメントを検索することができるのですが、その中から必要な情報を抜き出すことは一定量の負荷がかかります。そこで本アセットでは、Watson Assitantが連携するAPIサーバーを用意することで、顧客からの問い合わせに対してWatson Discoveryを用いるだけでなく、GPT-3.5による要約結果を返却することができます。皆様の環境情報を変数として入力いただくことで、非常に簡単にWatson Assistantを拡張することが可能となります。

![image](https://media.github.ibm.com/user/52348/files/a3f18642-1d74-4466-97db-25b4b5ca79e3)

## How to Setup

### 1. Watson Discoveryのセットアップ

Watson Discoveryにドキュメントを投入する手順は以下の通りです。  

1. サービス作成(ない場合)  
IBM Cloud にログインし、「Watson Discovery」を検索します。IBM Cloud カタログの Discovery リソース ・ページに移動し、プラス・プラン・サービス・インスタンスを作成します。作成できたら、.envファイル内に記載するための資格情報(API鍵/URL)をメモしておき、Watson Discoveryを起動します。  
2. プロジェクト作成とコレクションへのデータ投入  
Project nameやプロジェクトのタイプを入力・選択します。その後 Data Sourceを選択します。様々なデータソースやファイルタイプに対応していますが、画像では例として、Web crawlを選択しています。
  
詳しくは、[こちら](https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-projects)を参照ください。


3. Project IDの取得  
   「Integrate & Deploy」>「API Information」から.envファイル内に記載するためのProject IDをメモし、文書投入が終わるまで待ちます。



### 2. ローカル起動

APIサーバーをローカル環境でテストする手順は以下の通りです。

.envファイル内のAPIKeyやサービスURL等の情報を、各自の内容に更新する

npm install を実行する

node server を実行し、ローカルサーバーを立ち上げる

### IBM Cloudへデプロイ

APIサーバーをデプロイする実施手順は以下の通りです。

1. .envファイル内のAPIKeyやサービスURL等の情報を、各自の内容に更新する  
2. APIサーバーを用意する。本環境ではサンプルとしてIBM Code Engineにデプロイする  
3. デプロイ完了後にURLを確認し、openapi.jsonを更新する



### 【参考】 localサーバーにPOSTリクエストを送る

以下、discovery検索=>chatGPT要約を実施するAPIをコールするcurlコマンドのサンプルです

```shell
curl -X POST -H "Content-Type: application/json" -d '{"content":"WatsonAssistantってなに?一言で教えて"}' htt
```

### Watson Assistantのセットアップ

Watson AssistantとAPIサーバーを連携させる手順は以下の通りです。

1. サービスの作成(ない場合)  
IBM Cloud にログインし、「Watson Assistant」を検索します。IBM Cloud カタログの Assistant リソース ・ページに移動し、プラス・プラン・サービス・インスタンスを作成します。
2. Assistantの作成  
Watson Assistantを起動します。Assistant Nameの入力や、Watson Discoveryに投入した文書に合わせてlanguage等を選択します(環境によって画面が異なる場合があります)。  
3. Custom Extensionの作成  
[Integration]タブ に移動し、スクロールして[Build Custom extension] をクリックし、extensionを作成します。  
拡張機能に名前を付け、簡単な説明を入力します。OpenAPI ファイルをアップロードし、レビューを確認して[Finish] をクリックします。


詳しくは、以下を参照ください。
https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-build-custom-extension


4. Custom Extensionの追加  
   UIに従い、Custom Extentsionを追加します。  
   詳しくは、以下を参照ください。  
   https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-add-custom-extension

5. Custom Extensionの呼び出しの定義  
Action内で、Custom Extensionを呼び出す設定をします。Custom Extensionを呼び出し、返答を表示するように設定します。設定したactionを、任意の別のアクションから呼び出すこともできます。
  
詳しくは、以下を参照ください。

https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-call-extension