# Terraform + Ansible Integration Guide

## Overview

This project demonstrates **real-world DevOps practices** by using Terraform and Ansible together, each handling what they do best:

- **Terraform** = Infrastructure provisioning (WHAT to create)
- **Ansible** = Configuration management (HOW to configure)

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT WORKFLOW                       │
└─────────────────────────────────────────────────────────────┘

1. BUILD PHASE
   ├── Docker builds application images
   └── Images tagged: bank1-savings:latest, bank2-investment:latest

2. TERRAFORM PHASE (Infrastructure)
   ├── Creates Docker network (banking-network)
   ├── Creates persistent volumes (data, monitoring, backups)
   ├── Deploys containers (bank1-savings, bank2-investment)
   ├── Configures networking and basic health checks
   └── Outputs infrastructure details → JSON

3. ANSIBLE PHASE (Configuration)
   ├── Reads Terraform outputs
   ├── Configures application environment variables
   ├── Sets up monitoring scripts
   ├── Configures backup system
   ├── Implements health checks
   ├── Configures log rotation
   └── Verifies deployment

4. VERIFICATION PHASE
   ├── Tests application endpoints
   ├── Verifies inter-bank connectivity
   └── Displays management scripts
```

## Why Use Both?

### Terraform Strengths (Infrastructure)
- **Declarative**: Describe desired state, Terraform figures out how
- **State Management**: Tracks what exists, plans changes
- **Resource Dependencies**: Automatically orders creation
- **Cloud Agnostic**: Works with AWS, Azure, GCP, Docker, etc.
- **Immutable Infrastructure**: Replace rather than modify

### Ansible Strengths (Configuration)
- **Procedural**: Step-by-step configuration tasks
- **Agentless**: No software to install on targets
- **Idempotent**: Safe to run multiple times
- **Rich Modules**: Extensive library for configuration tasks
- **Dynamic Inventory**: Can discover infrastructure

### Together They Provide
1. **Separation of Concerns**: Infrastructure vs Configuration
2. **Flexibility**: Change infrastructure without touching config
3. **Reusability**: Same Ansible playbooks work on different infrastructure
4. **Team Specialization**: Infrastructure team uses Terraform, DevOps uses Ansible
5. **Disaster Recovery**: Terraform rebuilds, Ansible reconfigures

## File Structure

```
banking-demo/
├── terraform/                    # Infrastructure as Code
│   ├── main.tf                  # Resource definitions
│   ├── variables.tf             # Input variables
│   ├── outputs.tf               # Outputs for Ansible
│   └── terraform.tfvars         # Variable values
│
├── ansible/                      # Configuration Management
│   ├── playbook.yml             # Main configuration playbook
│   ├── requirements.yml         # Ansible dependencies
│   └── roles/                   # Reusable configuration roles
│       ├── configure_apps/      # App configuration
│       ├── monitoring/          # Monitoring setup
│       ├── backup/              # Backup configuration
│       └── health_check/        # Health validation
│
└── deploy.sh                     # Orchestrates both tools
```

## Terraform Resources (WHAT)

### Networks
```hcl
resource "docker_network" "banking_network" {
  name   = "banking-network"
  driver = "bridge"
  ipam_config {
    subnet  = "172.20.0.0/16"
    gateway = "172.20.0.1"
  }
}
```
**Purpose**: Isolated network for bank containers to communicate

### Volumes
```hcl
resource "docker_volume" "bank1_data" {
  name = "bank1-data"
}
```
**Purpose**: Persistent storage for databases and audit logs

### Containers
```hcl
resource "docker_container" "bank1_savings" {
  name  = "bank1-savings"
  image = docker_image.bank1_savings.image_id
  ports {
    internal = 5000
    external = 5001
  }
  volumes {
    volume_name    = docker_volume.bank1_data.name
    container_path = "/app/data"
  }
}
```
**Purpose**: Running application containers with basic configuration

### Outputs
```hcl
output "ansible_inventory" {
  value = jsonencode({
    banking_apps = {
      hosts = {
        bank1 = {
          container_name = docker_container.bank1_savings.name
          peer_url       = "http://bank2-investment:5000"
        }
      }
    }
  })
}
```
**Purpose**: Provide infrastructure details to Ansible

## Ansible Tasks (HOW)

### 1. Application Configuration
```yaml
- name: Configure Bank 1 environment
  community.docker.docker_container_exec:
    container: "{{ bank1_container }}"
    command: /bin/sh -c "echo 'BANK2_URL=http://bank2:5000' >> /app/.env"
```
**Purpose**: Set environment variables for inter-bank communication

### 2. Monitoring Setup
```yaml
- name: Create monitoring script
  copy:
    dest: "/tmp/monitor_bank1.sh"
    content: |
      #!/bin/bash
      while true; do
        curl -s http://localhost:5001/health
        sleep 30
      done
```
**Purpose**: Continuous health monitoring

### 3. Backup Configuration
```yaml
- name: Create backup script
  copy:
    dest: "/tmp/backup_banks.sh"
    content: |
      #!/bin/bash
      docker exec bank1-savings tar czf - /app/data > backup.tar.gz
