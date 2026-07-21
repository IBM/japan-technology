-- PostgreSQL Schema for Online Retailer Demo
-- This script creates the necessary tables for the CDC demo
-- Based on the original schema from README.md

-- Customers Table (simplified - no foreign keys)
CREATE TABLE IF NOT EXISTS customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Segment VARCHAR(50) NOT NULL,
    shipping_address_id VARCHAR(50),
    billing_address_id VARCHAR(50)
);

-- Addresses Table
CREATE TABLE IF NOT EXISTS addresses (
    AddressID VARCHAR(50) PRIMARY KEY,
    Street VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100)
);

-- Products Table
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

-- Orders Table
CREATE TABLE IF NOT EXISTS orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);

-- Order Items Table
CREATE TABLE IF NOT EXISTS order_items (
    OrderItemID INT PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);

-- Set REPLICA IDENTITY for CDC (Debezium requirement)
ALTER TABLE customers REPLICA IDENTITY FULL;
ALTER TABLE addresses REPLICA IDENTITY FULL;
ALTER TABLE products REPLICA IDENTITY FULL;
ALTER TABLE orders REPLICA IDENTITY FULL;
ALTER TABLE order_items REPLICA IDENTITY FULL;

-- Made with Bob
