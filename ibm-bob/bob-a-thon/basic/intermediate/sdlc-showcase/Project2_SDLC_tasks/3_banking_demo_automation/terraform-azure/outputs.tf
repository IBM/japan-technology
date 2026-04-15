# ============================================================================
# Azure Banking Demo - Outputs
# ============================================================================

output "resource_group_name" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.banking.name
}

output "resource_group_location" {
  description = "Location of the resource group"
  value       = azurerm_resource_group.banking.location
}

output "acr_login_server" {
  description = "Azure Container Registry login server"
  value       = azurerm_container_registry.banking.login_server
}

output "acr_admin_username" {
  description = "Azure Container Registry admin username"
  value       = azurerm_container_registry.banking.admin_username
  sensitive   = true
}

output "acr_admin_password" {
  description = "Azure Container Registry admin password"
  value       = azurerm_container_registry.banking.admin_password
  sensitive   = true
}

output "storage_account_name" {
  description = "Name of the storage account"
  value       = azurerm_storage_account.banking.name
}

output "storage_account_key" {
  description = "Primary access key for storage account"
  value       = azurerm_storage_account.banking.primary_access_key
  sensitive   = true
}

output "bank1_fqdn" {
  description = "Fully qualified domain name for Bank 1"
  value       = azurerm_container_group.bank1.fqdn
}

output "bank1_ip_address" {
  description = "Public IP address for Bank 1"
  value       = azurerm_container_group.bank1.ip_address
}

output "bank1_url" {
  description = "URL to access Bank 1 (Savings)"
  value       = "http://${azurerm_container_group.bank1.fqdn}:5000"
}

output "bank2_fqdn" {
  description = "Fully qualified domain name for Bank 2"
  value       = azurerm_container_group.bank2.fqdn
}

output "bank2_ip_address" {
  description = "Public IP address for Bank 2"
  value       = azurerm_container_group.bank2.ip_address
}

output "bank2_url" {
  description = "URL to access Bank 2 (Investment)"
  value       = "http://${azurerm_container_group.bank2.fqdn}:5000"
}

output "deployment_summary" {
  description = "Summary of deployed resources"
  value = {
    resource_group = {
      name     = azurerm_resource_group.banking.name
      location = azurerm_resource_group.banking.location
    }
    container_registry = {
      name         = azurerm_container_registry.banking.name
      login_server = azurerm_container_registry.banking.login_server
    }
    storage = {
      account_name = azurerm_storage_account.banking.name
      shares = {
        bank1_data      = azurerm_storage_share.bank1_data.name
        bank2_data      = azurerm_storage_share.bank2_data.name
        monitoring_data = azurerm_storage_share.monitoring_data.name
        backup_data     = azurerm_storage_share.backup_data.name
      }
    }
    bank1 = {
      name       = azurerm_container_group.bank1.name
      fqdn       = azurerm_container_group.bank1.fqdn
      ip_address = azurerm_container_group.bank1.ip_address
      url        = "http://${azurerm_container_group.bank1.fqdn}:5000"
    }
    bank2 = {
      name       = azurerm_container_group.bank2.name
      fqdn       = azurerm_container_group.bank2.fqdn
      ip_address = azurerm_container_group.bank2.ip_address
      url        = "http://${azurerm_container_group.bank2.fqdn}:5000"
    }
  }
}

output "next_steps" {
  description = "Next steps after deployment"
  value = <<-EOT
    ============================================
    Azure Deployment Complete!
    ============================================
    
    Access URLs:
      Bank 1 (Savings):    http://${azurerm_container_group.bank1.fqdn}:5000
      Bank 2 (Investment): http://${azurerm_container_group.bank2.fqdn}:5000
    
    Container Registry:
      Server: ${azurerm_container_registry.banking.login_server}
      
    Storage Account:
      Name: ${azurerm_storage_account.banking.name}
      
    To view logs:
      az container logs --resource-group ${azurerm_resource_group.banking.name} --name ${azurerm_container_group.bank1.name}
      az container logs --resource-group ${azurerm_resource_group.banking.name} --name ${azurerm_container_group.bank2.name}
    
    To destroy resources:
      cd terraform-azure && terraform destroy
    ============================================
  EOT
}