terraform {
  required_providers {
    confluent = {
      source  = "confluentinc/confluent"
      version = ">= 2.32.0"
    }
  }
}

resource "confluent_provider_integration" "main" {
  display_name = "s3_tableflow_integration_tableflow"
  environment {
    id = var.environment_id
  }
  # During the creation of confluent_provider_integration.main, the S3 role does not yet exist.
  # The role will be created after confluent_provider_integration.main is provisioned
  # by the s3_access_role module using the specified target name.
  # Note: This is a workaround to avoid updating an existing role or creating a circular dependency.
  aws {
    customer_role_arn = var.customer_role_arn
  }
}
