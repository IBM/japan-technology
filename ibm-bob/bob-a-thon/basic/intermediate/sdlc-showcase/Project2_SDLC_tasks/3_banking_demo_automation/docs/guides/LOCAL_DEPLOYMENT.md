# Local Deployment Guide

## Overview

This guide provides detailed instructions for deploying the Banking Demo application locally using Docker Desktop or Rancher Desktop. This deployment method is ideal for development, testing, and demonstration purposes.

## Prerequisites

### Required Software

1. **Docker** (Docker Desktop or Rancher Desktop)
   - Docker Desktop 4.0+ OR Rancher Desktop 1.0+
   - Minimum 4GB RAM allocated to Docker
   - Minimum 20GB disk space

2. **Terraform** 
   - Version 1.0 or higher
   - Installation: `brew install terraform` (macOS)

3. **Ansible**
   - Version 2.9 or higher
   - Installation: `brew install ansible` (macOS)

4. **Git**
   - For cloning the repository

### System Requirements

- **Operating System**: macOS, Linux, or Windows with WSL2
- **RAM**: Minimum 8GB (16GB recommended)
- **CPU**: 2+ cores
- **Disk Space**: 20GB free space

## Installation Steps

### Step 1: Install Docker

#### Option A: Docker Desktop

```bash
# macOS
brew install --cask docker

# Or download from: https://www.docker.com/products/docker-desktop

# Start Docker Desktop
open -a Docker

# Verify installation
docker --version
docker info
```

#### Option B: Rancher Desktop

```bash
# macOS
brew install --cask rancher

# Or download from: https://rancherdesktop.io

# Start Rancher Desktop
open -a "Rancher Desktop"
# OR
rdctl start

# Verify installation
docker --version
docker info
```

### Step 2: Install Terraform

```bash
# macOS
brew install terraform

# Linux
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/

# Verify installation
terraform version
```

### Step 3: Install Ansible

```bash
# macOS
brew install ansible

# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install ansible

# Linux (RHEL/CentOS)
sudo yum install ansible

# Python pip (any OS)
pip install ansible

# Verify installation
ansible --version
```

### Step 4: Clone Repository

```bash
git clone <repository-url>
cd banking-demo
```

## Deployment Methods

### Method 1: Automated Deployment (Recommended)

The `deploy.sh` script orchestrates the entire deployment process.

```bash
# One-command deployment
./deploy.sh

# Or explicitly specify local deployment
./deploy.sh --cloud local

# Skip Docker image rebuild (if images already exist)
./deploy.sh --skip-build

# Auto-approve without prompts
./deploy.sh --auto-approve
```

**What the script does:**
1. ✅ Checks Docker is running
2. ✅ Builds Docker images for both banks
3. ✅ Runs Terraform to provision infrastructure
4. ✅ Runs Ansible to configure applications
5. ✅ Verifies deployment health
6. ✅ Displays access URLs and management commands

### Method 2: Step-by-Step Deployment

#### Step 2.1: Start Docker

```bash
# Check if Docker is running
docker info

# If not running, start Docker
open -a Docker  # Docker Desktop
# OR
rdctl start     # Rancher Desktop

# Wait 10-15 seconds for Docker to start
```

#### Step 2.2: Build Docker Images

```bash
# Build Bank 1 (Savings) - React + Flask
cd bank1-savings
docker build -t bank1-savings:latest .
cd ..

# Build Bank 2 (Investment) - Flask only
cd bank2-investment
docker build -t bank2-investment:latest .
cd ..

# Verify images
docker images | grep bank
```

#### Step 2.3: Deploy with Terraform

```bash
cd terraform

# Initialize Terraform (first time only)
terraform init

# Preview changes
terraform plan

# Apply configuration
terraform apply

# Type 'yes' when prompted
```

**Terraform creates:**
- Docker network: `banking-network`
- Docker volumes: `bank1-data`, `bank2-data`, `monitoring-data`, `backup-data`
- Bank 1 container: `bank1-savings` (port 5001)
- Bank 2 container: `bank2-investment` (port 5002)

#### Step 2.4: Configure with Ansible

```bash
cd ../ansible

# Install Ansible collections (first time only)
ansible-galaxy collection install -r requirements.yml

# Run configuration playbook
ansible-playbook playbook.yml
```

