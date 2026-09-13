# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project Type
Workshop/demo infrastructure for Confluent Cloud + Apache Flink streaming data platform. NOT a production application - designed for educational deployment and teardown.

## Critical Non-Obvious Patterns

### Infrastructure Management
- **Terraform must run in same shell as AWS credentials**: AWS env vars (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN) must be exported in the SAME terminal where terraform commands execute
- **Destroy requires Confluent CLI**: The `demo-destroy.sh` script handles Tableflow disabling, catalog cleanup, and CSFLE key deletion BEFORE terraform destroy - running `terraform destroy` directly will fail
- **ECS restart required for schema changes**: After modifying Schema Registry rules (CSFLE, DQR), must restart ECS service via `aws ecs update-service --force-new-deployment` for producers to pick up new schema versions

### Java Application Configuration
- **No properties files generated**: Java apps read ALL config from environment variables injected via ECS task definitions (see terraform/apps.tf) - do NOT create .properties files
- **Schema auto-registration disabled**: Producers use `AUTO_REGISTER_SCHEMAS=false` and `USE_LATEST_VERSION=true` - schemas must exist in Schema Registry before producing
- **CSFLE requires AWS KMS permissions**: IAM user `payments_app_user` needs `kms:*` permissions (defined in terraform/apps.tf) - encryption fails silently without these

### Docker Images
- **Pre-built images on ECR Public**: Workshop uses pre-built images from `public.ecr.aws/v3a9u0p7/` - participants do NOT build images locally
- **CPU architecture must match images**: `cpu_architecture` variable (X86_64 or ARM64) must match pre-built image architecture or ECS tasks fail to start
- **Docker provider removed**: Terraform no longer builds images - see providers.tf line 40 comment

### PostgreSQL CDC Connector
- **Initial deploy may fail**: PostgreSQL instance may not be ready when connector tries to connect during first `terraform apply` - solution: `terraform apply -replace="confluent_connector.postgre-sql-cdc-source" -auto-approve`
- **Hostname must NOT include port**: Connector config requires hostname ONLY (e.g., `host.rds.amazonaws.com`) - including `:5432` causes connection failure
- **CDC table naming**: Tables appear in Flink as `` `prefix.schema.table_name` `` (backticks required, full path required)

### Flink SQL Specifics
- **Statements run continuously**: Flink SQL statements show "Running" status indefinitely - this is normal for streaming queries
- **Must stop before schema evolution**: When evolving schemas, STOP the Flink statement consuming the topic BEFORE recreating the table, or schema changes won't be picked up

### Tableflow (Iceberg)
- **5-15 minute materialization lag**: After enabling Tableflow, data takes 5-15 minutes to appear in Glue/Athena/Snowflake - this is expected
- **BYOS requires S3 bucket**: Tableflow uses "Bring Your Own Storage" mode with S3 bucket created by Terraform - cannot use Confluent-managed storage
- **Snowflake requires TWO IAM trust entries**: Both Glue catalog integration AND external volume need separate trust policy entries on the SAME IAM role

### Data Quality Rules
- **DLQ auto-flush required**: Data Quality Rules with DLQ routing need `dlq.auto.flush=true` parameter or messages buffer indefinitely
- **Only new messages affected**: Rules apply to messages produced AFTER rule creation - existing messages remain unchanged

## Build Commands
```bash
# Terraform (from terraform/ directory)
terraform init
terraform validate
terraform apply -auto-approve
./demo-destroy.sh  # macOS/Linux - handles cleanup properly
demo-destroy.bat   # Windows

# Java apps (Maven)
cd code/payments-app
mvn clean package  # Creates shaded JAR
mvn exec:java      # Runs ProducerApp locally

cd code/postgresql-data-feeder
mvn clean package
mvn exec:java      # Runs DataFeeder locally
```

## Testing
No automated tests - this is workshop infrastructure. Validation is manual via Confluent Cloud UI and AWS Console.