package com.example;

import java.io.*;
import java.sql.*;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;
import java.time.LocalDateTime;

public class DataFeeder {

    private static final int CUSTOMER_ID_MIN = 1;
    private static final int CUSTOMER_ID_MAX = 50;
    private static final int PRODUCT_ID_MIN = 1;
    private static final int PRODUCT_ID_MAX = 290;

    public static final int  INGESTION_INTERVAL = 1000;


    public static void main(String[] args) {
        Properties properties = getProperties();

        String dbUrl = properties.getProperty("db.url");
        String dbUser = properties.getProperty("db.user");
        String dbPassword = properties.getProperty("db.password");

        // Load data from three different CSV files
        List<String[]> customerData = readDataFromCSV("customers_sample_data.csv");
        List<String[]> addressData = readDataFromCSV("address_sample_data.csv");
        List<String[]> productData = readDataFromCSV("products_sample_data.csv");
        List<String[]> orderData = readDataFromCSV("orders_sample_data.csv");
        List<String[]> orderItemData = readDataFromCSV("order_items_sample_data.csv");

        String insertCustomerSQL = "INSERT INTO customers (CustomerID, CustomerName, Email, Segment, shipping_address_id, billing_address_id) VALUES (?, ?, ?, ?, ?, ?)";
        String insertAddressSQL = "INSERT INTO addresses (AddressID, Street, City, State, PostalCode, Country) VALUES (?, ?, ?, ?, ?, ?)";
        String insertProductSQL = "INSERT INTO products (ProductID,Brand,ProductName,Category,Description,Color,Size,Price,Stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
        String insertOrderSQL = "INSERT INTO orders (OrderID, CustomerID, OrderDate, Status)VALUES (?, ?, ?, ?)";
        String insertOrderItemsSQL = "INSERT INTO order_items (OrderItemID, OrderID, ProductID, Quantity) VALUES (?, ?, ?, ?)";


        List<String[]> ordersData = generateOrderData();
        List<String[]> orderItemsData = generateOrderItemsData();


        try (Connection connection = DriverManager.getConnection(dbUrl, dbUser, dbPassword)) {
            insertCustomerData(connection, insertCustomerSQL, customerData);
            insertAddressData(connection, insertAddressSQL, addressData);
            insertProductData(connection, insertProductSQL, productData);
            insertOrderData(connection, insertOrderSQL, orderData);
            insertOrderItemsData(connection, insertOrderItemsSQL, orderItemData);
            insertDataContinuously(connection);


        } catch (SQLException e) {
            e.printStackTrace();
        }
    }



    private static void insertDataContinuously(Connection connection) throws SQLException {
        String insertOrderSQL = "INSERT INTO orders (OrderID, CustomerID, OrderDate, Status) VALUES (?, ?, ?, ?)";
        String insertOrderItemSQL = "INSERT INTO order_items (OrderItemID, OrderID, ProductID, Quantity) VALUES (?, ?, ?, ?)";
        Random random = new Random();
        int orderID = 3000;
        int orderItemID = 9000;

        while (true) {
            // Insert Order
            try (PreparedStatement orderStatement = connection.prepareStatement(insertOrderSQL)) {
                int customerID = CUSTOMER_ID_MIN + random.nextInt(CUSTOMER_ID_MAX - CUSTOMER_ID_MIN + 1);
                LocalDateTime now = LocalDateTime.now();
                Timestamp orderDate = Timestamp.valueOf(now);
                String status = random.nextBoolean() ? "Completed" : "Pending";
                orderStatement.setInt(1, orderID);
                orderStatement.setInt(2, customerID);
                orderStatement.setTimestamp(3, orderDate);
                orderStatement.setString(4, status);
                orderStatement.executeUpdate();
                System.out.println("Order added with ID : " + orderID );

            }

            // Insert Multiple Order Items for the same OrderID
            try (PreparedStatement orderItemStatement = connection.prepareStatement(insertOrderItemSQL)) {
                int numberOfItems = 1 + random.nextInt(5); // Random number of order items between 1 and 5
                for (int i = 0; i < numberOfItems; i++) {
                    int productID = PRODUCT_ID_MIN + random.nextInt(PRODUCT_ID_MAX - PRODUCT_ID_MIN + 1);
                    int quantity = 1 + random.nextInt(10);
                    orderItemStatement.setInt(1, orderItemID++);
                    orderItemStatement.setInt(2, orderID);
                    orderItemStatement.setInt(3, productID);
                    orderItemStatement.setInt(4, quantity);
                    orderItemStatement.executeUpdate();
                    System.out.println("Order item added with ID : " + orderItemID );
                }
            }

            orderID++; // Increment orderID for the next order

            try {
                Thread.sleep(INGESTION_INTERVAL);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                // Handle the exception, if necessary
            }
        }
    }

