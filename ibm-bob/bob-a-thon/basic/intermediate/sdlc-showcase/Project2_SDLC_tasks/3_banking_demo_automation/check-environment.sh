#!/bin/bash

# Banking Demo - Environment Check Script
# Verifies all prerequisites are met before deployment

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================="
echo "Banking Demo - Environment Check"
echo -e "==========================================${NC}"
echo ""

ISSUES=0

# Check 1: Docker Installation
echo -e "${BLUE}1. Checking Docker installation...${NC}"
if command -v docker > /dev/null 2>&1; then
    DOCKER_VERSION=$(docker --version)
    echo -e "   ${GREEN}✓ Docker is installed: $DOCKER_VERSION${NC}"
else
    echo -e "   ${RED}✗ Docker is NOT installed${NC}"
    echo -e "   ${YELLOW}  Install: brew install --cask docker${NC}"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check 2: Docker Daemon Running
echo -e "${BLUE}2. Checking Docker daemon...${NC}"
if docker info > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓ Docker daemon is running${NC}"
    DOCKER_INFO=$(docker info --format '{{.ServerVersion}}')
    echo -e "   ${GREEN}  Server version: $DOCKER_INFO${NC}"
else
    echo -e "   ${RED}✗ Docker daemon is NOT running${NC}"
    echo -e "   ${YELLOW}  For Docker Desktop: open -a Docker${NC}"
    echo -e "   ${YELLOW}  For Rancher Desktop: open -a 'Rancher Desktop' OR rdctl start${NC}"
    echo -e "   ${YELLOW}  Wait 10-30 seconds for Docker to start${NC}"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check 3: Terraform Installation
echo -e "${BLUE}3. Checking Terraform installation...${NC}"
if command -v terraform > /dev/null 2>&1; then
    TERRAFORM_VERSION=$(terraform version -json 2>/dev/null | grep -o '"terraform_version":"[^"]*"' | cut -d'"' -f4)
    echo -e "   ${GREEN}✓ Terraform is installed: v$TERRAFORM_VERSION${NC}"
else
    echo -e "   ${RED}✗ Terraform is NOT installed${NC}"
    echo -e "   ${YELLOW}  Install: brew install terraform${NC}"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check 4: Ansible Installation
echo -e "${BLUE}4. Checking Ansible installation...${NC}"
if command -v ansible > /dev/null 2>&1; then
    ANSIBLE_VERSION=$(ansible --version | head -1 | awk '{print $3}')
    echo -e "   ${GREEN}✓ Ansible is installed: v$ANSIBLE_VERSION${NC}"
else
    echo -e "   ${RED}✗ Ansible is NOT installed${NC}"
    echo -e "   ${YELLOW}  Install: brew install ansible${NC}"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check 5: Port Availability
echo -e "${BLUE}5. Checking port availability...${NC}"
if lsof -i :5001 > /dev/null 2>&1; then
    echo -e "   ${RED}✗ Port 5001 is in use${NC}"
    echo -e "   ${YELLOW}  Process using port 5001:${NC}"
    lsof -i :5001 | tail -n +2
    ISSUES=$((ISSUES + 1))
else
    echo -e "   ${GREEN}✓ Port 5001 is available${NC}"
fi

if lsof -i :5002 > /dev/null 2>&1; then
    echo -e "   ${RED}✗ Port 5002 is in use${NC}"
    echo -e "   ${YELLOW}  Process using port 5002:${NC}"
    lsof -i :5002 | tail -n +2
    ISSUES=$((ISSUES + 1))
else
    echo -e "   ${GREEN}✓ Port 5002 is available${NC}"
fi
echo ""

# Check 6: Existing Banking Containers
echo -e "${BLUE}6. Checking for existing banking containers...${NC}"
if docker ps -a 2>/dev/null | grep -q bank; then
    echo -e "   ${YELLOW}⚠ Banking containers found:${NC}"
    docker ps -a | grep bank
    echo -e "   ${YELLOW}  Run cleanup before deploying:${NC}"
    echo -e "   ${YELLOW}  cd terraform && terraform destroy${NC}"
    echo -e "   ${YELLOW}  OR: cd ansible && ansible-playbook playbook.yml --tags cleanup${NC}"
else
    echo -e "   ${GREEN}✓ No existing banking containers${NC}"
fi
echo ""

# Check 7: Disk Space
echo -e "${BLUE}7. Checking disk space...${NC}"
AVAILABLE_SPACE=$(df -h . | tail -1 | awk '{print $4}')
echo -e "   ${GREEN}✓ Available space: $AVAILABLE_SPACE${NC}"
echo ""

# Check 8: Required Files
echo -e "${BLUE}8. Checking project files...${NC}"
REQUIRED_FILES=(
    "bank1-savings/app.py"
    "bank1-savings/Dockerfile"
    "bank2-investment/app.py"
    "bank2-investment/Dockerfile"
    "terraform/main.tf"
    "ansible/playbook.yml"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "   ${GREEN}✓ $file${NC}"
    else
        echo -e "   ${RED}✗ $file missing${NC}"
        ISSUES=$((ISSUES + 1))
    fi
done
echo ""

# Check 9: Python (for local testing)
echo -e "${BLUE}9. Checking Python installation...${NC}"
if command -v python3 > /dev/null 2>&1; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "   ${GREEN}✓ Python is installed: $PYTHON_VERSION${NC}"
else
    echo -e "   ${YELLOW}⚠ Python3 not found (optional for local testing)${NC}"
fi
echo ""

# Check 10: curl and jq (for testing)
echo -e "${BLUE}10. Checking testing tools...${NC}"
if command -v curl > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓ curl is installed${NC}"
else
    echo -e "   ${YELLOW}⚠ curl not found (needed for testing)${NC}"
    echo -e "   ${YELLOW}  Install: brew install curl${NC}"
fi

if command -v jq > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓ jq is installed${NC}"
else
    echo -e "   ${YELLOW}⚠ jq not found (optional, for pretty JSON)${NC}"
    echo -e "   ${YELLOW}  Install: brew install jq${NC}"
fi
echo ""

# Summary
echo -e "${BLUE}=========================================="
echo "Summary"
echo -e "==========================================${NC}"

if [ $ISSUES -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed! Ready to deploy.${NC}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "  1. Deploy with Terraform:"
    echo "     cd terraform && terraform init && terraform apply"
    echo ""
    echo "  2. OR deploy with Ansible:"
    echo "     cd ansible && ansible-galaxy collection install -r requirements.yml"
    echo "     ansible-playbook playbook.yml"
else
    echo -e "${RED}✗ Found $ISSUES issue(s) that need to be resolved.${NC}"
    echo ""
    echo -e "${YELLOW}Please fix the issues above before deploying.${NC}"
    echo ""
    echo -e "${BLUE}Common fixes:${NC}"
    echo "  • Start Docker Desktop: open -a Docker"
    echo "  • Start Rancher Desktop: open -a 'Rancher Desktop' OR rdctl start"
    echo "  • Install Terraform: brew install terraform"
    echo "  • Install Ansible: brew install ansible"
    echo "  • Free up ports: kill -9 <PID>"
fi

echo -e "${BLUE}==========================================${NC}"

exit $ISSUES

# Made with Bob
