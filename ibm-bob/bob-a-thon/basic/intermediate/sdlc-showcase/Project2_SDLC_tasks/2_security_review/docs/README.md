# Banking Demo - ドキュメント索引

Banking Demo ドキュメントへようこそ。この索引では、必要な情報にすばやくたどり着けるように構成を整理しています。

## 📚 ドキュメント構成

```text
docs/
├── README.md                          # このファイル - ドキュメント索引
├── operations/                        # IT 運用ガイド
│   └── DEPLOYMENT_OVERVIEW.md        # デプロイ方法とワークフロー
├── architecture/                      # システムアーキテクチャ資料
│   └── SYSTEM_ARCHITECTURE.md        # Bank 1 と Bank 2 の構成比較
├── guides/                           # 手順ガイド
│   ├── LOCAL_DEPLOYMENT.md           # ローカルデプロイガイド
│   ├── AZURE_DEPLOYMENT.md           # Azure デプロイガイド
│   ├── TERRAFORM_ANSIBLE.md          # Terraform と Ansible の連携
│   ├── QUICKSTART.md                 # クイックスタート
│   ├── RANCHER_DESKTOP.md            # Rancher Desktop セットアップ
│   └── REACT_FRONTEND_GUIDE.md       # React フロントエンド開発ガイド
└── reference/                        # リファレンス資料
    ├── API_REFERENCE.md              # API エンドポイント仕様
    ├── BANKING_FEATURES.md           # 機能一覧
    ├── TESTING.md                    # テストガイド
    ├── TROUBLESHOOTING.md            # トラブルシューティング
    └── PDF_GENERATION.md             # PDF 生成ガイド
```

## 🎯 クイックナビゲーション

### IT 運用チーム向け
インフラの運用やデプロイを担当する場合は、次から読み始めるのがおすすめです。

1. **[Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)** - ローカルと Azure の違いを含むデプロイ全体像
2. **[Local Deployment Guide](guides/LOCAL_DEPLOYMENT.md)** - Docker を使ったローカルデプロイ
3. **[Azure Deployment Guide](guides/AZURE_DEPLOYMENT.md)** - Azure クラウドへのデプロイ
4. **[Terraform & Ansible Guide](guides/TERRAFORM_ANSIBLE.md)** - 2 つのツールの役割分担

### アーキテクト・開発者向け
システム理解や拡張を目的とする場合は、次が入口になります。

1. **[System Architecture](architecture/SYSTEM_ARCHITECTURE.md)** - Bank 1 と Bank 2 の構成比較
2. **[Banking Features](reference/BANKING_FEATURES.md)** - 機能一覧と説明
3. **[API Reference](reference/API_REFERENCE.md)** - API エンドポイントと利用方法
4. **[Testing Guide](reference/TESTING.md)** - システムのテスト方法

### まず動かしたい場合
とにかく起動したい場合は、次の順で見るのが最短です。

1. **[Quick Start Guide](guides/QUICKSTART.md)** - 最短の起動手順
2. **[Troubleshooting](reference/TROUBLESHOOTING.md)** - よくある問題と対処法

## 📖 ドキュメント説明

### 運用ドキュメント

#### [Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)
**対象読者**: IT 運用、DevOps エンジニア  
**目的**: デプロイ方法、ワークフロー、ツール連携の全体像をまとめる

**主な内容**:
- デプロイアーキテクチャ図
- ローカルと Azure の比較
- Terraform と Ansible の連携
- 運用手順
- コスト観点
- セキュリティ上の考慮点

### アーキテクチャ資料

#### [System Architecture](architecture/SYSTEM_ARCHITECTURE.md)
**対象読者**: アーキテクト、シニア開発者  
**目的**: システム構成と設計判断を深く理解する

**主な内容**:
- プロジェクトの進化（4 フェーズ）
- Bank 1（React + Flask）の構成
- Bank 2（Flask 単体）の構成
- 機能比較マトリクス
- 銀行間通信
- データフローとセキュリティ
- パフォーマンス特性
- 技術選定の背景

### デプロイガイド

#### [Local Deployment Guide](guides/LOCAL_DEPLOYMENT.md)
**対象読者**: 開発者、QA エンジニア  
**目的**: ローカルデプロイを手順化して説明する

**主な内容**:
- 前提条件と初期設定
- Docker Desktop / Rancher の設定
- Terraform によるデプロイ
- Ansible の設定
- 検証とテスト
- 運用スクリプト

#### [Azure Deployment Guide](guides/AZURE_DEPLOYMENT.md)
**対象読者**: クラウドエンジニア、DevOps  
**目的**: Azure へのデプロイを手順で説明する

**主な内容**:
- Azure 側の前提条件
- Container Registry の設定
- Azure Container Instances
- ストレージ設定
- ネットワークとセキュリティ
- コスト管理
- 監視とログ

#### [Terraform & Ansible Integration](guides/TERRAFORM_ANSIBLE.md)
**対象読者**: インフラエンジニア  
**目的**: Terraform と Ansible の連携を理解する

**主な内容**:
- なぜ両方使うのか
- Terraform の責務（WHAT）
- Ansible の責務（HOW）
- 連携パターン
- ベストプラクティス
- トラブルシューティング

#### [Quick Start Guide](guides/QUICKSTART.md)
**対象読者**: 全員  
**目的**: すばやく起動する

