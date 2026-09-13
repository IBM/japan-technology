# Banking Applications - Testing Guide

## Quick Start Testing

This guide will help you test both banking applications with all their new features.

## Prerequisites

1. Python 3.8 or higher
2. Required Python packages (installed via requirements.txt)

## Setup

### 1. Install Dependencies

```bash
# Bank 1 (Savings)
cd banking-demo/bank1-savings
pip install -r requirements.txt

# Bank 2 (Investment)
cd banking-demo/bank2-investment
pip install -r requirements.txt
```

### 2. Optional Environment Variables

```bash
# Optional: Customize bank settings
export BANK_NAME="My Savings Bank"
export BANK_COLOR="#2E7D32"
```

**Note:** No API keys required! The applications work out-of-the-box.

### 3. Start the Applications

**Terminal 1 - Bank 1 (Savings):**
```bash
cd banking-demo/bank1-savings
python app.py
```
Access at: http://localhost:5000

**Terminal 2 - Bank 2 (Investment):**
```bash
cd banking-demo/bank2-investment
python app.py
```
Access at: http://localhost:5000 (or change port in app.py)

## Testing Scenarios

### Test 1: Web Interface Navigation

1. Open http://localhost:5000 in your browser
2. Verify the bank name and color scheme appear correctly
3. Check that all operation buttons are visible:
   - Check Balance/Portfolio
   - View Transactions
   - Spending/Investment Analytics
   - Transfer/Invest
   - Custom Query

### Test 2: Check Balance (Data Isolation)

**Via Web Interface:**
1. Click "Check Balance" button
2. Enter Customer ID: 1
3. Click "Execute"
4. Verify response shows only customer 1's data

**Via API (curl):**
```bash
curl -X POST http://localhost:5000/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'
```

**Expected Response:**
```json
{
  "success": true,
  "customer_name": "Alice Johnson",
  "query_type": "balance",
  "result_data": [
    {
      "name": "Alice Johnson",
      "email": "alice@example.com",
      "account_type": "savings",
      "balance": 5500.0
    }
  ],
  "compliance_disclaimer": "This banking information is provided...",
  "timestamp": "2025-11-17T20:30:00.000Z",
  "bank": "Savings Bank"
}
```

### Test 3: View Transactions

**Via Web Interface:**
1. Click "View Transactions"
2. Enter Customer ID: 1
3. Enter Limit: 5
4. Click "Execute"

**Via API:**
```bash
curl -X POST http://localhost:5000/api/transactions \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "limit": 5}'
```

**Verify:**
- Only transactions for customer 1 are returned
- Transactions are ordered by date (newest first)
- All required fields are present

### Test 4: Spending/Investment Analytics

**Via Web Interface:**
1. Click "Spending Analytics" (Bank 1) or "Investment Analytics" (Bank 2)
2. Enter Customer ID: 1
3. Click "Execute"
4. Verify charts appear below the result

**Via API:**
```bash
curl -X POST http://localhost:5000/api/analytics \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'
```

**Expected Features:**
- Category breakdown with totals
- Pie chart showing spending/investment distribution
- Line chart showing activity over time
- Total spent/invested amount

### Test 5: Transfer/Investment (Dual-Run Validation)

**Bank 1 - Transfer Funds:**
```bash
curl -X POST http://localhost:5000/api/transfer \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "amount": 100.0,
    "to_account_id": 2
  }'
```

**Bank 2 - Make Investment:**
```bash
curl -X POST http://localhost:5000/api/invest \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "amount": 500.0,
    "category": "stocks"
  }'
```

**Verify:**
- Dual-run validation executes (check audit log)
- Balance is updated correctly
- Transaction is recorded
- Audit log contains both validation runs

### Test 6: Custom Query (Natural Language Parsing)

**Via Web Interface:**
1. Click "Custom Query"
2. Enter Customer ID: 1
3. Enter Query Description: "Show my last 5 transactions"
4. Click "Execute"

**Via API:**
```bash
curl -X POST http://localhost:5000/api/custom_query \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "query_description": "Show my last 3 transactions"
  }'
```

**Supported Query Patterns:**
- "last X transactions" - Recent history
- "transactions over $X" - Large transactions
- "by category" - Category breakdown
- "monthly summary" - Monthly aggregation
- "account summary" - Portfolio overview

**Verify:**
- Parser selects appropriate SQL template
- Query includes WHERE customer_id = ? for isolation
- Results are returned correctly
- Generated SQL is shown in response
- `parsed_from` field shows original query

### Test 7: Audit Log Viewer

**Via Web Interface:**
1. Scroll to "Audit Log Viewer" section
2. Click "Refresh Audit Log"
3. Verify entries appear with:
   - Timestamp
   - Event type
   - Customer ID
   - SQL query
   - Hash (first 16 characters)

**Via API:**
```bash
curl http://localhost:5000/api/audit_log
```

**Verify:**
- Last 50 entries are returned
- Each entry has all required fields
- Hash is present for immutability verification

### Test 8: Schema Validation

**Test Negative Balance (Should Fail):**
```bash
# This should fail due to CHECK constraint
sqlite3 bank1_savings.db "UPDATE accounts SET balance = -100 WHERE customer_id = 1"
```

**Expected:** Error message about constraint violation

**Test Type Validation:**
Try to query with invalid data types and verify validation catches it.

### Test 9: Data Isolation Verification

**Attempt Cross-Customer Access:**
```bash
# Query for customer 1
curl -X POST http://localhost:5000/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'

# Query for customer 2
curl -X POST http://localhost:5000/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 2}'
```

