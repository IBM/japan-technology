#  Transactions Producer

This java app produces mock transaction and payments data.

## Prerequisites
The only requirements to run this application are [Docker](https://docs.docker.com/engine/install/), a Confluent Cloud Account, and Kafka Cluster in the account. 

## Authentication
To connect this application to your cluster, fill in the info in the [cc-orders.properties example](src/main/resources/cc-orders.properties.example) and save it as `cc-orders.properties` in the src/main/resources folder (the same folder as the template).
If you want to try out CSFLE as well, the properties file provides configurations to input key id and key secret for AWS KMS. If you are using other KMS, please update these properties

## Confluent Cloud
 Create two topics - `payments` and `error-payments`.  
 Set the schema for `payments` and `error-payments` to [this](src/main/datacontracts/avro/payments-value.avsc). 

Once the schemas are set, run the [`register_data_quality_rules.sh`](scripts/register_data_quality_rules.sh) script by running `./register_data_quality_rules.sh` in the scripts directory.  You can check to see the existing schema and data quality rules by running [`./get_orders_schema.sh`](scripts/get_orders_schema.sh), and reset the schema by running [`./clear_schema.sh`](scripts/clear_schema.sh).

## Build
To build this application, run `docker build -t <tag-name> .` in this folder.

## Run
To run this application, execute `docker run <tag-name>`. 
If you want multiple client applications, edit the DOCKERFILE and edit last argument (one after the cc-orders.properties file) to the number of clients you want running.
