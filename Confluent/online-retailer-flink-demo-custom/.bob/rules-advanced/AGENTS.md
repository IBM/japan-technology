# Project Advanced Coding Rules (Non-Obvious Only)

## Java Application Patterns

### Configuration Loading
- **Environment variables ONLY**: Java apps use [`ClientsUtils.loadConfigFromEnv()`](../../code/payments-app/src/main/java/io/confluent/examples/datacontract/utils/ClientsUtils.java) - do NOT create .properties files, they are ignored
- **Schema settings hardcoded**: Producers always set `AUTO_REGISTER_SCHEMAS=false` and `USE_LATEST_VERSION=true` in code (see [`ProducerApp.java:33-34`](../../code/payments-app/src/main/java/io/confluent/examples/datacontract/ProducerApp.java:33))

### Schema Registry Integration
- **Schemas must pre-exist**: Applications fail if schema doesn't exist in Schema Registry before producing - no auto-registration
- **Schema cache refresh**: Commented out `LATEST_CACHE_TTL` in ProducerApp suggests schema caching issues in past - be cautious when modifying

### Data Generation
- **Intentional duplicates**: [`ProducerApp.java:84-96`](../../code/payments-app/src/main/java/io/confluent/examples/datacontract/ProducerApp.java:84) generates duplicates 10% of the time - this is intentional for deduplication demos, not a bug

## Terraform Patterns

### Resource Dependencies
- **ECS tasks depend on schema versions**: Changing Schema Registry rules requires ECS service restart via `aws ecs update-service --force-new-deployment` - Terraform doesn't handle this automatically
- **Connector timing issue**: PostgreSQL CDC connector may fail on first apply if RDS not ready - use `terraform apply -replace="confluent_connector.postgre-sql-cdc-source"`

### Configuration Injection
- **No local config files**: All Java app config injected via ECS task definition environment variables in [`apps.tf`](../../terraform/apps.tf) - never create local .properties files

## Maven Build
- **Shaded JAR required**: Maven shade plugin creates fat JAR with all dependencies - this is required for Docker image, not optional
- **Avro code generation**: POJOs generated from [`src/main/datacontracts/avro/`](../../code/payments-app/src/main/datacontracts/avro/) during `mvn generate-sources` - do not manually edit generated classes

## Browser & MCP Tools Available
This mode has access to browser automation and MCP tools for enhanced capabilities beyond standard coding tasks.