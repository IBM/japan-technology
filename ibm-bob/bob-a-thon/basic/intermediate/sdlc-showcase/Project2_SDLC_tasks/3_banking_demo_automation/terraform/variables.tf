variable "network_name" {
  description = "Name of the Docker network for banking applications"
  type        = string
  default     = "banking-network"
}

variable "bank1_container_name" {
  description = "Name of the Bank 1 (Savings) container"
  type        = string
  default     = "bank1-savings"
}

variable "bank2_container_name" {
  description = "Name of the Bank 2 (Investment) container"
  type        = string
  default     = "bank2-investment"
}

variable "bank1_port" {
  description = "External port for Bank 1 (Savings) application"
  type        = number
  default     = 5001
  
  validation {
    condition     = var.bank1_port > 1024 && var.bank1_port < 65535
    error_message = "Port must be between 1024 and 65535"
  }
}

variable "bank2_port" {
  description = "External port for Bank 2 (Investment) application"
  type        = number
  default     = 5002
  
  validation {
    condition     = var.bank2_port > 1024 && var.bank2_port < 65535
    error_message = "Port must be between 1024 and 65535"
  }
}
# ============================================================================
# TERRAFORM VARIABLES - INFRASTRUCTURE CONFIGURATION
# ============================================================================

variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}
