package com.bank.rates;

/**
 * Simple POJO for Account Rate data
 * Legacy Java 8 style - no records, no modern features
 */
public class AccountRate {
    private String accountType;
    private double rate;
    private String lastUpdated;
    
    public AccountRate() {
        // Default constructor
    }
    
    public AccountRate(String accountType, double rate, String lastUpdated) {
        this.accountType = accountType;
        this.rate = rate;
        this.lastUpdated = lastUpdated;
    }
    
    // Getters and Setters - verbose Java 8 style
    public String getAccountType() {
        return accountType;
    }
    
    public void setAccountType(String accountType) {
        this.accountType = accountType;
    }
    
    public double getRate() {
        return rate;
    }
    
    public void setRate(double rate) {
        this.rate = rate;
    }
    
    public String getLastUpdated() {
        return lastUpdated;
    }
    
    public void setLastUpdated(String lastUpdated) {
        this.lastUpdated = lastUpdated;
    }
    
    @Override
    public String toString() {
        return "AccountRate{" +
                "accountType='" + accountType + '\'' +
                ", rate=" + rate +
                ", lastUpdated='" + lastUpdated + '\'' +
                '}';
    }
}

// Made with Bob
