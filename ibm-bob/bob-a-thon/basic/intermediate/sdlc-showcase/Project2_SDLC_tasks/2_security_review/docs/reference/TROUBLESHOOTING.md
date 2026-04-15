# Banking Demo - トラブルシューティングガイド

## Docker Daemon が起動していない

### エラーメッセージ
```text
Error: Error pinging Docker server, please make sure that unix:///var/run/docker.sock is reachable
Error: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

### 対処方法

**Step 1: Docker を起動する**

Docker Desktop または Rancher Desktop を使っている想定です。まず次を試してください。

```bash
# For Docker Desktop
open -a Docker

# For Rancher Desktop (if Docker Desktop not found)
open -a "Rancher Desktop"

# Or start Rancher Desktop from command line
rdctl start

# Or if using colima
colima start
```

**Step 2: 起動完了を待つ**  
Docker Desktop は完全に立ち上がるまで 10〜30 秒ほどかかります。メニューバーの Docker アイコンがアニメーションから静止状態に変われば起動完了です。

**Step 3: Docker の稼働確認**
```bash
docker info
```

エラーではなく Docker server 情報が返れば OK です。

**Step 4: デプロイを再実行する**
```bash
# For Terraform
cd banking-demo/terraform
terraform apply

# For Ansible
cd banking-demo/ansible
ansible-playbook playbook.yml
```

### 補足: Docker 状態の確認

```bash
# Check if Docker process is running
ps aux | grep -i docker

# Check Docker version
docker --version

# Test Docker with a simple container
docker run hello-world
```

## よくある問題と対処法

### 1. ポートがすでに使われている

**Error:**
```text
Bind for 0.0.0.0:5001 failed: port is already allocated
```

**Solution:**
```bash
# Find what's using the port
lsof -i :5001
lsof -i :5002

# Kill the process (replace PID with actual process ID)
kill -9 <PID>

# Or change ports in configuration
# Edit terraform/terraform.tfvars or ansible/inventory.yml
```

### 2. コンテナが起動しない

**Error:**  
起動直後にコンテナが終了する

**Solution:**
```bash
# Check container logs
docker logs bank1-savings
docker logs bank2-investment

# Check container status
docker ps -a

# Inspect container
docker inspect bank1-savings

# Try running interactively to see errors
docker run -it bank1-savings /bin/bash
```

### 3. ネットワーク接続の問題

**Error:**  
Bank 1 から Bank 2 へ接続できない

**Solution:**
```bash
# Verify network exists
docker network ls | grep banking

# Inspect network
docker network inspect banking-network

# Check if containers are on the network
docker network inspect banking-network | grep -A 5 Containers

# Test connectivity from Bank 1 to Bank 2
docker exec bank1-savings ping bank2-investment

# Test DNS resolution
docker exec bank1-savings nslookup bank2-investment
```

### 4. イメージのビルドに失敗する

**Error:**  
Docker build が途中で失敗する

**Solution:**
```bash
# Build manually to see detailed output
cd banking-demo/bank1-savings
docker build -t bank1-savings:latest . --no-cache

# Check Dockerfile syntax
cat Dockerfile

# Verify all files exist
ls -la

# Check requirements.txt
cat requirements.txt

# Try building with verbose output
docker build -t bank1-savings:latest . --progress=plain
```

### 5. Terraform の state lock

**Error:**
```text
Error acquiring the state lock
```

**Solution:**
```bash
cd banking-demo/terraform

# Force unlock (use the lock ID from error message)
terraform force-unlock <LOCK_ID>

# Or remove lock file manually
rm -f .terraform.tfstate.lock.info

# Then retry
terraform apply
```

### 6. Ansible collection が見つからない

**Error:**
```text
couldn't resolve module/action 'community.docker.docker_container'
```

**Solution:**
```bash
# Install the required collection
ansible-galaxy collection install community.docker

# Or install from requirements file
cd banking-demo/ansible
ansible-galaxy collection install -r requirements.yml

# Verify installation
ansible-galaxy collection list | grep docker
```

### 7. Permission Denied（Linux）

**Error:**
```text
permission denied while trying to connect to the Docker daemon socket
```

**Solution:**
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Apply group changes
newgrp docker

# Or run with sudo (not recommended)
sudo docker ps
```

### 8. リソース不足

**Error:**  
コンテナが落ちる、またはマシン全体が重くなる

**Solution:**
```bash
# Check Docker resource usage
docker stats

# Increase Docker Desktop resources:
# 1. Open Docker Desktop
# 2. Go to Settings/Preferences
# 3. Resources
# 4. Increase CPU/Memory limits
# 5. Apply & Restart

# Clean up unused resources
docker system prune -a
```

### 9. API が 404 を返す

**Error:**
```text
curl: (22) The requested URL returned error: 404
```

**Solution:**
```bash
# Verify containers are running
docker ps | grep bank

# Check container logs
docker logs bank1-savings
docker logs bank2-investment

# Verify port mappings
docker port bank1-savings
docker port bank2-investment

# Test with correct URL
curl http://localhost:5001/
curl http://localhost:5002/
```

### 10. 振込が失敗する

**Error:**  
振込 API がエラーを返す、または無言で失敗する

**Solution:**
```bash
# Check Bank 1 logs
docker logs bank1-savings

# Check Bank 2 logs
docker logs bank2-investment

# Verify user exists
curl http://localhost:5001/user/user1

# Check balance is sufficient
curl http://localhost:5001/users

# Test with smaller amount
curl -X POST http://localhost:5001/transfer \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user1", "amount": 100.00}'

# Verify network connectivity
docker exec bank1-savings curl http://bank2-investment:5000/health
```

