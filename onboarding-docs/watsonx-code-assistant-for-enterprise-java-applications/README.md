# IBM watsonx Code Assistant for Enterprise Java Applications

> 本ガイドは、IBM watsonx Code Assistant for Enterprise Java Applications のオンボーディングのために作成されています。
> 手順や画面が本ガイドと一致しない場合は、**IBM の最新ドキュメントや公式ガイドラインを必ず参照**し、最新版に沿った対応を行ってください。

## What is watsonx Code Assistant?

IBM watsonx Code Assistantは、Graniteモデルを活用して開発者のスキル・セットを強化し、開発とモダナイゼーションの取り組みを簡素化、自動化します。また、リアルタイムの類似性チェックを通じてIP補償と透明性を提供し、組み込みのアセスメント機能やチャット機能を通じてコードの整合性とコンプライアンスを確保します。<br>
詳細は[こちら](https://www.ibm.com/jp-ja/products/watsonx-code-assistant)をご覧ください。

## Onboarding Process
IBM watsonx Code Assistant for Enterprise Java Applications のオンボーディングプロセスは、以下の4つの領域に分かれています：

1. インスタンスを立てる

    1. [IBM Cloudログイン](./01_instance/01_01_ibmcloud_login/)
    1. [サブスクリプションコードの適用](./01_instance/01_02_subscription_code/)
    1. [リソース・グループの作成](./01_instance/01_03_resource_group/)
    1. [watsonx Code Assistant サービスインスタンスのプロビジョニング](./01_instance/01_04_create_instance/)
    1. [Cloud Object Storageインスタンスの作成](./01_instance/01_04_create_instance/)

1. watsonx Code Assistant のセットアップ

    1. [watsonx Code Assistant へのアクセス](./02_setup/02_01_access_watsonxcodeassistant/)
    1. [watsonx Code Assistant のセットアップ](./02_setup/02_02_setup_watsonxcodeassistant/)
        - インストールタイプの選択
        - アクセス・グループの作成　※「組織的利用」の場合のみ
        - デプロイメント・スペースの作成
        - デプロイメント・スペースへのアクセス・グループの追加　※「組織的利用」の場合のみ
        - コード候補の表示方法の設定
        - アクセス・グループへのユーザーの追加　※「組織的利用」の場合のみ

1. IDE拡張機能またはプラグインのインストール

    1. [IBM Cloud API Key の作成](./03_ide/03_01_create_apikey/)
    1. Visual Studio Code用拡張機能のインストール
        1. [Visual Studio Code用拡張機能のインストール](./03_ide/03_02_visual_studio_code/03_02_01_install_extention/)
        1. [Enterprise Java環境のセットアップ](./03_ide/03_02_visual_studio_code/03_02_02_setup_enterprise_java_environment/)
    1. Eclipse IDEプラグインのインストール
        1. [Eclipse IDEプラグインのインストール](./03_ide/03_03_eclipse/03_03_01_install_plugin/)
        1. [Enterprise Java環境のセットアップ](./03_ide/03_03_eclipse/03_03_02_setup_enterprise_java_environment/)

1. [watsonx Code Assistant for Enterprise Java Applications の主な使い方](./04_usecase/)

    1. コードの提案を得る
        1. チャットの会話を使う
            - プロンプト・ライブラリの使用
        1. ワークスペース内のコードを参照する
    1. アプリの解説
    1. Javaアプリケーションモダナイゼーション
    1. Javaバージョンアップグレード

それぞれのステップに関する情報、ガイド、参考リンクについては、該当するリンクを選択してください。
