variable "environment_id" {
  description = "The ID of the Confluent Cloud environment."
  type        = string
}


variable "customer_role_arn" {
  description = "The ARN of the customer S3 access IAM role."
  type        = string
}