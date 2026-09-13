# Troubleshooting Guide

Common issues and solutions for the Real-Time Stream Processing Workshop.

---

## Setup & Infrastructure Issues

### Docker Not Running or Not Signed In

**Problem:** When running `terraform apply`, you see:

```
Error: Unable to read Docker image into resource: unable to list Docker images:
Error response from daemon: Sign in to continue using Docker Desktop.
Membership in the [confluent cnfltraining cnfldemos confluentinc] organizations is required.
```

**Solutions:**

1. **Make sure Docker Desktop is running**
   - macOS: Check the menu bar for the Docker whale icon
   - Windows: Check the system tray for the Docker icon
   - If not running, launch Docker Desktop and wait for it to fully start

2. **Sign in to Docker Desktop**
   - Open Docker Desktop
   - Click "Sign in" in the top right
   - Use your Docker Hub credentials

3. **For Confluent employees:** Ensure you're connected to Twingate/VPN and have the proper Okta group memberships for Docker organizations

---

### Terraform Apply Fails with AWS Credential Errors

**Problem:**
```
Error: No valid credential sources found
```

**Solution:**

Make sure AWS credentials are configured:

```bash
# Option 1: Use AWS CLI
aws configure

# Option 2: Export environment variables
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"

# Verify credentials work
aws sts get-caller-identity
```

---

### Terraform Apply Times Out or Hangs

**Problem:** Terraform seems stuck during `terraform apply`

**Possible causes and solutions:**

1. **RDS PostgreSQL is taking longer than expected**
   - This is normal! RDS can take 10-20 minutes to provision
   - Look for the message "Still creating..." - this means it's working
   - Be patient and let it complete

2. **Network connectivity issues**
   - Check your internet connection
   - If behind a corporate proxy, ensure Terraform can reach AWS and Confluent APIs

---

## Connector Issues

### PostgreSQL CDC Connector Fails on Initial Deploy

**Problem:** During `terraform apply`, the PostgreSQL CDC connector fails with connection refused errors:

```
Error: connector provisioning status is "FAILED": Unable to validate configuration.
database.hostname: Connection to <ip>:5432 refused. Check that the hostname and port are correct
and that the postmaster is accepting TCP/IP connections.
```

**Cause:** The PostgreSQL instance may not be fully ready to accept connections when the connector tries to connect, even though Terraform reports the instance as created.

**Solution:**

Re-run the connector provisioning:

```bash
terraform apply -replace="confluent_connector.postgre-sql-cdc-source" -auto-approve
```

This recreates only the connector resource while leaving everything else intact. The PostgreSQL instance should be ready by this point.

---

### Selected SOURCE Connector Instead of SINK

**Problem:** You accidentally created a PostgreSQL Source connector when you needed a Sink connector (or vice versa)

**Solution:**

1. Delete the incorrect connector:
   - In Confluent Cloud, go to **Connectors**
   - Click on the wrong connector
   - **Settings** > **Delete**

2. Create the correct connector type:
   - Click **Add connector**
   - Search for "PostgreSQL CDC Sink" (or Source, depending on the lab)
   - Verify the connector type before configuring

**Prevention tip:** Look for these labels in the connector wizard:
- **Source connectors:** Have "→ Kafka" (data flows INTO Kafka)
- **Sink connectors:** Have "Kafka →" (data flows OUT OF Kafka)

---

### PostgreSQL Connection Fails - Port Issue

**Problem:** PostgreSQL Sink connector fails to connect, or you get connection errors in LAB 1

**Common mistake:** Copying the port number (`:5432`) when entering the PostgreSQL host

**Solution:**

When configuring the PostgreSQL connector in Confluent Cloud:

1. **Database Hostname:** Enter ONLY the hostname
   - ✅ Correct: `shiftleft-onlinestoredb-abc123.us-east-1.rds.amazonaws.com`
   - ❌ Wrong: `shiftleft-onlinestoredb-abc123.us-east-1.rds.amazonaws.com:5432`

2. **Database Port:** Enter `5432` in the separate Port field (this should be the default)

The connector wizard has separate fields for hostname and port - don't combine them!

---

### Connector Shows "Failed" Status

**Problem:** Connector status is red/failed in Confluent Cloud

**Debugging steps:**

1. **Check the error message:**
   - Click on the failed connector
   - Look at the **Tasks** tab for error details

2. **Common fixes:**
   - **Authentication error:** Double-check database username/password
   - **Network error:** Verify RDS security group allows inbound connections (Terraform should handle this, but verify in AWS Console)
   - **Schema error:** Ensure the table exists and has the correct schema

3. **Restart the connector:**
   - Click **Pause** then **Resume**
   - Check if the error persists

---

## Flink SQL Issues

### "Table Not Found" in Flink SQL

**Problem:** Running `SELECT * FROM table_name` returns "Table does not exist"

**Solutions:**

1. **Use the correct table naming:**
   - CDC tables use the format: `` `prefix.schema.table_name` ``
   - Example: `` SELECT * FROM `shiftleft.public.customers`; ``
   - Note the backticks and the full path

2. **Verify the table exists:**
   ```sql
   SHOW TABLES;
   ```

3. **Check your database selection:**
   - In Flink SQL workspace, ensure you've selected the correct Kafka cluster as your database (top right dropdown)

---

### Flink Statement Stays in "Running" Status Forever

**Problem:** Your Flink SQL statement shows "Running" but no results appear

**Possible causes:**

1. **This is normal for streaming queries!** Flink statements run continuously. You'll see results appear as data flows through

2. **No data in the source topic:**
   - Verify the source topic has data: In Confluent Cloud, go to **Topics** and check message count
   - If using the payments app, make sure it's running: Check the Docker containers

