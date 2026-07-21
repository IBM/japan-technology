
## PostgreSQL Table Schemas


### Products Table
CREATE TABLE products (
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


### Customers Table

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Segment VARCHAR(50) NOT NULL,
    Address VARCHAR(255) NOT NULL
);


### Orders Table
CREATE TABLE orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(50) NOT NULL, -- e.g., 'Completed', 'Pending'
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);


### Order_Items table
CREATE TABLE order_items (
    OrderItemID INT PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);



## Flink SQL

CREATE TABLE completed_orders (
    order_id STRING,
    customerid STRING,
    customername STRING,
    address STRING,
    amount DOUBLE,
    confirmation_code STRING,
    ts TIMESTAMP_LTZ(3)
); 


SELECT
orderid,
customerid,
$rowtime,
DATE_FORMAT(TO_TIMESTAMP_LTZ(orderdate / 1000, 3), 'yyyy-MM-dd HH:mm:ss') AS formatted_order_date,
status
FROM
`clothing_retail.public.orders`;







Connection URL
https://vrqoasm-sfb13236.snowflakecomputing.com
Connection user name
confluent
Private key



Snowflake role
kafka_connector_role
Database name
retail_db
Schema name
PUBLIC


Configuration
Ingestion method
SNOWPIPE_STREAMING
Input Kafka record value format
AVRO


