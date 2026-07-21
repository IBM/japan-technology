variable "customer_role_name" {
  description = "The name of the IAM role to create."
  type        = string
}

variable "provider_integration_role_arn" {
  description = "The ARN of the provider integration role that can assume this role."
  type        = string
}

variable "provider_integration_external_id" {
  description = "The external ID required by the provider integration for assuming the role."
  type        = string
}

variable "s3_bucket_name" {
  description = "The name of the S3 bucket to grant access to."
  type        = string
}


variable "random_suffix" {
  description = "A random integer suffix for uniqueness."
  type        = string
}

variable "aws_account_id" {
  description = "The AWS account ID where the role will be created."
  type        = string
  
}