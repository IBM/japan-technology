#!/bin/bash

# Script to register Debezium PostgreSQL CDC Connector
# This script reads environment variables from .env.local and registers the connector

set -e

# Check if .env.local exists
if [ ! -f .env.local ]; then
    echo "Error: .env.local file not found!"
    echo "Please run 'terraform output' first to generate the environment variables."
    exit 1
fi

# Load environment variables
source .env.local

# Wait for Debezium Connect to be ready
echo "Waiting for Debezium Connect to be ready..."
until curl -s http://localhost:8083/ > /dev/null; do
    echo "Debezium Connect is not ready yet. Waiting..."
    sleep 5
done
echo "Debezium Connect is ready!"

# Create connector configuration
CONNECTOR_CONFIG=$(cat <<EOF
{
  "name": "postgres-cdc-source",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "postgres",
    "database.port": "5432",
    "database.user": "postgres",
    "database.password": "Admin123456!!",
    "database.dbname": "onlinestoredb",
    "topic.prefix": "shiftleft",
    "table.include.list": "public.customers,public.addresses,public.products,public.orders,public.order_items",
    "plugin.name": "pgoutput",
    "publication.autocreate.mode": "filtered",
    "key.converter": "io.confluent.connect.avro.AvroConverter",
    "key.converter.schema.registry.url": "${SCHEMA_REGISTRY_URL}",
    "key.converter.basic.auth.credentials.source": "USER_INFO",
    "key.converter.basic.auth.user.info": "${SR_API_KEY}:${SR_API_SECRET}",
    "value.converter": "io.confluent.connect.avro.AvroConverter",
    "value.converter.schema.registry.url": "${SCHEMA_REGISTRY_URL}",
    "value.converter.basic.auth.credentials.source": "USER_INFO",
    "value.converter.basic.auth.user.info": "${SR_API_KEY}:${SR_API_SECRET}",
    "transforms": "unwrap",
    "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
    "transforms.unwrap.drop.tombstones": "false",
    "transforms.unwrap.delete.handling.mode": "rewrite"
  }
}
EOF
)

# Check if connector already exists
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8083/connectors/postgres-cdc-source)

if [ "$HTTP_STATUS" = "200" ]; then
    echo "Connector already exists. Updating configuration..."
    curl --fail -X PUT http://localhost:8083/connectors/postgres-cdc-source/config \
      -H "Content-Type: application/json" \
      -d "$(echo "$CONNECTOR_CONFIG" | jq '.config')"
else
    echo "Registering new Debezium PostgreSQL CDC Connector..."
    curl --fail -X POST http://localhost:8083/connectors \
      -H "Content-Type: application/json" \
      -d "$CONNECTOR_CONFIG"
fi

echo ""
echo "Connector registered/updated successfully!"
echo ""
echo "Check connector status:"
echo "  curl http://localhost:8083/connectors/postgres-cdc-source/status | jq"
echo ""
echo "CDC topics will be created with the following names:"
echo "  - shiftleft.public.customers"
echo "  - shiftleft.public.addresses"
echo "  - shiftleft.public.products"
echo "  - shiftleft.public.orders"
echo "  - shiftleft.public.order_items"

# Made with Bob
