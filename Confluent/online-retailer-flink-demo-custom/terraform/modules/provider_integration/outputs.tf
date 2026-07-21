output "provider_integration_role_arn" {
  description = "The ARN of the provider integration IAM role."
  value       = confluent_provider_integration.main.aws[0].customer_role_arn
}

output "confluent_iam_role_arn" {
  description = "The display name of the provider integration."
  value       = confluent_provider_integration.main.aws[0].iam_role_arn
}

output "provider_integration_external_id" {
  description = "The external ID for the provider integration."
  value       = confluent_provider_integration.main.aws[0].external_id
}

output "provider_integration_internal_id" {
  description = "The internal ID for the provider integration."
  value       = confluent_provider_integration.main.id
}