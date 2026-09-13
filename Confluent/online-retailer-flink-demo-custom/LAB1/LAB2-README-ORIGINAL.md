
## Daily Sales Trends

In this use case, we utilize Confluent Cloud and Apache Flink to validate payments and create completed orders, creating a valuable data product that could be used to analyse daily sales trends to empower sales teams to make informed business decisions.

While such analyses are typically conducted within a Lakehouse—as demonstrated in use cases 1 and 2. Confluent offers multiple integration options to seamlessly bring data streams into Lakehouses. This includes a suite of connectors that read data from Confluent and write to various engines. Another option is [Tableflow](https://www.confluent.io/product/tableflow/) .

Tableflow simplifies the process of transferring data from Confluent into a data lake, warehouse, or analytics engine. It enables users to convert Kafka topics and their schemas into Apache Iceberg tables with zero effort, significantly reducing the engineering time, compute resources, and costs associated with traditional data pipelines. This efficiency is achieved by leveraging Confluent's Kora Storage Layer and a new metadata materializer that works with Confluent Schema Registry to manage schema mapping and evolution.

Since sales team in our fictitious company store all their data in Iceberg format. Instead of sending data to S3 and transforming it there, we’ll leverage Tableflow, which allows Confluent to handle the heavy lifting of data movement, conversion, and compaction. With Tableflow enabled, data stored in a Confluent topic, is ready for analytics in Iceberg format.

![Architecture](./assets/LAB2.png)


But before doing this, let's make sure that the data is reliable and protected first.

### **[OPTIONAL] Data Contracts in Confluent Cloud**

Analytics teams are focused on general sales trends, so they don't need access to PII. Instead of relying on central teams to write ETL scripts for data encryption and quality, we’re shifting this process left. Central governance teams set data protection and quality rules, which are pushed to the client for enforcement— the beauty of this is that there is not need for code changes on the client side - **IT JUST WORKS**.

##### **Using Confluent Cloud Data Quality Rules**

We want to make sure that any data produced adheres to a specific format. In our case, we want to make sure that any payment event generated needs to have a valid `Confirmation Code`. This check is done by using [Data Quality Rules](https://docs.confluent.io/cloud/current/sr/fundamentals/data-contracts.html#data-quality-rules), these rules are set in Confluent Schema registry, and pushed to the clients, where they are enforced. No need to change any code.

The rules were already created by Terraform, there is no need to do anything here except validate that it is working.

1. In the [`payments`](https://confluent.cloud/go/topics) Topic UI, select **Data Contracts**. Under **Rules** notice that there is a rule already created.

   The rule basically says that `confirmation_code` field value should follow this regex expression `^[A-Z0-9]{8}$`. Any event that doesn't match, will be sent to a dead letter queue topic named `error-payments`.

   ![Data Quality Rule](./assets/LAB2_dqr.png)

2. To validate that it is working go to the DLQ topic and inspect the message headers there.

![Data Quality Rule](./assets/LAB2_msgdlq.png)


##### **Data Protection using Confluent Cloud Client Side Field Level Encryption**

[Client Side Field Level Encryption(CSFLE)](https://docs.confluent.io/cloud/current/security/encrypt/csfle/client-side.html) in Confluent Cloud works by setting the rules in Confluent Schema registry, these rules are then pushed to the clients, where they are enforced. The symmetric key is created in provider and the client should have necessary permission the provider and the client should have permission to use the key to encrypt the data.

1. In the `payments` topic we notice that, the topic contains credit card information in unencrypted form.
    ![Architecture](./assets/LAB2_msg.png)

This field should be encrypted, the Symmetric Key was already created by the Terraform in AWS KMS. The key ARN was also imported to Confluent by Terraform. We just need to create the rule in Confluent

2. In the [`payments`](
   https://confluent.cloud/go/topics) Topic UI, select **Data Contracts** then click **Evolve**. Tag `cc_number` field as `PII`.

2. Click **Rules** and then **+ Add rules** button. Configure as the following:
   * Category: Data Encryption Rule
   * Rule name: `Encrypt_PII`
   * Encrypt fields with: `PII`
   * using: The key added by Terraform (probably called CSFLE_Key)

    Then click **Add** and **Save**

    Our rule instructs the serializer to encrypt any field in this topic that is tagged as PII

    ![CSFLE Rule](./assets/LAB2_rule.png)
4. Restart the ECS Service for the changes to take effect immediately. Run ```terraform output``` to get the ECS command that should be used to restart the service. The command should look like this:
   ```
   aws ecs update-service --cluster <ECS_CLUSTER_NAME> --service payment-app-service --force-new-deployment
   ```
5. Go back to the `payments` Topic UI, you can see that the Credit number is now encrypted.

    ![Encrypted Field](./assets/LAB2_msgenc.png)


### **Analyzing Daily Sales Trends using Confluent Cloud for Apache Flink**

We have a separate topic for payment information, an order is considered complete once a valid payment is received. To accurately track daily sales trends, we join the ```orders``` and ```payments``` data.

#### **Payments deduplication**

However, before joining both streams together we need to make sure that there are no duplicates in `payments` data coming in.

1. Check if there are any duplicates in `payments` table
   ```sql
   SELECT * FROM
   ( SELECT order_id, amount, count(*) total
    FROM `payments`
    GROUP BY order_id, amount )
   WHERE total > 1;
   ```
   This query shows all `order_id`s with multiple payments coming in. Since the output returns results, this indicates that the there are duplicates in the `payments` table.

2. To fix this run the following query in a new Flink cell
   ```sql
   SET 'client.statement-name' = 'unique-payments-maintenance';
   SET 'sql.state-ttl' = '1 hour';

   CREATE TABLE unique_payments (
   order_id INT NOT NULL,
   product_id INT,
   customer_id INT,
   confirmation_code STRING,
   cc_number STRING,
   expiration STRING,
   amount DOUBLE,
   ts TIMESTAMP_LTZ(3),
   WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
   )
   AS SELECT
   COALESCE(order_id, 0) AS order_id,
   product_id,
   customer_id,
   confirmation_code,
   cc_number,
   expiration,
   amount,
   ts
   FROM (
   SELECT *,
            ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY ts ASC) AS rownum
   FROM payments
   )
   WHERE rownum = 1;
   ```
   This query creates the `unique_payments` table, ensuring only the latest recorded payment for each `order_id` is retained. It uses `ROW_NUMBER()` to order payments by event time (`$rowtime`) and filters for the earliest entry per order. This removes any duplicate entries.

   Update the watermarks from the default `source_watermark()` to `ts` for the payments stream.
   ```sql
   ALTER TABLE payments
   MODIFY WATERMARK FOR ts AS ts
   ```
   ```sql
   ALTER TABLE unique_payments
   MODIFY WATERMARK FOR ts AS ts
   ```
3. Let's validate that the new `unique_payments` does not contain any duplicates
   ```sql
   SELECT order_id, COUNT(*) AS count_total FROM `unique_payments` GROUP BY order_id;
   ```
   Every `order_id` will have a `count_total` of `1`, ensuring no duplicates exist in the new table. You will not find any `order_id` with a value greater than `1`.

#### **Using Interval joins to filter out invalid orders**

Now let's filter out invalid orders (orders with no payment received within 96 hours). To achieve this we will use Flink Interval joins.


1. Create a new table that will hold all completed orders and filter out orders with no valid payment recieved within `96` hours of the order being placed.
   ```sql
   SET 'client.statement-name' = 'completed-orders-materializer';
   CREATE TABLE completed_orders (
      order_id INT,
      amount DOUBLE,
      confirmation_code STRING,
      ts TIMESTAMP_LTZ(3),
      WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
   ) AS
   SELECT
      pymt.order_id,
      pymt.amount,
      pymt.confirmation_code,
      pymt.ts
   FROM unique_payments pymt, `shiftleft.public.orders` ord
   WHERE pymt.order_id = ord.orderid
   AND orderdate BETWEEN pymt.ts - INTERVAL '96' HOUR AND pymt.ts;
   ```

#### **Analyzing Sales Trends using Amazon Athena**

This data can be made available seamlessly to your Data lake query engines using Confluent Cloud Tableflow feature. When Tableflow is enabled on a topic, the topic is materialized as an Iceberg Table and is available for any Query engine. In this demo, we use Amazon Athena, you can use any Engine that supports Iceberg Rest Catalog.

##### Setting up Tableflow

<details>
<summary>If you would like to leverage Confluent Managed Storage, follow the instructions here:</summary>

1. First enable Tableflow on the topic. In the topic UI, click on **Enable Tableflow**, then **Use Confluent Storage**

![Tableflow Enable Tableflow](./assets/LAB2_enable_tableflow.png)

</details>
<details>
   <summary>If you would like to use your own storage (Amazon S3), click here to expand those instructions.</summary>

   1. As an alternative to using Confluent Managed Storage, you can leverage Amazon S3 storage in your own Amazon S3 Bucket.

   1. First enable Tableflow on the topic. In the topic UI, click on **Enable Tableflow** then **Configure Custom Storage**

   ![configure custom storage](./assets/LAB2_enable_tableflow_custom_storage.png)

   2. In the next menu, you will be able to choose the Provider Integration we created in the previous section. You can identify it by either the name of the provider integration or the IAM Role you created.

   3. There should be only one provider integration created, so select that one. It can also be found in the outputs by running `terraform output resource-ids` and looking for the provider integration name.

   4. Provide the AWS S3 bucket name (`shiftleft-tableflow-bucket...`) which can be found in the `resource-ids` list from terraform as well.

   ![alt text](assets/byos-instructions.png)

   5. Click Continue and Launch. The tableflow topic will now be materialized in the Amazon S3 Bucket you specified.

</details>

### Important: If you would like to complete Lab 3, you must choose your own storage (not Confluent Managed Storage)


##### Configure with Glue Data Catalog

We will now share our topic metadata with Amazon Glue Data Catalog for the purposes of querying via Amazon Athena as well as Snowflake.

- Navigate to the Tableflow main page within your environment (Environments > {Your Environment} > Clusters > {Your Cluster} > Tableflow (on Left Hand Side).

   ![Navigate to tableflow](assets/navigate-to-tableflow.gif)


- You will see we already have the Storage Provider Integration enabled. Scroll down to External Catalog Integrations and click **+ Add integration** on the right hand side.
- Select **AWS Glue** as the integration type and give the integration a name, `my-glue-integration`.
- Select **Iceberg** as the supported format and click **Continue**.

   ![Set up Glue Integration](assets/set-up-glue-integration.png)

- On the next page, you can choose the provider integration that was previously created. If there is more than one, it can also be found in the outputs by running `terraform output resource-ids` and looking for the provider integration ARN.

- Click Continue and Launch.

- The External Catalog Integration will show as Status Pending for some time, and transition to Connected. Once the Status shows as **Connected** you can proceed to the next section.

   ![Catalog Connected](assets/catalog-connected.png)


##### Query with Athena

>**NOTE: After enabling Tableflow, it may take up to 15 minutes for the data to become available for analysis in Amazon Athena.**

1. Open AWS and Navigate to your Glue Data Catalog by searching for `AWS Glue` in top search bar, and then clicking on `Glue Data Catalog on left hand side.


![Navigate to GDC](assets/navigate-to-gdc.png)

2. Once on the Data Catalog Tables page, search for the `completed_orders` table by first searching for our database which will have the same name as our **Cluster ID** on Confluent Cloud. This value can be found under the `Environment & Cluster Info` section of the `terraform output resource-ids` command.


3. Scroll to the right in the `completed_orders` row and click the link that reads **Table data** under View Data. It will ask you to confirm you will be charged separately for Athena queries. Click **Proceed**.

![Search for Cluster ID](assets/search-for-cluster-id.png)


2. `completed_orders` data can now be queried in Athena. A query should have automatically run, showcasing a sample of 10 `completed` orders by running the query below:

   ```sql
   SELECT * FROM "AwsDataCatalog"."<<cluster-id>>"."completed_orders" limit 10;
   ```

4. Now we can start analyzing daily sales trends in Athena.
   > NOTE: For demo puposes we will do hourly windows

   In a new cell copy the following SQL

   ```sql
   SELECT
   date_trunc('hour', ts) AS window_start,
   date_trunc('hour', ts) + INTERVAL '1' hour AS window_end,
   COUNT(*) AS total_orders,
   SUM(amount) AS total_revenue
   FROM "AwsDataCatalog"."<<cluster-id>>"."completed_orders"
   GROUP BY date_trunc('hour', ts)
   ORDER BY window_start;
   ```
That's it we were able analyse the data in Athena.

## Topics

**➡️ Next topic:** [Analyze the data in Snowflake](../LAB3/LAB3-README.md)

**🏁 Finished?** [Cleanup](../README.md#clean-up)

**🔙 Previous topic:** [Usecase 2 - Product Sales and Customer360 Aggregation](../LAB1/LAB1-README.md)

---

## 🆘 Need Help?

Running into issues? Check the [**Troubleshooting Guide**](../TROUBLESHOOTING.md) for common problems and solutions, or ask a workshop instructor!
