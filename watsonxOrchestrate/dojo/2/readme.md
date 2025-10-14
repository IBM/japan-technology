# AI Agent Dojo #2

* 最終更新日: 2025/10/14
* ハンズオンの実行までに、watsonx Orchestrateの環境を準備してください。
[準備方法])(https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)

## 1. [気象情報に回答するAIエージェントを作成する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2/WeatherAgent/readme.md)
Open Meteoが提供している気象情報APIを用いて、地名（経度、緯度）から現在の天気について回答するAIエージェントを作ります。

## 2. [AIエージェントにツールとして、MCPサーバーを追加する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2/TimeMCP/readme.md)
時刻に関するMCP serverをAIエージェントに追加する方法を体験します。

## 3. [ツールとワークフローを使って気象情報を取得する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2/WeatherFlow/readme.md)
1で作成したAIエージェントのツールを用いて、簡単なワークフローで回答内容を変化させる方法を体験します。

### 注意事項並びに免責事項
* IBM watsonx OrchestrateはSaaS製品であり、定期的に更新が発生します。変更により、ハンズオンの説明資料にある画面のスクリーンショットが実際のものと異なる場合があります。
* AIエージェントは、基盤モデルとツールやワークフローを組み合わせて、回答を生成します。AIエージェント内の推論結果によって回答内容の表現がハンズオンの資料と異なる場合があります。
* このハンズオンは、watsonx Orchestrateのハンズオン資料をベースに、30日無償評価版でも動作することを確認し、英語UIで実行した内容を説明しています。
* [ツールを定義して呼び出してみよう](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)
* [フローを実装してみよう！](https://ibm.github.io/ba-handson-jp/wxoagent/flow/)
