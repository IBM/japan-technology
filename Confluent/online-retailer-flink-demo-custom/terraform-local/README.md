# Terraform Local - Confluent Cloud セットアップ

このディレクトリには、AWS依存なしでConfluent Cloudリソースをプロビジョニングするためのterraform設定が含まれています。

## 前提条件

1. **Confluent CLI** がインストールされ、ログイン済み
2. **Terraform** がインストール済み
3. **Confluent Cloud API Key** (OrganizationAdmin権限)

## セットアップ手順

### 1. Confluent Cloud API Keyの生成

```bash
# Confluent Cloudにログイン
confluent login

# Cloud API Keyを作成
confluent api-key create --resource cloud --description "Local Workshop API Key"

# 出力を保存:
# API Key: XXXXXXXXXXXXXX
# API Secret: YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

### 2. Terraform変数の設定

```bash
# テンプレートをコピー
cp terraform.tfvars.template terraform.tfvars

# terraform.tfvarsをAPI認証情報で編集
# confluent_cloud_api_key    = "your-api-key"
# confluent_cloud_api_secret = "your-api-secret"
```

### 3. Confluent Cloudリソースのデプロイ

```bash
# Terraformの初期化
terraform init

# プランの確認
terraform plan

# 設定の適用（約5分）
terraform apply -auto-approve
```

### 4. デプロイの確認

```bash
# すべての出力を表示
terraform output

# 接続情報を表示
terraform output connection_info
```

`.env.local`ファイルがプロジェクトルートディレクトリに自動生成されます。

## 作成されるリソース

- **Confluent Environment** (Stream Governance Advanced付き)
- **Kafka Cluster** (Standard、Single-Zone)
- **Schema Registry** (環境と共に自動プロビジョニング)
- **Flink Compute Pool** (最大20 CFU)
- **Service Account** (EnvironmentAdminロール付き)
- **API Keys** (Kafka、Schema Registry、Flink用)
- **ACLs** (トピックの読み書き作成、コンシューマーグループアクセス)
- **Topics**: `payments`, `error-payments`
- **Schema**: `payments-value` (Avro)

## 次のステップ

Terraform完了後:

1. `.env.local`ファイルがプロジェクトルートに自動作成されます
2. Docker環境を起動:
   ```bash
   cd ..
   docker-compose -f docker-compose.local.yml --env-file .env.local up -d
   ```
3. Debezium connectorを登録:
   ```bash
   ./scripts/register-debezium-connector.sh
   ```

## クリーンアップ

```bash
# すべてのConfluent Cloudリソースを削除
terraform destroy -auto-approve
```

## トラブルシューティング

### API Key権限エラー

権限エラーが発生した場合、API Keyが`OrganizationAdmin`ロールを持っていることを確認:

```bash
# 現在ログインしているユーザーを確認
confluent iam user list

# または、ログイン情報を確認
confluent login --save
```

### スキーマファイルが見つからない

スキーマファイルパスは相対パス: `../terraform/schemas/avro/payments-value.avsc`

`terraform-local/`ディレクトリからTerraformを実行していることを確認してください。

### 環境が既に存在する

リソースを再作成する必要がある場合、まず既存のものを削除:

```bash
terraform destroy -auto-approve
terraform apply -auto-approve