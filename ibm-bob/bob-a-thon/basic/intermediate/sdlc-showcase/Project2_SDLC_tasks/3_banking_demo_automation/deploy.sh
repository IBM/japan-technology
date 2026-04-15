#!/bin/bash

# ============================================================================
# BANKING DEMO - AUTOMATED DEPLOYMENT SCRIPT
# ============================================================================
# This script demonstrates real-world Terraform + Ansible integration:
#   1. Terraform provisions infrastructure (containers, networks, volumes)
#   2. Ansible configures applications (environment, monitoring, backups)
#
# Supports multiple deployment targets:
#   - Local Docker (default)
#   - Azure Container Instances
# ============================================================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Default values
CLOUD_PROVIDER="local"
SKIP_BUILD=false
AUTO_APPROVE=false

# ============================================================================
# PARSE COMMAND LINE ARGUMENTS
# ============================================================================

show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --cloud <provider>    Cloud provider: 'local' (default) or 'azure'"
    echo "  --skip-build          Skip Docker image building"
    echo "  --auto-approve        Skip confirmation prompts"
    echo "  -h, --help            Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                           # Deploy locally (default)"
    echo "  $0 --cloud local             # Deploy locally (explicit)"
    echo "  $0 --cloud azure             # Deploy to Azure"
    echo "  $0 --cloud azure --auto-approve  # Deploy to Azure without prompts"
    echo ""
}

while [[ $# -gt 0 ]]; do
    case $1 in
        --cloud)
            CLOUD_PROVIDER="$2"
            shift 2
            ;;
        --skip-build)
            SKIP_BUILD=true
            shift
            ;;
        --auto-approve)
            AUTO_APPROVE=true
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            show_usage
            exit 1
            ;;
    esac
done

# Validate cloud provider
if [[ "$CLOUD_PROVIDER" != "local" && "$CLOUD_PROVIDER" != "azure" ]]; then
    echo -e "${RED}Invalid cloud provider: $CLOUD_PROVIDER${NC}"
    echo "Supported providers: local, azure"
    exit 1
fi

# ============================================================================
# DISPLAY DEPLOYMENT INFO
# ============================================================================

echo -e "${BLUE}============================================"
echo "Banking Demo - Deployment"
echo -e "============================================${NC}"
echo ""
echo -e "${CYAN}Deployment Target:${NC} ${YELLOW}$CLOUD_PROVIDER${NC}"
echo -e "${CYAN}Architecture:${NC}"
echo -e "  ${YELLOW}Terraform${NC} → Provisions infrastructure (WHAT)"
echo -e "  ${YELLOW}Ansible${NC}   → Configures applications (HOW)"
echo ""

# ============================================================================
# CLOUD-SPECIFIC PREREQUISITES
# ============================================================================

if [[ "$CLOUD_PROVIDER" == "azure" ]]; then
    echo -e "${BLUE}[1/6] Checking Azure Prerequisites...${NC}"
    
    # Check Azure CLI
    if ! command -v az &> /dev/null; then
        echo -e "${RED}✗ Azure CLI is not installed${NC}"
        echo -e "${YELLOW}Install Azure CLI:${NC}"
        echo "  macOS: brew install azure-cli"
        echo "  Linux: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash"
        echo "  Windows: https://aka.ms/installazurecliwindows"
        exit 1
    fi
    echo -e "${GREEN}✓ Azure CLI is installed${NC}"
    
    # Check Azure login
    if ! az account show &> /dev/null; then
        echo -e "${YELLOW}⚠ Not logged in to Azure${NC}"
        echo -e "${CYAN}Logging in to Azure...${NC}"
        az login
        if [ $? -ne 0 ]; then
            echo -e "${RED}✗ Azure login failed${NC}"
            exit 1
        fi
    fi
    echo -e "${GREEN}✓ Logged in to Azure${NC}"
    
    # Display current subscription
    SUBSCRIPTION=$(az account show --query name -o tsv)
    echo -e "${CYAN}Current subscription:${NC} $SUBSCRIPTION"
    echo ""
    
    TERRAFORM_DIR="terraform-azure"
    STEP_OFFSET=1
else
    echo -e "${BLUE}[1/5] Checking Docker...${NC}"
    if ! docker info > /dev/null 2>&1; then
        echo -e "${RED}✗ Docker is not running${NC}"
        echo -e "${YELLOW}Please start Docker:${NC}"
        echo "  For Docker Desktop: open -a Docker"
        echo "  For Rancher Desktop: open -a 'Rancher Desktop' OR rdctl start"
        exit 1
    fi
    echo -e "${GREEN}✓ Docker is running${NC}"
    echo ""
    
    TERRAFORM_DIR="terraform"
    STEP_OFFSET=0
