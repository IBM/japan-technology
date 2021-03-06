# 自動スケーリングによって銀行取引ピーク時の需要に対応する

### 需要に応じて自動的にスケーリングするモバイル小切手預金処理システムを実現する

English version: https://developer.ibm.com/patterns/automatically-scale-to-handle-peaks-in-banking-transaction-demand
 
ソースコード: https://github.com/IBM/ibm-cloud-functions-serverless-ocr-openchecks

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2017-10-04

 
## 概要

リテール・バンキングの預金処理においては、2 週間ごとの給与日といったピーク時の需要を想定して、IT システムがオーバー・プロビジョニングされがちです。サーバーレス・アーキテクチャーでは需要に応じて計算能力がスケーリングされます。したがってユーザー・エクスペリエンスが向上するだけでなく、必要に合わせて効率的にスケーリングされるため、銀行の IT コストと顧客の需要が正確に適合し、コストの無駄がなくなります。

## 説明

オンライン・バンキング・サービスを提供しているとしたら、どんなレベルの需要にでもうまく対応できる態勢を整えておくべきです。小売銀行がモバイル、Web、そして支店からのピーク時のトラフィックに対応できなければ、顧客はすぐに、より機動性のある競合他社に乗り換えてしまうでしょう。そのような事態を避けたいとしたら、幸いなことに、サーバーレス・アーキテクチャーがあります。サーバーレス・アーキテクチャーを利用すれば、効率的かつ自動的に、現在のワークロードに合わせて正確にスケールアップ、スケールダウンすることができます。

リテール・バンキング組織で働く開発者は例外なく、トランザクション数の大幅な増加に対処可能なコードやシステムを作成できなければなりません。あなたがそのような開発者の 1 人であるか、あるいはそのような開発者になることを目指しているとしたら、需要に応じて効率的にスケールアップする方法を見つけることで、IT 管理者や経営陣の間でのあなたの評判は飛躍的に高くなるはずです。

このコード・パターンでは、リテール・バンキングのモバイル・システムまたは支店の小切手預金システムをサポートする、サーバーレス・イベント駆動型アーキテクチャーの力を紹介し、サーバーレス関数を使用して小切手画像のアップロード、サイズ変更、解析、預金の処理を行う方法を説明します。この使用ケースで強調するのは、ピーク時とアイドル時とで需要にかなりの差があるリテール・バンキング・ワークロードには、その自動スケーリングとクラウド・サービスのきめ細かい料金設定により、サーバーレス・アーキテクチャーがなぜ魅力的な選択肢となるのかです。

このコード・パターンで取り上げるシナリオでは、まず、小切手の画像がクラウド上の Object Storage サービスにアップロードされます。アップロードされた画像は、顧客のポータル上およびアーカイブで使用するためにサイズ変更されます。次に、画像が解析されて、預金口座と銀行支店コードの情報が抽出されます。この情報に、ユーザーまたは出納係が提供した情報が補足されることにより、小切手が自動的に処理されます。このプロセスによってエラーが減るとともに、顧客がより短時間で預金を使用できるようになります。

ワークロードの需要の大小を問わず、小売銀行が効率的で信頼の置けるトランザクションを完了できるようにサポートする任務を負っている開発者、あるいはサーバーレスの手法とこの手法を実践するために役立つツールについて理解を深めたいと思っている開発者にとって、このコード・パターンは出発点になります。

## フロー

![フロー](./images/Automatically-scale-to-handle-peaks-in-banking-transaction-demand-.png)

1. モバイル・アプリのユーザーまたは銀行支店の出納係が、小切手の画像をスキャンして Object Storage サービス (着信コンテナー) にアップロードします。画像ファイルの名前には、顧客の e-メール、受取人名義の口座番号、小切手の金額、タイムスタンプがエンコードされて含められます。
1. 新しい小切手画像の有無を調べるために、「ポーリング・アラーム」によって「小切手検索」アクションが 20 秒間隔でトリガーされ、Object Storage サービスがポーリングされます (別の実装として、ポーリングするのではなく、このイベントをプッシュすることもできます)。
1. 「小切手検索」アクションは、Object Storage サービスに対してクエリーを実行します。ファイルが検出されるごとに、このアクションが「画像保存」アクションを呼び出して、小切手を非同期で並列処理します。
1. 「画像保存」アクションが画像をダウンロードし、サイズ変更した 2 つのコピー (倍率 50% と 25%) を「archived」データベースに、元の画像を「audited」データベースに挿入します。挿入処理がすべて正常に完了すると、ファイルが Object Storage サービスから削除されます。
1. 「audited」データベース上の変更トリガーによって「解析チェック」アクションが呼び出され、完全サイズの画像から情報が読み取られます。
1. 「解析チェック」アクションは画像を取得した後、「OCR アクション」アクションを呼び出して、支払者情報と銀行支店コードを読み取ります。この情報を読み取ることができない場合、小切手には人間によるレビューが必要であることを示すフラグが立てられます。読み取られた情報は、「parsed」データベースに保管されます。
1. 「parsed」データベースに対する変更によって別のトリガーが起動され、このデータベースに対して「預金記録」アクションが呼び出されます。
1. この最後の「預金記録」アクションは、解析されたレコードから口座の詳細情報を取得し、トランザクションを「processed」データベースに記録して、e-メール・アラートを顧客に送信します。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the [README](https://github.com/IBM/ibm-cloud-functions-serverless-ocr-openchecks/blob/master/README.md).
