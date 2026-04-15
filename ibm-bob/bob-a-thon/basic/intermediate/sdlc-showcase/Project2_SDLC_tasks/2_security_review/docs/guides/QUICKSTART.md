# Banking Demo - クイックスタートガイド

5 分以内にバンキングアプリを起動するための最短手順です。

## 前提条件の確認

開始前に、必要なツールが入っていることを確認してください。

```bash
# Check Docker
docker --version
# Expected: Docker version 20.x or higher

# Check Terraform
terraform version
# Expected: Terraform v1.x or higher

# Check Ansible
ansible --version
# Expected: ansible [core 2.x] or higher
```

## Step 1: Docker を起動する

デプロイ前に Docker が起動している必要があります。

```bash
# macOS: Start Docker Desktop
open -a Docker

# Wait 10-15 seconds for Docker to start, then verify:
docker info
```

## Step 2: デプロイ方法を選ぶ

### Option A: Terraform（推奨）

```bash
cd banking-demo/terraform
terraform init
terraform apply -auto-approve
```

### Option B: Ansible

```bash
cd banking-demo/ansible
ansible-galaxy collection install -r requirements.yml
ansible-playbook playbook.yml
```

### Option C: 手動 Docker

```bash
cd banking-demo

# Create network
docker network create banking-network

# Build and run Bank 1
cd bank1-savings
docker build -t bank1-savings .
docker run -d --name bank1-savings --network banking-network \
  -p 5001:5000 \
  -e BANK2_URL="http://bank2-investment:5000" \
  bank1-savings

# Build and run Bank 2
cd ../bank2-investment
docker build -t bank2-investment .
docker run -d --name bank2-investment --network banking-network \
  -p 5002:5000 \
  bank2-investment
```

## Step 3: デプロイ確認

```bash
# Check containers are running
docker ps

# Test Bank 1
curl http://localhost:5001/users

# Test Bank 2
curl http://localhost:5002/users
```

## Step 4: 振込テスト

```bash
# Transfer $500 from user1's savings to investment
curl -X POST http://localhost:5001/transfer \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user1", "amount": 500.00}'

# Verify balances
curl http://localhost:5001/user/user1
curl http://localhost:5002/user/user1
```

## Step 5: ブラウザで確認

ブラウザで次を開いてください。

- Bank 1 (Savings): http://localhost:5001
- Bank 2 (Investment): http://localhost:5002

## クリーンアップ

### Terraform
```bash
cd banking-demo/terraform
terraform destroy -auto-approve
```

### Ansible
```bash
cd banking-demo/ansible
ansible-playbook playbook.yml --tags cleanup
```

### 手動
```bash
docker stop bank1-savings bank2-investment
docker rm bank1-savings bank2-investment
docker rmi bank1-savings bank2-investment
docker network rm banking-network
```

## トラブルシューティング

### Docker が起動していない
```bash
# Start Docker Desktop
open -a Docker
# Wait 10-15 seconds, then retry
```

### ポートがすでに使用中
```bash
# Find what's using the port
lsof -i :5001
# Kill the process or change ports in configuration
```

### コンテナが起動しない
```bash
# Check logs
docker logs bank1-savings
docker logs bank2-investment
```

## 次のステップ

- 全体像は [`README.md`](README.md) を参照
- 技術的な背景は [`ARCHITECTURE.md`](ARCHITECTURE.md) を確認
- 詳しいデプロイ方法は [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md) を参照
- 図解は [`diagrams/architecture.md`](diagrams/architecture.md) を確認

## ヘルプが必要なとき

1. `docker info` で Docker が起動しているか確認する
2. `docker logs <container-name>` でログを確認する
3. `lsof -i :5001` と `lsof -i :5002` でポートの空きを確認する
4. 上記リンク先のドキュメントを確認する
