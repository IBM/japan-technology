# Deployment Overview - IT Operations Guide

## Executive Summary

This document provides a comprehensive overview of deployment options for the Banking Demo application, designed for IT Operations teams managing infrastructure deployment and maintenance.

## Deployment Architecture

### High-Level Overview

```mermaid
graph TB
    subgraph "Deployment Options"
        Local[Local Docker Deployment]
        Azure[Azure Cloud Deployment]
    end
    
    subgraph "Orchestration Tools"
        Deploy[deploy.sh<br/>Unified Deployment Script]
        TF[Terraform<br/>Infrastructure Provisioning]
        AN[Ansible<br/>Configuration Management]
    end
    
    subgraph "Target Infrastructure"
        LocalInfra[Docker Desktop/Rancher<br/>Local Containers]
        AzureInfra[Azure Container Instances<br/>Azure Storage<br/>Azure Networking]
    end
    
    Deploy --> Local
    Deploy --> Azure
    Local --> TF
    Local --> AN
    Azure --> TF
    TF --> LocalInfra
    TF --> AzureInfra
    AN --> LocalInfra
    
    style Deploy fill:#FFF176,stroke:#F57F17,stroke-width:3px,color:#000
    style TF fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style AN fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Local fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
    style Azure fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
    style LocalInfra fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style AzureInfra fill:#E1BEE7,stroke:#4A148C,stroke-width:2px,color:#000
```

## Deployment Workflow

### Complete Deployment Process

```mermaid
flowchart TD
    Start([Start Deployment]) --> Choice{Choose Target}
    
    Choice -->|Local| CheckDocker[Check Docker Running]
    Choice -->|Azure| CheckAzure[Check Azure CLI & Login]
    
    CheckDocker --> Build[Build Docker Images]
    CheckAzure --> Build
    
    Build --> BuildB1[Build Bank 1<br/>React + Flask]
    Build --> BuildB2[Build Bank 2<br/>Flask Only]
    
    BuildB1 --> AzureChoice{Target?}
    BuildB2 --> AzureChoice
    
    AzureChoice -->|Azure| PushACR[Push Images to<br/>Azure Container Registry]
    AzureChoice -->|Local| TFLocal[Terraform: Local]
    
    PushACR --> TFAzure[Terraform: Azure]
    
    TFLocal --> TFLocalSteps[Create Network<br/>Create Volumes<br/>Deploy Containers]
    TFAzure --> TFAzureSteps[Create Resource Group<br/>Create ACR<br/>Create Storage<br/>Create VNet<br/>Deploy ACI]
    
    TFLocalSteps --> Ansible[Ansible Configuration]
    TFAzureSteps --> Verify
    
    Ansible --> AnsibleSteps[Configure Environment<br/>Setup Monitoring<br/>Configure Backups<br/>Health Checks]
    
    AnsibleSteps --> Verify[Verify Deployment]
    
    Verify --> VerifySteps[Test Endpoints<br/>Check Health<br/>Verify Connectivity]
    
    VerifySteps --> Complete([Deployment Complete])
    
    style Start fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style Complete fill:#66BB6A,stroke:#1B5E20,stroke-width:3px,color:#000
    style Choice fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style AzureChoice fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style Build fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style BuildB1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style BuildB2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style TFLocal fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style TFAzure fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style Ansible fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style PushACR fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
```

## Deployment Options Comparison

### Local vs Azure Deployment

```mermaid
graph LR
    subgraph "Local Deployment"
        L1[Docker Desktop/Rancher]
        L2[Local Containers]
        L3[Docker Volumes]
        L4[Bridge Network]
        L5[Terraform + Ansible]
    end
    
    subgraph "Azure Deployment"
        A1[Azure Container Instances]
        A2[Azure Container Registry]
        A3[Azure File Shares]
        A4[Azure Virtual Network]
        A5[Terraform Only]
    end
    
    style L1 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style L2 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style L3 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style L4 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style L5 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style A1 fill:#E1BEE7,stroke:#4A148C,stroke-width:2px,color:#000
    style A2 fill:#E1BEE7,stroke:#4A148C,stroke-width:2px,color:#000
    style A3 fill:#E1BEE7,stroke:#4A148C,stroke-width:2px,color:#000
    style A4 fill:#E1BEE7,stroke:#4A148C,stroke-width:2px,color:#000
    style A5 fill:#E1BEE7,stroke:#4A148C,stroke-width:2px,color:#000
```

| Feature | Local Deployment | Azure Deployment |
|---------|-----------------|------------------|
| **Infrastructure** | Docker Desktop/Rancher | Azure Container Instances |
| **Networking** | Docker Bridge Network | Azure Virtual Network |
| **Storage** | Docker Volumes | Azure File Shares |
| **Registry** | Local Images | Azure Container Registry |
| **Orchestration** | Terraform + Ansible | Terraform Only |
| **Cost** | Free (local resources) | ~$66/month |
| **Scalability** | Limited to local machine | Cloud-scale |
| **Accessibility** | localhost only | Public internet |
| **Use Case** | Development, Testing | Production, Demo |