fi

# ============================================================================
# BUILD DOCKER IMAGES
# ============================================================================

STEP=$((2 + STEP_OFFSET))
if [[ "$SKIP_BUILD" == false ]]; then
    echo -e "${BLUE}[$STEP/$(( 5 + STEP_OFFSET ))] Building Docker images...${NC}"
    echo ""
    
    echo -e "${YELLOW}Building Bank 1 (Savings) image...${NC}"
    cd bank1-savings
    if docker build -t bank1-savings:latest . > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Bank 1 image built successfully${NC}"
    else
        echo -e "${RED}✗ Failed to build Bank 1 image${NC}"
        exit 1
    fi
    echo ""
    
    echo -e "${YELLOW}Building Bank 2 (Investment) image...${NC}"
    cd ../bank2-investment
    if docker build -t bank2-investment:latest . > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Bank 2 image built successfully${NC}"
    else
        echo -e "${RED}✗ Failed to build Bank 2 image${NC}"
        exit 1
    fi
    cd ..
    echo ""
else
    echo -e "${YELLOW}[$STEP/$(( 5 + STEP_OFFSET ))] Skipping Docker image build${NC}"
    echo ""
fi

# ============================================================================
# AZURE-SPECIFIC: PUSH IMAGES TO ACR
# ============================================================================

if [[ "$CLOUD_PROVIDER" == "azure" ]]; then
    STEP=$((3 + STEP_OFFSET))
    echo -e "${BLUE}[$STEP/$(( 5 + STEP_OFFSET ))] Pushing images to Azure Container Registry...${NC}"
    echo ""
    
    # Check if ACR exists, if not, we'll create it with Terraform first
    cd $TERRAFORM_DIR
    
    # Initialize Terraform if needed
    if [ ! -d ".terraform" ]; then
        echo -e "${YELLOW}Initializing Terraform...${NC}"
        terraform init
        echo ""
    fi
    
    # Check if terraform.tfvars exists
    if [ ! -f "terraform.tfvars" ]; then
        echo -e "${YELLOW}⚠ terraform.tfvars not found${NC}"
        echo -e "${CYAN}Creating terraform.tfvars from example...${NC}"
        if [ -f "terraform.tfvars.example" ]; then
            cp terraform.tfvars.example terraform.tfvars
            echo -e "${YELLOW}Please edit terraform-azure/terraform.tfvars with your unique values:${NC}"
            echo "  - prefix (must be globally unique)"
            echo "  - acr_name (must be globally unique)"
            echo "  - storage_account_name (must be globally unique)"
            echo ""
            echo -e "${RED}Exiting. Please configure terraform.tfvars and run again.${NC}"
            exit 1
        fi
    fi
    
    # Apply Terraform to create ACR (if it doesn't exist)
    echo -e "${YELLOW}Ensuring Azure Container Registry exists...${NC}"
    terraform apply -target=azurerm_resource_group.banking -target=azurerm_container_registry.banking -auto-approve
    
    # Get ACR details
    ACR_NAME=$(terraform output -raw acr_login_server 2>/dev/null | cut -d'.' -f1)
    ACR_LOGIN_SERVER=$(terraform output -raw acr_login_server 2>/dev/null)
    
    if [ -z "$ACR_LOGIN_SERVER" ]; then
        echo -e "${RED}✗ Failed to get ACR login server${NC}"
        exit 1
    fi
    
    echo -e "${CYAN}ACR Login Server:${NC} $ACR_LOGIN_SERVER"
    
    # Login to ACR
    echo -e "${YELLOW}Logging in to ACR...${NC}"
    az acr login --name $ACR_NAME
    
    # Tag and push images
    cd ..
    echo -e "${YELLOW}Tagging and pushing Bank 1 image...${NC}"
    docker tag bank1-savings:latest $ACR_LOGIN_SERVER/bank1-savings:latest
    docker push $ACR_LOGIN_SERVER/bank1-savings:latest
    echo -e "${GREEN}✓ Bank 1 image pushed${NC}"
    
    echo -e "${YELLOW}Tagging and pushing Bank 2 image...${NC}"
    docker tag bank2-investment:latest $ACR_LOGIN_SERVER/bank2-investment:latest
    docker push $ACR_LOGIN_SERVER/bank2-investment:latest
    echo -e "${GREEN}✓ Bank 2 image pushed${NC}"
    echo ""
fi

# ============================================================================
# TERRAFORM - INFRASTRUCTURE PROVISIONING
# ============================================================================

STEP=$((3 + STEP_OFFSET))
if [[ "$CLOUD_PROVIDER" == "azure" ]]; then
    STEP=$((4 + STEP_OFFSET))
fi

