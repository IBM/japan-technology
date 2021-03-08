# Spring Boot マイクロサービスを Kubernetes 上にデプロイする

### Java Spring Boot マイクロサービスを作成して Kubernetes クラスターにデプロイする

English version: https://developer.ibm.com/patterns/deploy-spring-boot-microservices-on-kubernetes
  ソースコード: https://github.com/IBM/spring-boot-microservices-on-kubernetes

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-05-14

 
## 概要

Spring Boot は、本番対応の Spring アプリケーションの迅速な構築を可能にする、こだわりを持ったフレームワークです。このコード・パターンでは、多言語アプリケーション内で Spring Boot マイクロサービスを作成してデプロイしてから、そのアプリを Kubernetes クラスターにデプロイする方法を説明します。

## 説明

Java コミュニティーは、Java EE などのテクノロジーをマイクロサービス・アーキテクチャー内で使用する革新的な方法を常に探し求めています。Spring フレームワークは Java エコシステム内で定着した存在となっていますが、現在、Spring Boot が大きな注目を集めています。それは、Spring Boot では飛躍的に単純化された方法で Spring アプリケーションを作成できるためです。

Spring Boot は Spring アプリケーションの構築をこだわりのある見解で捉えています。Spring Boot を使用すると、Java の `-jar` コマンドや従来型の WAR デプロイメントを使って起動できる、スタンドアロンの Java アプリケーションを作成できます。Spring アプリケーションは既存のアプリケーション・サーバー上に WAR ファイルとしてデプロイすることも、組み込みアプリケーション・サーバーと併せて 1 つの「fat」JAR ファイルにまとめることもできます。いずれの方法でも、Docker コンテナーとうまく連動します。あとは、Spring Cloud のようなネイティブ Spring プラットフォームを頼りに、サービス・ディスカバリー、登録、ロード・バランシングなどのタスクを実行することができます。

けれども、多言語アプリケーションのコンテキストの場合はどうなるでしょうか？さまざまな言語のマイクロサービスからなるシステムを管理するには、汎用のマイクロサービスとコンテナー・オーケストレーション・プラットフォームが必要になります。そこで力を発揮するのが Kubernetes です。このコード・パターンでは、「Office Space」という名前のアプリを構築します。そうです。映画「Office Space」の登場人物 Michael Bolton のアイデアから着想を得たアプリです。このコード・パターンを完了すると、Spring Boot マイクロサービスを含む多言語マイクロサービス・アプリケーションを Kubernetes クラスターにデプロイする方法がわかるようになります。

## フロー

![フロー](../../images/Deploy-Spring-Boot-microservices-on-Kubernetes.png)

1. Python で作成された Transaction Generator サービスがトランザクションをシミュレーションし、それらのトランザクションを Compute Interest マイクロサービスにプッシュします。
2. Compute Interest マイクロサービスが利益を計算し、そのほんのわずかな金額を MySQL データベースに移して保管します。このデータベースは、同じデプロイメント内のコンテナー内部で実行することも、IBM Cloud のようなパブリック・クラウド上で実行することもできます。
3. Compute Interest マイクロサービスが Notification サービスを呼び出して、該当する金額がユーザーのアカウントに預金されたことをユーザーに通知します。
4. Notification サービスは OpenWhisk アクションを使用して、ユーザーに e-メール・メッセージを送信します。メッセージを Slack に送信して OpenWhisk アクションを呼び出すこともできます。
5. さらに、メッセージを Slack に送信する OpenWhisk アクションを呼び出すこともできます。
6. ユーザーが Node.js Web インターフェースにアクセスして、口座残高を取得します。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the README.