**Ansible configures:**
- Environment variables for inter-bank communication
- Monitoring scripts (`/tmp/monitor_bank*.sh`)
- Backup scripts (`/tmp/backup_banks.sh`)
- Log rotation (`/tmp/rotate_logs.sh`)
- Health check validation

#### Step 2.5: Verify Deployment

```bash
# Check containers are running
docker ps

# Test Bank 1
curl http://localhost:5001/health

# Test Bank 2
curl http://localhost:5002/health

# Test inter-bank connectivity
curl -X POST http://localhost:5001/api/transfer \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 100.0}'
```

## Accessing the Applications

### Web Interfaces

- **Bank 1 (Savings)**: http://localhost:5001
  - Modern React UI with Material-UI
  - Dashboard, transactions, transfers, analytics
  
- **Bank 2 (Investment)**: http://localhost:5002
  - Traditional Flask interface
  - Simple forms and tables

### API Endpoints

#### Bank 1 API
```bash
# Get balance
curl http://localhost:5001/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'

# Get transactions
curl http://localhost:5001/api/transactions \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "limit": 10}'

# Transfer to Bank 2
curl -X POST http://localhost:5001/api/transfer \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 500.0}'
```

#### Bank 2 API
```bash
# Get balance
curl http://localhost:5002/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'

# Transfer to Bank 1
curl -X POST http://localhost:5002/api/transfer_to_savings \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 300.0}'
```

## Management Operations

### Monitoring

Ansible creates monitoring scripts in `/tmp/`:

```bash
# Monitor Bank 1 (runs continuously)
/tmp/monitor_bank1.sh

# Monitor Bank 2 (runs continuously)
/tmp/monitor_bank2.sh

# Run in background
/tmp/monitor_bank1.sh > /tmp/bank1_monitor.log 2>&1 &
/tmp/monitor_bank2.sh > /tmp/bank2_monitor.log 2>&1 &

# View logs
tail -f /tmp/bank1_monitor.log
tail -f /tmp/bank2_monitor.log
```

### Backups

```bash
# Create backup of both banks
/tmp/backup_banks.sh

# Backups are stored in Docker volume: backup-data
# View backups
docker run --rm -v backup-data:/backup alpine ls -lh /backup
```

### Log Management

```bash
# Rotate logs to prevent disk space issues
/tmp/rotate_logs.sh

# View container logs
docker logs bank1-savings
docker logs bank2-investment

# Follow logs in real-time
docker logs -f bank1-savings
docker logs -f bank2-investment
```

### Container Management

```bash
# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# Restart containers
docker restart bank1-savings bank2-investment

# Stop containers
docker stop bank1-savings bank2-investment

# Start containers
docker start bank1-savings bank2-investment

# Access container shell
docker exec -it bank1-savings /bin/sh
docker exec -it bank2-investment /bin/sh
```

### Network Inspection

```bash
# Inspect Docker network
docker network inspect banking-network

# View network connectivity
docker network ls

# Test inter-container communication
docker exec bank1-savings ping bank2-investment
```

### Volume Management

```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect bank1-data

# View volume contents
docker run --rm -v bank1-data:/data alpine ls -lh /data

# Backup volume to tar file
docker run --rm -v bank1-data:/data -v $(pwd):/backup alpine \
  tar czf /backup/bank1-data-backup.tar.gz -C /data .
```

## Infrastructure Management

### Terraform Operations

```bash
cd terraform

# View current state
terraform show

# View outputs
terraform output

# View specific output
terraform output bank1_url

# Refresh state
terraform refresh

# Plan changes (without applying)
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy
```

### Ansible Operations

```bash
cd ansible

# Run playbook
ansible-playbook playbook.yml

# Run with verbose output
ansible-playbook playbook.yml -v
ansible-playbook playbook.yml -vv
ansible-playbook playbook.yml -vvv

# Check syntax
ansible-playbook playbook.yml --syntax-check

# Dry run (check mode)
ansible-playbook playbook.yml --check

# Run specific tags
ansible-playbook playbook.yml --tags "monitoring"
ansible-playbook playbook.yml --tags "backup"
```

## Troubleshooting

### Docker Not Running