**Verify:**
- Each request returns ONLY data for the specified customer
- No cross-customer data leakage
- Different customer names in responses

### Test 10: Health Check

```bash
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "bank": "Savings Bank",
  "bank_id": "bank1",
  "database": "connected"
}
```

## Audit Log Verification

### View Audit Log File

```bash
# Bank 1
cat banking-demo/bank1-savings/bank1_audit.jsonl | jq .

# Bank 2
cat banking-demo/bank2-investment/bank2_audit.jsonl | jq .
```

### Verify Audit Entry Structure

Each entry should contain:
```json
{
  "timestamp": "2025-11-17T20:30:00.000Z",
  "bank_id": "bank1",
  "event_type": "balance_check",
  "customer_id": 1,
  "prompt": "Check balance",
  "generated_sql": "SELECT c.name, a.balance FROM...",
  "result": "[{'name': 'Alice Johnson', 'balance': 5500.0}]",
  "model_config": {"model": "direct_sql", "version": "1.0"},
  "error": null,
  "hash": "a1b2c3d4e5f6789..."
}
```

### Verify Hash Immutability

```bash
# Extract and verify hashes
cat bank1_audit.jsonl | jq -r '.hash' | head -5
```

Each hash should be unique and 64 characters (SHA-256).

## Database Inspection

### View Database Schema

```bash
sqlite3 bank1_savings.db ".schema"
```

### Query Demo Data

```bash
# View all customers
sqlite3 bank1_savings.db "SELECT * FROM customers;"

# View all accounts
sqlite3 bank1_savings.db "SELECT * FROM accounts;"

# View recent transactions
sqlite3 bank1_savings.db "SELECT * FROM transactions ORDER BY transaction_date DESC LIMIT 10;"

# View customer balances (using view)
sqlite3 bank1_savings.db "SELECT * FROM customer_balances;"
```

## Performance Testing

### Load Test with Multiple Requests

```bash
# Install Apache Bench (if not already installed)
# macOS: brew install httpd
# Ubuntu: apt-get install apache2-utils

# Test balance endpoint
ab -n 100 -c 10 -p balance_request.json -T application/json \
  http://localhost:5000/api/balance
```

**balance_request.json:**
```json
{"customer_id": 1}
```

### Monitor Audit Log Growth

```bash
# Watch audit log in real-time
tail -f bank1_audit.jsonl
```

## Error Testing

### Test Missing Customer ID

```bash
curl -X POST http://localhost:5000/api/balance \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Expected:** 400 error with message "Customer ID required"

### Test Invalid Customer ID

```bash
curl -X POST http://localhost:5000/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 999}'
```

**Expected:** 404 error with message "Customer not found"

### Test Insufficient Funds

```bash
curl -X POST http://localhost:5000/api/transfer \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "amount": 999999.0,
    "to_account_id": 2
  }'
```

**Expected:** 400 error with message "Insufficient funds"

### Test Without API Key (Custom Query)

```bash
# Unset API key
unset ANTHROPIC_API_KEY

# Restart app and try custom query
curl -X POST http://localhost:5000/api/custom_query \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "query_description": "Show my transactions"
  }'
```

**Expected:** 500 error with message "AI service not configured"

## Compliance Testing

### Verify Compliance Disclaimer

Check that every API response includes:
```json
{
  "compliance_disclaimer": "This banking information is provided for informational purposes only..."
}
```

### Verify Required Response Fields

Every response must include:
- `success` (boolean)
- `customer_name` (string)
- `query_type` (string)
- `result_data` (any)
- `compliance_disclaimer` (string)
- `timestamp` (ISO 8601 string)
- `bank` (string)

### Verify Data Isolation

Run multiple queries for different customers and verify:
1. No customer sees another customer's data
2. All queries include WHERE customer_id = ? clause
3. Audit log shows correct customer_id for each operation

## Visualization Testing

### Test Chart Generation

1. Navigate to Analytics page
2. Execute analytics for customer 1
3. Verify two charts appear:
   - Pie chart (category breakdown)
   - Line chart (time series)
4. Check that charts are interactive (hover, zoom)

### Test Chart Data Accuracy

Compare chart data with raw database queries:
```bash
sqlite3 bank1_savings.db "
  SELECT category, SUM(amount) as total 
  FROM transactions 
  WHERE customer_id = 1 AND amount < 0 
  GROUP BY category;
"
```

## Cleanup

### Reset Databases

```bash
cd banking-demo/bank1-savings
rm bank1_savings.db bank1_audit.jsonl

cd banking-demo/bank2-investment
rm bank2_investment.db bank2_audit.jsonl
```

### Restart Applications

After cleanup, restart both applications to recreate databases with fresh demo data.

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 5000
lsof -i :5000

# Kill process
kill -9 <PID>
```

### Database Locked

```bash
# Close all connections and restart
rm *.db-journal
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## Success Criteria

✅ All API endpoints return 200 status for valid requests
✅ Data isolation prevents cross-customer access
✅ Audit log captures all operations
✅ Schema validation catches invalid data
✅ Dual-run validation works for high-stakes operations
✅ Charts render correctly in web interface
✅ Compliance disclaimer appears in all responses
✅ Error handling returns appropriate status codes
✅ Database constraints prevent negative balances
✅ Parameterized queries prevent SQL injection

## Next Steps

After successful testing:
1. Review audit logs for any anomalies
2. Check database integrity
3. Verify all compliance requirements are met
4. Document any issues found
5. Prepare for production deployment

## Support

For issues during testing:
1. Check application logs
2. Review audit logs for error details
3. Verify environment variables
4. Ensure all dependencies are installed
5. Check database file permissions