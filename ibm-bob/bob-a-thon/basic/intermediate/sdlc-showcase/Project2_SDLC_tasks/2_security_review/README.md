# Banking Demo - モダンバンキングアプリケーション

## 🏦 概要

このプロジェクトは、Bob IDE のさまざまな機能や能力を紹介するための、
**本番品質を意識したデモ用バンキングアプリケーション** です。
現実的な金融アプリのシナリオを通じて、DevOps、クラウドデプロイ、
フルスタック開発、セキュリティレビューの流れを見せられる構成になっています。

このプロジェクトには、アーキテクチャとデプロイ方法が異なる 2 つの銀行アプリが含まれています。

### 主なポイント

- 🎨 **Bank 1 (Savings)**: React + Material-UI フロントエンドと Flask バックエンドを持つモダン構成
- 📊 **Bank 2 (Investment)**: サーバーサイドレンダリング中心の伝統的な Flask アプリ
- ☁️ **デュアルデプロイ**: ローカル Docker と Azure クラウドの両方に対応
- 🔧 **DevOps 連携**: Terraform と Ansible を組み合わせた構成
- 🔒 **エンタープライズセキュリティ**: 監査証跡、パラメータ化クエリ、データ分離
- 📈 **分析機能**: Plotly による対話的な可視化と支出分析

## 🚀 クイックスタート

### ワンコマンドデプロイ

```bash
# Clone repository
git clone <repository-url>
cd banking-demo

# Deploy locally (requires Docker, Terraform, Ansible)
./deploy.sh

# Or deploy to Azure
./deploy.sh --cloud azure
```

**アクセス先:**
- Bank 1 (Savings): http://localhost:5001
- Bank 2 (Investment): http://localhost:5002

### デプロイ後に得られるもの

デプロイが完了すると、次の状態になります。

- ✅ 2 つの銀行アプリが動作する
- ✅ 永続データストレージが使える
- ✅ 銀行間振込ができる
- ✅ 監視・バックアップ用スクリプトが使える
- ✅ ヘルスチェックエンドポイントが使える
- ✅ 監査ログが記録される

## 📚 ドキュメント

### 🎯 まず読むもの

- **[Quick Start Guide](docs/guides/QUICKSTART.md)** - 5 分で起動するためのガイド
- **[Documentation Index](docs/README.md)** - ドキュメント全体の索引

### 👨‍💼 IT 運用担当向け

- **[Deployment Overview](docs/operations/DEPLOYMENT_OVERVIEW.md)** - デプロイ方法とワークフローの概要
- **[Local Deployment Guide](docs/guides/LOCAL_DEPLOYMENT.md)** - Docker を使ったローカルデプロイ
- **[Azure Deployment Guide](docs/guides/AZURE_DEPLOYMENT.md)** - Azure へのデプロイ
- **[Terraform & Ansible Guide](docs/guides/TERRAFORM_ANSIBLE.md)** - 2 つのツールの連携方法

### 🏗️ アーキテクト・開発者向け

- **[System Architecture](docs/architecture/SYSTEM_ARCHITECTURE.md)** - Bank 1 と Bank 2 の構成比較
- **[API Reference](docs/reference/API_REFERENCE.md)** - API の完全な仕様
- **[Banking Features](docs/reference/BANKING_FEATURES.md)** - 機能一覧
- **[Testing Guide](docs/reference/TESTING.md)** - テスト方針と実行方法

### 🔧 トラブルシューティング

- **[Troubleshooting Guide](docs/reference/TROUBLESHOOTING.md)** - よくある問題と対処法

## 🏗️ アーキテクチャ概要

### システム構成

```
┌─────────────────────────────────────────────────────────────┐
│                    Banking Demo System                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌────────────────────┐         ┌────────────────────┐      │
│  │   Bank 1 (Savings) │         │ Bank 2 (Investment)│      │
│  │                    │◄───────►│                    │      │
│  │  React Frontend    │         │  Flask Traditional │      │
│  │  Flask Backend     │         │  Server-side HTML  │      │
│  │  Material-UI       │         │  Simple Forms      │      │
│  │  Port 5001         │         │  Port 5002         │      │
│  └────────────────────┘         └────────────────────┘      │
│                                                               │
│  Deployment Options:                                         │
│  • Local: Docker Desktop/Rancher                            │
│  • Cloud: Azure Container Instances                         │
│                                                               │
│  Orchestration:                                              │
│  • Terraform: Infrastructure provisioning                    │
│  • Ansible: Application configuration                        │
└─────────────────────────────────────────────────────────────┘
```