**主な内容**:
- 前提条件チェック
- ワンコマンドデプロイ
- 基本テスト
- クリーンアップ

#### [Rancher Desktop Guide](guides/RANCHER_DESKTOP.md)
**対象読者**: Rancher Desktop 利用者  
**目的**: Rancher Desktop でのセットアップと調整

**主な内容**:
- Rancher Desktop のインストール
- Banking Demo 向け設定
- Rancher 固有の問題の対処

#### [React Frontend Guide](guides/REACT_FRONTEND_GUIDE.md)
**対象読者**: フロントエンド開発者  
**目的**: Bank 1 の React フロントエンドを理解し、開発する

**主な内容**:
- React アプリの構造
- Material-UI コンポーネント
- フロントエンド開発フロー
- ビルドとデプロイ

### リファレンス資料

#### [API Reference](reference/API_REFERENCE.md)
**対象読者**: 開発者、API 利用者  
**目的**: API の完全な仕様を示す

**主な内容**:
- Bank 1 API エンドポイント
- Bank 2 API エンドポイント
- リクエスト / レスポンス形式
- エラーハンドリング
- 認証（今後の拡張）

#### [Banking Features](reference/BANKING_FEATURES.md)
**対象読者**: PM、開発者  
**目的**: 機能一覧と能力を整理する

**主な内容**:
- Bank 1 の機能（React UI）
- Bank 2 の機能（従来型 UI）
- セキュリティ機能
- 監査証跡
- 分析機能
- データベーススキーマ

#### [Testing Guide](reference/TESTING.md)
**対象読者**: QA エンジニア、開発者  
**目的**: テスト戦略と手順をまとめる

**主な内容**:
- ユニットテスト
- 統合テスト
- API テスト
- 負荷テスト
- テスト自動化

#### [Troubleshooting Guide](reference/TROUBLESHOOTING.md)
**対象読者**: 全員  
**目的**: よくある問題への対処法を示す

**主な内容**:
- Docker の問題
- Terraform の問題
- Ansible の問題
- Azure の問題
- ネットワークの問題
- コンテナの問題

#### [PDF Generation](reference/PDF_GENERATION.md)
**対象読者**: ドキュメント管理担当  
**目的**: PDF ドキュメントを生成する

**主な内容**:
- PDF 生成ツール
- Mermaid 図のレンダリング
- ドキュメントのコンパイル
- 配布方法

## 🚀 読み始めのおすすめルート

### Path 1: 開発者（ローカル開発）
```text
1. Quick Start Guide
2. Local Deployment Guide
3. API Reference
4. Testing Guide
```

### Path 2: DevOps エンジニア（本番デプロイ）
```text
1. Deployment Overview
2. System Architecture
3. Azure Deployment Guide
4. Terraform & Ansible Guide
5. Troubleshooting Guide
```

### Path 3: アーキテクト（システム理解）
```text
1. System Architecture
2. Deployment Overview
3. Banking Features
4. API Reference
```

### Path 4: QA エンジニア（テスト）
```text
1. Quick Start Guide
2. Testing Guide
3. API Reference
4. Troubleshooting Guide
```

## 📊 図の場所

アーキテクチャ図はすべて Mermaid で記述され、各ドキュメント内に埋め込まれています。

- **デプロイワークフロー**: [Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)
- **システムアーキテクチャ**: [System Architecture](architecture/SYSTEM_ARCHITECTURE.md)
- **データフロー**: [System Architecture](architecture/SYSTEM_ARCHITECTURE.md)
- **ネットワーク図**: [Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)

### 図の表示方法

Mermaid 図は次の環境で確認できます。

- **GitHub**: 自動レンダリング
- **VS Code**: "Markdown Preview Mermaid Support" 拡張
- **Online**: https://mermaid.live/
- **Documentation sites**: GitBook, Docusaurus など

## 🔄 ドキュメント保守

### バージョン履歴
- **v1.0** (2025-11-21): 初回の整理済みドキュメント構成
  - ルート直下のファイルを再整理
  - 包括的な図を追加
  - operations / architecture / guides / reference に分割

### 更新ルール
ドキュメントを更新するときは、次を守ってください。

1. コード変更に合わせて図も更新する
2. 適切なセクション（operations / architecture / guides / reference）に置く
3. 新規文書を追加したらこの索引も更新する
4. 体裁とスタイルを揃える

### ドキュメント担当
- **Operations**: IT Operations Team
- **Architecture**: Architecture Team
- **Guides**: DevOps Team
- **Reference**: Development Team

## 📞 サポート

質問や問題がある場合:

1. [Troubleshooting Guide](reference/TROUBLESHOOTING.md) を確認する
2. 該当セクションのドキュメントを確認する
3. GitHub issues を確認する
4. 必要なら担当チームに連絡する

## 🔗 外部リソース

- **Terraform Documentation**: https://www.terraform.io/docs
- **Ansible Documentation**: https://docs.ansible.com
- **Docker Documentation**: https://docs.docker.com
- **Azure Documentation**: https://docs.microsoft.com/azure
- **React Documentation**: https://react.dev
- **Flask Documentation**: https://flask.palletsprojects.com

---

**Last Updated**: 2025-11-21  
**Documentation Version**: 1.0
