# Banking Applications - Enhanced Features Documentation

## Overview

Both banking applications (Bank 1 - Savings Bank and Bank 2 - Investment Bank) have been updated with comprehensive security, compliance, and self-service features.

## Key Features Implemented

### 1. SQLite Database with Secure Schema

Each application uses a SQLite database with the following tables:

- **customers**: Customer information (customer_id, name, email, created_at)
- **accounts**: Account details (account_id, customer_id, account_type, balance, created_at)
- **transactions**: Transaction history (transaction_id, account_id, customer_id, transaction_type, category, amount, description, transaction_date)
- **customer_balances**: View for quick balance queries

**Security Features:**
- Balance constraints: `CHECK(balance >= 0)` ensures no negative balances
- Foreign key relationships for data integrity
- Parameterized queries prevent SQL injection

### 2. Secure Parameterized Queries

All database operations use parameterized queries with `?` placeholders:

```python
query = 'SELECT * FROM customers WHERE customer_id = ?'
execute_query(query, (customer_id,))
```

This prevents SQL injection attacks and ensures data security.

### 3. Schema Validation with Post-Execution Checks

Every query result is validated against expected schemas:

```python
expected_schema = {
    'name': 'str',
    'balance': 'float',
    'email': 'str'
}
```

**Business Rules Enforced:**
- Type checking for all fields
- Balance validation (must be >= 0)
- Required field verification

### 4. Immutable Audit Trail (JSONL Format)

All interactions are logged to an append-only JSONL file with:

- Timestamp (UTC ISO 8601 format)
- Bank ID and event type
- Customer ID
- User prompt/request
- Generated SQL query
- Query results (truncated to 500 chars)
- Model configuration
- SHA-256 hash for immutability verification

**Audit Log Location:**
- Bank 1: `bank1_audit.jsonl`
- Bank 2: `bank2_audit.jsonl`

**Example Audit Entry:**
```json
{
  "timestamp": "2025-11-17T20:30:00.000Z",
  "bank_id": "bank1",
  "event_type": "balance_check",
  "customer_id": 1,
  "prompt": "Check balance",
  "generated_sql": "SELECT c.name, a.balance FROM customers c...",
  "result": "[{'name': 'Alice Johnson', 'balance': 5000.0}]",
  "model_config": {"model": "direct_sql", "version": "1.0"},
  "error": null,
  "hash": "a1b2c3d4e5f6..."
}
```

### 5. Structured JSON Responses

All API responses follow a standardized format:

```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "balance",
  "result_data": [...],
  "error": null,
  "compliance_disclaimer": "This banking information is provided...",
  "timestamp": "2025-11-17T20:30:00.000Z",
  "bank": "Savings Bank"
}
```

**Required Fields:**
- `customer_name`: Customer's full name
- `query_type`: Type of operation performed
- `result_data`: Query results or operation outcome
- `compliance_disclaimer`: Regulatory compliance notice

### 6. Spending/Investment Analytics

Advanced analytics with visualizations using Plotly:

**Features:**
- Category breakdown (GROUP BY category)
- Time-series analysis (daily/monthly trends)
- Interactive pie charts for spending/investment allocation
- Line charts for activity over time
- Aggregated totals and counts

**Bank 1 (Savings):** Spending analytics by category (groceries, utilities, entertainment)
**Bank 2 (Investment):** Portfolio allocation (stocks, bonds, mutual funds, ETF)

### 7. Customer Data Isolation

**Strict Data Isolation:**
Every query includes `WHERE customer_id = ?` clause to prevent cross-customer data leakage.

```python
# Example: Only returns data for the specified customer
query = '''
    SELECT * FROM transactions 
    WHERE customer_id = ?
    ORDER BY transaction_date DESC
'''
```

**Security Benefits:**
- Prevents unauthorized access to other customers' data
- Enforces multi-tenant data separation
- Complies with privacy regulations (GDPR, CCPA)

### 8. Dual-Run Validation for High-Stakes Queries

For critical operations (transfers, investments), the system uses pre-validated SQL templates:

1. Parses the operation type from the request
2. Selects appropriate pre-validated SQL template
3. Validates query structure and parameters
4. Proceeds with validated query

**Use Cases:**
- Fund transfers
- Investment transactions
- Account modifications

**Example:**
```python
is_valid, sql_query, message = dual_run_validation(prompt, customer_id)
if not is_valid:
    return error_response(message)
# Proceed with validated query
```

**Note:** In production, this could be enhanced with AI-based dual-run validation where queries are generated twice and compared for consistency.

### 9. Web Interface with Self-Service Operations

**Bank 1 (Savings Bank) - Green Theme:**
- Check Balance
- View Transactions
- Spending Analytics
- Transfer Funds
- Custom Query (AI-powered)

**Bank 2 (Investment Bank) - Blue Theme:**
- Check Portfolio
- View Transactions
- Investment Analytics
- Make Investment
- Custom Query (AI-powered)

**Interface Features:**
- Responsive design
- Real-time result display
- Interactive charts
- Form validation
- Error handling

### 10. Audit Log Viewer

Built-in compliance tool for reviewing query provenance:

- Displays last 50 audit entries
- Shows timestamp, event type, customer ID
- Displays generated SQL queries
- Shows hash for immutability verification
- Refresh capability
- Searchable and filterable

## API Endpoints

### Common Endpoints (Both Banks)

#### GET /
Web interface for self-service banking

#### GET /health
Health check endpoint
```json
{
  "status": "healthy",
  "bank": "Savings Bank",
  "bank_id": "bank1",
  "database": "connected"
}
```

#### POST /api/balance
Get customer balance
```json
Request: {"customer_id": 1}
Response: {
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "balance",
  "result_data": [{"name": "Alice Johnson", "balance": 5000.0, ...}]
}
```