```bash
# Check Docker status
docker info

# If error, start Docker
open -a Docker          # Docker Desktop
rdctl start            # Rancher Desktop

# Wait 10-15 seconds, then retry
docker info
```

### Port Already in Use

```bash
# Check what's using port 5001
lsof -i :5001

# Check what's using port 5002
lsof -i :5002

# Kill process using port
kill -9 <PID>

# Or change ports in terraform/variables.tf
```

### Container Won't Start

```bash
# Check container logs
docker logs bank1-savings
docker logs bank2-investment

# Check container status
docker ps -a

# Remove and recreate container
docker rm -f bank1-savings
cd terraform && terraform apply
```

### Terraform State Issues

```bash
cd terraform

# Reinitialize
rm -rf .terraform .terraform.lock.hcl
terraform init

# Force refresh
terraform refresh

# If state is corrupted, remove and reapply
rm terraform.tfstate*
terraform apply
```

### Ansible Connection Issues

```bash
# Verify Docker is accessible
docker ps

# Check Ansible can connect
ansible localhost -m ping

# Run with verbose output
ansible-playbook playbook.yml -vvv
```

### Network Issues

```bash
# Recreate network
docker network rm banking-network
docker network create banking-network

# Or use Terraform
cd terraform
terraform destroy -target=docker_network.banking_network
terraform apply
```

## Cleanup

### Complete Cleanup

```bash
# Using Terraform (recommended)
cd terraform
terraform destroy -auto-approve

# This removes:
# - All containers
# - Docker network
# - Docker volumes (data will be lost!)
```

### Partial Cleanup

```bash
# Stop containers only (keep data)
docker stop bank1-savings bank2-investment

# Remove containers only (keep volumes)
docker rm bank1-savings bank2-investment

# Remove images
docker rmi bank1-savings:latest bank2-investment:latest

# Remove network
docker network rm banking-network
```

### Preserve Data

```bash
# Backup volumes before cleanup
docker run --rm -v bank1-data:/data -v $(pwd):/backup alpine \
  tar czf /backup/bank1-backup.tar.gz -C /data .

docker run --rm -v bank2-data:/data -v $(pwd):/backup alpine \
  tar czf /backup/bank2-backup.tar.gz -C /data .

# Then destroy infrastructure
cd terraform && terraform destroy
```

## Performance Tuning

### Docker Resource Allocation

```bash
# Docker Desktop: Preferences → Resources
# - CPUs: 2-4 cores
# - Memory: 4-8 GB
# - Disk: 20+ GB

# Rancher Desktop: Preferences → Virtual Machine
# - CPUs: 2-4 cores
# - Memory: 4-8 GB
```

### Container Resource Limits

Edit `terraform/main.tf` to add resource limits:

```hcl
resource "docker_container" "bank1" {
  # ... existing config ...
  
  memory = 512  # MB
  cpu_shares = 1024
}
```

## Security Considerations

### Local Development Security

- ✅ Isolated Docker network
- ✅ No external exposure (localhost only)
- ✅ Volume-based data persistence
- ⚠️ No authentication (demo environment)
- ⚠️ HTTP only (no HTTPS)

### Production Recommendations

- Add authentication (JWT/OAuth)
- Enable HTTPS/TLS
- Implement rate limiting
- Add input validation
- Enable audit logging
- Use secrets management
- Implement network policies

## Next Steps

- **Explore Features**: [Banking Features](../reference/BANKING_FEATURES.md)
- **Test APIs**: [API Reference](../reference/API_REFERENCE.md)
- **Run Tests**: [Testing Guide](../reference/TESTING.md)
- **Deploy to Azure**: [Azure Deployment Guide](AZURE_DEPLOYMENT.md)
- **Understand Architecture**: [System Architecture](../architecture/SYSTEM_ARCHITECTURE.md)

## Related Documentation

- [Deployment Overview](../operations/DEPLOYMENT_OVERVIEW.md)
- [Terraform & Ansible Integration](TERRAFORM_ANSIBLE.md)
- [Troubleshooting Guide](../reference/TROUBLESHOOTING.md)
- [Quick Start Guide](QUICKSTART.md)

---

**Document Version**: 1.0  
**Last Updated**: 2025-11-21  
**Maintained By**: DevOps Team