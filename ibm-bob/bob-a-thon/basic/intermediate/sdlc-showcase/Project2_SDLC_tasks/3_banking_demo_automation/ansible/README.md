# Ansible Deployment for Banking Demo

This directory contains Ansible playbooks and configuration for deploying the Banking Demo applications.

## Prerequisites

1. **Ansible installed**:
   ```bash
   brew install ansible
   ```

2. **Docker running**:
   ```bash
   docker info
   ```

3. **Ansible Docker collection**:
   ```bash
   ansible-galaxy collection install -r requirements.yml
   ```

## Quick Start

### Deploy the applications

```bash
cd banking-demo/ansible
ansible-playbook playbook.yml
```

### Deploy with verbose output

```bash
ansible-playbook playbook.yml -v
```

### Deploy only specific components

```bash
# Deploy only Bank 1
ansible-playbook playbook.yml --tags bank1

# Deploy only Bank 2
ansible-playbook playbook.yml --tags bank2

# Only build images
ansible-playbook playbook.yml --tags build

# Only verify deployment
ansible-playbook playbook.yml --tags verify
```

### Cleanup

```bash
ansible-playbook playbook.yml --tags cleanup
```

## Configuration

### Inventory Variables

Edit [`inventory.yml`](inventory.yml) to customize:

- **Network settings**: `docker_network_name`, `docker_network_subnet`
- **Port mappings**: `bank1_port`, `bank2_port`
- **Container names**: `bank1_name`, `bank2_name`
- **Restart policy**: `restart_policy`

### Example: Change Ports

```yaml
# In inventory.yml
vars:
  bank1_port: 8001
  bank2_port: 8002
```

## Playbook Structure

### Main Playbook (`playbook.yml`)

The playbook consists of two plays:

1. **Deploy Banking Demo Applications**
   - Checks Docker availability
   - Creates Docker network
   - Builds Docker images
   - Deploys containers
   - Verifies health
   - Displays summary

2. **Cleanup Banking Demo Applications**
   - Removes containers
   - Removes images
   - Removes network
   - Only runs with `--tags cleanup`

### Tags

- `check` - Check Docker status
- `network` - Create Docker network
- `build` - Build Docker images
- `deploy` - Full deployment
- `bank1` - Bank 1 specific tasks
- `bank2` - Bank 2 specific tasks
- `verify` - Health checks
- `cleanup` - Remove all resources

## Testing the Deployment

After deployment, test the applications:

```bash
# Check Bank 1 users
curl http://localhost:5001/users

# Check Bank 2 users
curl http://localhost:5002/users

# Transfer funds
curl -X POST http://localhost:5001/transfer \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user1", "amount": 500.00}'

# Verify transfer
curl http://localhost:5001/user/user1
curl http://localhost:5002/user/user1
```

## Troubleshooting

### Docker not running

```bash
# Start Docker Desktop on macOS
open -a Docker
```

### Permission denied

```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
newgrp docker
```

### Port already in use

```bash
# Check what's using the port
lsof -i :5001
lsof -i :5002

# Kill the process or change ports in inventory.yml
```

### Collection not found

```bash
# Install required collections
ansible-galaxy collection install community.docker
```

## Advanced Usage

### Dry Run (Check Mode)

```bash
ansible-playbook playbook.yml --check
```

### Limit to specific hosts

```bash
ansible-playbook playbook.yml --limit localhost
```

### Extra Variables

```bash
ansible-playbook playbook.yml -e "bank1_port=8001 bank2_port=8002"
```

## Files

- [`playbook.yml`](playbook.yml) - Main playbook
- [`inventory.yml`](inventory.yml) - Inventory and variables
- [`ansible.cfg`](ansible.cfg) - Ansible configuration
- [`requirements.yml`](requirements.yml) - Required collections
- `ansible.log` - Execution log (generated)

## Notes

- The playbook uses `community.docker` collection for Docker management
- All tasks run on localhost with local connection
- Health checks ensure containers are ready before completion
- Cleanup tasks are tagged with `never` to prevent accidental execution