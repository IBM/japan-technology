terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.17.0"
    }
  }
}

resource "aws_iam_role" "s3_access_role" {
  name        = var.customer_role_name
  description = "IAM role for accessing S3 with a trust policy for Confluent Tableflow"

  assume_role_policy = jsonencode({
    Version   = "2012-10-17"
    Statement = flatten(concat( 
      [
        {
          Effect    = "Allow"
          Principal = {
            AWS = var.provider_integration_role_arn
          }
          Action    = "sts:AssumeRole"
          Condition = {
            StringEquals = {
              "sts:ExternalId" = var.provider_integration_external_id
            }
          }
        },
        {
          Effect    = "Allow"
          Principal = {
            AWS = var.provider_integration_role_arn
          }
          Action    = "sts:TagSession"
        }
      ]
    ))
  })
}

# https://docs.confluent.io/cloud/current/connectors/cc-s3-sink/cc-s3-sink.html#user-account-iam-policy
resource "aws_iam_policy" "s3_access_policy" {
  name        = "TableflowS3AccessPolicy-${var.random_suffix}"
  description = "IAM policy for accessing the S3 bucket for Confluent Tableflow"

  policy      = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:ListBucket",
          "s3:GetBucketLocation"
        ]
        Resource = [
          "arn:aws:s3:::${var.s3_bucket_name}/*",
          "arn:aws:s3:::${var.s3_bucket_name}"
        ]
      }
    ]
  })
}


# Attach the primary S3 access policy
resource "aws_iam_role_policy_attachment" "s3_policy_attachment" {
  role       = aws_iam_role.s3_access_role.name
  policy_arn = aws_iam_policy.s3_access_policy.arn
}



resource "aws_iam_role_policy_attachment" "attach_glue_access" {
  role       = aws_iam_role.s3_access_role.name
  policy_arn = "arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess"
}
