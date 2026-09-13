# API Reference

## Overview

This document provides comprehensive API documentation for both Bank 1 (Savings Bank) and Bank 2 (Investment Bank). Both banks expose RESTful JSON APIs with similar structures but different capabilities.

## Base URLs

- **Bank 1 (Savings)**: `http://localhost:5001` (local) or `http://<bank1-fqdn>:5000` (Azure)
- **Bank 2 (Investment)**: `http://localhost:5002` (local) or `http://<bank2-fqdn>:5000` (Azure)

## Authentication

⚠️ **Current Version**: No authentication required (demo environment)

🔒 **Production**: Implement JWT/OAuth2 authentication

## Common Response Format

All API endpoints return JSON responses with the following structure:

```json
{
  "success": true|false,
  "customer_name": "string",
  "query_type": "string",
  "result_data": {},
  "error": null|"string",
  "compliance_disclaimer": "string",
  "timestamp": "ISO 8601 timestamp",
  "bank": "string"
}
```

## Bank 1 (Savings Bank) API

### Health Check

#### GET /health

Check if the service is healthy and responsive.

**Request:**
```bash
curl http://localhost:5001/health
```

**Response:**
```json
{
  "status": "healthy",
  "bank": "Savings Bank",
  "bank_id": "bank1",
  "database": "connected",
  "timestamp": "2025-11-21T15:00:00.000Z"
}
```

### Get Customer Balance

#### POST /api/balance

Retrieve the current balance for a customer.

**Request:**
```bash
curl -X POST http://localhost:5001/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'
```

**Request Body:**
```json
{
  "customer_id": 1
}
```

**Response:**
```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "balance",
  "result_data": [
    {
      "name": "Alice Johnson",
      "balance": 5500.00,
      "email": "alice@example.com",
      "account_type": "savings"
    }
  ],
  "error": null,
  "compliance_disclaimer": "This banking information is provided...",
  "timestamp": "2025-11-21T15:00:00.000Z",
  "bank": "Savings Bank"
}
```

### Get Transaction History

#### POST /api/transactions

Retrieve transaction history for a customer.

**Request:**
```bash
curl -X POST http://localhost:5001/api/transactions \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "limit": 10}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "limit": 10  // optional, default: 50
}
```

**Response:**
```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "transactions",
  "result_data": [
    {
      "transaction_id": 1,
      "transaction_type": "deposit",
      "category": "salary",
      "amount": 3000.00,
      "description": "Monthly salary",
      "transaction_date": "2025-11-01T10:00:00.000Z"
    },
    {
      "transaction_id": 2,
      "transaction_type": "withdrawal",
      "category": "groceries",
      "amount": -150.00,
      "description": "Grocery shopping",
      "transaction_date": "2025-11-05T14:30:00.000Z"
    }
  ],
  "error": null,
  "timestamp": "2025-11-21T15:00:00.000Z",
  "bank": "Savings Bank"
}
```

### Get Analytics

#### POST /api/analytics

Get spending analytics with interactive charts.

**Request:**
```bash
curl -X POST http://localhost:5001/api/analytics \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'
```

**Request Body:**
```json
{
  "customer_id": 1
}
```

**Response:**
```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "analytics",
  "result_data": {
    "category_breakdown": [
      {"category": "groceries", "count": 15, "total": -450.00},
      {"category": "utilities", "count": 3, "total": -300.00},
      {"category": "entertainment", "count": 8, "total": -200.00}
    ],
    "pie_chart": "<html>...</html>",
    "line_chart": "<html>...</html>",
    "total_spent": -950.00,
    "total_transactions": 26
  },
  "error": null,
  "timestamp": "2025-11-21T15:00:00.000Z",
  "bank": "Savings Bank"
}
```

### Transfer to Bank 2

#### POST /api/transfer

Transfer funds from savings account to investment account (Bank 2).

**Request:**
```bash
curl -X POST http://localhost:5001/api/transfer \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 500.0}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "amount": 500.0
}
```

**Success Response:**
```json
{
  "success": true,
  "message": "Transferred $500.00 to Investment Bank",
  "new_balance": 5000.00,
  "transaction_id": 123,
  "timestamp": "2025-11-21T15:00:00.000Z"
}
```

**Error Response (Insufficient Funds):**
```json
{
  "success": false,
  "error": "Insufficient funds. Current balance: $300.00",
  "current_balance": 300.00
}
```

**Error Response (Invalid Amount):**
```json
{
  "success": false,
  "error": "Amount must be greater than 0"
}
```

### Deposit Funds

#### POST /api/deposit

Deposit funds into savings account.

