resource "random_id" "env_display_id" {
    byte_length = 4
}

# ------------------------------------------------------
# ENVIRONMENT
# ------------------------------------------------------



resource "confluent_environment" "staging" {
  display_name = "${var.prefix}-environment-${random_id.env_display_id.hex}"

  stream_governance {
    package = "ADVANCED"
  }
}

# ------------------------------------------------------
# KAFKA Cluster
# ------------------------------------------------------

data "confluent_schema_registry_cluster" "sr-cluster" {
  environment {
    id = confluent_environment.staging.id
  }

  depends_on = [
    confluent_kafka_cluster.standard
  ]
}

# Update the config to use a cloud provider and region of your choice.
# https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_cluster
resource "confluent_kafka_cluster" "standard" {
  display_name = "${var.prefix}-cluster-${random_id.env_display_id.hex}"
  availability = "SINGLE_ZONE"
  cloud        = "AWS"
  region       = var.cloud_region
  standard {}
  environment {
    id = confluent_environment.staging.id
  }
}

# ------------------------------------------------------
# SERVICE ACCOUNTS
# ------------------------------------------------------

resource "confluent_service_account" "app-manager" {
  display_name = "${var.prefix}-app-manager-${random_id.env_display_id.hex}"
  description  = "Service account to manage 'inventory' Kafka cluster"
}

resource "confluent_role_binding" "app-manager-kafka-cluster-admin" {
  principal   = "User:${confluent_service_account.app-manager.id}"
  role_name   = "EnvironmentAdmin"
  crn_pattern = confluent_environment.staging.resource_name
}


# ------------------------------------------------------
# Flink Compute Pool
# ------------------------------------------------------

resource "confluent_flink_compute_pool" "flinkpool-main" {
  display_name     = "${var.prefix}_standard_compute_pool_${random_id.env_display_id.hex}"
  cloud            = "AWS"
  region           = var.cloud_region
  max_cfu          = 20
  environment {
    id = confluent_environment.staging.id
  }
}

# ------------------------------------------------------
# API Keys
# ------------------------------------------------------

resource "confluent_api_key" "app-manager-kafka-api-key" {
  display_name = "app-manager-kafka-api-key"
  description  = "Kafka API Key that is owned by 'app-manager' service account"
  owner {
    id          = confluent_service_account.app-manager.id
    api_version = confluent_service_account.app-manager.api_version
    kind        = confluent_service_account.app-manager.kind
  }

  managed_resource {
    id          = confluent_kafka_cluster.standard.id
    api_version = confluent_kafka_cluster.standard.api_version
    kind        = confluent_kafka_cluster.standard.kind

    environment {
      id = confluent_environment.staging.id
    }
  }

  depends_on = [
    confluent_role_binding.app-manager-kafka-cluster-admin
  ]
}


resource "confluent_api_key" "app-manager-schema-registry-api-key" {
  display_name = "env-manager-schema-registry-api-key"
  description  = "Schema Registry API Key that is owned by 'env-manager' service account"
  owner {
    id          = confluent_service_account.app-manager.id
    api_version = confluent_service_account.app-manager.api_version
    kind        = confluent_service_account.app-manager.kind
  }

  managed_resource {
    id          = data.confluent_schema_registry_cluster.sr-cluster.id
    api_version = data.confluent_schema_registry_cluster.sr-cluster.api_version
    kind        = data.confluent_schema_registry_cluster.sr-cluster.kind

    environment {
      id = confluent_environment.staging.id
    }
  }
  depends_on = [
    confluent_role_binding.app-manager-kafka-cluster-admin
  ]
}

data "confluent_flink_region" "demo_flink_region" {
  cloud   = "AWS"
  region  = var.cloud_region
}



# Flink management API Keys

resource "confluent_api_key" "app-manager-flink-api-key" {
  display_name = "env-manager-flink-api-key"
  description  = "Flink API Key that is owned by 'env-manager' service account"
  owner {
    id          = confluent_service_account.app-manager.id
    api_version = confluent_service_account.app-manager.api_version
    kind        = confluent_service_account.app-manager.kind
  }

  managed_resource {
    id          = data.confluent_flink_region.demo_flink_region.id
    api_version = data.confluent_flink_region.demo_flink_region.api_version
    kind        = data.confluent_flink_region.demo_flink_region.kind

    environment {
      id = confluent_environment.staging.id
    }
  }
}



# ------------------------------------------------------
# ACLS
# ------------------------------------------------------




resource "confluent_kafka_acl" "app-manager-read-on-topic" {
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  resource_type = "TOPIC"
  resource_name = "*"
  pattern_type  = "LITERAL"
  principal     = "User:${confluent_service_account.app-manager.id}"
  host          = "*"
  operation     = "READ"
  permission    = "ALLOW"
  rest_endpoint = confluent_kafka_cluster.standard.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-kafka-api-key.id
    secret = confluent_api_key.app-manager-kafka-api-key.secret
  }
}

resource "confluent_kafka_acl" "app-manager-describe-on-cluster" {
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  resource_type = "CLUSTER"
  resource_name = "kafka-cluster"
  pattern_type  = "LITERAL"
  principal     = "User:${confluent_service_account.app-manager.id}"
  host          = "*"
  operation     = "DESCRIBE"
  permission    = "ALLOW"
  rest_endpoint = confluent_kafka_cluster.standard.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-kafka-api-key.id
    secret = confluent_api_key.app-manager-kafka-api-key.secret
  }
}


