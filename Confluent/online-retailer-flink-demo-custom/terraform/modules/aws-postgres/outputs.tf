# ===============================
# AWS PostgreSQL Module Outputs
# ===============================

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.postgres.id
}

output "private_ip" {
  description = "Private IP of the instance"
  value       = aws_instance.postgres.private_ip
}

output "public_ip" {
  description = "Public IP of the instance"
  value       = aws_instance.postgres.public_ip
}

output "public_dns" {
  description = "Public DNS of the instance"
  value       = aws_instance.postgres.public_dns
}

output "address" {
  description = "Public DNS of the instance (for connector compatibility)"
  value       = aws_instance.postgres.public_dns
}

output "port" {
  description = "PostgreSQL port"
  value       = 5432
}

output "security_group_id" {
  description = "ID of the security group"
  value       = aws_security_group.postgres.id
}

output "connection_string" {
  description = "PostgreSQL connection string"
  value       = "postgresql://${var.db_username}:${var.db_password}@${aws_instance.postgres.public_dns}:5432/${var.db_name}"
  sensitive   = true
}
