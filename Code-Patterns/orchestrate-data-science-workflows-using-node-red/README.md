# データ・サイエンスのワークフローを、Node-RED を使用して編成する

### Node-RED を使用して、IBM Watson Studio 分析ワークフローをトリガーする Web インターフェースを作成する

English version: https://developer.ibm.com/patterns/orchestrate-data-science-workflows-using-node-red
  ソースコード: https://github.com/IBM/node-red-dsx-workflow

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-02-07

 
_**Note: This pattern is part of a composite pattern.** These are code patterns that can be stand-alone applications or might be a continuation of another code pattern. This composite pattern consists of:_

* データ・サイエンスのワークフローを、Node-RED を使用して編成する (このパターン)
* [ロボット型計算・推測エージェントを作成する](https://developer.ibm.com/jp/patterns/robotic-calculations-and-inference-agent/)

## 概要

ビジネス・ユーザーに、ユーザー・インターフェースのないデータ・サイエンスのワークフローについて説明するのは簡単なことではありません。そこで、このコード・パターンでは Node-RED を使用して Web インターフェースを作成する方法を説明します。このインターフェースでは、データ・サイエンスのワークフローをトリガーし、IBM Watson Studio 上で Jupyter Notebook コードを実行します。

## 説明

データ・サイエンスの目標は、データから洞察を引き出すことです。IBM Watson Studio などのツールは、データ・サイエンスの概念と応用統計学に関する深い知識を持つ専門家向けに設計されています。けれども最近では、データ・サイエンティストとビジネス・コミュニティーとの間のギャップを埋める方法を探している開発者たちが、この 2 つをつなげる新しいツールを使用できるようになっています。

このコード・パターンでは、アナリティクスのワークフローをトリガーする Web インターフェースを作成します。トリガーされたワークフローは、IBM Watson Studio 上で Jupyter Notebook コードを実行します。このようにして、データ・サイエンスの力をビジネス・ユーザーが利用できるようにする完全なアプリを作成します。

このコード・パターンをひととおり完了すると、以下の方法がわかるようになります。

* IBM Watson Studio 上で Python Pandas を使用してデータから洞察を引き出すアプリを開発する
* Node-RED を使用して、Web インターフェースを作成する
* Node-RED を使用して、IBM Watson Studio 内で Jupyter Notebook コードの実行をトリガーする

データ・サイエンスの力をビジネス・ユーザーに直接デモンストレーションしようとしている誰にとっても、このパターンは最適です。

## フロー

![フロー](../../images/Orchestrate-DSX-workflows-using-Node-RED-arch-flow.png)

1. Object Storage システムがデータ・ドキュメントを保管します。
2. Python コードが Object Storage システムからドキュメントのコンテンツを取得します。
3. Jupyter Notebook が UI から受け取ったイベントに応じて、データを処理し、洞察を生成します。IBM Watson Studio 上で Python コードが実行されて、そのレスポンスが Node-RED 上の WebSocket サーバーに返されます。
4. Jupyter Notebook は Spark によって駆動されます。
5. Node-RED がホストする WebSocket サーバーが、IBM Watson Studio 上の Jupyter Notebook と Web UI との通信を可能にします。
6. Web UI からイベントがトリガーされると、WebSocket を使用して Jupyter Notebook 上の Python コードにそのイベントが送信されます。UI が WebSocket サーバー上の Python コードからのレスポンスを読み取り、結果を表示します。

## 手順

1. Sign up for Watson Studio.
2. Create IBM Cloud services.
3. Import the Node-RED flow.
4. Note the websocket URL.
5. Update the websocket URL.
6. Create the notebook.
7. Add the data.
8. Update the notebook with service credentials.
9. Run the notebook.
10. Analyze the results.