resource "confluent_kafka_acl" "app-manager-write-on-topic" {
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  resource_type = "TOPIC"
  resource_name = "*"
  pattern_type  = "LITERAL"
  principal     = "User:${confluent_service_account.app-manager.id}"
  host          = "*"
  operation     = "WRITE"
  permission    = "ALLOW"
  rest_endpoint = confluent_kafka_cluster.standard.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-kafka-api-key.id
    secret = confluent_api_key.app-manager-kafka-api-key.secret
  }
}

resource "confluent_kafka_acl" "app-manager-create-topic" {
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  resource_type = "TOPIC"
  resource_name = "*"
  pattern_type  = "LITERAL"
  principal     = "User:${confluent_service_account.app-manager.id}"
  host          = "*"
  operation     = "CREATE"
  permission    = "ALLOW"
  rest_endpoint = confluent_kafka_cluster.standard.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-kafka-api-key.id
    secret = confluent_api_key.app-manager-kafka-api-key.secret
  }
}

resource "confluent_kafka_acl" "app-manager-read-on-group" {
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  resource_type = "GROUP"
  resource_name = "*"
  pattern_type  = "LITERAL"
  principal     = "User:${confluent_service_account.app-manager.id}"
  host          = "*"
  operation     = "READ"
  permission    = "ALLOW"
  rest_endpoint = confluent_kafka_cluster.standard.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-kafka-api-key.id
    secret = confluent_api_key.app-manager-kafka-api-key.secret
  }
}

# ------------------------------------------------------
# Connectors
# ------------------------------------------------------

resource "time_sleep" "wait_for_postgres" {
  depends_on      = [module.postgres, aws_ecs_service.dbfeeder_app_service]
  create_duration = "30s"
}

resource "confluent_connector" "postgre-sql-cdc-source" {
  environment {
    id = confluent_environment.staging.id
  }
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  config_sensitive = {
    "database.password" = var.db_password
  }
  config_nonsensitive = {
    "connector.class"          = "PostgresCdcSourceV2"
    "name"                     = "PostgresCdcSourceConnector_0"
    "kafka.auth.mode"          = "SERVICE_ACCOUNT"
    "kafka.service.account.id" = confluent_service_account.app-manager.id
    "database.hostname"        = module.postgres.public_ip
    "database.port"            = module.postgres.port
    "database.user"            = var.db_username
    "database.dbname"          = "onlinestoredb"
    "database.server.name"     = local.database_server_name
    "topic.prefix"             = var.prefix
    "after.state.only"         = "true"
    "plugin.name"              = "pgoutput"
    "output.data.format"       = "AVRO"
    "output.key.format"        = "AVRO"
    "tasks.max"                = "1"
    "transforms"               = "transform_0"
    "transforms.transform_0.type"= "org.apache.kafka.connect.transforms.MaskField$Value"
    "transforms.transform_0.fields"= "email"
    "transforms.transform_0.replacement"= "****"
    "time.precision.mode" = "connect"
    "csfle.configs.visible"    = "false"
  }

  depends_on = [
    confluent_kafka_acl.app-manager-describe-on-cluster,
    confluent_kafka_acl.app-manager-write-on-topic,
    confluent_kafka_acl.app-manager-create-topic,
    time_sleep.wait_for_postgres,
  ]
}

locals {
  database_server_name = "sql"
}

# ------------------------------------------------------
# Topics
# ------------------------------------------------------

resource "confluent_kafka_topic" "error-payments-topic" {
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  topic_name         = "error-payments"
  rest_endpoint      = confluent_kafka_cluster.standard.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-kafka-api-key.id
    secret = confluent_api_key.app-manager-kafka-api-key.secret
  }
}

resource "confluent_kafka_topic" "payments-topic" {
  kafka_cluster {
    id = confluent_kafka_cluster.standard.id
  }
  topic_name         = "payments"
  rest_endpoint      = confluent_kafka_cluster.standard.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-kafka-api-key.id
    secret = confluent_api_key.app-manager-kafka-api-key.secret
  }
}

# ------------------------------------------------------
# Schemas
# ------------------------------------------------------

resource "confluent_schema" "avro-payments" {
  schema_registry_cluster {
    id = data.confluent_schema_registry_cluster.sr-cluster.id
  }
  rest_endpoint = data.confluent_schema_registry_cluster.sr-cluster.rest_endpoint
  subject_name = "payments-value"
  format = "AVRO"
  schema = file("./schemas/avro/payments-value.avsc")
  hard_delete = true
  credentials {
    key    = confluent_api_key.app-manager-schema-registry-api-key.id
    secret = confluent_api_key.app-manager-schema-registry-api-key.secret
  }
  depends_on = [
    confluent_role_binding.app-manager-kafka-cluster-admin,
    confluent_schema_registry_kek.aws_key
  ]
}

# ------------------------------------------------------
# CSFLE Encryption Keys
# ------------------------------------------------------


resource "confluent_schema_registry_kek" "aws_key" {
  schema_registry_cluster {
    id = data.confluent_schema_registry_cluster.sr-cluster.id
  }
  rest_endpoint = data.confluent_schema_registry_cluster.sr-cluster.rest_endpoint
  credentials {
    key    = confluent_api_key.app-manager-schema-registry-api-key.id
    secret = confluent_api_key.app-manager-schema-registry-api-key.secret
  }

  name = "CSFLE_Key"
  kms_type = "aws-kms"
  kms_key_id = aws_kms_key.kms_key.arn
  hard_delete = true
}