```
**Purpose**: Automated data backups

### 4. Health Validation
```yaml
- name: Wait for Bank 1 to be healthy
  uri:
    url: "http://localhost:5001/health"
    status_code: 200
  retries: 10
  delay: 3
```
**Purpose**: Ensure applications are ready before proceeding

### 5. Log Management
```yaml
- name: Configure log rotation
  copy:
    dest: "/tmp/rotate_logs.sh"
    content: |
      #!/bin/bash
      find /app/data -name "*.jsonl" -size +10M -exec gzip {} \;
```
**Purpose**: Prevent disk space issues from growing logs

## Data Flow

```
┌──────────────┐
│  Terraform   │
│   Outputs    │
└──────┬───────┘
       │
       │ JSON
       ▼
┌──────────────┐
│   Ansible    │
│  Variables   │
└──────┬───────┘
       │
       │ Configuration
       ▼
┌──────────────┐
│ Application  │
│  Containers  │
└──────────────┘
```

### Example: Inter-Bank Communication

1. **Terraform** creates both containers on same network
2. **Terraform** outputs container names: `bank1-savings`, `bank2-investment`
3. **Ansible** reads outputs and configures environment:
   - Bank 1: `BANK2_URL=http://bank2-investment:5000`
   - Bank 2: `BANK1_URL=http://bank1-savings:5000`
4. **Applications** use environment variables to communicate

## Deployment Commands

### Full Deployment
```bash
./deploy.sh
```
Runs Terraform → Ansible in sequence

### Terraform Only (Infrastructure)
```bash
cd terraform
terraform init
terraform apply
```

### Ansible Only (Configuration)
```bash
cd ansible
ansible-playbook playbook.yml
```

### Destroy Everything
```bash
cd terraform
terraform destroy -auto-approve
```

## Real-World Scenarios

### Scenario 1: Add New Bank
1. **Terraform**: Add new container resource
2. **Terraform**: Update network configuration
3. **Ansible**: Add configuration tasks for new bank
4. **Ansible**: Update monitoring and backups

### Scenario 2: Change Configuration
1. **Ansible**: Update playbook with new settings
2. **Ansible**: Re-run playbook (no Terraform needed)
3. Applications reconfigured without infrastructure changes

### Scenario 3: Scale Infrastructure
1. **Terraform**: Increase container resources
2. **Terraform**: Add load balancer
3. **Ansible**: Configure new instances
4. **Ansible**: Update monitoring for scale

### Scenario 4: Disaster Recovery
1. **Terraform**: Rebuild all infrastructure from code
2. **Ansible**: Restore configurations
3. **Ansible**: Restore backups
4. **Ansible**: Verify health

## Best Practices

### Terraform
- ✅ Use for infrastructure resources
- ✅ Keep state file secure
- ✅ Use variables for flexibility
- ✅ Output data for Ansible
- ❌ Don't use for application configuration
- ❌ Don't use for file management

### Ansible
- ✅ Use for configuration tasks
- ✅ Make playbooks idempotent
- ✅ Use roles for reusability
- ✅ Read Terraform outputs
- ❌ Don't use for infrastructure provisioning
- ❌ Don't manage Terraform state

### Integration
- ✅ Terraform outputs → Ansible variables
- ✅ Run Terraform first, Ansible second
- ✅ Keep concerns separated
- ✅ Document data flow
- ❌ Don't duplicate responsibilities
- ❌ Don't create circular dependencies

## Troubleshooting

### Terraform Issues
```bash
# View current state
terraform show

# Plan changes without applying
terraform plan

# Refresh state
terraform refresh

# View outputs
terraform output -json
```

### Ansible Issues
```bash
# Run with verbose output
ansible-playbook playbook.yml -vvv

# Check syntax
ansible-playbook playbook.yml --syntax-check

# Dry run
ansible-playbook playbook.yml --check

# Run specific tasks
ansible-playbook playbook.yml --tags "monitoring"
```

### Integration Issues
```bash
# Verify Terraform outputs are available
cd terraform && terraform output -json

# Test Ansible can read outputs
cd ansible && ansible-playbook playbook.yml --check

# Verify containers exist
docker ps

# Check container logs
docker logs bank1-savings
docker logs bank2-investment
```

## Learning Resources

### Terraform
- [Official Documentation](https://www.terraform.io/docs)
- [Docker Provider](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs)
- [Best Practices](https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html)

### Ansible
- [Official Documentation](https://docs.ansible.com/)
- [Docker Module](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)
- [Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)

## Summary

This project demonstrates how Terraform and Ansible work together in production environments:

- **Terraform** handles the "what" - creating infrastructure resources
- **Ansible** handles the "how" - configuring those resources
- **Together** they provide a complete, maintainable deployment solution

The banking demo shows this pattern at work with two applications that need to communicate, be monitored, backed up, and maintained - just like real production systems.