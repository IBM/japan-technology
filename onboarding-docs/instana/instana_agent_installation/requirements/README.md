# Instana Agent の要件

公式ドキュメント：<https://www.ibm.com/docs/ja/instana-observability/current?topic=requirements-instana-agent#host-agents>

本書では、VMやKubernetesクラスタ向けエージェントである「ホストエージェント」のインストールを前提としてご案内しています。

Instana Agentをインストールする前に、エージェントの要件を満たしていることを[公式ドキュメント:Instana Agentの要件 > ホストエージェント](https://www.ibm.com/docs/ja/instana-observability/current?topic=requirements-instana-agent#host-agents)で確認してください。

なお、AWS RDSやAzureサブスクリプションのようなマネージドクラウドサービスに対する監視を行う場合は、 [公式ドキュメント:クラウド・サービス・エージェント](https://www.ibm.com/docs/ja/instana-observability/current?topic=agents-installing-configuring-cloud-service)を参照の上、導入を検討ください。

また、AWS Fargate, LambdaやAzure Functionsのようなサーバーレスクラウドサービスに対する監視を行う場合は [公式ドキュメント:サーバーレス・エージェント](https://www.ibm.com/docs/ja/instana-observability/current?topic=agents-installing-configuring-serverless)を参照の上、導入を検討ください。

加えて、エージェントをインストールする際には、インストール対象のホストから（https://setup.instana.io）にアクセスできる必要があるため、ご注意ください。
