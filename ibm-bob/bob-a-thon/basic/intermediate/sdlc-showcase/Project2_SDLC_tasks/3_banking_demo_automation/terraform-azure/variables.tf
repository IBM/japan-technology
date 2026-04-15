# ============================================================================
# Azure Banking Demo - Variables
# ============================================================================

variable "resource_group_name" {
  description = "Name of the Azure resource group"
  type        = string
  default     = "banking-demo-rg"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "eastus"
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "prefix" {
  description = "Prefix for resource names (must be globally unique)"
  type        = string
  default     = "bankdemo"
  
  validation {
    condition     = can(regex("^[a-z0-9]{3,15}$", var.prefix))
    error_message = "Prefix must be 3-15 lowercase alphanumeric characters."
  }
}

variable "acr_name" {
  description = "Name of the Azure Container Registry (must be globally unique)"
  type        = string
  default     = "bankdemoacr"
  
  validation {
    condition     = can(regex("^[a-zA-Z0-9]{5,50}$", var.acr_name))
    error_message = "ACR name must be 5-50 alphanumeric characters."
  }
}

variable "storage_account_name" {
  description = "Name of the storage account (must be globally unique)"
  type        = string
  default     = "bankdemostorage"
  
  validation {
    condition     = can(regex("^[a-z0-9]{3,24}$", var.storage_account_name))
    error_message = "Storage account name must be 3-24 lowercase alphanumeric characters."
  }
}

variable "bank1_cpu" {
  description = "CPU cores for Bank 1 container"
  type        = number
  default     = 1.0
}

variable "bank1_memory" {
  description = "Memory in GB for Bank 1 container"
  type        = number
  default     = 1.5
}

variable "bank2_cpu" {
  description = "CPU cores for Bank 2 container"
  type        = number
  default     = 1.0
}

variable "bank2_memory" {
  description = "Memory in GB for Bank 2 container"
  type        = number
  default     = 1.5
}

variable "tags" {
  description = "Additional tags for resources"
  type        = map(string)
  default     = {}
}