echo -e "${BLUE}[$STEP/$(( 5 + STEP_OFFSET ))] Terraform - Provisioning Infrastructure...${NC}"
if [[ "$CLOUD_PROVIDER" == "azure" ]]; then
    echo -e "${CYAN}Purpose: Create Azure Container Instances, Storage, Networking${NC}"
else
    echo -e "${CYAN}Purpose: Create containers, networks, and volumes${NC}"
fi
echo ""

cd $TERRAFORM_DIR

# Initialize if needed
if [ ! -d ".terraform" ]; then
    echo -e "${YELLOW}Initializing Terraform...${NC}"
    terraform init
    echo ""
fi

# Apply configuration
echo -e "${YELLOW}Applying Terraform configuration...${NC}"
if [[ "$AUTO_APPROVE" == true ]]; then
    APPROVE_FLAG="-auto-approve"
else
    APPROVE_FLAG=""
fi

if terraform apply $APPROVE_FLAG; then
    echo ""
    echo -e "${GREEN}✓ Infrastructure provisioned successfully${NC}"
else
    echo ""
    echo -e "${RED}✗ Terraform provisioning failed${NC}"
    exit 1
fi

# Show infrastructure details
echo ""
echo -e "${CYAN}Infrastructure Created:${NC}"
if [[ "$CLOUD_PROVIDER" == "azure" ]]; then
    terraform output -json deployment_summary 2>/dev/null | jq -r '
        "  Resource Group: " + .resource_group.name,
        "  Location: " + .resource_group.location,
        "  Container Registry: " + .container_registry.name,
        "  Storage Account: " + .storage.account_name,
        "  Bank 1 Container: " + .bank1.name,
        "  Bank 2 Container: " + .bank2.name
    ' 2>/dev/null || echo "  (Terraform outputs available)"
else
    terraform output -json | jq -r '
        "  Network: " + .network_name.value,
        "  Bank 1 Container: " + .bank1_container_name.value,
        "  Bank 2 Container: " + .bank2_container_name.value,
        "  Bank 1 Volume: " + .bank1_volume.value,
        "  Bank 2 Volume: " + .bank2_volume.value,
        "  Monitoring Volume: " + .monitoring_volume.value,
        "  Backup Volume: " + .backup_volume.value
    ' 2>/dev/null || echo "  (Terraform outputs available)"
fi

cd ..
echo ""

# ============================================================================
# ANSIBLE - CONFIGURATION MANAGEMENT (Local only for now)
# ============================================================================

if [[ "$CLOUD_PROVIDER" == "local" ]]; then
    STEP=$((4 + STEP_OFFSET))
    echo -e "${BLUE}[$STEP/$(( 5 + STEP_OFFSET ))] Ansible - Configuring Applications...${NC}"
    echo -e "${CYAN}Purpose: Configure environment, monitoring, backups, health checks${NC}"
    echo ""
    
    cd ansible
    
    # Install collections if needed
    if ! ansible-galaxy collection list 2>/dev/null | grep -q community.docker; then
        echo -e "${YELLOW}Installing Ansible collections...${NC}"
        ansible-galaxy collection install -r requirements.yml
        echo ""
    fi
    
    # Run playbook
    echo -e "${YELLOW}Running Ansible playbook...${NC}"
    if ansible-playbook playbook.yml; then
        echo ""
        echo -e "${GREEN}✓ Applications configured successfully${NC}"
    else
        echo ""
        echo -e "${RED}✗ Ansible configuration failed${NC}"
        exit 1
    fi
    
    cd ..
    echo ""
fi

# ============================================================================
# VERIFICATION
# ============================================================================

STEP=$((5 + STEP_OFFSET))
echo -e "${BLUE}[$STEP/$(( 5 + STEP_OFFSET ))] Verifying Deployment...${NC}"
echo ""

# Wait a moment for containers to stabilize
sleep 3

if [[ "$CLOUD_PROVIDER" == "azure" ]]; then
    cd $TERRAFORM_DIR
    BANK1_URL=$(terraform output -raw bank1_url 2>/dev/null)
    BANK2_URL=$(terraform output -raw bank2_url 2>/dev/null)
    cd ..
    
    echo -e "${YELLOW}Checking Bank 1 (Savings)...${NC}"
    if curl -s -f "$BANK1_URL/health" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Bank 1 is responding${NC}"
    else
        echo -e "${YELLOW}⚠ Bank 1 is not responding yet (Azure containers may take 1-2 minutes to start)${NC}"
    fi
    
    echo -e "${YELLOW}Checking Bank 2 (Investment)...${NC}"
    if curl -s -f "$BANK2_URL/health" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Bank 2 is responding${NC}"
    else
        echo -e "${YELLOW}⚠ Bank 2 is not responding yet (Azure containers may take 1-2 minutes to start)${NC}"
    fi
