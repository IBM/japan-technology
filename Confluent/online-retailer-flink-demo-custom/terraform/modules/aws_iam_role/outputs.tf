output "role_name" {
  description = "The name of the IAM role created for S3 access."
  value       = aws_iam_role.s3_access_role.name
}

output "role_arn" {
  description = "The ARN of the IAM role created for S3 access."
  value       = aws_iam_role.s3_access_role.arn
}

output "policy_arn" {
  description = "The ARN of the IAM policy attached to the role."
  value       = aws_iam_policy.s3_access_policy.arn
}

output "role_id" {
  description = "The ID of the IAM role created for S3 access."
  value       = aws_iam_role.s3_access_role.id
}

output "policy_id" {
  description = "The ID of the IAM policy attached to the role."
  value       = aws_iam_policy.s3_access_policy.id
}

output "iam_policy_attachment_id" {
  description = "The ID of the IAM policy attachment."
  value       = aws_iam_role_policy_attachment.s3_policy_attachment.id
}