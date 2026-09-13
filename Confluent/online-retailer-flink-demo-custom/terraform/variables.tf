variable "prefix" {
  description = "Prefix for resource names"
  type        = string
  default     = "shiftleft"
}

variable "cloud_region" {
  description = "AWS Cloud Region"
  type        = string
}

variable "db_username" {
  description = "Postgres DB username"
  type        = string
  default     = "postgres"
}

variable "db_password" {
  description = "Postgres DB password"
  type        = string
  default     = "Admin123456!!"
}

variable "postgres_instance_type" {
  description = "EC2 instance type for PostgreSQL"
  type        = string
  default     = "t3.medium"
}

variable "confluent_cloud_api_key" {
  description = "Confluent Cloud API Key"
  type        = string
}

variable "confluent_cloud_api_secret" {
  description = "Confluent Cloud API Secret"
  type        = string
}

variable "image_tag" {
  description = "Docker image tag to deploy from ECR Public (e.g., 'latest', 'v1.0.0')"
  type        = string
  default     = "latest"
}

variable "cpu_architecture" {
  description = "CPU architecture for ECS tasks (must match the architecture of pre-built Docker images). Valid values: X86_64, ARM64"
  type        = string
  default     = "X86_64"

  validation {
    condition     = contains(["X86_64", "ARM64"], var.cpu_architecture)
    error_message = "cpu_architecture must be either X86_64 or ARM64"
  }
}

# -------------------------------
# ECR Public Image Configuration
# -------------------------------
# Images are pre-built and hosted on ECR Public by the workshop maintainer.
# Participants do not need to build or push images.

variable "ecr_public_alias" {
  description = "ECR Public registry alias (e.g., 'a1b2c3d4' from public.ecr.aws/a1b2c3d4/)"
  type        = string
  default     = "v3a9u0p7"
}

variable "payments_app_image_name" {
  description = "ECR Public repository name for payments app"
  type        = string
  default     = "payments-app"
}

variable "data_feeder_image_name" {
  description = "ECR Public repository name for postgresql data feeder app"
  type        = string
  default     = "postgresql-data-feeder"
}
