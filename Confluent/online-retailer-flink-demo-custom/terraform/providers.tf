# AWS provider configuration
# This is required to manage AWS resources. The region is dynamically set via a variable.
provider "aws" {
  region = var.cloud_region
  # Default tags to apply to all resources
  default_tags {
    tags = {
      Created_by = "Shift-left Terraform script"
      Project    = "Shift-left Demo"
    }
  }
}

# Here we are using the Confluent provider for managing Confluent Cloud resources.
terraform {
  required_providers {
    confluent = {
      source  = "confluentinc/confluent"
      version = "2.32.0"
    }
    external = {
      source  = "hashicorp/external"
      version = "~> 2.3"
    }
  }
}

provider "confluent" {
  cloud_api_key    = var.confluent_cloud_api_key
  cloud_api_secret = var.confluent_cloud_api_secret
}

# Local provider for accessing and managing local system resources.
# This is useful for tasks like rendering templates, reading local files, etc.
provider "local" {}

# TLS provider for generating SSH key pairs.
provider "tls" {}

# NOTE: Docker provider removed - images are now built externally and pushed to ECR.
# See REMOVE_DOCKER_BUILD.md for instructions on building and pushing images.
