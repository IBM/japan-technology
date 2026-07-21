resource "aws_iam_user" "payments_app_user" {
  name = "payments_app_user_${random_id.env_display_id.hex}"
}

resource "aws_iam_access_key" "payments_app_aws_key" {
  user = aws_iam_user.payments_app_user.name
}

# NOTE: CPU architecture is now configured via the cpu_architecture variable.
# This should match the architecture of your pre-built Docker images.
# If building on CI (e.g., GitHub Actions), this is typically X86_64.
# If building on Apple Silicon, use ARM64.


resource "aws_iam_user_policy" "payments_app_iam_policy" {
  name = "payments_app_iam_policy__${random_id.env_display_id.hex}"
  user = aws_iam_user.payments_app_user.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "kms:*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

# NOTE: Properties files are no longer generated here.
# Java apps now read configuration from environment variables injected via ECS task definitions.
# See the ECS task definitions below for environment variable configuration.

# NOTE: Data Quality Rules (DQR) are registered via confluent_schema_registry_kek resource in confluent.tf
# The DQR file is not needed in the source code as it's not used by the producer.

# -------------------------------
# Containers Networking
# -------------------------------

# -------------------------------
#  VPC and Subnets
# -------------------------------
# Pick an AZ that supports the Postgres instance type.
data "aws_availability_zones" "available" {
  state = "available"
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}

data "aws_ec2_instance_type_offerings" "postgres" {
  location_type = "availability-zone"

  filter {
    name   = "instance-type"
    values = [var.postgres_instance_type]
  }

  filter {
    name   = "location"
    values = data.aws_availability_zones.available.names
  }
}

locals {
  public_subnet_az = length(data.aws_ec2_instance_type_offerings.postgres.locations) > 0 ? data.aws_ec2_instance_type_offerings.postgres.locations[0] : data.aws_availability_zones.available.names[0]
}

# VPC
resource "aws_vpc" "ecs_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
}

# Public Subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.ecs_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = local.public_subnet_az
  map_public_ip_on_launch = true
}

# -------------------------------
# Internet Gateway
# -------------------------------

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.ecs_vpc.id
}


# -------------------------------
# Public Route Table
# -------------------------------

resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.ecs_vpc.id

  route {
    cidr_block = "0.0.0.0/0"                 # This route allows all outbound traffic
    gateway_id = aws_internet_gateway.igw.id # Route to the Internet Gateway
  }
}

# -------------------------------
# Associate Public Route Table with Public Subnet
# -------------------------------

resource "aws_route_table_association" "public_route_table_association" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route_table.id
}


# -------------------------------
# Security Group for ECS
# -------------------------------

