# AI Agent Dojo #2 (リフレッシュ版)

* 最終更新日: 2026/01/18
* [準備方法](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)をご覧の上、ハンズオンの実行までに、watsonx Orchestrateの環境を用意してください。
* ハンズオンは、watsonx Orchestrate 30日無償評価版で動作を確認してあります。
* 以前に公開したAI Agent Dojo #2を発展させ、利用できる基盤モデルの変更、watsonx Orchestrateの機能改善に合わせて、内容を改良したものになります。
* 主な改良点: 
  指定された地名から、緯度・経度をMCP serverで取得することで、AIエージェントがユーザーに緯度・経度を問い合わせずに気象情報の取得に進められること。

## 1. [気象情報に回答するAIエージェントを作成する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-refresh/01WeatherAgent/readme.md)
* Open Meteoが提供している気象情報APIを用いて、地名から現在の天気について回答するAIエージェントを作ります。
* 指定した地名からMCP serverを利用して、緯度、経度を求めます。
* 気象情報APIをツールとして登録し、緯度・経度を指定して、現在の天気を求めます。

## ２. [気象情報を取得するワークフローを作成する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-refresh/WeatherFlow/readme.md)
1と同様の動きをするAIエージェントをMCP server、気象APIを組み合わせて、簡単なワークフローと一緒に作ります。指定された地名が米国であれば華氏表示、それ以外は摂氏表示で気温を含めた気象情報を回答するAIエージェントを作ります。

### 注意事項並びに免責事項
* IBM watsonx OrchestrateはSaaS製品であり、定期的に更新が発生します。変更により、ハンズオンの説明資料にある画面のスクリーンショットが実際のものと異なる場合があります。
* AIエージェントは、基盤モデルとツールやワークフローを組み合わせて、回答を生成します。AIエージェント内の推論結果によって回答内容の表現がハンズオンの資料と異なる場合があります。
* このハンズオンは、watsonx Orchestrateのハンズオン資料をベースに、30日無償評価版でも動作することを確認し、英語UIで実行した内容を説明しています。
* [ツールを定義して呼び出してみよう](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)
* [フローを実装してみよう！](https://ibm.github.io/ba-handson-jp/wxoagent/flow/)