else
    # Check Bank 1
    echo -e "${YELLOW}Checking Bank 1 (Savings)...${NC}"
    if curl -s -f http://localhost:5001/health > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Bank 1 is responding${NC}"
    else
        echo -e "${YELLOW}⚠ Bank 1 is not responding yet (may need more time)${NC}"
    fi
    
    # Check Bank 2
    echo -e "${YELLOW}Checking Bank 2 (Investment)...${NC}"
    if curl -s -f http://localhost:5002/health > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Bank 2 is responding${NC}"
    else
        echo -e "${YELLOW}⚠ Bank 2 is not responding yet (may need more time)${NC}"
    fi
fi

# ============================================================================
# DEPLOYMENT SUMMARY
# ============================================================================

echo ""
echo -e "${BLUE}============================================"
echo "Deployment Complete!"
echo -e "============================================${NC}"
echo ""
echo -e "${GREEN}✓ Infrastructure provisioned (Terraform)${NC}"
if [[ "$CLOUD_PROVIDER" == "local" ]]; then
    echo -e "${GREEN}✓ Applications configured (Ansible)${NC}"
fi
echo ""

if [[ "$CLOUD_PROVIDER" == "azure" ]]; then
    cd $TERRAFORM_DIR
    echo -e "${CYAN}Access URLs:${NC}"
    echo "  Bank 1 (Savings):    $(terraform output -raw bank1_url 2>/dev/null)"
    echo "  Bank 2 (Investment): $(terraform output -raw bank2_url 2>/dev/null)"
    echo ""
    echo -e "${CYAN}Azure Resources:${NC}"
    echo "  Resource Group: $(terraform output -raw resource_group_name 2>/dev/null)"
    echo "  Location: $(terraform output -raw resource_group_location 2>/dev/null)"
    echo ""
    echo -e "${CYAN}Management Commands:${NC}"
    echo ""
    echo -e "${YELLOW}View Container Logs:${NC}"
    echo "  az container logs --resource-group \$(cd $TERRAFORM_DIR && terraform output -raw resource_group_name) --name \$(cd $TERRAFORM_DIR && terraform output -json deployment_summary | jq -r '.bank1.name')"
    echo ""
    echo -e "${YELLOW}View in Azure Portal:${NC}"
    echo "  https://portal.azure.com"
    echo ""
    echo -e "${YELLOW}Destroy Resources:${NC}"
    echo "  cd $TERRAFORM_DIR && terraform destroy"
    cd ..
else
    echo -e "${CYAN}Access URLs:${NC}"
    echo "  Bank 1 (Savings):    http://localhost:5001"
    echo "  Bank 2 (Investment): http://localhost:5002"
    echo ""
    echo -e "${CYAN}Management Scripts (created by Ansible):${NC}"
    echo "  Monitor Bank 1:  /tmp/monitor_bank1.sh"
    echo "  Monitor Bank 2:  /tmp/monitor_bank2.sh"
    echo "  Backup Data:     /tmp/backup_banks.sh"
    echo "  Rotate Logs:     /tmp/rotate_logs.sh"
    echo ""
    echo -e "${CYAN}Example Usage:${NC}"
    echo ""
    echo -e "${YELLOW}1. View Bank 1 Dashboard:${NC}"
    echo "   open http://localhost:5001"
    echo ""
    echo -e "${YELLOW}2. Monitor Health (run in background):${NC}"
    echo "   /tmp/monitor_bank1.sh > /tmp/bank1_monitor.log 2>&1 &"
    echo "   /tmp/monitor_bank2.sh > /tmp/bank2_monitor.log 2>&1 &"
    echo ""
    echo -e "${YELLOW}3. Create Backup:${NC}"
    echo "   /tmp/backup_banks.sh"
    echo ""
    echo -e "${YELLOW}4. Test Inter-Bank Transfer:${NC}"
    echo "   curl -X POST http://localhost:5001/api/transfer \\"
    echo "     -H \"Content-Type: application/json\" \\"
    echo "     -d '{\"customer_id\": 1, \"amount\": 100.0}'"
    echo ""
    echo -e "${YELLOW}5. View Terraform State:${NC}"
    echo "   cd terraform && terraform show"
    echo ""
    echo -e "${YELLOW}6. Re-run Ansible Configuration:${NC}"
    echo "   cd ansible && ansible-playbook playbook.yml"
    echo ""
    echo -e "${YELLOW}7. Destroy Everything:${NC}"
    echo "   cd terraform && terraform destroy -auto-approve"
fi

echo ""
echo -e "${BLUE}============================================${NC}"
echo ""

# Made with Bob