3. **Join condition never matches:**
   - Check your join keys are correct
   - Verify data exists in both sides of the join

---

## Data Issues

### No Data Appearing in Topics

**Problem:** Topics are empty or data isn't flowing

**Debugging steps:**

1. **Check the data producer apps:**
   ```bash
   # List running containers
   docker ps

   # Check logs for the payments app
   docker logs <container_id>
   ```

2. **Verify CDC connector is running:**
   - In Confluent Cloud, check the PostgreSQL Source connector status
   - It should show "Running" in green

3. **Check the PostgreSQL database has data:**
   - The Terraform scripts should have populated initial data
   - Verify using a PostgreSQL client or the AWS RDS console

---

### Snowflake Cannot Read Iceberg Tables

**Problem:** Snowflake queries on Iceberg tables fail with permission or access errors

**Solutions:**

1. **Verify IAM trust policy entries:**
   - Navigate to the IAM role in the AWS Console (from `terraform output snowflake-setup`)
   - Click **Trust Relationships** and verify there are entries for both the Glue catalog integration (`GLUE_AWS_IAM_USER_ARN`) and the external volume (`STORAGE_AWS_IAM_USER_ARN`)
   - Each entry should have the correct `sts:ExternalId` condition

2. **Test external volume connectivity:**
   ```sql
   SELECT SYSTEM$VERIFY_EXTERNAL_VOLUME('iceberg_external_volume_<your_initials>');
   ```
   - If this returns an error, the S3 storage trust policy entry is missing or incorrect

3. **Table not found in Snowflake:**
   - First verify the table exists in AWS Glue Data Catalog
   - Check that Tableflow status shows **Syncing** in Confluent Cloud
   - Ensure the `CATALOG_TABLE_NAME` in your `CREATE ICEBERG TABLE` matches the exact Glue table name

4. **Permission denied errors:**
   - Both the Catalog Integration and External Volume require separate trust policy entries on the same IAM role
   - Run `DESCRIBE CATALOG INTEGRATION glueCatalogInt_<your_initials>;` and `DESC EXTERNAL VOLUME iceberg_external_volume_<your_initials>;` to verify the ARNs and external IDs match what's in the IAM trust policy

---

### CSFLE Encryption Not Working

**Problem:** After setting up CSFLE, credit card numbers are still appearing in plain text

**Solutions:**

1. **Wait for ECS deployment:**
   - After restarting the ECS service, wait 1-2 minutes for the new task to start
   - Check the ECS service in the AWS Console to verify the deployment completed

2. **Verify encryption rule in Data Contracts:**
   - Navigate to the `payments` topic > **Data Contracts** tab
   - Check that the `Encrypt_PII` rule appears under **Domain Rules**
   - Ensure the rule is using the correct KMS key (`CSFLE_Key`)

3. **Verify PII tag on cc_number:**
   - In the schema editor (Tree View), confirm that the `cc_number` field has the `PII` tag applied
   - If the tag is missing, add it and save the schema before restarting ECS

4. **Check KMS key permissions:**
   - Verify the KMS key exists in the AWS Console (search for `CSFLE_Key`)
   - Ensure the ECS task role has permissions to use the KMS key for encryption
   - Check the KMS key policy allows the service account to perform `kms:Encrypt` and `kms:GenerateDataKey` operations

5. **Check older vs. newer messages:**
   - Only messages produced **after** the ECS restart will be encrypted
   - Look at message timestamps to distinguish old (unencrypted) from new (encrypted) messages

---

## Confluent Cloud Issues

### "Unauthorized" or "403 Forbidden" Errors

**Problem:** Getting permission errors when creating resources

**Solution:**

1. **Verify API Key permissions:**
   - Your Confluent Cloud API key must have **Organization Admin** permissions
   - Check in Confluent Cloud: **Administration** > **API Keys**

2. **Create a new API key if needed:**
   - Go to **Administration** > **API Keys**
   - Click **Add key**
   - Select **Cloud resource management** scope
   - Assign **OrganizationAdmin** role

---

### Environment or Cluster Not Showing Up

**Problem:** Can't find your environment or cluster in Confluent Cloud

**Solution:**

1. **Check the environment prefix:**
   - By default, all resources are prefixed with `shiftleft`
   - Look for `shiftleft-environment-<random_id>`

2. **Verify region:**
   - Make sure you're looking in the correct cloud region (default: `us-east-1`)

3. **Check that Terraform completed successfully:**
   ```bash
   terraform show | grep environment
   ```

---

## Cleanup Issues

### Terraform Destroy Fails

**Problem:** `terraform destroy` or `demo-destroy.sh` fails with errors

**Common causes:**

1. **Connectors still exist:**
   - You MUST delete connectors manually before running destroy
   - See the [Cleanup section in README.md](./README.md#clean-up-important)

2. **Resources have dependencies:**
   - Try running the destroy script again - sometimes resources need to be deleted in order

3. **Manual resources created:**
   - If you created any resources manually in Confluent Cloud (topics, schemas, etc.), delete them first

---

## Still Stuck?

1. **During the workshop:**
   - Raise your hand or ask in the Slack channel
   - Workshop instructors are here to help!

2. **After the workshop:**
   - Check the [demo video](https://www.confluent.io/resources/demo/shift-left-dsp-demo/)
   - [Open a GitHub issue](https://github.com/confluentinc/online-retailer-flink-demo/issues)

3. **Confluent Documentation:**
   - [Confluent Cloud Connectors](https://docs.confluent.io/cloud/current/connectors/index.html)
   - [Flink SQL Reference](https://docs.confluent.io/cloud/current/flink/reference/overview.html)
   - [Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