## 確認チェックリスト

デプロイ前に、次を確認してください。

- [ ] Docker Desktop がインストール済み
- [ ] Docker Desktop が起動している
- [ ] `docker info` で server 情報が返る
- [ ] ポート 5001 / 5002 が空いている
- [ ] Terraform がインストール済み（`terraform version`）
- [ ] Ansible がインストール済み（`ansible --version`）
- [ ] 正しいディレクトリにいる

## 簡易診断スクリプト

環境をまとめて確認したい場合は、次を使ってください。

```bash
#!/bin/bash

echo "=== Banking Demo Diagnostics ==="
echo ""

echo "1. Checking Docker..."
if docker info > /dev/null 2>&1; then
    echo "   ✓ Docker is running"
else
    echo "   ✗ Docker is NOT running - Start Docker Desktop!"
fi

echo ""
echo "2. Checking Terraform..."
if command -v terraform > /dev/null 2>&1; then
    echo "   ✓ Terraform is installed: $(terraform version -json | jq -r .terraform_version)"
else
    echo "   ✗ Terraform is NOT installed"
fi

echo ""
echo "3. Checking Ansible..."
if command -v ansible > /dev/null 2>&1; then
    echo "   ✓ Ansible is installed: $(ansible --version | head -1)"
else
    echo "   ✗ Ansible is NOT installed"
fi

echo ""
echo "4. Checking ports..."
if lsof -i :5001 > /dev/null 2>&1; then
    echo "   ✗ Port 5001 is in use"
else
    echo "   ✓ Port 5001 is available"
fi

if lsof -i :5002 > /dev/null 2>&1; then
    echo "   ✗ Port 5002 is in use"
else
    echo "   ✓ Port 5002 is available"
fi

echo ""
echo "5. Checking existing containers..."
if docker ps | grep -q bank; then
    echo "   ⚠ Banking containers already running:"
    docker ps | grep bank
else
    echo "   ✓ No banking containers running"
fi

echo ""
echo "=== End Diagnostics ==="
```

`check-environment.sh` として保存し、次のように実行します。

```bash
chmod +x check-environment.sh
./check-environment.sh
```

## それでも解決しないとき

1. **ログを確認する**
   ```bash
   docker logs bank1-savings
   docker logs bank2-investment
   ```

2. **ドキュメントを見直す**
   - [README.md](README.md)
   - [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
   - [QUICKSTART.md](QUICKSTART.md)

3. **実行環境を確認する**
   - Docker Desktop が起動している
   - ポートが空いている
   - ディスク容量が足りている
   - メモリが足りている

4. **初期化してやり直す**
   ```bash
   # Clean up everything
   cd banking-demo/terraform
   terraform destroy -auto-approve
   
   # Or with Ansible
   cd banking-demo/ansible
   ansible-playbook playbook.yml --tags cleanup
   
   # Remove all Docker resources
   docker system prune -a
   
   # Start over
   terraform apply -auto-approve
   ```

## Docker Hub の rate limit

### エラーメッセージ
```text
Error: Error running legacy build: python:3.9-slim: failed to resolve source metadata
429 Too Many Requests - Server message: toomanyrequests: You have reached your
unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit
```

### 何が起きているか

Docker Hub では、未認証ユーザーに対して 6 時間あたり 100 回までの pull 制限があります。この上限を超えると、ベースイメージ取得で失敗します。

### 対処方法

**Option 1: 待つ（最も簡単）**  
1〜6 時間待って制限がリセットされるのを待ちます。

**Option 2: Docker Hub にログインする（推奨）**  
無料アカウントでも 6 時間あたり 200 回まで pull できます。

```bash
# Login to Docker Hub
docker login

# Enter your Docker Hub username and password
# Then retry deployment
cd banking-demo/terraform
terraform apply -auto-approve
```

**Option 3: 先にローカルビルドする**

```bash
# Build Bank 1 image
cd banking-demo/bank1-savings
docker build -t bank1-savings:latest .

# Build Bank 2 image
cd ../bank2-investment
docker build -t bank2-investment:latest .

# Now run Terraform (it will use cached images)
cd ../terraform
terraform apply -auto-approve
```

**Option 4: Ansible を使う**

```bash
cd banking-demo/ansible
ansible-galaxy collection install -r requirements.yml
ansible-playbook playbook.yml
```

**Option 5: 無料アカウントを作る**
1. https://hub.docker.com/signup を開く
2. 無料アカウントを作成する
3. `docker login` を実行する
4. もう一度デプロイする

### 予防策

- 先に `docker login` しておく
- Docker Hub アカウントを使う
- 初回ビルド後はローカルキャッシュを活用する
- 混雑時間帯を避ける

### rate limit 状態の確認

```bash
# Check remaining pulls (requires authentication token)
TOKEN=$(curl -s "https://auth.docker.io/token?service=registry.docker.io&scope=repository:ratelimitpreview/test:pull" | jq -r .token)
curl -s -H "Authorization: Bearer $TOKEN" https://registry-1.docker.io/v2/ratelimitpreview/test/manifests/latest -I | grep -i ratelimit
```

## Contact & Support

追加で確認するときは、次も参照してください。

- [`diagrams/architecture.md`](diagrams/architecture.md) の図
- [`ARCHITECTURE.md`](ARCHITECTURE.md) の詳細構成
- [`README.md`](README.md) の前提条件一覧
