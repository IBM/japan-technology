package com.bank.rates;

import org.apache.commons.lang.StringUtils;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * Legacy Rate Service - Banking Account Rate Lookup
 * 
 * LEGACY ISSUES PRESENT:
 * - Java 8 (outdated)
 * - Synchronous blocking calls
 * - No connection pooling
 * - Deprecated Apache Commons libraries
 * - No structured logging
 * - Try-catch soup
 * 
 * @deprecated This is legacy code that needs modernization
 */
public class RateService {
    
    // ISSUE 1: Hardcoded database connection - no connection pooling
    private static final String DB_URL = "jdbc:mysql://localhost:3306/bankrates";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "password123";
    
    // ISSUE 2: Using deprecated Apache Commons HttpClient 3.x
    private HttpClient httpClient = new HttpClient();
    
    /**
     * Get all account types and their current rates
     * 
     * ISSUES:
     * - Synchronous blocking database call
     * - No connection pooling
     * - Try-catch soup
     * - No structured logging (using System.out.println)
     */
    public List<AccountRate> getAllAccountRates() {
        List<AccountRate> rates = new ArrayList<>();
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        // ISSUE 3: Try-catch soup begins
        try {
            // ISSUE 4: No structured logging - using System.out.println
            System.out.println("Starting to fetch account rates...");
            
            // ISSUE 5: Synchronous blocking call - creates new connection every time
            // ISSUE 6: No connection pooling
            conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            System.out.println("Database connection established");
            
            stmt = conn.createStatement();
            
            // ISSUE 7: Synchronous blocking query
            rs = stmt.executeQuery("SELECT account_type, rate, last_updated FROM account_rates");
            
            System.out.println("Query executed successfully");
            
            while (rs.next()) {
                try {
                    String accountType = rs.getString("account_type");
                    double rate = rs.getDouble("rate");
                    String lastUpdated = rs.getString("last_updated");
                    
                    // ISSUE 8: Using deprecated Apache Commons StringUtils
                    if (StringUtils.isNotEmpty(accountType)) {
                        AccountRate accountRate = new AccountRate();
                        accountRate.setAccountType(accountType);
                        accountRate.setRate(rate);
                        accountRate.setLastUpdated(lastUpdated);
                        rates.add(accountRate);
                        
                        System.out.println("Added rate for: " + accountType);
                    }
                } catch (Exception e) {
                    // ISSUE 9: Swallowing exceptions with poor error handling
                    System.out.println("Error processing row: " + e.getMessage());
                    e.printStackTrace();
                }
            }
            
            System.out.println("Fetched " + rates.size() + " account rates");
            
        } catch (Exception e) {
            // ISSUE 10: Generic exception catching
            System.out.println("Error fetching account rates: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // ISSUE 11: Manual resource cleanup - error prone
            try {
                if (rs != null) rs.close();
            } catch (Exception e) {
                System.out.println("Error closing ResultSet: " + e.getMessage());
            }
            
            try {
                if (stmt != null) stmt.close();
            } catch (Exception e) {
                System.out.println("Error closing Statement: " + e.getMessage());
            }
            
            try {
                if (conn != null) conn.close();
            } catch (Exception e) {
                System.out.println("Error closing Connection: " + e.getMessage());
            }
        }
        
        return rates;
    }
    
    /**
     * Get rate for specific account type
     * 
     * ISSUES:
     * - Synchronous blocking call
     * - No connection pooling
     * - Nested try-catch blocks
     */
    public AccountRate getRateByAccountType(String accountType) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        AccountRate accountRate = null;
        
        try {
            System.out.println("Fetching rate for account type: " + accountType);
            
            // ISSUE 12: Using deprecated StringUtils from Apache Commons Lang 2.x
            if (StringUtils.isEmpty(accountType)) {
                System.out.println("Account type is empty");
                return null;
            }
            
            try {
                // ISSUE 13: New connection for every request - no pooling
                conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
                
                try {
                    stmt = conn.createStatement();
                    
                    try {
                        // ISSUE 14: SQL injection vulnerability (not parameterized)
                        String query = "SELECT account_type, rate, last_updated FROM account_rates WHERE account_type = '" + accountType + "'";
                        rs = stmt.executeQuery(query);
                        
                        if (rs.next()) {
                            try {
                                accountRate = new AccountRate();
                                accountRate.setAccountType(rs.getString("account_type"));
                                accountRate.setRate(rs.getDouble("rate"));
                                accountRate.setLastUpdated(rs.getString("last_updated"));
                                System.out.println("Found rate: " + accountRate.getRate());
                            } catch (Exception e) {
                                System.out.println("Error creating AccountRate object: " + e.getMessage());
                                e.printStackTrace();
                            }
                        } else {
                            System.out.println("No rate found for account type: " + accountType);
                        }
                    } catch (Exception e) {
                        System.out.println("Error executing query: " + e.getMessage());
                        e.printStackTrace();
                    }
                } catch (Exception e) {
                    System.out.println("Error creating statement: " + e.getMessage());
                    e.printStackTrace();
                }
            } catch (Exception e) {
                System.out.println("Error connecting to database: " + e.getMessage());
                e.printStackTrace();
            }
        } catch (Exception e) {
            System.out.println("Unexpected error: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // ISSUE 15: More nested try-catch for cleanup
            try {
                if (rs != null) {
                    try {
                        rs.close();
                    } catch (Exception e) {
                        System.out.println("Error closing ResultSet: " + e.getMessage());
                    }
                }
            } catch (Exception e) {
                System.out.println("Error in finally block: " + e.getMessage());
            }
            
            try {
                if (stmt != null) {
                    try {
                        stmt.close();
                    } catch (Exception e) {
                        System.out.println("Error closing Statement: " + e.getMessage());
                    }
                }
            } catch (Exception e) {
                System.out.println("Error in finally block: " + e.getMessage());
            }
            
            try {
                if (conn != null) {
                    try {
                        conn.close();
                    } catch (Exception e) {
                        System.out.println("Error closing Connection: " + e.getMessage());
                    }
                }
            } catch (Exception e) {
                System.out.println("Error in finally block: " + e.getMessage());
            }
        }
        
        return accountRate;
    }
    
    /**
     * Fetch current market rates from external API
     * 
     * ISSUES:
     * - Using deprecated Apache Commons HttpClient 3.x
     * - Synchronous blocking HTTP call
     * - No timeout configuration
     * - Poor error handling
     */
    public String fetchMarketRates() {
        String response = null;
        GetMethod getMethod = null;
        
        try {
            System.out.println("Fetching market rates from external API...");
            
            // ISSUE 16: Using deprecated HttpClient 3.x (Apache Commons HttpClient)
            // Should use HttpClient 4.x or modern alternatives
            String url = "https://api.federalreserve.gov/rates/current";
            getMethod = new GetMethod(url);
            
            try {
                // ISSUE 17: Synchronous blocking HTTP call - no async support
                // ISSUE 18: No timeout configuration
                int statusCode = httpClient.executeMethod(getMethod);
                
                System.out.println("HTTP Status Code: " + statusCode);
                
                if (statusCode == 200) {
                    try {
                        // ISSUE 19: Blocking read of response body
                        response = getMethod.getResponseBodyAsString();
                        System.out.println("Successfully fetched market rates");
                    } catch (Exception e) {
                        System.out.println("Error reading response body: " + e.getMessage());
                        e.printStackTrace();
                    }
                } else {
                    System.out.println("Failed to fetch market rates. Status: " + statusCode);
                }
            } catch (Exception e) {
                System.out.println("Error executing HTTP request: " + e.getMessage());
                e.printStackTrace();
            }
        } catch (Exception e) {
            System.out.println("Error in fetchMarketRates: " + e.getMessage());
            e.printStackTrace();
        } finally {
            if (getMethod != null) {
                try {
                    getMethod.releaseConnection();
                } catch (Exception e) {
                    System.out.println("Error releasing connection: " + e.getMessage());
                }
            }
        }
        
        return response;
    }
    
    /**
     * Update account rate in database
     * 
     * ISSUES:
     * - Synchronous blocking update
     * - No connection pooling
     * - No transaction management
     * - Try-catch soup
     */
    public boolean updateAccountRate(String accountType, double newRate) {
        Connection conn = null;
        Statement stmt = null;
        boolean success = false;
        
        try {
            System.out.println("Updating rate for " + accountType + " to " + newRate);
            
            try {
                // ISSUE 20: No connection pooling - creates new connection
                conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
                
                try {
                    stmt = conn.createStatement();
                    
                    try {
                        // ISSUE 21: No transaction management
                        // ISSUE 22: SQL injection vulnerability
                        String updateQuery = "UPDATE account_rates SET rate = " + newRate + 
                                           ", last_updated = NOW() WHERE account_type = '" + accountType + "'";
                        
                        // ISSUE 23: Synchronous blocking update
                        int rowsAffected = stmt.executeUpdate(updateQuery);
                        
                        if (rowsAffected > 0) {
                            success = true;
                            System.out.println("Successfully updated " + rowsAffected + " rows");
                        } else {
                            System.out.println("No rows updated for account type: " + accountType);
                        }
                    } catch (Exception e) {
                        System.out.println("Error executing update: " + e.getMessage());
                        e.printStackTrace();
                    }
                } catch (Exception e) {
                    System.out.println("Error creating statement: " + e.getMessage());
                    e.printStackTrace();
                }
            } catch (Exception e) {
                System.out.println("Error connecting to database: " + e.getMessage());
                e.printStackTrace();
            }
        } catch (Exception e) {
            System.out.println("Unexpected error in updateAccountRate: " + e.getMessage());
            e.printStackTrace();
        } finally {
            try {
                if (stmt != null) {
                    try {
                        stmt.close();
                    } catch (Exception e) {
                        System.out.println("Error closing statement: " + e.getMessage());
                    }
                }
            } catch (Exception e) {
                System.out.println("Error in finally: " + e.getMessage());
            }
            
            try {
                if (conn != null) {
                    try {
                        conn.close();
                    } catch (Exception e) {
                        System.out.println("Error closing connection: " + e.getMessage());
                    }
                }
            } catch (Exception e) {
                System.out.println("Error in finally: " + e.getMessage());
            }
        }
        
        return success;
    }
    
    /**
     * Calculate compound interest - demonstrates performance bottleneck
     * 
     * ISSUES:
     * - Synchronous blocking calculation
     * - No caching
     * - Inefficient algorithm
     */
    public double calculateCompoundInterest(double principal, double rate, int years) {
        System.out.println("Calculating compound interest...");
        
        try {
            // ISSUE 24: Inefficient calculation - could be optimized
            double result = principal;
            
            // ISSUE 25: Synchronous blocking loop - no parallelization
            for (int i = 0; i < years; i++) {
                try {
                    // ISSUE 26: Artificial delay simulating slow calculation
                    Thread.sleep(100); // Simulates slow processing
                    result = result * (1 + rate);
                    System.out.println("Year " + (i + 1) + ": " + result);
                } catch (InterruptedException e) {
                    System.out.println("Calculation interrupted: " + e.getMessage());
                    e.printStackTrace();
                } catch (Exception e) {
                    System.out.println("Error in calculation: " + e.getMessage());
                    e.printStackTrace();
                }
            }
            
            System.out.println("Final amount: " + result);
            return result;
            
        } catch (Exception e) {
            System.out.println("Error calculating compound interest: " + e.getMessage());
            e.printStackTrace();
            return 0.0;
        }
    }
}

// Made with Bob
