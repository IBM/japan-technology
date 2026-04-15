# Banking Demo - Troubleshooting Guide

## Docker Daemon Not Running

### Error Message
```
Error: Error pinging Docker server, please make sure that unix:///var/run/docker.sock is reachable
Error: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

### Solution

**Step 1: Start Docker**

You may be using Docker Desktop or Rancher Desktop. Try these commands:

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

**Step 2: Wait for Docker to Start**
Docker Desktop takes 10-30 seconds to fully start. You'll see the Docker icon in your menu bar change from animated to static.

**Step 3: Verify Docker is Running**
```bash
docker info
```

Expected output should show Docker server information, not an error.

**Step 4: Retry Your Deployment**
```bash
# For Terraform
cd banking-demo/terraform
terraform apply

# For Ansible
cd banking-demo/ansible
ansible-playbook playbook.yml
```

### Alternative: Check Docker Status

```bash
# Check if Docker process is running
ps aux | grep -i docker

# Check Docker version
docker --version

# Test Docker with a simple container
docker run hello-world
```

## Common Issues and Solutions

### 1. Port Already in Use

**Error:**
```
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

### 2. Container Won't Start

**Error:**
Container exits immediately after starting

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

### 3. Network Connection Issues

**Error:**
Bank 1 cannot connect to Bank 2

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

### 4. Image Build Fails

**Error:**
Docker build fails with various errors

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

### 5. Terraform State Lock

**Error:**
```
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

### 6. Ansible Collection Not Found

**Error:**
```
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

### 7. Permission Denied (Linux)

**Error:**
```
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

### 8. Insufficient Resources

**Error:**
Container crashes or system becomes slow

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

### 9. API Returns 404

**Error:**
```
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

### 10. Transfer Fails

**Error:**
Transfer returns error or fails silently

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

## Verification Checklist

Before deploying, verify:

- [ ] Docker Desktop is installed
- [ ] Docker Desktop is running (icon in menu bar)
- [ ] `docker info` returns server information
- [ ] Ports 5001 and 5002 are available
- [ ] Terraform is installed (`terraform version`)
- [ ] Ansible is installed (`ansible --version`)
- [ ] You're in the correct directory

## Quick Diagnostic Script

Run this to check your environment:

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

Save this as `check-environment.sh` and run:
```bash
chmod +x check-environment.sh
./check-environment.sh
```

## Getting Help

If you're still having issues:

1. **Check the logs:**
   ```bash
   docker logs bank1-savings
   docker logs bank2-investment
   ```

2. **Review the documentation:**
   - [README.md](README.md)
   - [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
   - [QUICKSTART.md](QUICKSTART.md)

3. **Verify your environment:**
   - Docker Desktop is running
   - Ports are available
   - Sufficient disk space
   - Sufficient memory

4. **Start fresh:**
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

## Docker Hub Rate Limit

### Error Message
```
Error: Error running legacy build: python:3.9-slim: failed to resolve source metadata
429 Too Many Requests - Server message: toomanyrequests: You have reached your
unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit
```

### What This Means
Docker Hub limits unauthenticated users to 100 image pulls per 6 hours per IP address. You've exceeded this limit.

### Solutions

**Option 1: Wait (Simplest)**
Wait 1-6 hours for the rate limit to reset, then try again.

**Option 2: Login to Docker Hub (Recommended)**
Free Docker Hub accounts get 200 pulls per 6 hours:

```bash
# Login to Docker Hub
docker login

# Enter your Docker Hub username and password
# Then retry deployment
cd banking-demo/terraform
terraform apply -auto-approve
```

**Option 3: Build Images Manually First**
Build the images manually to cache them, then Terraform won't need to pull:

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

**Option 4: Use Ansible Instead**
Ansible might handle the rate limit better:

```bash
cd banking-demo/ansible
ansible-galaxy collection install -r requirements.yml
ansible-playbook playbook.yml
```

**Option 5: Create Free Docker Hub Account**
1. Go to https://hub.docker.com/signup
2. Create a free account
3. Login: `docker login`
4. Retry deployment

### Prevention

To avoid this in the future:
- Login to Docker Hub before building: `docker login`
- Use a Docker Hub account (free accounts get higher limits)
- Build images during off-peak hours
- Cache images locally after first build

### Check Your Rate Limit Status

```bash
# Check remaining pulls (requires authentication token)
TOKEN=$(curl -s "https://auth.docker.io/token?service=registry.docker.io&scope=repository:ratelimitpreview/test:pull" | jq -r .token)
curl -s -H "Authorization: Bearer $TOKEN" https://registry-1.docker.io/v2/ratelimitpreview/test/manifests/latest -I | grep -i ratelimit
```

## Contact & Support

For additional help:
- Review the architecture diagrams in [`diagrams/architecture.md`](diagrams/architecture.md)
- Check the detailed architecture in [`ARCHITECTURE.md`](ARCHITECTURE.md)
- Ensure all prerequisites are met as listed in [`README.md`](README.md)