    private static Properties getProperties() {
        Properties properties = new Properties();

        // Load from environment variables (required)
        String dbUrl = System.getenv("DB_URL");
        String dbUser = System.getenv("DB_USER");
        String dbPassword = System.getenv("DB_PASSWORD");

        if (dbUrl == null || dbUser == null || dbPassword == null) {
            System.err.println("ERROR: Required environment variables not set.");
            System.err.println("Please set: DB_URL, DB_USER, DB_PASSWORD");
            System.exit(1);
        }

        System.out.println("Loading database configuration from environment variables");
        properties.setProperty("db.url", dbUrl);
        properties.setProperty("db.user", dbUser);
        properties.setProperty("db.password", dbPassword);
        return properties;
    }

    private static List<String[]> readDataFromCSV(String fileName) {
        List<String[]> data = new ArrayList<>();
        try (InputStream inputStream = DataFeeder.class.getClassLoader().getResourceAsStream(fileName)) {
            if (inputStream != null) {
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream))) {
                    String line;
                    // Ignore the header line.
                    reader.readLine();
                    while ((line = reader.readLine()) != null) {
                        // Split the line into values using comma as delimiter
                        String[] row = line.split(",");
                        data.add(row);
                    }
                }
            } else {
                System.out.println("File not found: " + fileName);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return data;
    }


    public static void insertCustomerData(Connection connection, String insertSQL, List<String[]> data) throws SQLException {
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
            for (String[] row : data) {
                preparedStatement.setInt(1, Integer.parseInt(row[0].trim())); // CustomerID
                preparedStatement.setString(2, row[1].trim()); // CustomerName
                preparedStatement.setString(3, row[2].trim()); // Email
                preparedStatement.setString(4, row[3].trim()); // Segment
                preparedStatement.setString(5, row[4].trim()); // shipping_address_id
                preparedStatement.setString(6, row[5].trim()); // billing_address_id
                int rowsInserted = preparedStatement.executeUpdate();
                // Handle insertion result
            }
        }
    }

    public static void insertAddressData(Connection connection, String insertSQL, List<String[]> data) throws SQLException {
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
            for (String[] row : data) {
                preparedStatement.setString(1, row[0].trim()); //AddressID
                preparedStatement.setString(2, row[1].trim()); // Street
                preparedStatement.setString(3, row[2].trim()); // City
                preparedStatement.setString(4, row[3].trim()); // State
                preparedStatement.setString(5, row[4].trim()); // PostalCode
                preparedStatement.setString(6, row[5].trim()); // Country
                int rowsInserted = preparedStatement.executeUpdate();
                // Handle insertion result
            }
        }
    }


    public static void insertProductData(Connection connection, String insertSQL, List<String[]> data) throws SQLException {
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
            for (String[] row : data) {
                preparedStatement.setInt(1, Integer.parseInt(row[0].trim())); // ProductID
                preparedStatement.setString(2, row[1].trim()); // Brand
                preparedStatement.setString(3, row[2].trim()); // ProductName
                preparedStatement.setString(4, row[3].trim()); // Category
                preparedStatement.setString(5, row[4].trim()); // Description
                preparedStatement.setString(6, row[5].trim()); // Color
                preparedStatement.setString(7, row[6].trim()); // Size
                preparedStatement.setDouble(8, Double.parseDouble(row[7].trim())); // Price
                preparedStatement.setInt(9, Integer.parseInt(row[8].trim())); // Stock
                int rowsInserted = preparedStatement.executeUpdate();
                // Handle insertion result
            }
        }
    }


    public static void insertOrderData(Connection connection, String insertSQL, List<String[]> data) throws SQLException {
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
            for (String[] row : data) {
                preparedStatement.setInt(1, Integer.parseInt(row[0].trim())); // OrderID
                preparedStatement.setInt(2, Integer.parseInt(row[1].trim())); // CustomerID
                preparedStatement.setTimestamp(3, Timestamp.valueOf(row[2].trim()));// OrderDate
                preparedStatement.setString(4, row[3].trim()); // Status
                int rowsInserted = preparedStatement.executeUpdate();
                // Handle insertion result
            }
        }
    }

    public static void insertOrderItemsData(Connection connection, String insertSQL, List<String[]> data) throws SQLException {
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
            for (String[] row : data) {
                preparedStatement.setInt(1, Integer.parseInt(row[0].trim())); // OrderItemID
                preparedStatement.setInt(2, Integer.parseInt(row[1].trim())); // OrderID
                preparedStatement.setInt(3, Integer.parseInt(row[2].trim())); // ProductID
                preparedStatement.setInt(4, Integer.parseInt(row[3].trim())); // Quantity
                int rowsInserted = preparedStatement.executeUpdate();
                // Handle insertion result, if necessary
            }
        }
    }


    private static void insertOrderData(Connection connection, List<String[]> data) throws SQLException {
        String insertSQL = "INSERT INTO orders (OrderID, CustomerID, OrderDate, Status) VALUES (?, ?, ?, ?)";
        Random random = new Random();

        while (true) {
            Collections.shuffle(data, random);

            try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
                for (String[] row : data) {
                    preparedStatement.setInt(1, Integer.parseInt(row[0].trim())); // OrderID
                    preparedStatement.setInt(2, Integer.parseInt(row[1].trim())); // CustomerID
                    preparedStatement.setTimestamp(3, Timestamp.valueOf(row[2].trim())); // OrderDate
                    preparedStatement.setString(4, row[3].trim()); // Status
                    int rowsInserted = preparedStatement.executeUpdate();
                    System.out.println("Order added : " + rowsInserted);
                    // Handle insertion result, if necessary

                    // Delay for 500 ms
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        // Handle the exception, if necessary
                    }
                }
            }
        }
    }

    private static void insertOrderItemsData(Connection connection, List<String[]> data) throws SQLException {
        String insertSQL = "INSERT INTO order_items (OrderItemID, OrderID, ProductID, Quantity) VALUES (?, ?, ?, ?)";
        Random random = new Random();

        while (true) {
            Collections.shuffle(data, random);

            try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
                for (String[] row : data) {
                    preparedStatement.setInt(1, Integer.parseInt(row[0].trim())); // OrderItemID
                    preparedStatement.setInt(2, Integer.parseInt(row[1].trim())); // OrderID
                    preparedStatement.setInt(3, Integer.parseInt(row[2].trim())); // ProductID
                    preparedStatement.setInt(4, Integer.parseInt(row[3].trim())); // Quantity
                    int rowsInserted = preparedStatement.executeUpdate();
                    System.out.println("OrderItems added : " + rowsInserted);

                    // Handle insertion result, if necessary

                    // Delay for 500 ms
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        // Handle the exception, if necessary
                    }
                }
            }
        }
    }

    private static List<String[]> generateOrderData() {
        List<String[]> data = new CopyOnWriteArrayList<>();
        Random random = new Random();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        for (int i = 1; i <= 1000; i++) {
            int orderID = i;
            int customerID = CUSTOMER_ID_MIN + random.nextInt(CUSTOMER_ID_MAX - CUSTOMER_ID_MIN + 1);
            String orderDate = LocalDateTime.now().format(formatter);
            String status = random.nextBoolean() ? "Completed" : "Pending";
            data.add(new String[]{String.valueOf(orderID), String.valueOf(customerID), orderDate, status});
        }

        return data;
    }


    private static List<String[]> generateOrderItemsData() {
        List<String[]> data = new CopyOnWriteArrayList<>();
        Random random = new Random();

        for (int i = 1; i <= 5000; i++) {
            int orderItemID = i;
            int orderID = 1 + random.nextInt(1000);
            int productID = PRODUCT_ID_MIN + random.nextInt(PRODUCT_ID_MAX - PRODUCT_ID_MIN + 1);
            int quantity = 1 + random.nextInt(10);
            data.add(new String[]{String.valueOf(orderItemID), String.valueOf(orderID), String.valueOf(productID), String.valueOf(quantity)});
        }

        return data;
    }
}