### Bank 1 と Bank 2 の比較

| 項目 | Bank 1 (Savings) | Bank 2 (Investment) |
|---------|------------------|---------------------|
| **フロントエンド** | React + Material-UI | 伝統的な HTML |
| **ユーザー体験** | モダンで対話的 | シンプルで機能重視 |
| **ビルド方式** | Multi-stage Docker | Single-stage Docker |
| **コンテナサイズ** | 約 200MB | 約 150MB |
| **用途** | モダン Web アプリのデモ | 伝統的アプリのデモ |

詳細は [System Architecture](docs/architecture/SYSTEM_ARCHITECTURE.md) を参照してください。

## 🎯 プロジェクトの進化

このプロジェクトは次の 4 フェーズを経て発展してきました。

1. **Phase 1**: 基本機能を持つ 2 つの Python Flask 銀行アプリ
2. **Phase 2**: Terraform + Ansible によるデプロイ統合
3. **Phase 3**: Bank 1 をモダンな React UI に刷新
4. **Phase 4**: Azure クラウドデプロイを追加

## 💻 主な機能

### バンキング機能

- ✅ **顧客口座管理**: 複数顧客と個別口座を管理
- ✅ **残高管理**: リアルタイムな残高追跡
- ✅ **取引**: 入金、出金、振込
- ✅ **銀行間振込**: 2 行間でシームレスに送金
- ✅ **取引履歴**: 完全な監査証跡
- ✅ **分析機能**: グラフを使った支出・投資分析
- ✅ **監査ログ**: SHA-256 ハッシュ付きの不変 JSONL ログ

### セキュリティ機能

- ✅ **パラメータ化クエリ**: SQL Injection を防止
- ✅ **データ分離**: 顧客データを分離管理
- ✅ **スキーマ検証**: 実行後のデータ検証
- ✅ **監査証跡**: コンプライアンス向けの包括的ログ
- ✅ **トランザクションロールバック**: 失敗時は自動で巻き戻し

### DevOps 機能

- ✅ **Infrastructure as Code**: Terraform による構成管理
- ✅ **Configuration Management**: Ansible によるセットアップ
- ✅ **永続ストレージ**: Docker Volume または Azure File Share
- ✅ **ヘルスチェック**: 自動監視に対応
- ✅ **バックアップ**: 自動バックアップスクリプト
- ✅ **ログローテーション**: ディスク逼迫を防止

## 🛠️ 技術スタック

### Bank 1 (Savings Bank)
- **Frontend**: React 18, Material-UI, Vite
- **Backend**: Python Flask 3.0
- **Database**: SQLite
- **Visualization**: Plotly
- **Container**: Docker (multi-stage build)

### Bank 2 (Investment Bank)
- **Backend**: Python Flask 3.0
- **Templates**: Jinja2
- **Database**: SQLite
- **Visualization**: Plotly
- **Container**: Docker (single-stage build)

### Infrastructure & DevOps
- **Orchestration**: Terraform 1.0+
- **Configuration**: Ansible 2.9+
- **Containers**: Docker
- **Cloud**: Azure (optional)
- **Networking**: Docker Bridge / Azure VNet
- **Storage**: Docker Volumes / Azure File Shares

## 📊 デプロイ方法

### ローカルデプロイ
- **Platform**: Docker Desktop または Rancher Desktop
- **Cost**: 無料（ローカルリソースを利用）
- **Use Case**: 開発、テスト、デモ
- **Access**: localhost のみ
- **Tools**: Terraform + Ansible

### Azure デプロイ
- **Platform**: Azure Container Instances
- **Cost**: 約 $66/月
- **Use Case**: 本番、外部公開デモ
- **Access**: インターネット公開
- **Tools**: Terraform のみ

詳細は [Deployment Overview](docs/operations/DEPLOYMENT_OVERVIEW.md) を参照してください。

## 💻 利用例

### API テスト

```bash
# Get customer balance
curl -X POST http://localhost:5001/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'

# View transactions
curl -X POST http://localhost:5001/api/transactions \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "limit": 10}'

# Transfer between banks
curl -X POST http://localhost:5001/api/transfer \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 500.0}'
```

### 運用操作

