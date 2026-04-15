# Using Banking Demo with Rancher Desktop

## Good News!

The Terraform and Ansible configurations work perfectly with Rancher Desktop without any modifications. Both Docker Desktop and Rancher Desktop use the same Docker socket (`unix:///var/run/docker.sock`), so all the infrastructure code remains the same.

## Quick Start with Rancher Desktop

### Step 1: Start Rancher Desktop

```bash
# Option 1: Open from Applications
open -a "Rancher Desktop"

# Option 2: Use rdctl command
rdctl start

# Wait 10-30 seconds for Docker to fully start
```

### Step 2: Verify Docker is Running

```bash
docker info
```

You should see output showing Docker server information. If you see "Cannot connect to the Docker daemon", wait a bit longer for Rancher Desktop to fully start.

### Step 3: Check Your Environment

```bash
cd banking-demo
./check-environment.sh
```

This script will verify:
- Docker is running
- Terraform is installed
- Ansible is installed
- Required ports are available

### Step 4: Deploy with Terraform

```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### Step 5: Test the Applications

```bash
# View Bank 1 users
curl http://localhost:5001/users

# View Bank 2 users
curl http://localhost:5002/users

# Transfer $500 from user1's savings to investment
curl -X POST http://localhost:5001/transfer \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user1", "amount": 500.00}'

# Verify the transfer
curl http://localhost:5001/user/user1
curl http://localhost:5002/user/user1
```

## Alternative: Deploy with Ansible

```bash
cd ansible
ansible-galaxy collection install -r requirements.yml
ansible-playbook playbook.yml
```

## Rancher Desktop vs Docker Desktop

### Similarities
- Both use the same Docker socket: `unix:///var/run/docker.sock`
- Both support the same Docker CLI commands
- Both work with Terraform's Docker provider
- Both work with Ansible's Docker modules
- Both support Docker Compose

### Differences
- **Startup**: Different commands to launch the application
- **UI**: Different management interfaces
- **Kubernetes**: Rancher Desktop includes Kubernetes by default
- **License**: Rancher Desktop is fully open source

## Configuration

No changes needed! The existing configuration works because:

1. **Terraform** (`terraform/main.tf`):
   ```hcl
   provider "docker" {
     host = "unix:///var/run/docker.sock"
   }
   ```
   This socket path is the same for both Docker Desktop and Rancher Desktop.

2. **Ansible** (`ansible/playbook.yml`):
   Uses the `community.docker` collection which automatically detects the Docker socket.

## Troubleshooting

### Rancher Desktop Won't Start

```bash
# Check if Rancher Desktop is already running
ps aux | grep rancher

# Check rdctl status
rdctl list-settings

# Restart Rancher Desktop
rdctl shutdown
rdctl start
```

### Docker Commands Not Found

Rancher Desktop installs Docker CLI at `/Users/clazzaro/.rd/bin/Docker`. Ensure this is in your PATH:

```bash
# Check your PATH
echo $PATH | grep .rd

# If not in PATH, add to your shell profile (~/.zshrc or ~/.bash_profile)
export PATH="$HOME/.rd/bin:$PATH"

# Reload your shell
source ~/.zshrc  # or source ~/.bash_profile
```

### Port Conflicts

If ports 5001 or 5002 are already in use:

```bash
# Find what's using the ports
lsof -i :5001
lsof -i :5002

# Kill the process
kill -9 <PID>

# Or change ports in terraform/terraform.tfvars
bank1_port = 8001
bank2_port = 8002
```

## Cleanup

Same cleanup process works for both:

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
docker rmi bank1-savings:latest bank2-investment:latest
docker network rm banking-network
```

## Additional Rancher Desktop Features

While not required for this demo, Rancher Desktop offers:

1. **Kubernetes**: Built-in Kubernetes cluster
2. **Container Runtime**: Choice between containerd and dockerd
3. **Image Management**: GUI for managing images
4. **Port Forwarding**: Easy port forwarding setup
5. **Volume Management**: GUI for managing volumes

## Performance Tips

1. **Allocate Resources**: In Rancher Desktop preferences, allocate sufficient CPU and memory
2. **Use BuildKit**: Enable Docker BuildKit for faster builds
3. **Prune Regularly**: Clean up unused resources with `docker system prune`

## Summary

✅ **No code changes needed** - Everything works out of the box with Rancher Desktop!

The only difference is how you start Docker:
- Docker Desktop: `open -a Docker`
- Rancher Desktop: `open -a "Rancher Desktop"` or `rdctl start`

After that, all commands and configurations are identical.

## Resources

- [Rancher Desktop Documentation](https://docs.rancherdesktop.io/)
- [Rancher Desktop GitHub](https://github.com/rancher-sandbox/rancher-desktop)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)