**Request:**
```bash
curl -X POST http://localhost:5001/api/deposit \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 1000.0, "description": "Paycheck"}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "amount": 1000.0,
  "description": "Paycheck"  // optional
}
```

**Response:**
```json
{
  "success": true,
  "message": "Deposited $1000.00",
  "new_balance": 6500.00,
  "transaction_id": 124
}
```

### Custom Query

#### POST /api/custom_query

Execute a natural language query (parsed into SQL).

**Request:**
```bash
curl -X POST http://localhost:5001/api/custom_query \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "query_description": "Show my last 5 transactions over $100"}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "query_description": "Show my last 5 transactions over $100"
}
```

**Response:**
```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "custom_query",
  "result_data": {
    "sql": "SELECT * FROM transactions WHERE customer_id = ? AND ABS(amount) > ? ORDER BY transaction_date DESC LIMIT ?",
    "results": [...],
    "parsed_from": "Show my last 5 transactions over $100"
  }
}
```

### Audit Log

#### GET /api/audit_log

Retrieve audit log entries (last 50).

**Request:**
```bash
curl http://localhost:5001/api/audit_log
```

**Response:**
```json
{
  "success": true,
  "audit_entries": [
    {
      "timestamp": "2025-11-21T15:00:00.000Z",
      "bank_id": "bank1",
      "event_type": "balance_check",
      "customer_id": 1,
      "generated_sql": "SELECT...",
      "hash": "a1b2c3..."
    }
  ],
  "total_entries": 150
}
```

## Bank 2 (Investment Bank) API

### Health Check

#### GET /health

Check if the service is healthy and responsive.

**Request:**
```bash
curl http://localhost:5002/health
```

**Response:**
```json
{
  "status": "healthy",
  "bank": "Investment Bank",
  "bank_id": "bank2",
  "database": "connected",
  "timestamp": "2025-11-21T15:00:00.000Z"
}
```

### Get Customer Balance

#### POST /api/balance

Retrieve the current investment balance for a customer.

**Request:**
```bash
curl -X POST http://localhost:5002/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'
```

**Request Body:**
```json
{
  "customer_id": 1
}
```

**Response:**
```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "balance",
  "result_data": [
    {
      "name": "Alice Johnson",
      "balance": 11000.00,
      "email": "alice@example.com",
      "account_type": "investment"
    }
  ],
  "error": null,
  "timestamp": "2025-11-21T15:00:00.000Z",
  "bank": "Investment Bank"
}
```

### Get Transaction History

#### POST /api/transactions

Retrieve investment transaction history.

**Request:**
```bash
curl -X POST http://localhost:5002/api/transactions \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "limit": 10}'
```

**Response:** Similar to Bank 1, but with investment-specific categories (stocks, bonds, mutual_funds, etf).

### Get Investment Analytics

#### POST /api/analytics

Get investment portfolio analytics with charts.

**Request:**
```bash
curl -X POST http://localhost:5002/api/analytics \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'
```

**Response:**
```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "analytics",
  "result_data": {
    "category_breakdown": [
      {"category": "stocks", "count": 10, "total": 5000.00},
      {"category": "bonds", "count": 5, "total": 3000.00},
      {"category": "mutual_funds", "count": 3, "total": 2000.00},
      {"category": "etf", "count": 2, "total": 1000.00}
    ],
    "pie_chart": "<html>...</html>",
    "line_chart": "<html>...</html>",
    "total_invested": 11000.00,
    "total_transactions": 20
  }
}
```

### Receive Transfer from Bank 1

#### POST /api/receive_transfer

Receive funds transferred from Bank 1 (internal API, called by Bank 1).

**Request:**
```bash
curl -X POST http://localhost:5002/api/receive_transfer \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 500.0}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "amount": 500.0
}
```

**Response:**
```json
{
  "success": true,
  "message": "Received $500.00 from Savings Bank",
  "new_balance": 11500.00,
  "transaction_id": 456
}
```

### Transfer to Bank 1

#### POST /api/transfer_to_savings

Transfer funds from investment account back to savings account (Bank 1).

**Request:**
```bash
curl -X POST http://localhost:5002/api/transfer_to_savings \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 300.0}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "amount": 300.0
}
```

**Response:**
```json
{
  "success": true,
  "message": "Transferred $300.00 to Savings Bank",
  "new_balance": 11200.00,
  "transaction_id": 457
}
```

### Make Investment

#### POST /api/invest

Make a new investment.

**Request:**
```bash
curl -X POST http://localhost:5002/api/invest \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 1000.0, "category": "stocks", "description": "Tech stocks"}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "amount": 1000.0,
  "category": "stocks",  // stocks, bonds, mutual_funds, etf
  "description": "Tech stocks"  // optional
}
```

