# ===============================
# AWS SSH Key Pair Module
# ===============================
# Creates SSH key pair for EC2 instance access

resource "tls_private_key" "main" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "main" {
  key_name   = "${var.prefix}-key-${var.resource_suffix}"
  public_key = tls_private_key.main.public_key_openssh

  tags = var.common_tags
}

resource "local_file" "private_key" {
  content         = tls_private_key.main.private_key_pem
  filename        = "${var.output_path}/sshkey-${aws_key_pair.main.key_name}.pem"
  file_permission = "0400"
}