```bash
# Monitor health (created by Ansible)
/tmp/monitor_bank1.sh
/tmp/monitor_bank2.sh

# Create backups
/tmp/backup_banks.sh

# Rotate logs
/tmp/rotate_logs.sh

# View container logs
docker logs bank1-savings
docker logs bank2-investment

# View Terraform state
cd terraform && terraform show

# Re-run Ansible configuration
cd ansible && ansible-playbook playbook.yml
```

### クリーンアップ

```bash
# Destroy all infrastructure
cd terraform && terraform destroy -auto-approve
```

## 🎓 学習目標

このプロジェクトでは次の内容を学べます。

1. **モダン Web 開発**: React + Material-UI フロントエンド
2. **フルスタック構成**: フロントエンドとバックエンドの分離
3. **Infrastructure as Code**: Terraform による構成管理
4. **Configuration Management**: Ansible によるセットアップ
5. **コンテナオーケストレーション**: Docker ネットワークと永続ボリューム
6. **クラウドデプロイ**: Azure Container Instances
7. **DevOps 連携**: Terraform と Ansible の併用
8. **セキュリティのベストプラクティス**: パラメータ化クエリ、監査証跡
9. **API 設計**: RESTful JSON API
10. **データベース設計**: 適切なスキーマを持つ SQLite

## 🐛 トラブルシューティング

よくある問題と対処法は次を参照してください。
- **[Troubleshooting Guide](docs/reference/TROUBLESHOOTING.md)** - 包括的なトラブルシューティング
- **[Quick Start Guide](docs/guides/QUICKSTART.md)** - 基本セットアップで詰まりやすい点

よく使う確認コマンド:
```bash
# Docker not running
docker info || open -a Docker

# Port conflicts
lsof -i :5001
lsof -i :5002

# Terraform state issues
cd terraform && rm -rf .terraform && terraform init

# View logs
docker logs bank1-savings
docker logs bank2-investment
```

## 📝 プロジェクト構成

```
banking-demo/
├── README.md                     # このファイル - プロジェクト概要
├── deploy.sh                     # 統合デプロイスクリプト
│
├── docs/                         # 📚 ドキュメント
│   ├── README.md                # ドキュメント索引
│   ├── operations/              # IT 運用ガイド
│   ├── architecture/            # システムアーキテクチャ
│   ├── guides/                  # ステップ別ガイド
│   └── reference/               # リファレンス資料
│
├── bank1-savings/               # Bank 1 - モダン React アプリ
│   ├── app.py                  # Flask バックエンド
│   ├── Dockerfile              # Multi-stage build
│   ├── requirements.txt        # Python 依存関係
│   └── frontend/               # React フロントエンド
│       ├── src/
│       │   ├── App.jsx
│       │   ├── components/
│       │   └── services/
│       └── package.json
│
├── bank2-investment/            # Bank 2 - 伝統的な Flask アプリ
│   ├── app.py                  # Flask アプリケーション
│   ├── Dockerfile              # Single-stage build
│   └── requirements.txt        # Python 依存関係
│
├── terraform/                   # ローカルデプロイ用（Docker）
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── terraform-azure/             # Azure デプロイ用（ACI）
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── ansible/                     # 構成管理
│   ├── playbook.yml
│   ├── requirements.yml
│   └── roles/
│
└── diagrams/                    # アーキテクチャ図
    └── architecture.md          # Mermaid 図
```

## 🤝 コントリビュート

これは学習・デモ用のプロジェクトです。次のような使い方を歓迎します。

- Fork して試す
- 新機能を追加する
- ドキュメントを改善する
- フィードバックを共有する
- 問題を報告する

## 📄 ライセンス

このプロジェクトは教育およびデモ用途を目的としています。

## 🙏 謝辞

- **Technologies**: React, Material-UI, Flask, SQLite, Plotly, Terraform, Ansible, Docker, Azure
- **Purpose**: 実運用に近い DevOps とモダン Web 開発を示すためのデモ
- **Audience**: 開発者、DevOps エンジニア、アーキテクト、学生

## 📞 サポート

- **Documentation**: 全体像は [docs/README.md](docs/README.md) を参照
- **Issues**: [Troubleshooting Guide](docs/reference/TROUBLESHOOTING.md) を確認
- **Questions**: 関連するドキュメントを確認

---

**デプロイを始めるには**

```bash
./deploy.sh                # ローカルデプロイ
./deploy.sh --cloud azure  # Azure デプロイ
```

**ドキュメントを見る**: [docs/README.md](docs/README.md)

🚀 **Happy Banking!**
