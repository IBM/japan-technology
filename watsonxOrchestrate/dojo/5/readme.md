# AI Agent Dojo #5: watsonx.ai AIエージェント体験
* 最終更新日: 2026/1/21

* ハンズオンの目的: watsonx.ai のAI Agent Betaを体験する

## 演習: [AI エージェントを試してみる](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/07/readme.md)

## オプション演習: [Quick start: Build and deploy an agent](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-build-deploy-agent)
Pythonを使って、watsonx.aiを使ったAIエージェントを作るためのチュートリアルです。こちらは、必要に応じて自習してください。

##

## ご案内: AI Agent Dojo #2の簡略版、MCPサーバーを使うRefresh版の提供開始

AI Agent Dojo #2、watsonx Orchestrate フローの作成について、関連する機能が大きく改良されたため、ハンズオン資料を改めて作り直しました。

* [簡略版](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-simple/readme.md)
* 説明動画: https://video.ibm.com/recorded/134672335

指定した地名から、緯度・経度・国コード・気象情報を取得するAgentic Workflowを作成します。Pythonのコードは使いません。

* [リフレッシュ版](https://github.com/IBM/japan-technology/tree/main/watsonxOrchestrate/dojo/2-refresh)

指定した地名から、緯度・経度・国コードについて Geocoding-ai/mcp サーバーを利用して取得し、気象情報を呼び出すAgentic Workflowを作成します。
MCP serverを呼び出し、JSON文字列を解析することで、データを取り出しています。MCP serverとの連携を試すパターンの学習に活用してください。
注意点はlimit、Geocoding-ai/mcp サーバーが利用しているNominatim APIは、呼び出しの制約があり、1秒間に2回以上呼び出してしまうと、418エラーとなります。
このため、複数の地点を一度に呼び出すのには向いていません。複数地点の気象情報を取得したい場合は、簡略版の実装方法が安全です。

