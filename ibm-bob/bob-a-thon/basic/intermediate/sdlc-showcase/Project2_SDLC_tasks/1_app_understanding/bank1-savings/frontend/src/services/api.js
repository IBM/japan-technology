import axios from 'axios';

// Get API base URL from environment variable or use default
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log(`API Request: ${config.method.toUpperCase()} ${config.url}`, config.data);
    return config;
  },
  (error) => {
    console.error('API Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    console.log(`API Response: ${response.config.url}`, response.data);
    return response;
  },
  (error) => {
    console.error('API Response Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// API Service Methods
const apiService = {
  // Get customer balance
  getBalance: async (customerId) => {
    const response = await api.post('/balance', { customer_id: customerId });
    return response.data;
  },

  // Get recent transactions
  getTransactions: async (customerId, limit = 10) => {
    const response = await api.post('/transactions', {
      customer_id: customerId,
      limit: limit
    });
    return response.data;
  },

  // Get spending analytics
  getAnalytics: async (customerId) => {
    const response = await api.post('/analytics', { customer_id: customerId });
    return response.data;
  },

  // Transfer to investment bank
  transferToInvestment: async (customerId, amount) => {
    const response = await api.post('/transfer', {
      customer_id: customerId,
      amount: parseFloat(amount)
    });
    return response.data;
  },

  // Get audit log
  getAuditLog: async () => {
    const response = await api.get('/audit_log');
    return response.data;
  },

  // Get all customers (for admin)
  getCustomers: async () => {
    const response = await api.get('/customers');
    return response.data;
  },

  // Health check
  healthCheck: async () => {
    const response = await axios.get('/health');
    return response.data;
  },

  // Custom query
  customQuery: async (customerId, queryDescription) => {
    const response = await api.post('/custom_query', {
      customer_id: customerId,
      query_description: queryDescription
    });
    return response.data;
  },
};

export default apiService;

// Made with Bob
