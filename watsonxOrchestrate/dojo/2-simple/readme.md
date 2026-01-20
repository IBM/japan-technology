# AI Agent Dojo #2、簡略版

* 最終更新日: 2026/01/21
* [準備方法](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)をご覧の上、ハンズオンの実行までに、watsonx Orchestrateの環境を用意してください。
* ハンズオンは、watsonx Orchestrate 30日無償評価版で動作を確認してあります。
* 以前に公開したAI Agent Dojo #2を発展させ、利用できる基盤モデルの変更、watsonx Orchestrateの機能改善に合わせて、内容を改良したものになります。
## リフレッシュ版からの主な改良点: 
  * 指定された地名から、緯度・経度を基盤モデル自身で取得することで、AIエージェントがユーザーに緯度・経度を問い合わせずに気象情報の取得に進められること。別の言い方をすると、Nominatim APIの呼び出し制約を気にしなくて良いこと。
  * Pythonコードは使わず、ノーコードによるアプローチにより、デバッグを容易にしたこと

## 1. [地名から緯度、経度、国コードを求めるフローを作成する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-simple/01Geocoding/readme.md)
指定した地名を使って、基盤モデルが学習している情報を使って、緯度、経度、国コードを求める簡単なフローを作成します。

## ２. [気象情報を取得するワークフローを作成する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-simple/02WeatherFlow/readme.md)
1で作ったフローに気象情報の取得を追加します。

### 注意事項並びに免責事項
* IBM watsonx OrchestrateはSaaS製品であり、定期的に更新が発生します。変更により、ハンズオンの説明資料にある画面のスクリーンショットが実際のものと異なる場合があります。
* AIエージェントは、基盤モデルとツールやワークフローを組み合わせて、回答を生成します。AIエージェント内の推論結果によって回答内容の表現がハンズオンの資料と異なる場合があります。
* このハンズオンは、watsonx Orchestrateのハンズオン資料をベースに、30日無償評価版でも動作することを確認し、英語UIで実行した内容を説明しています。
* [ツールを定義して呼び出してみよう](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)
* [フローを実装してみよう！](https://ibm.github.io/ba-handson-jp/wxoagent/flow/)
