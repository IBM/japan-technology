# 成熟度モデルとカスタマージャーニー

成熟度モデルとカスタマージャーニーは競合APM製品ではWeb上で定義されているものが多くありますが、Instanaに関してはグローバルでも定義されておらず、現在 IBM Japan CSM チームを中心に検討を進めています。

このオンボーディングガイドでは、**成熟度Level1** を目指します。

## 成熟度

|Level|成熟度|内容|
|----|----|----|
|5|Agentic AI|Full Automation <br> Scale IT Automation Agentic AI|
|4|Predictive Analytics|Predict potential issues <br> Prevent encountering problem <br> Proactively identify potential issues based on trend analysis and learned experiences|
|3a|Observability for AI|Visualization for OpenLLM-based models|
|3b|Integration|Streamlined operations through integration with tools like Terraform, Ansible, and Concert <br> Applying FinOps principles|
|2|APM|Full Stack Monitoring|
|1|Monitoring|Monitoring Iinfrastructure <br> Real-time detection and mapping of interdependencies|
|0|Onboarding||

## カスタマージャーニー

|成熟度|ジャーニー|概要|IT 管理者|SRE|開発者|DevOps|
|----|----|----|----|----|----|----|
|3→4|インテリジェントな修復|watsonx.aiを用いて、問題の自動修復についての説明。問題を自動的に検出し、解決する方法||◯||
||スマート・アラート|スマートアラート機能についての説明。問題を自動的に検出し、通知する方法<br>[Qiita](https://qiita.com/mayamasaki68/items/fbf3f5164e12b22e8796)||◯||◯|
|2→3b|パイプラインのフィードバック|パイプラインのフィードバックループを実装する方法についての説明。パイプラインのパフォーマンスや質を分析する方法<br>[Qiita_1](https://qiita.com/mumumu_666/items/71f6c99ca312756c5474),[Qiita_2](https://qiita.com/mumumu_666/items/706fbbb9cb47d79290c3)|||◯||
||Git ベースの構成管理|Gitベースの構成管理機能についての説明。ホストやサービスの構成をバージョン制御システム（Git）で管理する方法||||◯|
||自動化アクション Ansible|InstanaとAnsibleの統合についての説明。自動化アクションを組み込む方法||||◯|
||自動化の管理|アクションを管理する方法についての説明。問題の解決やメンテナンス作業を実行するための方法||◯||◯|
||Terraform の統合|InstanaとTerraformの統合についての説明。インフラストラクチャーの自動化管理を支援する方法<br>[Qiita_1](https://qiita.com/nobuking/items/89e3b344f0d3abacc2bc),[Qiita_2](https://qiita.com/daihiraoka/items/b197e849cd54465f1bd9)||||◯|
||統合、SDK、および API|Instana SDKやAPIの使用方法、さらにはさまざまなサービスやツールとのインテグレーション方法<br>[Qiita](https://qiita.com/daihiraoka/items/4273ef4272b66a9e080d)||◯|||
|1→2|アプリケーション・パースペクティブ|アプリケーションの様々な側面を理解するための機能についての説明。ユーザーの経験やアプリケーションのパフォーマンス分析方法<br>[Qiita_1](https://qiita.com/daihiraoka/items/2e3f66a61e61afa60324),[Qiita_2](https://qiita.com/daihiraoka/items/a49b7492a2da68c78a92)||◯|◯||
||Instana AutoProfile|プロセスをプロファイルする方法についての説明。リソースの使用状況やパフォーマンスに関する詳細な情報の取得方法||◯|◯||
||プロファイルの分析|プロファイルを分析する方法についての説明。リソースの使用状況やパフォーマンスに関する詳細な情報を得る方法|||◯||
||コンテキスト・ガイド|コンテキストガイド機能についての説明。アプリケーションやインフラストラクチャーのコンテキストを提供し、問題の分析支援方法|◯||||
||ロギング|ロギングの設定方法、さらにはログデータの表示方法|||||
||根本原因分析|問題の根本原因を分析する方法についての説明。問題の原因を特定し、解決する方法<br>[Qiita](https://qiita.com/daihiraoka/items/a49b7492a2da68c78a92)|◯|◯|◯|◯|
||無制限分析|Instanaの大規模なデータ分析機能についての説明。大量のデータを効率的に処理し、パフォーマンス最適化方法||||◯|
||インフラストラクチャーの分析|インフラストラクチャーを分析する方法についての説明。ノード、コンテナ、サービス、アプリケーションのパフォーマンス監視方法<br>[Qiita](https://qiita.com/daihiraoka/items/c6fd7cfa9e4a59b3038a)|◯|◯|◯||
||Web サイトのモニター|ウェブサイトをモニタリングする方法についての説明。ウェブサイトのパフォーマンスや可用性の監視方法<br>[Qiita](https://qiita.com/iwashinat/items/d2a05186bca7cc627128)|◯||||
||モバイル・アプリケーションのモニター|モバイルアプリケーションをモニタリングする方法についての説明。モバイルアプリのパフォーマンスや可用性を監視する方法|◯||||
||合成モニタリング|合成モニタリング機能についての説明。アプリケーションの外部からのテストを行い、パフォーマンスや可用性を確認する方法<br>[Qiita](https://qiita.com/iwashinat/items/3e1d9587513814a4b4fc)||◯|◯|◯|
||サービス・レベル目標|サービスレベルの目標（SLO）を設定する方法についての説明。サービスのパフォーマンスを定義し、監視する方法<br>[Qiita](https://qiita.com/komuroki/items/5a6c926d2c4fc45a2607)|◯|◯||
|0→1|アラートの構成と管理|アラートルールの作成、編集、削除方法、アラート通知の設定方法||◯||
||インフラストラクチャーのモニター|ノード、コンテナ、サービス、およびアプリケーションのモニタリング方法、インフラストラクチャーのカスタマイズ方法<br>[Qiita](https://qiita.com/daihiraoka/items/c6fd7cfa9e4a59b3038a)|◯|◯|||
||ダイナミック・グラフの活用|ダイナミック・グラフの表示方法、ネットワークトラフィックの探索方法、サービス間の関係のカスタマイズ方法|◯||||
||組み込みの問題およびインシデントの管理|ビルトインの問題やインシデントの自動検出方法、さらにはその解決方法<br>[Qiita_1](https://qiita.com/komuroki/items/f55ff29ed5e75340b8e4),[Qiita_2](https://qiita.com/komuroki/items/6f5d992bf490d90bc6ce)||◯||◯|
|0|APMとは？||||||
||プロビジョニング||◯|◯|◯|◯|
||2段階認証||◯|◯|◯|◯|
||ユーザー招待||◯||||
||ユーザー権限・グループ設定||◯||||
||Instana Agentのインストール|[Qiita](https://qiita.com/M_Beach/items/37eb0eec0f9e2ab81ca8)<br>[Movie](https://video.ibm.com/recorded/134391694)|◯|◯|◯|◯|