## Tool Integration: Terraform & Ansible

### How They Work Together

```mermaid
sequenceDiagram
    participant Ops as IT Operator
    participant Deploy as deploy.sh
    participant TF as Terraform
    participant Docker as Docker/Azure
    participant AN as Ansible
    participant App as Applications
    
    Ops->>Deploy: ./deploy.sh --cloud local
    Deploy->>Docker: Check Docker running
    Docker-->>Deploy: ✓ Running
    
    Deploy->>TF: terraform init
    Deploy->>TF: terraform apply
    
    TF->>Docker: Create network
    TF->>Docker: Create volumes
    TF->>Docker: Deploy containers
    Docker-->>TF: Infrastructure ready
    
    TF->>TF: Generate outputs.json
    TF-->>Deploy: Infrastructure provisioned
    
    Deploy->>AN: ansible-playbook playbook.yml
    AN->>TF: Read terraform outputs
    AN->>App: Configure environment
    AN->>App: Setup monitoring
    AN->>App: Configure backups
    AN->>App: Validate health
    App-->>AN: Configuration complete
    
    AN-->>Deploy: Applications configured
    Deploy-->>Ops: Deployment complete
```

### Terraform Responsibilities (WHAT)

- **Infrastructure Provisioning**
  - Create Docker networks or Azure VNets
  - Deploy containers or Azure Container Instances
  - Create storage volumes or Azure File Shares
  - Configure basic networking and ports

- **State Management**
  - Track infrastructure state
  - Plan changes before applying
  - Enable infrastructure versioning

- **Outputs**
  - Container names and IDs
  - Network details
  - Volume mount points
  - URLs and endpoints

### Ansible Responsibilities (HOW)

- **Application Configuration**
  - Set environment variables
  - Configure inter-service communication
  - Setup application-specific settings

- **Operational Tools**
  - Create monitoring scripts
  - Setup backup automation
  - Configure log rotation
  - Implement health checks

- **Validation**
  - Verify service health
  - Test connectivity
  - Validate configuration

## Quick Start Commands

### Local Deployment

```bash
# One-command deployment
./deploy.sh

# Or step-by-step
./deploy.sh --cloud local

# Skip image rebuild
./deploy.sh --skip-build

# Auto-approve (no prompts)
./deploy.sh --auto-approve
```

### Azure Deployment

```bash
# Deploy to Azure
./deploy.sh --cloud azure

# With auto-approve
./deploy.sh --cloud azure --auto-approve

# Prerequisites
az login
# Edit terraform-azure/terraform.tfvars with unique names
```

## Infrastructure Components

### Local Deployment Architecture

```mermaid
graph TB
    subgraph "MacBook/Workstation"
        subgraph "Docker Environment"
            Network[Docker Network<br/>banking-network<br/>172.20.0.0/16]
            
            subgraph "Bank 1 Container"
                B1[Bank 1 - Savings<br/>React Frontend + Flask API<br/>Port 5001]
                B1Vol[Docker Volume<br/>bank1-data]
            end
            
            subgraph "Bank 2 Container"
                B2[Bank 2 - Investment<br/>Flask API<br/>Port 5002]
                B2Vol[Docker Volume<br/>bank2-data]
            end
            
            MonVol[Docker Volume<br/>monitoring-data]
            BackupVol[Docker Volume<br/>backup-data]
        end
        
        subgraph "Management Tools"
            TF[Terraform<br/>terraform/]
            AN[Ansible<br/>ansible/]
            Scripts[Management Scripts<br/>/tmp/*.sh]
        end
    end
    
    User[Developer/Operator] -->|localhost:5001| B1
    User -->|localhost:5002| B2
    B1 <-->|Internal DNS| B2
    B1 -.-> B1Vol
    B2 -.-> B2Vol
    B1 -.-> Network
    B2 -.-> Network
    TF -.->|Provisions| Network
    TF -.->|Deploys| B1
    TF -.->|Deploys| B2
    AN -.->|Configures| B1
    AN -.->|Configures| B2
    AN -.->|Creates| Scripts
    
    style B1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style B2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Network fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
    style TF fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style AN fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style B1Vol fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B2Vol fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style MonVol fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style BackupVol fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style Scripts fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style User fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
```

### Azure Deployment Architecture

