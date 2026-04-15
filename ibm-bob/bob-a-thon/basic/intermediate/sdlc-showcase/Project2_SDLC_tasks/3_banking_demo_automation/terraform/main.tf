# ============================================================================
# TERRAFORM CONFIGURATION - INFRASTRUCTURE PROVISIONING
# ============================================================================
# Purpose: Provision infrastructure resources (containers, networks, volumes)
# Ansible will handle configuration, monitoring, and application deployment
# ============================================================================

terraform {
  required_version = ">= 1.0"
  
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

# Configure the Docker provider
provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# ============================================================================
# NETWORK INFRASTRUCTURE
# ============================================================================

resource "docker_network" "banking_network" {
  name   = var.network_name
  driver = "bridge"
  
  ipam_config {
    subnet  = "172.20.0.0/16"
    gateway = "172.20.0.1"
  }
  
  labels {
    label = "managed_by"
    value = "terraform"
  }
  
  labels {
    label = "environment"
    value = var.environment
  }
}

# ============================================================================
# PERSISTENT STORAGE VOLUMES
# ============================================================================

# Volume for Bank 1 database and audit logs
resource "docker_volume" "bank1_data" {
  name = "bank1-data"
  
  labels {
    label = "managed_by"
    value = "terraform"
  }
  
  labels {
    label = "bank"
    value = "savings"
  }
}

# Volume for Bank 2 database and audit logs
resource "docker_volume" "bank2_data" {
  name = "bank2-data"
  
  labels {
    label = "managed_by"
    value = "terraform"
  }
  
  labels {
    label = "bank"
    value = "investment"
  }
}

# Volume for monitoring data
resource "docker_volume" "monitoring_data" {
  name = "monitoring-data"
  
  labels {
    label = "managed_by"
    value = "terraform"
  }
  
  labels {
    label = "purpose"
    value = "monitoring"
  }
}

# Volume for backup storage
resource "docker_volume" "backup_data" {
  name = "backup-data"
  
  labels {
    label = "managed_by"
    value = "terraform"
  }
  
  labels {
    label = "purpose"
    value = "backups"
  }
}

# ============================================================================
# DOCKER IMAGES
# ============================================================================

resource "docker_image" "bank1_savings" {
  name = "bank1-savings:latest"
  
  build {
    context    = "${path.module}/../bank1-savings"
    dockerfile = "Dockerfile"
    tag        = ["bank1-savings:latest"]
    label = {
      managed_by  = "terraform"
      bank        = "savings"
      environment = var.environment
    }
  }
  
  triggers = {
    dir_sha1 = sha1(join("", [
      filesha1("${path.module}/../bank1-savings/Dockerfile"),
      filesha1("${path.module}/../bank1-savings/app.py"),
      filesha1("${path.module}/../bank1-savings/requirements.txt")
    ]))
  }
}

resource "docker_image" "bank2_investment" {
  name = "bank2-investment:latest"
  
  build {
    context    = "${path.module}/../bank2-investment"
    dockerfile = "Dockerfile"
    tag        = ["bank2-investment:latest"]
    label = {
      managed_by  = "terraform"
      bank        = "investment"
      environment = var.environment
    }
  }
  
  triggers = {
    dir_sha1 = sha1(join("", [
      filesha1("${path.module}/../bank2-investment/Dockerfile"),
      filesha1("${path.module}/../bank2-investment/app.py"),
      filesha1("${path.module}/../bank2-investment/requirements.txt")
    ]))
  }
}

# ============================================================================
# CONTAINER INFRASTRUCTURE
# ============================================================================

resource "docker_container" "bank1_savings" {
  name  = var.bank1_container_name
  image = docker_image.bank1_savings.image_id
  
  restart = "unless-stopped"
  
  # Port mapping
  ports {
    internal = 5000
    external = var.bank1_port
    protocol = "tcp"
  }
  
  # Minimal environment - Ansible will configure the rest
  env = [
    "BANK_NAME=Savings Bank",
    "BANK_ID=bank1",
    "BANK2_URL=http://${var.bank2_container_name}:5000"
  ]
  
  # Mount persistent volume
  volumes {
    volume_name    = docker_volume.bank1_data.name
    container_path = "/app/data"
  }
  
  # Network configuration
  networks_advanced {
    name    = docker_network.banking_network.name
    aliases = [var.bank1_container_name, "bank1"]
  }
  
  # Basic health check - Ansible will configure advanced monitoring
  healthcheck {
    test         = ["CMD", "python", "-c", "import requests; requests.get('http://localhost:5000/health')"]
    interval     = "30s"
    timeout      = "3s"
    start_period = "10s"
    retries      = 3
  }
  
  labels {
    label = "managed_by"
    value = "terraform"
  }
  
  labels {
    label = "bank"
    value = "savings"
  }
  
  labels {
    label = "environment"
    value = var.environment
  }
  
  depends_on = [docker_network.banking_network, docker_volume.bank1_data]
}

resource "docker_container" "bank2_investment" {
  name  = var.bank2_container_name
  image = docker_image.bank2_investment.image_id
  
  restart = "unless-stopped"
  
  # Port mapping
  ports {
    internal = 5000
    external = var.bank2_port
    protocol = "tcp"
  }
  
  # Minimal environment - Ansible will configure the rest
  env = [
    "BANK_NAME=Investment Bank",
    "BANK_ID=bank2"
  ]
  
  # Mount persistent volume
  volumes {
    volume_name    = docker_volume.bank2_data.name
    container_path = "/app/data"
  }
  
  # Network configuration
  networks_advanced {
    name    = docker_network.banking_network.name
    aliases = [var.bank2_container_name, "bank2"]
  }
  
  # Basic health check - Ansible will configure advanced monitoring
  healthcheck {
    test         = ["CMD", "python", "-c", "import requests; requests.get('http://localhost:5000/health')"]
    interval     = "30s"
    timeout      = "3s"
    start_period = "10s"
    retries      = 3
  }
  
  labels {
    label = "managed_by"
    value = "terraform"
  }
  
  labels {
    label = "bank"
    value = "investment"
  }
  
  labels {
    label = "environment"
    value = var.environment
  }
  
  depends_on = [docker_network.banking_network, docker_volume.bank2_data]
}