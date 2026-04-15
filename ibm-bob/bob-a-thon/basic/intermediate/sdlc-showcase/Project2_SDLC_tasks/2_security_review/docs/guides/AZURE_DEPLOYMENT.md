# Banking Demo - Azure Deployment Guide

Complete guide for deploying the banking applications to Azure Container Instances.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Azure Setup](#azure-setup)
3. [Quick Start](#quick-start)
4. [Detailed Deployment Steps](#detailed-deployment-steps)
5. [Configuration](#configuration)
6. [Accessing Applications](#accessing-applications)
7. [Monitoring](#monitoring)
8. [Troubleshooting](#troubleshooting)
9. [Cost Estimation](#cost-estimation)
10. [Cleanup](#cleanup)

---

## Prerequisites

### Required Tools

1. **Azure CLI** (version 2.50+)
   ```bash
   # Install Azure CLI
   # macOS
   brew install azure-cli
   
   # Linux
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   
   # Windows
   # Download from: https://aka.ms/installazurecliwindows
   
   # Verify installation
   az --version
   ```

2. **Terraform** (version 1.0+)
   ```bash
   # Already installed for local deployment
   terraform version
   ```

3. **Docker** (for building images)
   ```bash
   docker --version
   ```

### Azure Account

- Active Azure subscription
- Sufficient permissions to create resources
- Resource quota for Container Instances

---

## Azure Setup

### Step 1: Login to Azure

```bash
# Login to Azure
az login

# Set your subscription (if you have multiple)
az account list --output table
az account set --subscription "YOUR_SUBSCRIPTION_ID"

# Verify current subscription
az account show
```

### Step 2: Create Service Principal (Optional but Recommended)

For automated deployments, create a service principal:

```bash
# Create service principal
az ad sp create-for-rbac \
  --name "banking-demo-sp" \
  --role="Contributor" \
  --scopes="/subscriptions/YOUR_SUBSCRIPTION_ID"

# Save the output - you'll need:
# - appId (client_id)
# - password (client_secret)
# - tenant
```

### Step 3: Configure Terraform Authentication

**Option A: Using Azure CLI (Recommended for Development)**
```bash
# Already authenticated via 'az login'
# Terraform will use your Azure CLI credentials
```

**Option B: Using Service Principal (Recommended for CI/CD)**
```bash
export ARM_CLIENT_ID="your-app-id"
export ARM_CLIENT_SECRET="your-password"
export ARM_SUBSCRIPTION_ID="your-subscription-id"
export ARM_TENANT_ID="your-tenant-id"
```

---

## Quick Start

### Deploy to Azure in 3 Commands

```bash
cd banking-demo

# 1. Deploy using the enhanced deploy.sh script
./deploy.sh --cloud azure

# That's it! The script will:
# - Build Docker images
# - Push to Azure Container Registry
# - Deploy with Terraform
# - Configure with Ansible
# - Display access URLs
```

---

## Detailed Deployment Steps

### Step 1: Configure Variables

```bash
cd banking-demo/terraform-azure

# Copy example variables
cp terraform.tfvars.example terraform.tfvars

# Edit terraform.tfvars with your unique values
nano terraform.tfvars
```

**Important**: Update these values to be globally unique:
- `prefix`: Your unique prefix (e.g., "bankdemo123")
- `acr_name`: Your ACR name (e.g., "bankdemo123acr")
- `storage_account_name`: Your storage name (e.g., "bankdemo123storage")

### Step 2: Initialize Terraform

```bash
cd banking-demo/terraform-azure

# Initialize Terraform
terraform init

# Validate configuration
terraform validate

# Preview changes
terraform plan
```

### Step 3: Build and Push Docker Images

```bash
# Build images locally
cd banking-demo
docker build -t bank1-savings:latest ./bank1-savings
docker build -t bank2-investment:latest ./bank2-investment

# Get ACR login server (after terraform apply creates ACR)
ACR_NAME="your-acr-name"
ACR_LOGIN_SERVER=$(az acr show --name $ACR_NAME --query loginServer --output tsv)

# Login to ACR
az acr login --name $ACR_NAME

# Tag images for ACR
docker tag bank1-savings:latest $ACR_LOGIN_SERVER/bank1-savings:latest
docker tag bank2-investment:latest $ACR_LOGIN_SERVER/bank2-investment:latest

# Push images to ACR
docker push $ACR_LOGIN_SERVER/bank1-savings:latest
docker push $ACR_LOGIN_SERVER/bank2-investment:latest
```

### Step 4: Deploy Infrastructure

```bash
cd banking-demo/terraform-azure

# Apply Terraform configuration
terraform apply

# Review the plan and type 'yes' to proceed
```

### Step 5: Verify Deployment

```bash
# Get deployment outputs
terraform output

# Test Bank 1
BANK1_URL=$(terraform output -raw bank1_url)
curl $BANK1_URL/health

# Test Bank 2
BANK2_URL=$(terraform output -raw bank2_url)
curl $BANK2_URL/health
```

---

## Configuration

### Resource Naming

All resources use a consistent naming pattern:

- Resource Group: `{prefix}-rg`
- Container Registry: `{acr_name}`
- Storage Account: `{storage_account_name}`
- Container Groups: `{prefix}-bank1-savings`, `{prefix}-bank2-investment`
- Virtual Network: `{prefix}-vnet`

### Environment Variables

Containers are configured with:

**Bank 1 (Savings)**:
- `BANK_NAME=Savings Bank`
- `BANK_ID=bank1`
- `BANK2_URL=http://{prefix}-bank2.{location}.azurecontainer.io:5000`

**Bank 2 (Investment)**:
- `BANK_NAME=Investment Bank`
- `BANK_ID=bank2`

### Persistent Storage

Azure File Shares are mounted to containers:

- `/app/data` - Application data (SQLite databases, audit logs)
- Backed by Azure Storage Account
- Survives container restarts

---

## Accessing Applications

### Public URLs

After deployment, access your applications at:

```bash
# Get URLs from Terraform output
terraform output bank1_url
terraform output bank2_url

# Example URLs:
# Bank 1: http://bankdemo123-bank1.eastus.azurecontainer.io:5000
# Bank 2: http://bankdemo123-bank2.eastus.azurecontainer.io:5000
```

### Using Azure Portal

1. Navigate to Azure Portal: https://portal.azure.com
2. Go to Resource Groups → `{your-resource-group}`
3. Click on Container Instance
4. View "Overview" for FQDN and IP address
5. Click FQDN to access application

---

## Monitoring

### View Container Logs

```bash
# Get resource group and container names
RG_NAME=$(terraform output -raw resource_group_name)
BANK1_NAME=$(terraform output -json deployment_summary | jq -r '.bank1.name')
BANK2_NAME=$(terraform output -json deployment_summary | jq -r '.bank2.name')

# View Bank 1 logs
az container logs --resource-group $RG_NAME --name $BANK1_NAME

# View Bank 2 logs
az container logs --resource-group $RG_NAME --name $BANK2_NAME

# Stream logs in real-time
az container logs --resource-group $RG_NAME --name $BANK1_NAME --follow
```

### Container Metrics

```bash
# View container metrics
az monitor metrics list \
  --resource "/subscriptions/{subscription-id}/resourceGroups/{rg-name}/providers/Microsoft.ContainerInstance/containerGroups/{container-name}" \
  --metric "CpuUsage,MemoryUsage"
```

### Azure Portal Monitoring

1. Go to Container Instance in Azure Portal
2. Click "Metrics" in left menu
3. View CPU, Memory, Network metrics
4. Set up alerts if needed

---

## Troubleshooting

### Container Won't Start

```bash
# Check container status
az container show \
  --resource-group $RG_NAME \
  --name $BANK1_NAME \
  --query "containers[0].instanceView.currentState"

# View detailed logs
az container logs --resource-group $RG_NAME --name $BANK1_NAME

# Check events
az container show \
  --resource-group $RG_NAME \
  --name $BANK1_NAME \
  --query "containers[0].instanceView.events"
```

### Image Pull Errors

```bash
# Verify ACR credentials
az acr credential show --name $ACR_NAME

# Check if image exists in ACR
az acr repository list --name $ACR_NAME

# Verify image tags
az acr repository show-tags --name $ACR_NAME --repository bank1-savings
```

### Network Connectivity Issues

```bash
# Test connectivity between containers
az container exec \
  --resource-group $RG_NAME \
  --name $BANK1_NAME \
  --exec-command "curl http://{bank2-fqdn}:5000/health"

# Check NSG rules
az network nsg rule list \
  --resource-group $RG_NAME \
  --nsg-name {prefix}-nsg \
  --output table
```

### Storage Mount Issues

```bash
# Verify storage account
az storage account show --name $STORAGE_ACCOUNT_NAME

# List file shares
az storage share list --account-name $STORAGE_ACCOUNT_NAME

# Check file share contents
az storage file list \
  --account-name $STORAGE_ACCOUNT_NAME \
  --share-name bank1-data
```

---

## Cost Estimation

### Monthly Cost Breakdown (East US region)

| Resource | Specification | Estimated Cost |
|----------|--------------|----------------|
| Container Instance (Bank 1) | 1 vCPU, 1.5GB RAM | ~$30/month |
| Container Instance (Bank 2) | 1 vCPU, 1.5GB RAM | ~$30/month |
| Container Registry (Basic) | 10GB storage | ~$5/month |
| Storage Account (LRS) | 25GB | ~$0.50/month |
| Virtual Network | Standard | ~$0/month |
| **Total** | | **~$65-70/month** |

**Notes**:
- Costs vary by region
- Actual costs depend on usage
- Stop containers when not in use to save costs
- Use Azure Cost Management for tracking

### Cost Optimization Tips

1. **Stop containers when not needed**:
   ```bash
   az container stop --resource-group $RG_NAME --name $BANK1_NAME
   az container stop --resource-group $RG_NAME --name $BANK2_NAME
   ```

2. **Use smaller container sizes** for development

3. **Delete resources when done**:
   ```bash
   terraform destroy
   ```

---

## Cleanup

### Option 1: Using Terraform (Recommended)

```bash
cd banking-demo/terraform-azure

# Destroy all resources
terraform destroy

# Type 'yes' to confirm
```

### Option 2: Using Azure CLI

```bash
# Delete entire resource group (deletes all resources)
az group delete --name $RG_NAME --yes --no-wait

# Verify deletion
az group list --output table
```

### Option 3: Using Azure Portal

1. Go to Azure Portal
2. Navigate to Resource Groups
3. Select your resource group
4. Click "Delete resource group"
5. Type the resource group name to confirm
6. Click "Delete"

---

## Security Best Practices

### 1. Network Security

- Use Azure Virtual Network for isolation
- Configure Network Security Groups (NSGs)
- Consider Azure Private Link for ACR
- Use Azure Firewall for advanced protection

### 2. Access Control

- Use Azure RBAC for resource access
- Enable Azure AD authentication for ACR
- Use Managed Identities instead of passwords
- Implement least privilege access

### 3. Data Protection

- Enable encryption at rest for Storage Account
- Use Azure Key Vault for secrets
- Enable soft delete for Storage Account
- Regular backups of persistent data

### 4. Monitoring and Auditing

- Enable Azure Monitor
- Configure diagnostic settings
- Set up alerts for critical events
- Review Activity Logs regularly

---

## Advanced Configuration

### Custom Domain

To use a custom domain:

1. Create Azure Application Gateway or Azure Front Door
2. Configure SSL certificate
3. Point domain to Application Gateway
4. Update NSG rules

### High Availability

For production deployments:

1. Deploy to multiple regions
2. Use Azure Traffic Manager
3. Implement health checks
4. Configure auto-restart policies

### CI/CD Integration

Integrate with Azure DevOps or GitHub Actions:

```yaml
# Example GitHub Actions workflow
name: Deploy to Azure
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
      - name: Deploy with Terraform
        run: |
          cd terraform-azure
          terraform init
          terraform apply -auto-approve
```

---

## Support and Resources

### Azure Documentation

- [Azure Container Instances](https://docs.microsoft.com/azure/container-instances/)
- [Azure Container Registry](https://docs.microsoft.com/azure/container-registry/)
- [Azure Storage](https://docs.microsoft.com/azure/storage/)
- [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)

### Troubleshooting Resources

- [Azure Status](https://status.azure.com/)
- [Azure Support](https://azure.microsoft.com/support/)
- [Stack Overflow - Azure](https://stackoverflow.com/questions/tagged/azure)

### Project Documentation

- [Main README](README.md)
- [Local Deployment Guide](DEPLOYMENT_GUIDE.md)
- [Terraform + Ansible Guide](TERRAFORM_ANSIBLE_GUIDE.md)
- [React Frontend Guide](REACT_FRONTEND_GUIDE.md)

---

## Next Steps

After successful Azure deployment:

1. **Test the applications** thoroughly
2. **Set up monitoring** and alerts
3. **Configure backups** for persistent data
4. **Review security** settings
5. **Optimize costs** based on usage
6. **Document** your specific configuration

---

**Deployment Status**: Ready for Azure deployment! 🚀

**Last Updated**: 2025-11-18