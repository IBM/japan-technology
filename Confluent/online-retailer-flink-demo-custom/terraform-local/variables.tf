variable "prefix" {
  description = "Prefix for resource names"
  type        = string
  default     = "local-workshop"
}

variable "cloud_region" {
  description = "Confluent Cloud Region"
  type        = string
  default     = "us-east-1"
}

variable "confluent_cloud_api_key" {
  description = "Confluent Cloud API Key (generated via Confluent CLI)"
  type        = string
  sensitive   = true
}

variable "confluent_cloud_api_secret" {
  description = "Confluent Cloud API Secret (generated via Confluent CLI)"
  type        = string
  sensitive   = true
}