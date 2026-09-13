# Helper local for OS detection (used by destroy script generation)
locals {
  is_windows = fileexists("C:\\Windows\\System32\\cmd.exe")
}

output "resource-ids" {

  value = <<-EOT

==============================
   ENVIRONMENT & CLUSTER INFO
==============================
  Environment ID:         ${confluent_environment.staging.id}
  Kafka Cluster ID:       ${confluent_kafka_cluster.standard.id}
  Flink Compute Pool ID:  ${confluent_flink_compute_pool.flinkpool-main.id}

------------------------------
   S3 BUCKET
------------------------------
  Name: ${module.aws_s3_bucket.bucket_name}
  ARN:  ${module.aws_s3_bucket.bucket_arn}

------------------------------
   PROVIDER INTEGRATION
------------------------------

  Role ARN:     ${module.provider_integration.provider_integration_role_arn}
  External ID:  ${module.provider_integration.provider_integration_external_id}

------------------------------
   SNOWFLAKE SETUP INFO (Optional)
------------------------------
  IAM Role ARN:   ${module.provider_integration.provider_integration_role_arn}
  AWS Account ID: ${data.aws_caller_identity.current.account_id}
  AWS Region:     ${var.cloud_region}

------------------------------
   SERVICE ACCOUNTS & API KEYS
------------------------------
  App Manager: ${confluent_service_account.app-manager.display_name}
    - ID:         ${confluent_service_account.app-manager.id}
    - Kafka API Key:    "${confluent_api_key.app-manager-kafka-api-key.id}"
    - Kafka API Secret: "${confluent_api_key.app-manager-kafka-api-key.secret}"
    - Flink API Key:    "${confluent_api_key.app-manager-flink-api-key.id}"
    - Flink API Secret: "${confluent_api_key.app-manager-flink-api-key.secret}"

------------------------------
   CONNECTION CONFIGS
------------------------------
  SASL JAAS Config:
    org.apache.kafka.common.security.plain.PlainLoginModule required \
      username="${confluent_api_key.app-manager-kafka-api-key.id}" \
      password="${confluent_api_key.app-manager-kafka-api-key.secret}";
  Bootstrap Servers: ${confluent_kafka_cluster.standard.bootstrap_endpoint}
  Schema Registry URL: ${data.confluent_schema_registry_cluster.sr-cluster.rest_endpoint}
  Schema Registry Auth: "${confluent_api_key.app-manager-schema-registry-api-key.id}:${confluent_api_key.app-manager-schema-registry-api-key.secret}"

------------------------------
   DATABASE & KMS
------------------------------
  PostgreSQL Endpoint: ${module.postgres.public_ip}:${module.postgres.port}
  PostgreSQL Instance ID: ${module.postgres.instance_id}
  SSH Key Path: ${module.keypair.private_key_path}
  KMS Key ARN:  ${aws_kms_key.kms_key.arn}

  EOT

  sensitive = true
}

output "ecs-service-restart-command" {
  value = "aws ecs update-service --cluster ${aws_ecs_cluster.ecs_cluster.name} --service payment-app-service --force-new-deployment --region ${var.cloud_region}"
}

output "ecr-public-images" {
  description = "ECR Public image URLs being used"
  value = {
    payments_app = local.payment_app_image
    data_feeder  = local.dbfeeder_app_image
  }
}

output "snowflake-setup" {
  description = "Values needed for Snowflake catalog integration and external volume setup"
  value = <<-EOT

==============================
   SNOWFLAKE SETUP VALUES
==============================

------------------------------
   Catalog Integration (Glue)
------------------------------
  CATALOG_NAMESPACE:   ${confluent_kafka_cluster.standard.id}
  GLUE_AWS_ROLE_ARN:   ${module.provider_integration.provider_integration_role_arn}
  GLUE_CATALOG_ID:     ${data.aws_caller_identity.current.account_id}
  GLUE_REGION:         ${var.cloud_region}

------------------------------
   External Volume (S3)
------------------------------
  STORAGE_BASE_URL:          s3://${module.aws_s3_bucket.bucket_name}
  STORAGE_AWS_ROLE_ARN:      ${module.provider_integration.provider_integration_role_arn}
  STORAGE_AWS_EXTERNAL_ID:   ${module.provider_integration.provider_integration_external_id}

------------------------------
   IAM Role (for Trust Policy)
------------------------------
  Role ARN:   ${module.provider_integration.provider_integration_role_arn}

  EOT

  sensitive = true
}

output "athena-setup" {
  description = "Values needed for querying Iceberg tables in Amazon Athena"
  value = <<-EOT

==============================
   ATHENA SETUP VALUES
==============================
  Glue Database Name:   ${confluent_kafka_cluster.standard.id}
  S3 Bucket (for Tableflow data & Athena query output):   s3://${module.aws_s3_bucket.bucket_name}
  AWS Region:           ${var.cloud_region}

  EOT

  sensitive = true
}

