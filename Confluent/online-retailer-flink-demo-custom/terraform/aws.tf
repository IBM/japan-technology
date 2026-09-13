# ===============================
# SSH Key Pair for EC2 Access
# ===============================

module "keypair" {
  source = "./modules/aws-keypair"

  prefix          = var.prefix
  resource_suffix = random_id.env_display_id.hex
  output_path     = path.module
  common_tags = {
    Created_by  = "Shift-left Terraform script"
    Project     = "Online Retailer Demo"
  }
}

# ===============================
# PostgreSQL EC2 Instance
# ===============================

module "postgres" {
  source = "./modules/aws-postgres"

  prefix              = var.prefix
  random_suffix       = random_id.env_display_id.hex
  vpc_id              = aws_vpc.ecs_vpc.id
  subnet_id           = aws_subnet.public_subnet.id
  key_name            = module.keypair.key_name
  instance_type       = var.postgres_instance_type
  allowed_cidr_blocks = ["0.0.0.0/0"]
  db_name             = "onlinestoredb"
  db_username         = var.db_username
  db_password         = var.db_password
  common_tags = {
    Created_by  = "Shift-left Terraform script"
    Project     = "Online Retailer Demo"
  }

  depends_on = [module.keypair, aws_vpc.ecs_vpc, aws_subnet.public_subnet]
}


# ------------------------------------------------------
# KMS Key for CSFLE
# ------------------------------------------------------

data "aws_caller_identity" "current" {}

resource "aws_kms_alias" "kms_key_alias" {
  name          = "alias/${var.prefix}_csfle_key_${random_id.env_display_id.hex}"
  target_key_id = aws_kms_key.kms_key.key_id
}

resource "aws_kms_key" "kms_key" {
  description    = "An symmetric encryption KMS key used for CSFLE"
  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "key-default-1-${random_id.env_display_id.hex}"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "${data.aws_caller_identity.current.arn}"
        },
        Action   = "kms:*",
        Resource = "*"
      },
      {
        Sid    = "Enable Any IAM User Permission to DESCRIBE"
        Effect = "Allow"
        Principal = {
          AWS = "*"
        },
        Action   = [
            "kms:DescribeKey",
            "kms:GetKeyPolicy"
        ]
        Resource = "*"
      },
      {
        Sid    = "Allow use of the key"
        Effect = "Allow"
        Principal = {
          AWS = "${aws_iam_user.payments_app_user.arn}"
        },
        Action = [
          "kms:DescribeKey",
          "kms:Encrypt",
          "kms:Decrypt",
          "kms:ReEncrypt*",
          "kms:GenerateDataKey",
          "kms:GenerateDataKeyWithoutPlaintext"
        ],
        Resource = "*"
      }
    ]
  })
}




locals {
  tableflow_iam_role_name = "${var.prefix}-tableflow-role-${random_id.env_display_id.hex}"
  tableflow_bucket_name   = "${var.prefix}-tableflow-bucket-${random_id.env_display_id.hex}"
  customer_s3_access_role_arn = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/${local.tableflow_iam_role_name}"

}

module "aws_s3_bucket" {
  source        = "./modules/aws_s3_bucket"
  bucket_name = local.tableflow_bucket_name
}

module "provider_integration" {
  source            = "./modules/provider_integration"
  environment_id    = confluent_environment.staging.id
  customer_role_arn = local.customer_s3_access_role_arn
  depends_on        = [confluent_environment.staging, module.aws_s3_bucket, confluent_kafka_cluster.standard]
}


# creates IAM role for Tableflow Provider Integration
module "aws_iam_role" {
  source                           = "./modules/aws_iam_role"
  customer_role_name               = local.tableflow_iam_role_name
  s3_bucket_name                   = local.tableflow_bucket_name
  provider_integration_role_arn    = module.provider_integration.confluent_iam_role_arn
  provider_integration_external_id = module.provider_integration.provider_integration_external_id
  random_suffix                    = random_id.env_display_id.hex
  aws_account_id                   = data.aws_caller_identity.current.account_id
}
