# ===============================
# AWS PostgreSQL Module
# ===============================
# Creates EC2 instance running PostgreSQL with CDC enabled

# ===============================
# Security Group
# ===============================

resource "aws_security_group" "postgres" {
  name        = "${var.prefix}-postgres-sg-${var.random_suffix}"
  description = "Allow SSH and PostgreSQL inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidr_blocks
  }

  ingress {
    description = "PostgreSQL access"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidr_blocks
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(var.common_tags, {
    Name = "${var.prefix}-postgres-sg-${var.random_suffix}"
  })
}

# ===============================
# AMI Data Source
# ===============================

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023*"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}

# ===============================
# EC2 Instance
# ===============================

resource "aws_instance" "postgres" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = var.subnet_id

  vpc_security_group_ids = [aws_security_group.postgres.id]

  root_block_device {
    volume_size = var.volume_size
    volume_type = "gp3"
  }

  user_data_replace_on_change = true
  user_data                   = templatefile("${path.module}/templates/user-data.sh.tpl", {
    db_password = var.db_password
    db_name     = var.db_name
    db_username = var.db_username
  })

  tags = merge(var.common_tags, {
    Name = "${var.prefix}-postgres-${var.random_suffix}"
  })
}
