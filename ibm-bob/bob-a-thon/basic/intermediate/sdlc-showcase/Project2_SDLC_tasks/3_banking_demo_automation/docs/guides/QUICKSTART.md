# Banking Demo - Quick Start Guide

Get the banking applications running in under 5 minutes!

## Prerequisites Check

Before starting, verify you have everything installed:

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

## Step 1: Start Docker

Docker must be running before deployment:

```bash
# macOS: Start Docker Desktop
open -a Docker

# Wait 10-15 seconds for Docker to start, then verify:
docker info
```

## Step 2: Choose Your Deployment Method

### Option A: Terraform (Recommended)

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

### Option C: Manual Docker

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

## Step 3: Verify Deployment

```bash
# Check containers are running
docker ps

# Test Bank 1
curl http://localhost:5001/users

# Test Bank 2
curl http://localhost:5002/users
```

## Step 4: Test Transfer

```bash
# Transfer $500 from user1's savings to investment
curl -X POST http://localhost:5001/transfer \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user1", "amount": 500.00}'

# Verify balances
curl http://localhost:5001/user/user1
curl http://localhost:5002/user/user1
```

## Step 5: Access in Browser

Open your browser and visit:
- Bank 1 (Savings): http://localhost:5001
- Bank 2 (Investment): http://localhost:5002

## Cleanup

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

### Manual
```bash
docker stop bank1-savings bank2-investment
docker rm bank1-savings bank2-investment
docker rmi bank1-savings bank2-investment
docker network rm banking-network
```

## Troubleshooting

### Docker not running
```bash
# Start Docker Desktop
open -a Docker
# Wait 10-15 seconds, then retry
```

### Port already in use
```bash
# Find what's using the port
lsof -i :5001
# Kill the process or change ports in configuration
```

### Container won't start
```bash
# Check logs
docker logs bank1-savings
docker logs bank2-investment
```

## Next Steps

- Read [`README.md`](README.md) for complete documentation
- Review [`ARCHITECTURE.md`](ARCHITECTURE.md) for technical details
- Check [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md) for advanced options
- View [`diagrams/architecture.md`](diagrams/architecture.md) for visual diagrams

## Need Help?

1. Ensure Docker is running: `docker info`
2. Check container logs: `docker logs <container-name>`
3. Verify ports are free: `lsof -i :5001` and `lsof -i :5002`
4. Review the full documentation in the links above