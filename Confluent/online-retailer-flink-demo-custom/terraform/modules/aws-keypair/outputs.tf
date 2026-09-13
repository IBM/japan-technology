# ===============================
# AWS Key Pair Module Outputs
# ===============================

output "key_name" {
  description = "Name of the key pair"
  value       = aws_key_pair.main.key_name
}

output "key_pair_id" {
  description = "ID of the key pair"
  value       = aws_key_pair.main.id
}

output "private_key_path" {
  description = "Path to the private key file"
  value       = local_file.private_key.filename
}

output "private_key_pem" {
  description = "Private key in PEM format"
  value       = tls_private_key.main.private_key_pem
  sensitive   = true
}
