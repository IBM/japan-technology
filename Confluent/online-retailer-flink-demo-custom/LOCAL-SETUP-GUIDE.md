# ローカル環境構築ガイド（AWS不要版）

このガイドでは、オリジナルのワークショップリソースを変更せずに、Confluent CloudとローカルのDocker環境で検証できる環境を構築する手順を説明します。

## 📋 前提条件

| 要件 | 説明 |
|------|------|
| **Confluent Cloud アカウント** | [無料トライアル](https://www.confluent.io/get-started/)で開始可能 |
| **Confluent CLI** | API Key生成とリソース管理用 |
| **Terraform** | Confluent Cloudリソースの自動プロビジョニング用 |
| **Docker** | ローカルでPostgreSQLとアプリケーションを実行 |
| **Docker Compose** | 複数コンテナの管理用 |
| **Git** | リポジトリのクローン用 |

### インストールコマンド

**macOS:**
```bash
brew tap hashicorp/tap
brew tap confluentinc/tap
brew install git hashicorp/tap/terraform confluentinc/tap/confluent
```

**Windows (PowerShell):**
```powershell
winget install -e --id Git.Git
winget install -e --id HashiCorp.Terraform
winget install -e --id Confluent.ConfluentCLI
```

## 🏗️ アーキテクチャ概要

### オリジナル構成（AWS使用）
```
┌─────────────────────────────────────────────────────────────┐
│ AWS                                                          │
│  ├─ ECS (Fargate)                                           │
│  │   ├─ Payment Producer App                                │
│  │   └─ PostgreSQL Data Feeder                              │
│  ├─ EC2 PostgreSQL Instance                                 │
│  ├─ KMS (CSFLE暗号化キー)                                   │
│  ├─ S3 (Tableflow用ストレージ)                              │
│  └─ Glue Data Catalog + Athena                              │
└─────────────────────────────────────────────────────────────┘
                        ↓↑
┌─────────────────────────────────────────────────────────────┐
│ Confluent Cloud                                              │
│  ├─ Kafka Cluster                                           │
│  ├─ Schema Registry (CSFLE + DQR)                           │
│  ├─ Flink Compute Pool                                      │
│  ├─ PostgreSQL CDC Connector (Managed)                      │
│  └─ Tableflow (Iceberg)                                     │
└─────────────────────────────────────────────────────────────┘
```

### ローカル構成（AWS不要）
```
┌─────────────────────────────────────────────────────────────┐
│ ローカル Docker 環境                                         │
│  ├─ PostgreSQL Container (WAL有効化)                        │
│  ├─ Debezium Connect Container (CDC)                        │
│  ├─ Payment Producer App Container                          │
│  └─ PostgreSQL Data Feeder Container                        │
└─────────────────────────────────────────────────────────────┘
                        ↓↑
┌─────────────────────────────────────────────────────────────┐
│ Confluent Cloud (Terraform管理)                             │
│  ├─ Environment                                             │
│  ├─ Kafka Cluster (Standard)                               │
│  ├─ Schema Registry                                         │
│  ├─ Flink Compute Pool                                      │
│  └─ Service Accounts & ACLs                                 │
└─────────────────────────────────────────────────────────────┘
```

## 📝 実装計画

### 検証可能な機能
- ✅ Confluent Cloud環境（Terraform自動構築）
- ✅ PostgreSQL CDC → Kafka（Debezium経由）
- ✅ Payment Producer → Kafka
- ✅ Data Quality Rules (DQR)
- ✅ Flink SQL (joins, deduplication, aggregations)
- ✅ Schema Registry

### スキップする機能
- ❌ CSFLE (AWS KMS依存)
- ❌ Tableflow + Athena/Snowflake (S3/Glue依存)

## 🚀 セットアップ手順

### ステップ1: リポジトリのクローン

```bash
git clone git@github.ibm.com:ISE-MQ/online-retailer-flink-demo-custom.git
cd online-retailer-flink-demo-custom
```

### ステップ2: Confluent CLIのセットアップ

```bash
# Confluent CLIにログイン
confluent login

# 現在のユーザーを確認
confluent iam user list

# Cloud API Keyを作成（OrganizationAdmin権限）
confluent api-key create --resource cloud --description "Local Workshop API Key"

# 出力されたAPI KeyとSecretを記録
# API Key: XXXXXXXXXXXXXX
# API Secret: YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

### ステップ3: Terraform変数の設定

```bash
# terraform-localディレクトリに移動
cd terraform-local

# テンプレートファイルをコピーしてterraform.tfvarsを作成
cp terraform.tfvars.template terraform.tfvars

# terraform.tfvarsを編集（ステップ2で取得したAPI Keyを設定）
# macOS/Linux
nano terraform.tfvars
# または
vi terraform.tfvars

# Windows
notepad terraform.tfvars
```

`terraform.tfvars`ファイルの内容を編集:

```hcl
# Confluent Cloud API Key (ステップ2で生成したもの)
confluent_cloud_api_key    = "your-cloud-api-key"
confluent_cloud_api_secret = "your-cloud-api-secret"

# リソース名のプレフィックス
prefix = "local-workshop"

# Confluent Cloudのリージョン
cloud_region = "us-east-1"  # 最寄りのリージョンに変更可能
```

### ステップ4: Terraformでconfluent Cloud環境を構築

```bash
cd terraform-local

# Terraformの初期化
terraform init

# プランの確認
terraform plan

# リソースの作成（約5分）
# 注意: .env.localファイルが自動生成されます
terraform apply -auto-approve

# 出力情報を確認
terraform output
```

Terraformが以下のリソースを作成します:
- Confluent Environment
- Kafka Cluster (Standard)
- Schema Registry
- Flink Compute Pool
- Service Account & API Keys
- ACLs
- **`.env.local`ファイル（プロジェクトルートに自動生成）**

### ステップ5: 環境変数の確認

Terraformが自動生成した`.env.local`ファイルを確認:

```bash
cd ..

# 環境変数ファイルの確認
cat .env.local

# 以下のような内容が含まれています:
# BOOTSTRAP_SERVERS=pkc-xxxxx.us-east-1.aws.confluent.cloud:9092
# KAFKA_API_KEY=XXXXXXXXXXXXXX
# KAFKA_API_SECRET=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
# SCHEMA_REGISTRY_URL=https://psrc-xxxxx.us-east-1.aws.confluent.cloud
# SR_API_KEY=XXXXXXXXXXXXXX
# SR_API_SECRET=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

> **注意**: `.env.local`ファイルは`terraform apply`実行時に自動生成されるため、手動で作成する必要はありません。

### ステップ6: Dockerイメージのビルドと起動

**重要**: 初回起動時は、Debezium Connectのカスタムイメージをビルドする必要があります。

#### Debeziumバージョンの互換性について

このプロジェクトでは、Confluent Platform 7.5.0 (Kafka 3.5系相当) と互換性のある **Debezium 2.4.2** を使用しています。

**互換性マトリックス:**
| コンポーネント | バージョン | Kafka互換性 |
|---------------|-----------|------------|
| Confluent Platform | 7.5.0 | Kafka 3.5系 |
| Debezium Connector | 2.4.2 | Kafka 3.5系対応 ✅ |
| Debezium 3.x系 | 3.2.6+ | Kafka 3.7+対応 ❌ |

> **注意**: Debezium 3.x系（latest）は Kafka 3.7+ 向けで、Confluent Platform 7.5.0 とは互換性がありません。プラグインがインストールされても認識されない問題が発生します。

#### ビルドと起動

```bash
# 1. Debezium Connectイメージをビルド（初回のみ、数分かかります）
docker-compose -f docker-compose.local.yml build debezium-connect

# 2. すべてのコンテナを起動
docker-compose -f docker-compose.local.yml --env-file .env.local up -d

# 3. ログ確認
docker-compose -f docker-compose.local.yml logs -f

# 個別のログ確認
docker-compose -f docker-compose.local.yml logs -f postgres
docker-compose -f docker-compose.local.yml logs -f data-feeder
docker-compose -f docker-compose.local.yml logs -f debezium-connect
docker-compose -f docker-compose.local.yml logs -f payment-producer
```

> **重要**:
> - **初回起動時**: `docker-compose build debezium-connect`でDebeziumプラグインを含むカスタムイメージをビルドします（数分かかります）
> - PostgreSQLコンテナは初回起動時に`init-schema.sql`を自動実行してテーブルを作成します
> - Debezium Connectコンテナは、ビルド済みのイメージを使用するため、起動後すぐに利用可能です
>
> 以下のテーブルが作成されます:
> - `addresses` - 住所情報
> - `customers` - 顧客情報
> - `products` - 商品情報
> - `orders` - 注文情報
> - `order_items` - 注文明細

#### PostgreSQLテーブルの確認

```bash
# PostgreSQLに接続
docker exec -it local-postgres psql -U postgres -d onlinestoredb

# テーブル一覧を表示
\dt

# 各テーブルのレコード数を確認
SELECT COUNT(*) FROM addresses;
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM order_items;

# 終了
\q
```

期待される結果:
- `addresses`: 初期データ投入後に件数が表示される
- `customers`: 50件
- `products`: 290件
- `orders`: 初期データ + 継続的に増加
- `order_items`: 初期データ + 継続的に増加

> **注意**:
> - Payment Producerコンテナには、ダミーのAWS認証情報（`AWS_ACCESS_KEY_ID`と`AWS_SECRET_ACCESS_KEY`）が設定されています。これらは`ClientsUtils.java`の検証を通過するために必要ですが、CSFLEを使用しないため実際には使用されません。
> - Payment ProducerとData Feederは継続的にデータを生成し続けます。検証が完了したら、以下のコマンドで停止できます。

#### データ生成コンテナの制御

**Payment Producer（Kafkaへ直接送信）**:
```bash
# Payment Producerを停止（Paymentsメッセージ送信を停止）
docker-compose -f docker-compose.local.yml stop payment-producer

# Payment Producerを再開（Paymentsメッセージ送信を再開）
docker-compose -f docker-compose.local.yml start payment-producer

# Payment Producerのログをリアルタイムで確認
docker-compose -f docker-compose.local.yml logs -f payment-producer
```

**Data Feeder（PostgreSQL経由でCDC）**:
```bash
# Data Feederを停止（Orders/OrderItemsデータ生成を停止）
docker-compose -f docker-compose.local.yml stop data-feeder

# Data Feederを再開（Orders/OrderItemsデータ生成を再開）
docker-compose -f docker-compose.local.yml start data-feeder

# Data Feederのログをリアルタイムで確認
docker-compose -f docker-compose.local.yml logs -f data-feeder
```

**両方を同時に制御**:
```bash
# 両方のデータ生成を停止
docker-compose -f docker-compose.local.yml stop payment-producer data-feeder

# 両方のデータ生成を再開
docker-compose -f docker-compose.local.yml start payment-producer data-feeder
```

### ステップ7: Debezium PostgreSQL Connectorの設定

Debezium Connectコンテナが起動したら（約30秒）、PostgreSQL CDC Connectorを登録します。

#### プラグインの確認

```bash
# Kafka Connectが起動したか確認（約30秒待つ）
curl http://localhost:8083/

# プラグインが正しくインストールされたか確認
curl http://localhost:8083/connector-plugins | jq '.[] | select(.class | contains("PostgresConnector"))'

# 以下のような出力が表示されればOK:
# {
#   "class": "io.debezium.connector.postgresql.PostgresConnector",
#   "type": "source",
#   "version": "2.4.2.Final"
# }
```

> **注意**:
> - Debeziumプラグインは、Dockerイメージのビルド時に既にインストールされているため、コンテナ起動後すぐに利用可能です
> - バージョンは **2.4.2.Final** であることを確認してください（Confluent Platform 7.5.0との互換性のため）

#### Connectorの登録

```bash
# 環境変数を読み込み
source .env.local

# Connectorを登録（スクリプトが環境変数を自動展開）
./scripts/register-debezium-connector.sh

# Connector状態を確認
curl http://localhost:8083/connectors/postgres-cdc-source/status | jq

# 期待される出力:
# {
#   "name": "postgres-cdc-source",
#   "connector": {
#     "state": "RUNNING",
#     "worker_id": "debezium-connect:8083"
#   },
#   "tasks": [
#     {
#       "id": 0,
#       "state": "RUNNING",
#       "worker_id": "debezium-connect:8083"
#     }
#   ],
#   "type": "source"
# }
```

#### CDCトピックの確認

Connectorが正常に動作すると、PostgreSQLのテーブルごとにKafkaトピックが自動作成されます。

**Confluent Cloud CLIで確認:**

```bash
# Kafka Cluster IDを取得
export KAFKA_CLUSTER_ID=$(terraform -chdir=terraform-local output -raw kafka_cluster_id)
export ENVIRONMENT_ID=$(terraform -chdir=terraform-local output -raw environment_id)

# トピック一覧を表示
confluent kafka topic list --cluster $KAFKA_CLUSTER_ID --environment $ENVIRONMENT_ID

# CDCトピックのみをフィルタ（shiftleftプレフィックス）
confluent kafka topic list --cluster $KAFKA_CLUSTER_ID --environment $ENVIRONMENT_ID | grep shiftleft

# 期待されるトピック:
# shiftleft.public.addresses
# shiftleft.public.customers
# shiftleft.public.order_items
# shiftleft.public.orders
# shiftleft.public.products
```

**特定のトピックの詳細を確認:**

```bash
# Customersトピックの詳細
confluent kafka topic describe shiftleft.public.customers \
  --cluster $KAFKA_CLUSTER_ID \
  --environment $ENVIRONMENT_ID

# Customersトピックのメッセージ数を確認（最新10件を表示）
confluent kafka topic consume shiftleft.public.customers \
  --cluster $KAFKA_CLUSTER_ID \
  --environment $ENVIRONMENT_ID \
  --from-beginning \
  --max-messages 10
```

**Confluent Cloud UIで確認:**

1. Confluent Cloud UIにログイン
2. Environment → Cluster → Topics
3. 以下のトピックが作成されていることを確認:
   - `shiftleft.public.addresses`
   - `shiftleft.public.customers`
   - `shiftleft.public.order_items`
   - `shiftleft.public.orders`
   - `shiftleft.public.products`
   - `payments` (Payment Producerから)
   - `error-payments` (DQR設定後)

> **注意**:
> - CDCトピックは、Connectorが起動してから数秒～数十秒で作成されます
> - Data Feederが継続的にデータを投入しているため、トピックには常に新しいメッセージが追加されます
> - トピック名は `{database.server.name}.{schema}.{table}` の形式です（例: `shiftleft.public.customers`）

### ステップ8: Schemaの登録

Payment Producerアプリが起動すると、自動的にスキーマが登録されます。

確認方法:
```bash
# Confluent CLIでスキーマを確認
confluent schema-registry schema list --environment $(terraform -chdir=terraform-local output -raw environment_id)

# または、Confluent Cloud UIで確認
# Schema Registry > Schemas > payments-value
```

### ステップ9: Data Quality Ruleの設定

Confluent Cloud UIまたはCLIでData Quality Ruleを追加:

**UIの場合:**
1. Schema Registryで`payments-value`スキーマを選択
2. **Evolve**をクリック
3. **Rules**タブで**Add rules**
4. Data Quality Ruleを追加:
   - **Category**: `Data quality rule`
   - **Rule name**: `validateConfirmationCode`
   - **Description**: Validate that the confirmation code is uppercase alphanumeric and only 8 characters
   - **Rule expression**: `message.confirmation_code.matches('^[A-Z0-9]{8}$')`
   - **On failure**: `DLQ`
   - **Parameters**:
     - `dlq.topic` = `error-payments`
     - `dlq.auto.flush` = `true`
5. **Add** → **Save**

**CLIの場合:**
```bash
# スクリプトを使用してDQRを登録
./scripts/register-data-quality-rule.sh
```

### ステップ10: Flink SQLでの検証

Confluent CloudのFlink SQL Workspaceで以下を実行:

```sql
-- CDC トピックの確認
SHOW TABLES;

-- Customers テーブルのクエリ（Debeziumのトピック名）
SELECT * FROM `shiftleft.public.customers` LIMIT 10;

-- Orders テーブル
SELECT * FROM `shiftleft.public.orders` LIMIT 10;

-- Payments トピックのクエリ
SELECT * FROM payments LIMIT 10;

-- エラーメッセージの確認
SELECT * FROM `error-payments` LIMIT 10;
```

### ステップ11: 重複排除とJoinの実装

```sql
-- 重複排除テーブルの作成
CREATE TABLE deduplicated_payments AS
SELECT 
  order_id,
  customer_id,
  amount,
  cc_number,
  confirmation_code,
  order_ts
FROM (
  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY order_id 
      ORDER BY $rowtime
    ) AS row_num
  FROM payments
)
WHERE row_num = 1;

-- Completed Orders (Interval Join)
CREATE TABLE completed_orders AS
SELECT 
  o.OrderID,
  o.CustomerID,
  o.OrderDate,
  p.amount,
  p.confirmation_code
FROM `shiftleft.public.orders` o
INNER JOIN deduplicated_payments p
  ON o.OrderID = p.order_id
WHERE p.$rowtime BETWEEN o.$rowtime AND o.$rowtime + INTERVAL '1' HOUR;

-- 結果の確認
SELECT * FROM completed_orders LIMIT 10;
```

## 🔍 検証項目

### ✅ 動作確認チェックリスト

- [ ] Confluent Cloud環境がTerraformで作成されている
- [ ] PostgreSQLコンテナが起動している
- [ ] Data Feederがデータを投入している
- [ ] Debezium Connectが起動している
- [ ] PostgreSQL CDC Connectorが登録されている
- [ ] CDC トピック（`shiftleft.public.*`）にデータが流れている
- [ ] Payment Producerがメッセージを送信している
- [ ] `payments`トピックにメッセージが届いている
- [ ] Data Quality Ruleが動作し、無効なメッセージが`error-payments`に送られている
- [ ] Flink SQLでCDCテーブルをクエリできる
- [ ] Flink SQLでJoinとDeduplicationが動作する

### 確認コマンド

```bash
# Terraformリソースの確認
cd terraform-local
terraform show

# コンテナの状態確認
cd ..
docker-compose -f docker-compose.local.yml ps

# PostgreSQLに接続してデータ確認
docker exec -it local-postgres psql -U postgres -d onlinestoredb
# \dt  -- テーブル一覧
# SELECT COUNT(*) FROM customers;
# SELECT COUNT(*) FROM orders;

# Debezium Connectorの状態確認
curl http://localhost:8083/connectors/postgres-cdc-source/status | jq

# Confluent Cloudでトピック確認（CLI）
confluent kafka topic list --cluster $(terraform -chdir=terraform-local output -raw kafka_cluster_id)

# または、Confluent Cloud UIで確認:
# - shiftleft.public.customers
# - shiftleft.public.orders
# - shiftleft.public.products
# - shiftleft.public.order_items
# - shiftleft.public.addresses
# - payments
# - error-payments
```

## 🚫 制限事項

### スキップされる機能

1. **CSFLE (Client-Side Field Level Encryption)**
   - AWS KMS依存のため、ローカル環境では実装困難
   - 代替: DQRのみで検証
   - **重要**: Payment Producerアプリは起動時にAWS認証情報を要求しますが、`docker-compose.local.yml`でダミー値を設定済みです。これらの認証情報は実際には使用されません。

2. **Tableflow + Iceberg**
   - AWS S3/Glue/Athena依存
   - 代替: Flink SQLの結果をKafkaトピックに出力して確認

3. **Snowflake統合**
   - Tableflow依存のため利用不可

### 動作する機能

- ✅ Confluent Cloud環境（Terraform管理）
- ✅ PostgreSQL CDC (Debezium経由)
- ✅ Kafka Producer (Payments)
- ✅ Schema Registry
- ✅ Data Quality Rules (DQR)
- ✅ Flink SQL (全機能)
- ✅ Stream Processing (joins, aggregations, deduplication)

### Debezium vs Confluent Cloud CDC Connectorの違い

| 機能 | Debezium (ローカル) | Confluent Cloud CDC |
|------|---------------------|---------------------|
| トピック名 | `prefix.schema.table` | `prefix.schema.table` |
| スキーマ形式 | Avro (設定可能) | Avro |
| 管理 | 手動（Kafka Connect） | フルマネージド |
| モニタリング | 手動 | Confluent Cloud UI |
| スケーリング | 手動 | 自動 |

## 🛠️ トラブルシューティング

### Terraform apply が失敗する

**問題**: API Key権限エラー

**解決策**:
```bash
# Confluent CLIで現在のユーザーを確認
confluent iam user list

# OrganizationAdmin権限を持つAPI Keyを使用していることを確認
# 必要に応じて新しいAPI Keyを作成
confluent api-key create --resource cloud --description "Admin API Key"
```

### Debezium Connectが起動しない

**問題1**: Confluent Cloudへの接続エラー

**解決策**:
```bash
# ログ確認
docker-compose -f docker-compose.local.yml logs debezium-connect

# 環境変数の確認
cat .env.local

# Terraformの出力を再確認
cd terraform-local
terraform output
```

**問題2**: Debeziumプラグインがインストールされていない

**症状**:
```bash
curl http://localhost:8083/connector-plugins | jq '.[] | select(.class | contains("PostgresConnector"))'
# 何も出力されない
```

**原因**:
1. Dockerイメージがビルドされていない、または古いイメージを使用している
2. **互換性問題**: Debezium 3.x系を使用している（Confluent Platform 7.5.0と互換性なし）

**解決策**:
```bash
# 1. 既存のコンテナを停止・削除
docker-compose -f docker-compose.local.yml down

# 2. Dockerfileを確認（Debezium 2.4.2を使用していることを確認）
cat code/debezium-connect/Dockerfile
# 以下の行があることを確認:
# RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:2.4.2

# 3. Debezium Connectイメージを再ビルド（--no-cacheで完全に再ビルド）
docker-compose -f docker-compose.local.yml build --no-cache debezium-connect

# 4. コンテナを再起動
docker-compose -f docker-compose.local.yml --env-file .env.local up -d

# 5. Kafka Connectが起動するまで待つ（約30秒）
sleep 30

# 6. プラグインが正しくインストールされたか確認
curl http://localhost:8083/connector-plugins | jq '.[] | select(.class | contains("PostgresConnector"))'

# 期待される出力:
# {
#   "class": "io.debezium.connector.postgresql.PostgresConnector",
#   "type": "source",
#   "version": "2.4.2.Final"
# }
```

**重要**: バージョンが `2.4.2.Final` であることを確認してください。`3.x.x` の場合は互換性問題があります。

### PostgreSQL CDC Connectorの登録に失敗

**問題**: WALが有効化されていない

**解決策**:
```bash
# PostgreSQLに接続
docker exec -it local-postgres psql -U postgres

# WAL設定を確認
SHOW wal_level;  -- 'logical'であること
SHOW max_wal_senders;  -- 1以上
SHOW max_replication_slots;  -- 1以上
```

### CDCトピックにデータが流れない

**問題**: Connectorの状態がFAILED

**解決策**:
```bash
# Connector状態確認
curl http://localhost:8083/connectors/postgres-cdc-source/status | jq

# Connectorを再起動
curl -X POST http://localhost:8083/connectors/postgres-cdc-source/restart

# Connectorを削除して再作成
curl -X DELETE http://localhost:8083/connectors/postgres-cdc-source
./scripts/register-debezium-connector.sh
```

### Payment Producerがスキーマエラーで失敗

**問題**: Schema Registryにスキーマが登録されていない

**解決策**:
```bash
# スキーマの確認
confluent schema-registry schema list --environment $(terraform -chdir=terraform-local output -raw environment_id)

# 手動でスキーマを登録（必要に応じて）
# Confluent Cloud UI > Schema Registry > Create Schema
```

### Flink SQLでテーブルが見つからない

**問題**: トピック名が異なる

**解決策**:
```sql
-- Debeziumのトピック名を使用（バッククォート必須）
SELECT * FROM `shiftleft.public.customers`;

-- トピック一覧を確認
SHOW TABLES;
```

## 🧹 クリーンアップ

### 一時停止と再開

```bash
# すべてのコンテナを一時停止
docker-compose -f docker-compose.local.yml stop

# すべてのコンテナを再開
docker-compose -f docker-compose.local.yml start

# データ生成コンテナのみ停止（PostgreSQL、Debezium Connectは継続）
docker-compose -f docker-compose.local.yml stop payment-producer data-feeder

# データ生成コンテナのみ再開
docker-compose -f docker-compose.local.yml start payment-producer data-feeder

# 特定のコンテナのみ停止/再開
docker-compose -f docker-compose.local.yml stop payment-producer
docker-compose -f docker-compose.local.yml start payment-producer
```

### Dockerリソースの削除

```bash
# すべてのコンテナを停止・削除
docker-compose -f docker-compose.local.yml down -v

# イメージも削除する場合
docker-compose -f docker-compose.local.yml down -v --rmi all
```

> **ヒント**:
> - **Payment Producer**: Kafkaトピックへ直接メッセージを送信（高頻度）
> - **Data Feeder**: PostgreSQLへデータを挿入（1秒ごと）→ Debezium CDCでKafkaへ
> - 検証中は両方またはいずれかを停止して、データ量を制御できます

### Confluent Cloudリソースの削除

```bash
# Terraformでリソースを削除
cd terraform-local
terraform destroy -auto-approve

# または、手動で削除
# Confluent Cloud UI > Environment > Delete
```

## 📚 参考リソース

- [Debezium PostgreSQL Connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html)
- [Confluent Cloud Documentation](https://docs.confluent.io/cloud/current/overview.html)
- [Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
- [Flink SQL Reference](https://docs.confluent.io/cloud/current/flink/reference/overview.html)
- [Data Quality Rules](https://docs.confluent.io/cloud/current/sr/fundamentals/data-contracts.html#data-quality-rules)

## 🎯 学習できる内容

このローカル環境で以下を学習できます:

### LAB 1の一部: Payment Processing & Data Quality
- ✅ Data Quality Rules
- ✅ Flink SQL (deduplication, joins)
- ✅ PostgreSQL CDC (Debezium経由)
- ✅ Terraform Infrastructure as Code
- ❌ CSFLE（スキップ）
- ❌ Tableflow（スキップ）

### LAB 2の一部: Customer360 & Product Sales
- ✅ Flink SQL (temporal joins, aggregations)
- ✅ CDC データの活用
- ❌ Tableflow（スキップ）

### 独自の実験
- Terraform でのインフラ管理
- カスタムFlink SQLクエリ
- 追加のData Quality Rules
- 新しいトピックとスキーマ
- Debezium Connectorの設定変更

## 📁 プロジェクト構造

```
online-retailer-flink-demo/
├── terraform/                    # オリジナルのTerraform（AWS使用）
├── terraform-local/              # ローカル用Terraform（Confluent Cloudのみ）
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── providers.tf
│   └── terraform.tfvars
├── docker-compose.local.yml      # ローカルDocker環境
├── .env.local                    # 環境変数（Terraformから生成）
├── scripts/
│   ├── register-debezium-connector.sh
│   └── register-data-quality-rule.sh
├── LOCAL-SETUP-GUIDE.md          # このガイド
└── code/                         # オリジナルのJavaアプリ（変更なし）
    ├── payments-app/
    └── postgresql-data-feeder/
```

---

**注意**: このガイドは教育目的です。本番環境では適切なセキュリティ、スケーラビリティ、可用性の設計が必要です。