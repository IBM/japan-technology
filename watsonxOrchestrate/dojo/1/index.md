# AI Agent Dojo #1

最終更新日: 2025/9/24

第1回目は、企業の生産性を高める生成AIエージェント watsonx Orchestrateの環境を構築し、 IBMについての情報に回答するAIエージェントを作り、IBMの2024年の財務情報を知識として登録し、その知識をツールを呼び出す方法について、ハンズオンを通じて体験します。

## ゴール:
* watsonx Orchestrateを実行しながら学ぶ環境を整えます。
* Agent Builderを使って、AIエージェントを作成します。
* 文書ファイルを使って、RAGの手法でAIエージェントに知識を与え、回答に利用できるようにします。
* AIエージェントをデプロイして、チャットなどから利用できるようにします。

### ご注意:
* このハンズオンでは、watsonx OrchestrateのSaaS環境を利用します。
* ハンズオン資料内のスクリーンショットは、最終更新日の直前に作成しています。SaaSの製品は、予告なく画面仕様が変わる場合がありますので、ご注意ください。
* watsonx Orchestrateの評価版(Trial版)は、Amazon Web Services上にデプロイされている環境をIBMが無償で提供しています。このため、サービス・レベルの保証はありません。
* IBM Technology Zoneのwatsonx Orchestrate Trial版は、IBM Cloud上にデプロイされています。利用条件は、IBM Technology Zoneに準拠します。[利用条件](https://techzone.ibm.com/terms)の範囲内でご利用ください。実稼働システムの実行にはご利用いただけません。また[セキュリティー・ポリシー](https://techzone.ibm.com/terms/securitypolicy)もご確認の上、ご利用ください。
* watsonx Orchestrate 評価版環境のコンピューター・リソースの空き状況によっては、予期せぬエラーが生じたり、適切に応答が返ってこない場合もあります。その際は、時間をおいて、再試行をお願いします。

## [watsonx Orchestrate 環境の準備](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)
watsonx Orchestrateの環境を準備します。準備が整っている方は、次のPart 1へ進んでください。

## [watsonx Orchestrate AI エージェント体験 Part 1](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/01HelloAgent/readme.md)

この演習は、IBMについて回答するAIエージェント 'IBMInfo' を作成します。ProfileとBehaviorを設定し、AIエージェントの入り口を体験しましょう。

## [watsonx Orchestrate AI エージェント体験 Part 2](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/02RagAgent/readme.md)

この演習は、IBMについて回答するAIエージェント 'IBMInfo' にRAGの手法で知識を追加します。Part 1が終わっている状態からスタートします。Knowledgeを設定することで、企業情報など、AIエージェントに知識を与えます。

### 注意事項並びに免責事項
* IBM watsonx OrchestrateはSaaS製品であり、定期的に更新が発生します。ハンズオンの説明資料にある画面のスクリーンショットが実際と異なる場合があります。
* AIエージェントは、基盤モデルとツールやワークフローを組み合わせて、回答を生成します。AIエージェント内の推論結果によって回答内容の表現がハンズオンの資料と異なる場合があります。
* このハンズオンは、watsonx Orchestrateのハンズオン資料をベースに、評価版でも動作することを確認し、英語UIで実行した内容を説明しています。
* [AI Agentを作ってみよう](https://ibm.github.io/ba-handson-jp/wxoagent/agent/)