# Create destroy.sh file based on variables used in this script
resource "local_file" "destroy_sh" {
  count    = local.is_windows ? 0 : 1
  filename = "./demo-destroy.sh"
  content  = <<-EOT
    #!/bin/bash
    set -e

    ENV_ID="${confluent_environment.staging.id}"
    CLUSTER_ID="${confluent_kafka_cluster.standard.id}"

    echo "==> Disabling Tableflow on topics..."
    confluent tableflow topic disable completed_orders --cluster $CLUSTER_ID --environment $ENV_ID --force 2>/dev/null || true
    confluent tableflow topic disable product_sales --cluster $CLUSTER_ID --environment $ENV_ID --force 2>/dev/null || true
    confluent tableflow topic disable thirty_day_customer_snapshot --cluster $CLUSTER_ID --environment $ENV_ID --force 2>/dev/null || true

    echo "==> Deleting catalog integrations..."
    for INTEGRATION_ID in $(confluent tableflow catalog-integration list --cluster $CLUSTER_ID --environment $ENV_ID -o json 2>/dev/null | grep '"id"' | sed 's/.*"id": *"//;s/".*//' || true); do
      confluent tableflow catalog-integration delete $INTEGRATION_ID --cluster $CLUSTER_ID --environment $ENV_ID --force 2>/dev/null || true
    done

    echo "==> Cleaning up CSFLE keys..."
    confluent schema-registry dek delete --kek-name CSFLE_Key --subject payments-value --force --environment $ENV_ID 2>/dev/null || true
    confluent schema-registry dek delete --kek-name CSFLE_Key --subject payments-value --force --permanent --environment $ENV_ID 2>/dev/null || true

    echo "==> Cleaning up AWS Glue tables and database..."
    GLUE_DB="${confluent_kafka_cluster.standard.id}"
    REGION="${var.cloud_region}"
    for TABLE in completed_orders product_sales thirty_day_customer_snapshot; do
      aws glue delete-table --database-name $GLUE_DB --name $TABLE --region $REGION 2>/dev/null || true
    done
    aws glue delete-database --name $GLUE_DB --region $REGION 2>/dev/null || true

    echo "==> Running terraform destroy..."
    terraform destroy --auto-approve
  EOT
  depends_on = [
    random_id.env_display_id
  ]
}

resource "local_file" "destroy_bat" {
  count    = local.is_windows ? 1 : 0
  filename = "./demo-destroy.bat"
  content  = <<-EOT
    @echo off
    set ENV_ID=${confluent_environment.staging.id}
    set CLUSTER_ID=${confluent_kafka_cluster.standard.id}
    set GLUE_DB=${confluent_kafka_cluster.standard.id}
    set REGION=${var.cloud_region}

    echo ==> Disabling Tableflow on topics...
    confluent tableflow topic disable completed_orders --cluster %CLUSTER_ID% --environment %ENV_ID% --force 2>nul
    confluent tableflow topic disable product_sales --cluster %CLUSTER_ID% --environment %ENV_ID% --force 2>nul
    confluent tableflow topic disable thirty_day_customer_snapshot --cluster %CLUSTER_ID% --environment %ENV_ID% --force 2>nul

    echo ==> Deleting catalog integrations...
    for /f "tokens=*" %%i in ('confluent tableflow catalog-integration list --cluster %CLUSTER_ID% --environment %ENV_ID% -o json 2^>nul ^| findstr "id"') do (
      for /f "tokens=2 delims=:" %%j in ("%%i") do (
        set "INTID=%%~j"
        setlocal enabledelayedexpansion
        set "INTID=!INTID: =!"
        set "INTID=!INTID:"=!"
        set "INTID=!INTID:,=!"
        confluent tableflow catalog-integration delete !INTID! --cluster %CLUSTER_ID% --environment %ENV_ID% --force 2>nul
        endlocal
      )
    )

    echo ==> Cleaning up CSFLE keys...
    confluent schema-registry dek delete --kek-name CSFLE_Key --subject payments-value --force --environment %ENV_ID% 2>nul
    confluent schema-registry dek delete --kek-name CSFLE_Key --subject payments-value --force --permanent --environment %ENV_ID% 2>nul

    echo ==> Cleaning up AWS Glue tables and database...
    aws glue delete-table --database-name %GLUE_DB% --name completed_orders --region %REGION% 2>nul
    aws glue delete-table --database-name %GLUE_DB% --name product_sales --region %REGION% 2>nul
    aws glue delete-table --database-name %GLUE_DB% --name thirty_day_customer_snapshot --region %REGION% 2>nul
    aws glue delete-database --name %GLUE_DB% --region %REGION% 2>nul

    echo ==> Running terraform destroy...
    terraform destroy --auto-approve
  EOT
  depends_on = [
    random_id.env_display_id
  ]
}
