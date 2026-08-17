# Project 6: MCPサーバーの利用

## 概要

Bobに**リモートMCPサーバー**と**ローカルMCPサーバー**を追加し、Web検索やGitなどの外部ツールを利用できるようにします。

## 目的

* BobにMCPサーバーを接続する方法を理解する
* BobからMCPサーバーのツールを呼び出す方法を確認する
* リモートMCPとローカルMCPの追加方法を体験する
* 想定所要時間: 1〜2時間

## 状況の想定

Bob単体では利用できないWeb検索やGitなどの機能を、MCPサーバーを追加することで利用します。

## 本ハンズオンを開始する前に

* Bobを利用できる環境を準備する
* リモートMCPサーバーを利用する場合は、必要なサービスへのサインアップを行う
* 本ハンズオンでは、リモートMCPサーバーの例として **Tavily** を利用する


## 手順

### Part 1：リモートMCPサーバーの追加

#### 1. BobがWeb検索できるかの確認

Bobに以下のように質問します。

```text
Web検索はできますか？
```

Web検索機能が利用できるか確認します。

#### 2. Web検索ツールの追加方法をBobに確認

Bobに以下のように質問します。

```text
Web検索を行うためのツールを追加する方法を教えてください。
```

Bobから提案された方法を確認してください。

#### 3. 利用するMCPサーバーを選択

Bobから提案された方法の中から、利用するMCPサーバーを選択します。

本ハンズオンでは、例として **Tavily Remote MCP Server** を利用します。



#### 4. リモートMCPサーバーの設定
利用するMCPサーバーのドキュメントを確認し、記載されている手順に従ってサーバーの設定を行ってください。以下には、Tavilyの接続方法を記します。

ドキュメントのリンク：https://bob.ibm.com/docs/ide/configuration/mcp/understanding-mcp



* Bobを立ち上げ、Bob sesttingから、MCPサーバーを開き、赤枠のプラスをクリックしてください。  


<img width="1179" height="923" alt="スクリーンショット 2026-08-17 16 30 52" src="https://github.com/user-attachments/assets/9b606f5f-39cb-4553-8c2f-55b4b76ab6fb" />  




* 設定スコープを選択し、「設定ファイルを開く」を選択してください。すべてのワークスペースで利用する場合は「グローバル」を選択し、それ以外の場合は「特定のワークスペースに追加する」を選択してください。  


<img width="929" height="398" alt="スクリーンショット 2026-08-17 16 31 05" src="https://github.com/user-attachments/assets/c1efbafb-2af9-42d2-a8d0-3d4616968c35" />  



* 下記のサイトからTavilyへのサインアップを行い、取得したAPIキーを入力してください。mcp.jsonの書き方を参考にしてください。  

Tavilyのサインアップのサイト：
https://auth.tavily.com/u/login/identifier?state=hKFo2SBtNDFSSzJXSWJKckV0RUQtMGliQzZWWGt3NmJ1ZUF0c6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHh5UjNub1RfVms3eFNja05DMVlhQ3JEajdxWkVIc1Zko2NpZNkgUlJJQXZ2WE5GeHBmVFdJb3pYMW1YcUxueVVtWVNUclE

mcp.jsonの書き方：
```text
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.tavily.com/mcp/?tavilyApiKey=***"]
    }
  }
}
```


<img width="1168" height="480" alt="スクリーンショット 2026-08-17 16 42 52" src="https://github.com/user-attachments/assets/f469e9b1-fff3-4037-b038-24728c32f25c" />

これで設定は完了です。


#### 5. Web検索を実行

設定が完了したら、BobにWeb検索を依頼し、接続されているか確認しましょう。

```text
最新のAI関連ニュースをWeb検索してください。
```

<img width="704" height="156" alt="スクリーンショット 2026-08-17 16 44 02" src="https://github.com/user-attachments/assets/5cf05964-a5f4-46ba-b2a5-343be85c1a9e" />

MCPサーバーへの接続許可を求められるので、承認します。

<img width="708" height="348" alt="スクリーンショット 2026-08-17 16 44 15" src="https://github.com/user-attachments/assets/beab4400-8b75-43c2-b1b3-e0297d3a9166" />

Tavily Searchが実行され、サーチ結果が出力されます。

<img width="703" height="685" alt="スクリーンショット 2026-08-17 16 44 44" src="https://github.com/user-attachments/assets/b7d86fb8-7bc7-44f2-9cdc-ee7515725895" />


#### 6. 接続できない場合

MCPサーバーに接続できない場合は、以下を確認してください。

* **MCPJam** など別のツールからMCPサーバーへ接続し、接続自体に問題がないか確認

参考リンク：https://www.mcpjam.com/

### Part 2：ローカルMCPサーバーの追加

#### 1. Bob Marketplace

BobのMarketplace（画像の赤枠部分）から利用可能なMCPサーバーを確認します。

<img width="332" height="529" alt="bob_marketplace" src="https://github.com/user-attachments/assets/c4c9af07-32d9-4223-9815-6c01a3ef895a" />


#### 2. MCPサーバーの追加

Marketplaceから利用したいMCPサーバーを選択して追加してください。

本ハンズオンでは、例として **Git関連のMCPサーバー**を利用します。



#### 3. MCPツールをBobから実行

追加したMCPサーバーが提供するツールの1つを、Bobから実行するよう指示します。

```text
追加したGit MCPサーバーのツールを使ってください。
```

#### 4. 実行結果の確認

BobがMCPサーバーのツールを呼び出し、正常に結果を取得できることを確認してください。



## 完了条件

以下が確認できればハンズオン完了です！

* リモートMCPサーバーをBobに追加できた
* BobからWeb検索ツールを実行できた
* ローカルMCPサーバーをBobに追加できた
* BobからローカルMCPサーバーのツールを実行できた
