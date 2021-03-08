# サーバーレス関数を実行して画像を認識する

### 画像をデータベースにアップロードすると同時にサーバーレス関数で分類する

English version: https://developer.ibm.com/patterns/run-serverless-functions-with-image-recognition
ソースコード: https://github.com/IBM/ibm-cloud-functions-refarch-serverless-image-recognition

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated:	2018-08-28

 
## 概要

開発サイクルの一環としてアプリケーションのサーバーをセットアップするのに思いのほか時間がかかることがあります。サーバーレス・アーキテクチャーであれば、サーバーをセットアップしなくてもコードを実行できます。つまり、アプリケーションのプログラミングに費やす時間を増やし、サーバーを管理する時間を節約できるということです。サーバーレス・コンピューティング・プラットフォームはその名前とは裏腹に、実際にはサーバーを使用して関数を実行しますが、その違いは料金にあります。コードの実行にかかった時間の分だけ料金が請求されるため、サーバーがアイドル状態の期間については料金を懸念する必要はありません。関数が実行されるのは、イベントが発生した場合、または REST API によって直接呼び出された場合だけです。

このコード・パターンでは IBM Cloud 上の Cloudant データベースを使用し、データベース内の変更に応じてアクション (Cloud Functions) をトリガーします。アクションの目的は、データベースにアップロードされた画像を分類することです。アクションでは、サーバーレス画像認識 Web アプリを使用して、サーバーレスの実装例を紹介します。エンド・ユーザーが画像をアップロードすると、アクションが実行されます。このアクションは取得した画像を分類するために Watson Visual Recognition サービスを利用し、このサービスから返された分類子に基づいて画像にタグを付けます。

## 説明

このアプリケーションが説明しているのは、Apache OpenWhisk ベースの Cloud Functions を使用して、Cloudant データベースから画像を取得し、Watson Visual Recognition サービスを利用して画像を分類する方法です。このコード・パターンでは、アクションがデータ・サービスと連動し、Cloudant イベントに応じてロジックを実行する仕組みをデモンストレーションします。

Cloudant データベース内の変更 (この使用ケースでは、ドキュメントのアップロード) によって1 つの関数、つまりアクションがトリガーされます。アップロードされたドキュメントは別のアクションの入力になります。そのアクションは Watson Visual Recognition に画像をアップロードした後、Watson によって生成された分類子と一緒に新しいドキュメントを Cloudant にアップロードするというものです。

このコード・パターンでは以下のコンポーネントを使用します。

* [Cloud Functions](https://cloud.ibm.com/docs/openwhisk/index.html#getting-started-with-openwhisk) (Apache OpenWhisk ベース): 極めてスケーラブルなサーバーレス環境内で、オンデマンドでコードを実行できます。
* [Cloudant](https://cloud.ibm.com/catalog/services/cloudant?cm_sp=ibmdev-_-developer-patterns-_-cloudreg): 柔軟な JSON スキーマを使用する最新式の Web およびモバイル・アプリケーションを対象に設計された、完全に管理されたデータ層を使用します。
* [Watson Visual Recognition](https://www.ibm.com/jp-ja/cloud/watson-visual-recognition): 画像の内容を理解する Visual Recognition サービスを利用します。<!--視覚概念のタグを画像に付け、人間の顔を検出し、年齢と性別を概算して、画像の集まりの中から同様の画像を見つけます。-->

このコード・パターンでは、以下のタスクに対処する方法を説明します。

* Cloud Functions を作成してデプロイする
* Cloudant の変更によって Cloud Functions をトリガーする
* Cloud Functions で Watson Image Recognition サービスを利用する

## フロー

![フロー](../../images/serverless-image-recognition-arch.png)

1. ユーザーがギャラリーから写真を選択します。
2. 画像が Cloudant データベース内に保管されます。
3. データベース内に新しい画像が追加されると、Cloud Function がトリガーされます。
4. Cloud Function が画像を取得し、Watson Visual Recognition を利用して画像を処理します。
5. Cloud Function が、視覚認識による結果 (スコア付きクラス) を Cloudant データベース内に保管します。
6. ユーザーがアップロードした画像内に、新しいタグまたはクラスが表示されます。

## 手順

このコード・パターンに関する詳細な手順は、GitHub リポジトリー内にある [README.md](https://github.com/IBM/ibm-cloud-functions-refarch-serverless-image-recognition/blob/master/README.md) ファイルに記載されています。手順の概要は以下のとおりです。

1. リポジトリーを複製します。
2. IBM Cloud サービスを作成します。
3. Cloud Functions をデプロイします。
4. 画像認識アプリを起動します。