```mermaid
graph TB
    subgraph "Azure Cloud"
        subgraph "Resource Group"
            ACR[Azure Container Registry<br/>bankdemoXXXacr.azurecr.io]
            
            subgraph "Virtual Network"
                subgraph "Container Subnet"
                    ACI1[Container Instance<br/>Bank 1 - Savings<br/>Public FQDN]
                    ACI2[Container Instance<br/>Bank 2 - Investment<br/>Public FQDN]
                end
                NSG[Network Security Group<br/>Firewall Rules]
            end
            
            Storage[Storage Account<br/>bankdemoXXXstorage]
            FS1[File Share: bank1]
            FS2[File Share: bank2]
            FSB[File Share: backup]
        end
    end
    
    Internet[Internet Users] -->|HTTPS| ACI1
    Internet -->|HTTPS| ACI2
    ACI1 <-->|Internal| ACI2
    ACI1 -.-> FS1
    ACI2 -.-> FS2
    FS1 -.-> Storage
    FS2 -.-> Storage
    FSB -.-> Storage
    ACR -.->|Pull Images| ACI1
    ACR -.->|Pull Images| ACI2
    NSG -.->|Protects| ACI1
    NSG -.->|Protects| ACI2
    
    style ACR fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
    style ACI1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style ACI2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Storage fill:#E1BEE7,stroke:#4A148C,stroke-width:2px,color:#000
    style NSG fill:#EF5350,stroke:#B71C1C,stroke-width:2px,color:#fff
    style FS1 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style FS2 fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style FSB fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style Internet fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
```

## Management Operations

### Monitoring

```bash
# Local deployment - Ansible creates these scripts
/tmp/monitor_bank1.sh    # Continuous health monitoring
/tmp/monitor_bank2.sh    # Continuous health monitoring

# Azure deployment
az container logs --resource-group <rg-name> --name <container-name>
```

### Backup

```bash
# Local deployment
/tmp/backup_banks.sh     # Backup databases and logs

# Azure deployment
# Data persists in Azure File Shares automatically
```

### Log Management

```bash
# Local deployment
/tmp/rotate_logs.sh      # Rotate and compress logs

# Azure deployment
az container logs --resource-group <rg-name> --name <container-name>
```

### Health Checks

```bash
# Local deployment
curl http://localhost:5001/health
curl http://localhost:5002/health

# Azure deployment
curl http://<bank1-fqdn>:5000/health
curl http://<bank2-fqdn>:5000/health
```

## Troubleshooting

### Common Issues

#### Docker Not Running (Local)
```bash
# Check status
docker info

# Start Docker Desktop
open -a Docker

# Start Rancher Desktop
rdctl start
```

#### Azure Login Issues
```bash
# Login to Azure
az login

# Verify subscription
az account show

# List subscriptions
az account list --output table
```

#### Port Conflicts (Local)
```bash
# Check what's using ports
lsof -i :5001
lsof -i :5002

# Kill process or change ports in terraform/variables.tf
```

#### Terraform State Issues
```bash
# Reinitialize
cd terraform && rm -rf .terraform && terraform init

# Force refresh
terraform refresh

# View state
terraform show
```

## Cleanup

### Local Deployment
```bash
cd terraform
terraform destroy -auto-approve
```

### Azure Deployment
```bash
cd terraform-azure
terraform destroy -auto-approve
```

## Security Considerations

### Local Deployment
- ✅ Isolated Docker network
- ✅ No external exposure (localhost only)
- ✅ Volume-based data persistence
- ⚠️ No authentication (demo environment)

### Azure Deployment
- ✅ Azure Virtual Network isolation
- ✅ Network Security Group firewall
- ✅ Private Container Registry
- ✅ Encrypted storage at rest
- ⚠️ Public endpoints (configure NSG rules)
- ⚠️ No authentication (add Azure AD)

## Cost Management

### Local Deployment
- **Cost**: Free (uses local resources)
- **Resources**: CPU, memory, disk from local machine

### Azure Deployment
- **Estimated Monthly Cost**: ~$66
  - Container Instances: ~$60
  - Container Registry: ~$5
  - Storage: ~$0.50
  - Bandwidth: ~$0.87

### Cost Optimization
- Stop containers when not in use
- Use Azure Dev/Test pricing
- Implement auto-shutdown schedules
- Monitor usage with Azure Cost Management

## Next Steps

- **For Development**: Use local deployment
- **For Production**: Use Azure deployment with additional security
- **For Testing**: Use either, depending on test requirements
- **For Demos**: Use Azure deployment for accessibility

## Related Documentation

- [Architecture Overview](../architecture/SYSTEM_ARCHITECTURE.md)
- [Local Deployment Guide](../guides/LOCAL_DEPLOYMENT.md)
- [Azure Deployment Guide](../guides/AZURE_DEPLOYMENT.md)
- [Terraform & Ansible Integration](../guides/TERRAFORM_ANSIBLE.md)
- [Troubleshooting Guide](../reference/TROUBLESHOOTING.md)

---

**Document Version**: 1.0  
**Last Updated**: 2025-11-21  
**Maintained By**: IT Operations Team