**Response:**
```json
{
  "success": true,
  "message": "Invested $1000.00 in stocks",
  "new_balance": 12200.00,
  "transaction_id": 458
}
```

### Withdraw Funds

#### POST /api/withdraw

Withdraw funds from investment account.

**Request:**
```bash
curl -X POST http://localhost:5002/api/withdraw \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 500.0, "description": "Cash out"}'
```

**Request Body:**
```json
{
  "customer_id": 1,
  "amount": 500.0,
  "description": "Cash out"  // optional
}
```

**Response:**
```json
{
  "success": true,
  "message": "Withdrew $500.00",
  "new_balance": 11700.00,
  "transaction_id": 459
}
```

## Error Handling

### Error Response Format

```json
{
  "success": false,
  "error": "Error message describing what went wrong",
  "error_code": "ERROR_CODE",  // optional
  "timestamp": "2025-11-21T15:00:00.000Z"
}
```

### Common Error Codes

| HTTP Status | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_REQUEST | Missing or invalid request parameters |
| 400 | INSUFFICIENT_FUNDS | Not enough balance for transaction |
| 400 | INVALID_AMOUNT | Amount must be greater than 0 |
| 404 | CUSTOMER_NOT_FOUND | Customer ID does not exist |
| 500 | DATABASE_ERROR | Database operation failed |
| 500 | INTERNAL_ERROR | Unexpected server error |
| 503 | SERVICE_UNAVAILABLE | Bank service is temporarily unavailable |

### Example Error Responses

**Invalid Customer ID:**
```json
{
  "success": false,
  "error": "Customer not found: customer_id=999",
  "error_code": "CUSTOMER_NOT_FOUND"
}
```

**Insufficient Funds:**
```json
{
  "success": false,
  "error": "Insufficient funds. Current balance: $100.00, requested: $500.00",
  "error_code": "INSUFFICIENT_FUNDS",
  "current_balance": 100.00,
  "requested_amount": 500.00
}
```

**Invalid Amount:**
```json
{
  "success": false,
  "error": "Amount must be greater than 0",
  "error_code": "INVALID_AMOUNT"
}
```

## Rate Limiting

⚠️ **Current Version**: No rate limiting (demo environment)

🔒 **Production**: Implement rate limiting
- 100 requests per minute per IP
- 1000 requests per hour per customer
- Exponential backoff for repeated failures

## CORS Configuration

⚠️ **Current Version**: CORS enabled for all origins (demo environment)

🔒 **Production**: Configure specific allowed origins

## Testing the API

### Using cURL

```bash
# Test Bank 1 health
curl http://localhost:5001/health

# Get balance
curl -X POST http://localhost:5001/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'

# Transfer funds
curl -X POST http://localhost:5001/api/transfer \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 100.0}'
```

### Using Postman

1. Import the API collection (if available)
2. Set base URL: `http://localhost:5001` or `http://localhost:5002`
3. Set Content-Type header: `application/json`
4. Send requests with JSON body

### Using Python

```python
import requests

# Get balance
response = requests.post(
    'http://localhost:5001/api/balance',
    json={'customer_id': 1}
)
data = response.json()
print(f"Balance: ${data['result_data'][0]['balance']}")

# Transfer funds
response = requests.post(
    'http://localhost:5001/api/transfer',
    json={'customer_id': 1, 'amount': 100.0}
)
result = response.json()
print(f"Transfer: {result['message']}")
```

### Using JavaScript/Fetch

```javascript
// Get balance
fetch('http://localhost:5001/api/balance', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({customer_id: 1})
})
.then(res => res.json())
.then(data => console.log('Balance:', data.result_data[0].balance));

// Transfer funds
fetch('http://localhost:5001/api/transfer', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({customer_id: 1, amount: 100.0})
})
.then(res => res.json())
.then(data => console.log('Transfer:', data.message));
```

## WebSocket Support

⚠️ **Not Currently Supported**

🔮 **Future Enhancement**: Real-time balance updates via WebSocket

## API Versioning

⚠️ **Current Version**: No versioning (v1 implicit)

🔒 **Production**: Implement API versioning
- URL-based: `/api/v1/balance`, `/api/v2/balance`
- Header-based: `Accept: application/vnd.bank.v1+json`

## Related Documentation

- [Banking Features](BANKING_FEATURES.md)
- [System Architecture](../architecture/SYSTEM_ARCHITECTURE.md)
- [Testing Guide](TESTING.md)
- [Local Deployment](../guides/LOCAL_DEPLOYMENT.md)

---

**Document Version**: 1.0  
**Last Updated**: 2025-11-21  
**API Version**: 1.0 (implicit)  
**Maintained By**: Development Team