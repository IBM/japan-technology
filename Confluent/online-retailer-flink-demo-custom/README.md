# Online Retailer Flink Demo Custom

このリポジトリは、Confluent の `online-retailer-flink-demo` をベースに、**AWS を使わずローカル環境で検証できるようにカスタマイズした版**です。

## このリポジトリについて

オリジナル版は AWS を前提としており、主に以下の構成で動作します。

- AWS 上の PostgreSQL
- ECS / Fargate 上のアプリケーション実行
- S3 / Glue / Athena を使った Tableflow 検証
- AWS KMS を使った CSFLE

このカスタム版では、**AWS 依存部分をローカル Docker 環境に置き換え**、ローカル PC 上で学習・検証しやすいようにしています。

## このカスタム版で検証できる内容

- Confluent Cloud
- ローカル PostgreSQL
- ローカル Debezium Connect
- ローカル実行の Payment Producer / PostgreSQL Data Feeder
- Flink SQL
- Schema Registry
- Data Quality Rules

## オリジナル版との違い

このリポジトリでは、元のワークショップ資産を参照できる形で残しつつ、ローカル実行向けの導線を追加しています。

- オリジナルの README は [`README-original.md`](./README-original.md) に保存
- ローカル環境向けの構築手順は [`LOCAL-SETUP-GUIDE.md`](./LOCAL-SETUP-GUIDE.md) に記載
- `terraform/` はオリジナルの AWS 前提構成
- `terraform-local/` はローカル検証向けの Confluent Cloud 構成
- `docker-compose.local.yml` でローカル実行環境を起動

## 最初に確認するファイル

### ローカル構築手順
- [`LOCAL-SETUP-GUIDE.md`](./LOCAL-SETUP-GUIDE.md)

### オリジナルの README を参照したい場合
- [`README-original.md`](./README-original.md)

## 想定している利用シーン

このカスタム版は、以下のようなケースを想定しています。

- AWS アカウントなしでワークショップ内容を試したい
- Confluent Cloud + Flink + PostgreSQL CDC の一連の流れをローカル中心で確認したい
- 元の教材をベースに、手元で検証・学習・デモを行いたい

## ローカル版の構成概要

### Confluent Cloud 側
- Kafka Cluster
- Schema Registry
- Flink Compute Pool
- Service Accounts / ACLs

### ローカル Docker 側
- PostgreSQL
- Debezium Connect
- Payment Producer App
- PostgreSQL Data Feeder

## 主な差分

### 利用するもの
- Confluent Cloud
- Terraform
- Docker / Docker Compose
- Git
- Confluent CLI

### 利用しないもの
- AWS ECS
- AWS EC2 / RDS 相当の実環境
- AWS S3 / Glue / Athena
- AWS KMS を使う CSFLE 検証

## 注意事項

- 元の README に書かれている AWS 前提の手順は、このカスタム版ではそのままでは使えません
- AWS 前提の検証項目の一部はスキップ、またはローカル向け代替手順に置き換えています
- オリジナルの手順や背景を確認したい場合は [`README-original.md`](./README-original.md) を参照してください

## 推奨スタート地点

ローカル環境で開始する場合は、以下から進めてください。

👉 [`LOCAL-SETUP-GUIDE.md`](./LOCAL-SETUP-GUIDE.md)

## 補足

このリポジトリは、オリジナルのワークショップを完全に置き換えるものではなく、**AWS を使わずに学習・検証しやすくするためのカスタマイズ版**です。
