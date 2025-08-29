# エージェント一覧

公式ドキュメント：<https://www.ibm.com/docs/en/instana-observability/current?topic=planning-instana-agent-types>

Instanaで利用できる各種エージェントの種類とその機能を整理し、導入時の参考になるよう解説します。

> [!NOTE]  
> このページは2025年6月頃の情報をベースにしています。最新のAgentを導入する場合は、必ず[公式ドキュメント](https://www.ibm.com/docs/en/instana-observability/current?topic=planning-instana-agent-types)を参照してください。  

## Instana Agent タイプ一覧

### ホストエージェント

| サブタイプ / モード         | 特徴                                                                 | 推奨環境                     | 更新方法                             |
|----------------------------|----------------------------------------------------------------------|------------------------------|--------------------------------------|
| **動的 (Dynamic)**         | 起動時に最新センサーを取得し、毎日自動更新。新機能やバグ修正に迅速対応。 | 一般的な環境                 | 自動更新（Bootstrapは手動）         |
| **静的 (Static)**          | 自己完結型。更新不可。ネットワーク制限環境向け。                       | 金融機関など制限環境         | 手動更新（Ansible/Terraformなど）   |
| **モード：OFF**            | 監視なし。アイドル状態を通知。                                       | 一時停止中のホスト           | -                                    |
| **モード：INFRASTRUCTURE** | ホスト監視のみ。アプリトレースなし。                                 | 基盤監視のみ必要な場合       | -                                    |
| **モード：APM（デフォルト）** | フル監視＋トレース。Instanaの全機能を活用。                           | 通常運用環境                 | -                                    |
| **モード：AWS**            | AWSデータ収集に特化。INFRAに近い。                                   | AWSクラウド環境              | -                                    |

基本的に動的エージェントが推奨されており、静的エージェントは制限環境での利用が中心です。  
モード変更は導入後でも可能です（例：INFRASTRUCTURE → APM）。

### クラウドサービスエージェント

| 対象クラウド | セットアップ方法 |
|--------------|------------------|
| AWS          | ホストエージェントをAWSモードで実行 |
| Azure        | Azureセンサーの有効化 |
| GCP          | GCPセンサーの有効化 |
| IBM Cloud    | 特殊なセットアップが必要（調査中） |
| Alibaba      | Alibabaセンサーの有効化 |

### サーバーレスエージェント

| 対象サービス | セットアップ方法 |
|--------------|------------------|
| AWS Lambda   | Lambda関数にInstanaトレーサー追加 |
| AWS Fargate  | Fargateコレクターのセットアップ |
| Azure Functions | Azure Functionsアプリにトレーサー追加 |
| Google Cloud Run | Cloud Native Buildpackまたは手動セットアップ |

### Webサイト・モバイルエージェント

| 対象 | セットアップ方法 |
|------|------------------|
| Webサイト | JavaScriptエージェントを組み込み（Instana UI提供コード） |
| iOSアプリ | Swift Package ManagerまたはCocoaPods |
| Androidアプリ | Gradleプラグイン＋SDK依存関係追加 |
| React Native | npmでパッケージ追加 |
| Flutter | pub.devからパッケージ追加 |