#### POST /api/transactions
Get transaction history
```json
Request: {"customer_id": 1, "limit": 10}
Response: {
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "transactions",
  "result_data": [...]
}
```

#### POST /api/analytics
Get spending/investment analytics with visualizations
```json
Request: {"customer_id": 1}
Response: {
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "analytics",
  "result_data": {
    "category_breakdown": [...],
    "pie_chart": "<html>...</html>",
    "line_chart": "<html>...</html>",
    "total_spent": 1500.0
  }
}
```

#### POST /api/custom_query
Execute custom query using natural language parsing
```json
Request: {
  "customer_id": 1,
  "query_description": "Show my last 5 transactions over $100"
}
Response: {
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "custom_query",
  "result_data": {
    "sql": "SELECT * FROM transactions WHERE...",
    "results": [...],
    "parsed_from": "Show my last 5 transactions over $100"
  }
}
```

**Supported Query Patterns:**
- "last X transactions" - Recent transaction history
- "transactions over $X" - Transactions above amount
- "by category" - Category breakdown
- "monthly summary" - Monthly aggregation
- "account summary" - Portfolio overview

#### GET /api/audit_log
Retrieve audit log entries
```json
Response: {
  "success": true,
  "audit_entries": [...],
  "total_entries": 150
}
```

### Bank 1 Specific

#### POST /api/transfer
Transfer funds with dual-run validation
```json
Request: {
  "customer_id": 1,
  "amount": 500.0,
  "to_account_id": 2
}
```

### Bank 2 Specific

#### POST /api/invest
Make investment with dual-run validation
```json
Request: {
  "customer_id": 1,
  "amount": 1000.0,
  "category": "stocks"
}
```

## Environment Variables

### Optional Configuration

```bash
# Bank 1 (Savings)
BANK_NAME="Savings Bank"
BANK_ID="bank1"
BANK_COLOR="#2E7D32"  # Green
DB_PATH="bank1_savings.db"
AUDIT_LOG_PATH="bank1_audit.jsonl"

# Bank 2 (Investment)
BANK_NAME="Investment Bank"
BANK_ID="bank2"
BANK_COLOR="#1565C0"  # Blue
DB_PATH="bank2_investment.db"
AUDIT_LOG_PATH="bank2_audit.jsonl"
```

**Note:** No API keys required! The applications use pre-generated SQL templates and natural language parsing.

## Running the Applications

### Installation

```bash
# Bank 1
cd banking-demo/bank1-savings
pip install -r requirements.txt
python app.py

# Bank 2
cd banking-demo/bank2-investment
pip install -r requirements.txt
python app.py
```

### Docker Deployment

```bash
# Build and run Bank 1
cd banking-demo/bank1-savings
docker build -t bank1-savings .
docker run -p 5001:5000 -e ANTHROPIC_API_KEY=your-key bank1-savings

# Build and run Bank 2
cd banking-demo/bank2-investment
docker build -t bank2-investment .
docker run -p 5002:5000 -e ANTHROPIC_API_KEY=your-key bank2-investment
```

### Access the Applications

- Bank 1 (Savings): http://localhost:5001
- Bank 2 (Investment): http://localhost:5002

## Security Best Practices

1. **Always use parameterized queries** - Never concatenate user input into SQL
2. **Validate all inputs** - Check types, ranges, and business rules
3. **Enforce data isolation** - Always include customer_id filters
4. **Log everything** - Maintain comprehensive audit trails
5. **Use dual-run validation** - For high-stakes operations
6. **Verify schema** - Post-execution validation of results
7. **Protect API keys** - Use environment variables, never commit keys
8. **Monitor audit logs** - Regular compliance reviews

## Compliance Features

### GDPR/CCPA Compliance
- Customer data isolation
- Audit trail for data access
- Structured consent disclaimers
- Data minimization (only query what's needed)

### Financial Regulations
- Immutable audit logs
- Transaction provenance tracking
- Dual-run validation for critical operations
- Balance constraints and validation

### SOC 2 / ISO 27001
- Comprehensive logging
- Access control (customer_id isolation)
- Data integrity checks
- Security monitoring capabilities

## Demo Data

### Bank 1 (Savings) - 5 Customers
- Alice Johnson: $5,500 (savings)
- Bob Smith: $4,000 (savings)
- Carol Davis: $6,500 (savings)
- David Wilson: $3,300 (savings)
- Emma Brown: $4,600 (savings)

### Bank 2 (Investment) - 5 Customers
- Alice Johnson: $11,000 (investment)
- Bob Smith: $12,000 (investment)
- Carol Davis: $13,000 (investment)
- David Wilson: $14,000 (investment)
- Emma Brown: $15,000 (investment)

## Troubleshooting

### Database Issues
```bash
# Reset database
rm bank1_savings.db bank2_investment.db
python app.py  # Will recreate with demo data
```

### Audit Log Issues
```bash
# View audit log
cat bank1_audit.jsonl | jq .
cat bank2_audit.jsonl | jq .
```

### API Key Issues
```bash
# Verify API key is set
echo $ANTHROPIC_API_KEY

# Set API key
export ANTHROPIC_API_KEY="your-key-here"
```

## Future Enhancements

- [ ] Multi-factor authentication
- [ ] Real-time fraud detection
- [ ] Advanced ML-based analytics
- [ ] Blockchain-based audit trail
- [ ] Mobile app integration
- [ ] Biometric authentication
- [ ] Real-time notifications
- [ ] Advanced reporting dashboard

## Support

For issues or questions:
1. Check the audit logs for error details
2. Review the TROUBLESHOOTING.md file
3. Verify environment variables are set correctly
4. Ensure all dependencies are installed

## License

This is a demonstration application for educational purposes.