# ============================================================================
# TERRAFORM OUTPUTS - FOR ANSIBLE CONSUMPTION
# ============================================================================
# These outputs provide infrastructure details to Ansible for configuration
# ============================================================================

# Network Information
output "network_id" {
  description = "Docker network ID for banking applications"
  value       = docker_network.banking_network.id
}

output "network_name" {
  description = "Docker network name"
  value       = docker_network.banking_network.name
}

# Bank 1 (Savings) Infrastructure
output "bank1_container_id" {
  description = "Bank 1 container ID"
  value       = docker_container.bank1_savings.id
}

output "bank1_container_name" {
  description = "Bank 1 container name"
  value       = docker_container.bank1_savings.name
}

output "bank1_ip_address" {
  description = "Bank 1 internal IP address"
  value       = docker_container.bank1_savings.network_data[0].ip_address
}

output "bank1_port" {
  description = "Bank 1 external port"
  value       = var.bank1_port
}

output "bank1_url" {
  description = "Bank 1 external URL"
  value       = "http://localhost:${var.bank1_port}"
}

output "bank1_volume" {
  description = "Bank 1 data volume name"
  value       = docker_volume.bank1_data.name
}

# Bank 2 (Investment) Infrastructure
output "bank2_container_id" {
  description = "Bank 2 container ID"
  value       = docker_container.bank2_investment.id
}

output "bank2_container_name" {
  description = "Bank 2 container name"
  value       = docker_container.bank2_investment.name
}

output "bank2_ip_address" {
  description = "Bank 2 internal IP address"
  value       = docker_container.bank2_investment.network_data[0].ip_address
}

output "bank2_port" {
  description = "Bank 2 external port"
  value       = var.bank2_port
}

output "bank2_url" {
  description = "Bank 2 external URL"
  value       = "http://localhost:${var.bank2_port}"
}

output "bank2_volume" {
  description = "Bank 2 data volume name"
  value       = docker_volume.bank2_data.name
}

# Volume Information
output "monitoring_volume" {
  description = "Monitoring data volume name"
  value       = docker_volume.monitoring_data.name
}

output "backup_volume" {
  description = "Backup data volume name"
  value       = docker_volume.backup_data.name
}

# Ansible Inventory (JSON format)
output "ansible_inventory" {
  description = "Ansible inventory in JSON format"
  value = jsonencode({
    banking_apps = {
      hosts = {
        bank1 = {
          ansible_connection        = "docker"
          ansible_docker_extra_args = "-H=unix:///var/run/docker.sock"
          container_id              = docker_container.bank1_savings.id
          container_name            = docker_container.bank1_savings.name
          bank_name                 = "Savings Bank"
          bank_id                   = "bank1"
          internal_port             = 5000
          external_port             = var.bank1_port
          data_volume               = docker_volume.bank1_data.name
          peer_container            = docker_container.bank2_investment.name
          peer_url                  = "http://${docker_container.bank2_investment.name}:5000"
        }
        bank2 = {
          ansible_connection        = "docker"
          ansible_docker_extra_args = "-H=unix:///var/run/docker.sock"
          container_id              = docker_container.bank2_investment.id
          container_name            = docker_container.bank2_investment.name
          bank_name                 = "Investment Bank"
          bank_id                   = "bank2"
          internal_port             = 5000
          external_port             = var.bank2_port
          data_volume               = docker_volume.bank2_data.name
          peer_container            = docker_container.bank1_savings.name
          peer_url                  = "http://${docker_container.bank1_savings.name}:5000"
        }
      }
      vars = {
        network_name      = docker_network.banking_network.name
        monitoring_volume = docker_volume.monitoring_data.name
        backup_volume     = docker_volume.backup_data.name
        environment       = var.environment
      }
    }
  })
}

# Summary output for display
output "deployment_summary" {
  description = "Deployment summary"
  value = {
    network = {
      name = docker_network.banking_network.name
      id   = docker_network.banking_network.id
    }
    bank1 = {
      name = docker_container.bank1_savings.name
      port = var.bank1_port
      url  = "http://localhost:${var.bank1_port}"
    }
    bank2 = {
      name = docker_container.bank2_investment.name
      port = var.bank2_port
      url  = "http://localhost:${var.bank2_port}"
    }
    volumes = {
      bank1_data      = docker_volume.bank1_data.name
      bank2_data      = docker_volume.bank2_data.name
      monitoring_data = docker_volume.monitoring_data.name
      backup_data     = docker_volume.backup_data.name
    }
  }
}