resource "aws_security_group" "ecs_sg" {
  vpc_id = aws_vpc.ecs_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# -------------------------------
#  ECR Public Image References
# -------------------------------
# NOTE: Docker images are pre-built by the workshop maintainer and hosted on ECR Public.
# Workshop participants do not need to build or push images.
# See REMOVE_DOCKER_BUILD.md for details.

locals {
  payment_app_image  = "public.ecr.aws/${var.ecr_public_alias}/${var.payments_app_image_name}:${var.image_tag}"
  dbfeeder_app_image = "public.ecr.aws/${var.ecr_public_alias}/${var.data_feeder_image_name}:${var.image_tag}"
}


# -------------------------------
#  ECS Cluster
# -------------------------------

# ECS Cluster
resource "aws_ecs_cluster" "ecs_cluster" {
  name = "${var.prefix}-esc-cluster-${random_id.env_display_id.hex}"
}

resource "aws_iam_role_policy" "kms_usage_policy" {
  name = "kms_usage_policy_${random_id.env_display_id.hex}"
  role = aws_iam_role.ecs_container_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "kms:*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

# IAM Role for ECS Task Execution
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole_${random_id.env_display_id.hex}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ECS-task-execution-attach" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# IAM Role for the containers
resource "aws_iam_role" "ecs_container_role" {
  name = "ecsTaskRole_${random_id.env_display_id.hex}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

}

# -------------------------------
# ECS Task Definitions and Services for Both Apps
# -------------------------------

resource "aws_cloudwatch_log_group" "dbfeeder-log-group" {
  name = "/ecs/db-feeder-task-${random_id.env_display_id.hex}"
}

resource "aws_cloudwatch_log_group" "payments-task-log-group" {
  name = "/ecs/payments-task-${random_id.env_display_id.hex}"
}



# Task Definition for Payment App
resource "aws_ecs_task_definition" "payment_app_task" {
  family                   = "payment-app-task-${random_id.env_display_id.hex}"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn            = aws_iam_role.ecs_container_role.arn
  memory                   = "512"
  cpu                      = "256"
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = var.cpu_architecture
  }

  container_definitions = jsonencode([
    {
      name      = "payment-app"
      image     = local.payment_app_image
      essential = true

      environment = [
        {
          name  = "BOOTSTRAP_SERVERS"
          value = confluent_kafka_cluster.standard.bootstrap_endpoint
        },
        {
          name  = "SASL_USERNAME"
          value = confluent_api_key.app-manager-kafka-api-key.id
        },
        {
          name  = "SASL_PASSWORD"
          value = confluent_api_key.app-manager-kafka-api-key.secret
        },
        {
          name  = "SCHEMA_REGISTRY_URL"
          value = data.confluent_schema_registry_cluster.sr-cluster.rest_endpoint
        },
        {
          name  = "SR_API_KEY"
          value = confluent_api_key.app-manager-schema-registry-api-key.id
        },
        {
          name  = "SR_API_SECRET"
          value = confluent_api_key.app-manager-schema-registry-api-key.secret
        },
        {
          name  = "AWS_ACCESS_KEY_ID"
          value = aws_iam_access_key.payments_app_aws_key.id
        },
        {
          name  = "AWS_SECRET_ACCESS_KEY"
          value = aws_iam_access_key.payments_app_aws_key.secret
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = aws_cloudwatch_log_group.payments-task-log-group.name
          awslogs-region        = var.cloud_region
          awslogs-stream-prefix = "ecs"
        }
      }
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
    }
  ])
}


# Task Definition for DB Feeder App
resource "aws_ecs_task_definition" "dbfeeder_app_task" {
  family                   = "dbfeeder-app-task-${random_id.env_display_id.hex}"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn            = aws_iam_role.ecs_container_role.arn
  memory                   = "512"
  cpu                      = "256"
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = var.cpu_architecture
  }

  container_definitions = jsonencode([
    {
      name      = "dbfeeder-app"
      image     = local.dbfeeder_app_image
      essential = true

      environment = [
        {
          name  = "DB_URL"
          value = "jdbc:postgresql://${module.postgres.public_ip}:5432/onlinestoredb"
        },
        {
          name  = "DB_USER"
          value = var.db_username
        },
        {
          name  = "DB_PASSWORD"
          value = var.db_password
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = aws_cloudwatch_log_group.dbfeeder-log-group.name
          awslogs-region        = var.cloud_region
          awslogs-stream-prefix = "ecs"
        }
      }
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
    }
  ])
}


# ECS Service for Payment App
resource "aws_ecs_service" "payment_app_service" {
  name            = "payment-app-service"
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.payment_app_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.public_subnet.id]
    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }

  depends_on = [
    confluent_kafka_topic.error-payments-topic,
    confluent_kafka_topic.payments-topic,
    confluent_schema.avro-payments
  ]
}



# ECS Service for DB Feeder App
resource "aws_ecs_service" "dbfeeder_app_service" {
  name            = "dbfeeder-app-service"
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.dbfeeder_app_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.public_subnet.id]
    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }

  depends_on = [
    module.postgres
  ]
}
