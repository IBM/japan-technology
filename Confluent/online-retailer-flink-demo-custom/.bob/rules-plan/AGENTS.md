# Project Architecture Rules (Non-Obvious Only)

## System Architecture

### Component Dependencies
- **ECS apps depend on Schema Registry**: Java producers fail immediately if schemas don't exist - no graceful degradation
- **Terraform order matters**: Schema Registry cluster created implicitly when Kafka cluster is created - can't reference SR until after Kafka exists
- **IAM user for CSFLE**: Separate IAM user `payments_app_user` created just for KMS permissions - not using ECS task role for encryption

### Data Flow Patterns
- **Intentional duplicate generation**: Payment producer generates duplicates 10% of time - this is BY DESIGN for teaching deduplication, not a bug to fix
- **No consumer apps**: This is producer-only architecture - Flink SQL and Tableflow consume data, no custom consumer applications
- **CDC captures all tables**: PostgreSQL CDC connector streams ALL tables from public schema - selective table filtering happens in Flink

### Infrastructure Coupling
- **S3 bucket required for Tableflow**: Cannot use Confluent-managed storage - BYOS (Bring Your Own Storage) is mandatory for this workshop
- **Glue catalog integration**: Tableflow writes to AWS Glue Data Catalog - this is the bridge between Kafka and Athena/Snowflake
- **VPC for ECS only**: VPC created solely for ECS tasks - Confluent Cloud resources are in Confluent's VPC, not customer VPC

## Scaling Constraints
- **Single-zone Kafka cluster**: Uses SINGLE_ZONE availability for cost - not production-ready
- **Flink compute pool max 20 CFU**: Hard limit set in terraform - queries may queue if limit reached
- **No auto-scaling**: ECS tasks run at fixed count - no scaling based on load

## State Management
- **Stateless producers**: Java apps have no persistent state - restart safe
- **Flink state in Confluent**: Flink statement state managed by Confluent Cloud - not visible in AWS
- **Iceberg metadata in Glue**: Table metadata stored in AWS Glue - S3 only has data files

## Security Model
- **CSFLE uses AWS KMS**: Encryption keys in AWS KMS, not Confluent - requires cross-cloud permissions
- **Service account per function**: Separate Confluent service accounts for app-manager, connectors - principle of least privilege
- **No VPC peering**: ECS tasks reach Confluent Cloud over public internet with TLS - no private networking

## Hidden Constraints
- **Schema evolution requires Flink restart**: Changing schema while Flink statement runs causes stale schema cache - must stop statement first
- **Connector hostname format**: PostgreSQL connector fails if hostname includes port - must be hostname only in separate field
- **DQR requires auto-flush**: Dead letter queue routing buffers indefinitely without `dlq.auto.flush=true` parameter