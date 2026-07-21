#!/bin/bash

# Log everything to a file for debugging
exec > >(tee -a /var/log/postgres-setup.log)
exec 2>&1

# Set error handling
set -euo pipefail

echo "================================================"
echo "PostgreSQL Online Retailer Instance Setup Started"
echo "Script PID: $$"
echo "Start Time: $(date)"
echo "================================================"

# ===============================
# START TIMING
# ===============================
START_TIME=$(date +%s)

# Update system (with retry logic)
echo "Updating system packages..."
dnf update -y || {
  echo "WARNING: dnf update failed, continuing anyway..."
}

# Install Docker
echo "Installing Docker..."
dnf install -y docker
systemctl enable docker
systemctl start docker

# Verify Docker is running
echo "Verifying Docker installation..."
docker --version
systemctl status docker --no-pager

# Install Docker Compose
echo "Installing Docker Compose..."
curl -L "https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version

# Create directory for PostgreSQL data and init scripts
echo "Creating PostgreSQL directories..."
mkdir -p /opt/postgres/data
mkdir -p /opt/postgres/init-scripts
chmod -R 777 /opt/postgres

# Create PostgreSQL initialization script
echo "Creating PostgreSQL init script..."
cat > /opt/postgres/init-scripts/01-init.sql <<'INIT_SQL'
-- Create tables for Online Retailer demo

CREATE TABLE IF NOT EXISTS products (
    ProductID INT PRIMARY KEY,
    Brand VARCHAR(255) NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Description TEXT,
    Color VARCHAR(50),
    Size VARCHAR(50),
    Price DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Segment VARCHAR(50) NOT NULL,
    shipping_address_id VARCHAR(255) NOT NULL,
    billing_address_id VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS addresses (
    AddressID VARCHAR(255) PRIMARY KEY,
    Street VARCHAR(255) NOT NULL,
    City VARCHAR(255) NOT NULL UNIQUE,
    State VARCHAR(50) NOT NULL,
    PostalCode VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);

CREATE TABLE IF NOT EXISTS order_items (
    OrderItemID INT PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);

-- Create publication for CDC (all tables in public schema)
CREATE PUBLICATION dbz_publication FOR ALL TABLES;

-- Log completion
\echo 'PostgreSQL initialization complete'
\echo 'Database: ${db_name}'
\echo 'Tables: products, customers, addresses, orders, order_items'
\echo 'Publication: dbz_publication (FOR ALL TABLES)'
INIT_SQL

# Create docker-compose.yml file
cat > /opt/postgres/docker-compose.yml <<'DOCKER_COMPOSE'
version: '3.8'
services:
  postgres:
    image: postgres:16-alpine
    container_name: postgres-onlineretailer
    environment:
      POSTGRES_PASSWORD: ${db_password}
      POSTGRES_DB: ${db_name}
      POSTGRES_USER: ${db_username}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    command:
      - "postgres"
      - "-c"
      - "wal_level=logical"
      - "-c"
      - "max_replication_slots=10"
      - "-c"
      - "max_wal_senders=10"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  postgres_data:
DOCKER_COMPOSE

# Start PostgreSQL container
echo "Starting PostgreSQL container..."
cd /opt/postgres
docker-compose up -d

# Wait for PostgreSQL to be healthy
echo "Waiting for PostgreSQL to become healthy (this may take 2-3 minutes)..."
until [ "$(docker inspect -f '{{.State.Health.Status}}' postgres-onlineretailer 2>/dev/null)" == "healthy" ]; do
  echo -n "."
  sleep 5
done
echo ""
HEALTHY_TIME=$(date +%s)
ELAPSED=$((HEALTHY_TIME - START_TIME))
ELAPSED_MIN=$((ELAPSED / 60))
echo "================================================"
echo "PostgreSQL is healthy!"
echo "Time to healthy: $ELAPSED seconds ($ELAPSED_MIN minutes)"
echo "================================================"

# Verify setup
echo "Verifying PostgreSQL setup..."
docker exec postgres-onlineretailer psql -U postgres -d ${db_name} -c "SELECT version();"
docker exec postgres-onlineretailer psql -U postgres -d ${db_name} -c "SHOW wal_level;"
docker exec postgres-onlineretailer psql -U postgres -d ${db_name} -c "SELECT * FROM pg_publication;"
docker exec postgres-onlineretailer psql -U postgres -d ${db_name} -c "\dt"

# Set up a welcome message
PUBLIC_HOSTNAME=$(curl -s http://169.254.169.254/latest/meta-data/public-hostname)
cat > /etc/motd <<MOTD_EOF
╔═══════════════════════════════════════════════════════════╗
║      PostgreSQL 16 Online Retailer Instance Ready         ║
╚═══════════════════════════════════════════════════════════╝

Connection Details:
  Hostname:  $PUBLIC_HOSTNAME
  Port:      5432
  Database:  ${db_name}
  Username:  ${db_username}
  Password:  ${db_password}

CDC Configuration:
  Publication:  dbz_publication
  WAL Level:    logical

Tables:
  - products
  - customers
  - addresses
  - orders
  - order_items

Container Management:
  Status:     docker ps
  Logs:       docker logs -f postgres-onlineretailer
  Shell:      docker exec -it postgres-onlineretailer psql -U postgres -d ${db_name}
  Restart:    cd /opt/postgres && docker-compose restart
  Stop:       cd /opt/postgres && docker-compose stop

For more info: /opt/postgres/
MOTD_EOF

# ===============================
# END TIMING
# ===============================
END_TIME=$(date +%s)
TOTAL_ELAPSED=$((END_TIME - START_TIME))
TOTAL_MIN=$((TOTAL_ELAPSED / 60))

echo "================================================"
echo "PostgreSQL online retailer instance setup complete!"
echo "End Time: $(date)"
echo "Total Duration: $TOTAL_ELAPSED seconds ($TOTAL_MIN minutes)"
echo "================================================"
echo ""
echo "TIMING SUMMARY:"
echo "  - PostgreSQL Healthy: $ELAPSED seconds ($ELAPSED_MIN minutes)"
echo "  - Total Setup: $TOTAL_ELAPSED seconds ($TOTAL_MIN minutes)"
echo ""

# Write timing to a dedicated file for easy retrieval
cat > /opt/postgres/setup-timing.txt <<TIMING_EOF
PostgreSQL Online Retailer Setup Timing
========================================
Start Time: $(date -d @$START_TIME)
PostgreSQL Healthy: $ELAPSED seconds ($ELAPSED_MIN minutes)
Setup Complete: $(date -d @$END_TIME)
Total Duration: $TOTAL_ELAPSED seconds ($TOTAL_MIN minutes)
TIMING_EOF

# Mark setup as complete
touch /opt/postgres/.setup-complete

echo "================================================"
echo "Setup script completed successfully!"
echo "Check /var/log/postgres-setup.log for full logs"
echo "================================================"

exit 0
