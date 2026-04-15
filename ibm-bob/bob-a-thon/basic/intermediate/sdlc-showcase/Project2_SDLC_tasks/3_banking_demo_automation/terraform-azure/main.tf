# ============================================================================
# Azure Banking Demo - Terraform Configuration
# ============================================================================
# This configuration deploys the banking applications to Azure Container Instances
# with Azure File Shares for persistent storage and Azure Container Registry
# ============================================================================

terraform {
  required_version = ">= 1.0"
  
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# ============================================================================
# RESOURCE GROUP
# ============================================================================

resource "azurerm_resource_group" "banking" {
  name     = var.resource_group_name
  location = var.location
  
  tags = {
    Environment = var.environment
    Project     = "Banking Demo"
    ManagedBy   = "Terraform"
  }
}

# ============================================================================
# AZURE CONTAINER REGISTRY
# ============================================================================

resource "azurerm_container_registry" "banking" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.banking.name
  location            = azurerm_resource_group.banking.location
  sku                 = "Basic"
  admin_enabled       = true
  
  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# ============================================================================
# STORAGE ACCOUNT FOR PERSISTENT DATA
# ============================================================================

resource "azurerm_storage_account" "banking" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.banking.name
  location                 = azurerm_resource_group.banking.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  
  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# File shares for persistent storage
resource "azurerm_storage_share" "bank1_data" {
  name                 = "bank1-data"
  storage_account_name = azurerm_storage_account.banking.name
  quota                = 5
}

resource "azurerm_storage_share" "bank2_data" {
  name                 = "bank2-data"
  storage_account_name = azurerm_storage_account.banking.name
  quota                = 5
}

resource "azurerm_storage_share" "monitoring_data" {
  name                 = "monitoring-data"
  storage_account_name = azurerm_storage_account.banking.name
  quota                = 5
}

resource "azurerm_storage_share" "backup_data" {
  name                 = "backup-data"
  storage_account_name = azurerm_storage_account.banking.name
  quota                = 10
}

# ============================================================================
# VIRTUAL NETWORK
# ============================================================================

resource "azurerm_virtual_network" "banking" {
  name                = "${var.prefix}-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.banking.location
  resource_group_name = azurerm_resource_group.banking.name
  
  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

resource "azurerm_subnet" "banking" {
  name                 = "${var.prefix}-subnet"
  resource_group_name  = azurerm_resource_group.banking.name
  virtual_network_name = azurerm_virtual_network.banking.name
  address_prefixes     = ["10.0.1.0/24"]
  
  delegation {
    name = "acidelegation"
    
    service_delegation {
      name    = "Microsoft.ContainerInstance/containerGroups"
      actions = ["Microsoft.Network/virtualNetworks/subnets/action"]
    }
  }
}

# ============================================================================
# NETWORK SECURITY GROUP
# ============================================================================

resource "azurerm_network_security_group" "banking" {
  name                = "${var.prefix}-nsg"
  location            = azurerm_resource_group.banking.location
  resource_group_name = azurerm_resource_group.banking.name
  
  security_rule {
    name                       = "AllowHTTP"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_ranges    = ["80", "5001", "5002"]
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  
  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

resource "azurerm_subnet_network_security_group_association" "banking" {
  subnet_id                 = azurerm_subnet.banking.id
  network_security_group_id = azurerm_network_security_group.banking.id
}

# ============================================================================
# CONTAINER GROUP - BANK 1 (SAVINGS)
# ============================================================================

resource "azurerm_container_group" "bank1" {
  name                = "${var.prefix}-bank1-savings"
  location            = azurerm_resource_group.banking.location
  resource_group_name = azurerm_resource_group.banking.name
  ip_address_type     = "Public"
  dns_name_label      = "${var.prefix}-bank1"
  os_type             = "Linux"
  
  image_registry_credential {
    server   = azurerm_container_registry.banking.login_server
    username = azurerm_container_registry.banking.admin_username
    password = azurerm_container_registry.banking.admin_password
  }
  
  container {
    name   = "bank1-savings"
    image  = "${azurerm_container_registry.banking.login_server}/bank1-savings:latest"
    cpu    = "1.0"
    memory = "1.5"
    
    ports {
      port     = 5000
      protocol = "TCP"
    }
    
    environment_variables = {
      BANK_NAME = "Savings Bank"
      BANK_ID   = "bank1"
      BANK2_URL = "http://${var.prefix}-bank2.${var.location}.azurecontainer.io:5000"
    }
    
    volume {
      name                 = "bank1-data"
      mount_path           = "/app/data"
      storage_account_name = azurerm_storage_account.banking.name
      storage_account_key  = azurerm_storage_account.banking.primary_access_key
      share_name           = azurerm_storage_share.bank1_data.name
    }
  }
  
  tags = {
    Environment = var.environment
    Bank        = "Savings"
    ManagedBy   = "Terraform"
  }
  
  depends_on = [
    azurerm_subnet_network_security_group_association.banking
  ]
}

# ============================================================================
# CONTAINER GROUP - BANK 2 (INVESTMENT)
# ============================================================================

resource "azurerm_container_group" "bank2" {
  name                = "${var.prefix}-bank2-investment"
  location            = azurerm_resource_group.banking.location
  resource_group_name = azurerm_resource_group.banking.name
  ip_address_type     = "Public"
  dns_name_label      = "${var.prefix}-bank2"
  os_type             = "Linux"
  
  image_registry_credential {
    server   = azurerm_container_registry.banking.login_server
    username = azurerm_container_registry.banking.admin_username
    password = azurerm_container_registry.banking.admin_password
  }
  
  container {
    name   = "bank2-investment"
    image  = "${azurerm_container_registry.banking.login_server}/bank2-investment:latest"
    cpu    = "1.0"
    memory = "1.5"
    
    ports {
      port     = 5000
      protocol = "TCP"
    }
    
    environment_variables = {
      BANK_NAME = "Investment Bank"
      BANK_ID   = "bank2"
    }
    
    volume {
      name                 = "bank2-data"
      mount_path           = "/app/data"
      storage_account_name = azurerm_storage_account.banking.name
      storage_account_key  = azurerm_storage_account.banking.primary_access_key
      share_name           = azurerm_storage_share.bank2_data.name
    }
  }
  
  tags = {
    Environment = var.environment
    Bank        = "Investment"
    ManagedBy   = "Terraform"
  }
  
  depends_on = [
    azurerm_subnet_network_security_group_association.banking
  ]
}