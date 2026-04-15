from flask import Flask, jsonify, request, render_template_string, send_from_directory
import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Tuple, Optional
import hashlib
import re
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

#test

app = Flask(__name__, static_folder='static', static_url_path='')

# Bank configuration
BANK_NAME = os.getenv('BANK_NAME', 'Savings Bank')
BANK_ID = os.getenv('BANK_ID', 'bank1')
BANK_COLOR = os.getenv('BANK_COLOR', '#2E7D32')  # Green for savings
DB_PATH = os.getenv('DB_PATH', 'bank1_savings.db')
AUDIT_LOG_PATH = os.getenv('AUDIT_LOG_PATH', 'bank1_audit.jsonl')
BANK2_URL = os.getenv('BANK2_URL', 'http://localhost:5002')

# VULNERABILITY 1: Hardcoded credentials (CWE-798: Use of Hard-coded Credentials)
# PCI-DSS Requirement 8.2.1: Do not use vendor-supplied defaults
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "P@ssw0rd123"  # Hardcoded password
API_KEY = "sk_live_51234567890abcdef"  # Hardcoded API key
DATABASE_PASSWORD = "db_secret_2024"  # Hardcoded database password

# VULNERABILITY 2: Sensitive data in logs (CWE-532: Insertion of Sensitive Information into Log File)
# PCI-DSS Requirement 3.4: Render PAN unreadable
def log_transaction(customer_id, card_number, amount):
    """Log transaction with sensitive data exposed"""
    print(f"Transaction: Customer {customer_id}, Card: {card_number}, Amount: ${amount}")
    # This violates PCI-DSS by logging full card numbers

# Compliance disclaimer
COMPLIANCE_DISCLAIMER = "This banking information is provided for informational purposes only. All transactions are subject to verification and regulatory compliance. Customer data is protected under applicable privacy laws."

# Pre-generated SQL query templates for common operations
SQL_TEMPLATES = {
    'recent_transactions': '''
        SELECT t.transaction_id, t.transaction_type, t.category, t.amount,
               t.description, t.transaction_date
        FROM transactions t
        WHERE t.customer_id = ?
        ORDER BY t.transaction_date DESC
        LIMIT ?
    ''',
    'large_transactions': '''
        SELECT t.transaction_id, t.transaction_type, t.category, t.amount,
               t.description, t.transaction_date
        FROM transactions t
        WHERE t.customer_id = ? AND ABS(t.amount) > ?
        ORDER BY t.transaction_date DESC
    ''',
    'transactions_by_category': '''
        SELECT t.category, COUNT(*) as count, SUM(t.amount) as total
        FROM transactions t
        WHERE t.customer_id = ?
        GROUP BY t.category
        ORDER BY total DESC
    ''',
    'monthly_summary': '''
        SELECT strftime('%Y-%m', t.transaction_date) as month,
               COUNT(*) as transaction_count,
               SUM(CASE WHEN t.amount > 0 THEN t.amount ELSE 0 END) as deposits,
               SUM(CASE WHEN t.amount < 0 THEN ABS(t.amount) ELSE 0 END) as withdrawals
        FROM transactions t
        WHERE t.customer_id = ?
        GROUP BY month
        ORDER BY month DESC
    ''',
    'account_summary': '''
        SELECT c.name, c.email, a.account_type, a.balance,
               COUNT(t.transaction_id) as transaction_count
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
        LEFT JOIN transactions t ON a.account_id = t.account_id
        WHERE c.customer_id = ?
        GROUP BY c.customer_id, a.account_id
    '''
}

# Natural language query parser
def parse_natural_language_query(description: str, customer_id: int) -> Tuple[str, Tuple]:
    """Parse natural language description and return appropriate SQL query"""
    description_lower = description.lower()
    
    # Pattern matching for common queries
    if 'last' in description_lower and 'transaction' in description_lower:
        # Extract number if present
        match = re.search(r'(\d+)', description_lower)
        limit = int(match.group(1)) if match else 10
        return SQL_TEMPLATES['recent_transactions'], (customer_id, limit)
    
    elif 'over' in description_lower or 'more than' in description_lower or 'greater than' in description_lower:
        # Extract amount
        match = re.search(r'\$?(\d+(?:\.\d{2})?)', description_lower)
        amount = float(match.group(1)) if match else 100.0
        return SQL_TEMPLATES['large_transactions'], (customer_id, amount)
    
    elif 'category' in description_lower or 'categories' in description_lower:
        return SQL_TEMPLATES['transactions_by_category'], (customer_id,)
    
    elif 'month' in description_lower or 'summary' in description_lower:
        return SQL_TEMPLATES['monthly_summary'], (customer_id,)
    
    elif 'account' in description_lower or 'summary' in description_lower:
        return SQL_TEMPLATES['account_summary'], (customer_id,)
    
    else:
        # Default to recent transactions
        return SQL_TEMPLATES['recent_transactions'], (customer_id, 10)

# Database initialization
def init_db():
    """Initialize SQLite database with schema"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            ssn TEXT,
            card_number TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Accounts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            account_type TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            transaction_type TEXT NOT NULL,
            category TEXT,
            amount REAL NOT NULL,
            description TEXT,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Balances view (for quick access)
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS customer_balances AS
        SELECT 
            c.customer_id,
            c.name,
            c.email,
            a.account_id,
            a.account_type,
            a.balance
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
    ''')
    
    # Insert demo data if tables are empty
    cursor.execute('SELECT COUNT(*) FROM customers')
    if cursor.fetchone()[0] == 0:
        # VULNERABILITY 3: Storing sensitive data unencrypted (CWE-311: Missing Encryption of Sensitive Data)
        # PCI-DSS Requirement 3.4: Render PAN unreadable anywhere it is stored
        demo_customers = [
            ('Alice Johnson', 'alice@example.com', '123-45-6789', '4532-1234-5678-9010'),
            ('Bob Smith', 'bob@example.com', '987-65-4321', '5425-2345-6789-0123'),
            ('Carol Davis', 'carol@example.com', '456-78-9012', '4916-3456-7890-1234'),
            ('David Wilson', 'david@example.com', '789-01-2345', '4024-4567-8901-2345'),
            ('Emma Brown', 'emma@example.com', '234-56-7890', '5105-5678-9012-3456')
        ]
        cursor.executemany('INSERT INTO customers (name, email, ssn, card_number) VALUES (?, ?, ?, ?)', demo_customers)
        
        # Create accounts for each customer
        for i in range(1, 6):
            cursor.execute('INSERT INTO accounts (customer_id, account_type, balance) VALUES (?, ?, ?)',
                         (i, 'savings', 5000.0 + (i * 500)))
        
        # Insert demo transactions
        demo_transactions = [
            (1, 1, 'deposit', 'salary', 3000.0, 'Monthly salary'),
            (1, 1, 'withdrawal', 'groceries', -150.0, 'Supermarket'),
            (1, 1, 'withdrawal', 'utilities', -200.0, 'Electric bill'),
            (2, 2, 'deposit', 'salary', 2500.0, 'Monthly salary'),
            (2, 2, 'withdrawal', 'entertainment', -80.0, 'Movie tickets'),
            (3, 3, 'deposit', 'salary', 4000.0, 'Monthly salary'),
            (3, 3, 'withdrawal', 'groceries', -300.0, 'Weekly shopping'),
            (4, 4, 'deposit', 'salary', 2800.0, 'Monthly salary'),
            (5, 5, 'deposit', 'salary', 3500.0, 'Monthly salary'),
        ]
        cursor.executemany(
            'INSERT INTO transactions (account_id, customer_id, transaction_type, category, amount, description) VALUES (?, ?, ?, ?, ?, ?)',
            demo_transactions
        )
    
    conn.commit()
    conn.close()

# Audit logging
def log_audit(event_type: str, customer_id: Optional[int], prompt: str, sql_query: str, 
              result: Any, model_config: Dict, error: Optional[str] = None):
    """Log all interactions to immutable audit trail"""
    audit_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'bank_id': BANK_ID,
        'event_type': event_type,
        'customer_id': customer_id,
        'prompt': prompt,
        'generated_sql': sql_query,
        'result': str(result)[:500],  # Truncate large results
        'model_config': model_config,
        'error': error,
        'hash': ''  # Will be filled
    }
    
    # Create hash for immutability verification
    hash_input = json.dumps(audit_entry, sort_keys=True)
    audit_entry['hash'] = hashlib.sha256(hash_input.encode()).hexdigest()
    
    # Append to JSONL file
    with open(AUDIT_LOG_PATH, 'a') as f:
        f.write(json.dumps(audit_entry) + '\n')

# Schema validation
def validate_result(result: List[Dict], expected_schema: Dict) -> Tuple[bool, str]:
    """Validate query results against expected schema and business rules"""
    if not result:
        return True, "No data to validate"
    
    for row in result:
        for field, field_type in expected_schema.items():
            if field not in row:
                return False, f"Missing required field: {field}"
            
            value = row[field]
            
            # Type checking
            if field_type == 'float' and not isinstance(value, (int, float)):
                return False, f"Field {field} must be numeric, got {type(value)}"
            
            if field_type == 'str' and not isinstance(value, str):
                return False, f"Field {field} must be string, got {type(value)}"
            
            # Business rule: balances must be >= 0
            if field == 'balance' and value < 0:
                return False, f"Balance cannot be negative: {value}"
    
    return True, "Validation passed"

# Secure database query execution
def execute_query(query: str, params: Tuple, customer_id: Optional[int] = None, 
                 expected_schema: Optional[Dict] = None) -> Tuple[List[Dict], Optional[str]]:
    """Execute parameterized query with validation"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(query, params)
        
        if query.strip().upper().startswith('SELECT'):
            rows = cursor.fetchall()
            result = [dict(row) for row in rows]
            
            # Schema validation
            if expected_schema:
                is_valid, message = validate_result(result, expected_schema)
                if not is_valid:
                    conn.close()
                    return [], f"Validation failed: {message}"
            
            conn.close()
            return result, None
        else:
            conn.commit()
            affected_rows = cursor.rowcount
            conn.close()
            return [{'affected_rows': affected_rows}], None
            
    except sqlite3.Error as e:
        return [], str(e)

# VULNERABILITY 4: SQL Injection (CWE-89: Improper Neutralization of Special Elements used in an SQL Command)
# PCI-DSS Requirement 6.5.1: Injection flaws, particularly SQL injection
@app.route('/api/search_customer', methods=['POST'])
def search_customer():
    """Search customer by name - VULNERABLE TO SQL INJECTION"""
    data = request.get_json()
    search_term = data.get('search_term', '')
    
    query = f"SELECT customer_id, name, email, ssn, card_number FROM customers WHERE name LIKE '%{search_term}%'"
    
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query)  # SQL Injection vulnerability
        rows = cursor.fetchall()
        result = [dict(row) for row in rows]
        conn.close()
        

        return jsonify({
            'success': True,
            'customers': result  # Returns SSN and full card numbers
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/admin/delete_customer', methods=['POST'])
def delete_customer():
    """Delete customer - NO AUTHENTICATION REQUIRED"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    
    # No authentication check!
    query = "DELETE FROM customers WHERE customer_id = ?"
    result, error = execute_query(query, (customer_id,))
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    return jsonify({'success': True, 'message': f'Customer {customer_id} deleted'})

# VULNERABILITY 7: Weak session management (CWE-384: Session Fixation)
# PCI-DSS Requirement 8.2.3: Passwords/passphrases must meet minimum strength
@app.route('/api/login', methods=['POST'])
def login():
    """Login endpoint with weak session management"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # VULNERABLE: Weak password comparison, no rate limiting
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        # VULNERABLE: Predictable session token
        session_token = f"session_{username}_{datetime.now().strftime('%Y%m%d')}"
        
        return jsonify({
            'success': True,
            'session_token': session_token,
            'admin_password': ADMIN_PASSWORD  # VULNERABILITY: Exposing password in response
        })
    
    return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

# VULNERABILITY 8: Missing input validation (CWE-20: Improper Input Validation)
@app.route('/api/update_balance', methods=['POST'])
def update_balance():
    """Update account balance - NO INPUT VALIDATION"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    new_balance = data.get('new_balance')  # No validation - could be negative or extremely large
    
    # No validation of balance amount
    query = "UPDATE accounts SET balance = ? WHERE customer_id = ?"
    result, error = execute_query(query, (new_balance, customer_id))
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    return jsonify({'success': True, 'new_balance': new_balance})

# VULNERABILITY 9: Insecure direct object reference (CWE-639: Authorization Bypass Through User-Controlled Key)
# PCI-DSS Requirement 7.1: Limit access to system components and cardholder data
@app.route('/api/get_customer_details/<int:customer_id>', methods=['GET'])
def get_customer_details(customer_id):
    """Get customer details - NO AUTHORIZATION CHECK"""
    # Any user can access any customer's data by changing the ID
    query = "SELECT * FROM customers WHERE customer_id = ?"
    result, error = execute_query(query, (customer_id,))
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    return jsonify({'success': True, 'customer': result[0] if result else None})

# VULNERABILITY 10: Missing HTTPS/TLS (CWE-319: Cleartext Transmission of Sensitive Information)
# PCI-DSS Requirement 4.1: Use strong cryptography and security protocols
# Note: This Flask app runs on HTTP, not HTTPS

# Dual-run validation for high-stakes queries
def dual_run_validation(prompt: str, customer_id: int) -> Tuple[bool, str, str]:
    """
    Simulate dual-run validation using deterministic SQL generation.
    In production, this would use AI to generate queries twice and compare them.
    For this demo, we use pre-validated SQL templates.
    """
    # Parse the prompt to determine the operation
    prompt_lower = prompt.lower()
    
    # Generate SQL based on operation type
    if 'transfer' in prompt_lower:
        sql_query = '''
            UPDATE accounts
            SET balance = balance - ?
            WHERE customer_id = ? AND balance >= ?
        '''
    elif 'invest' in prompt_lower:
        sql_query = '''
            INSERT INTO transactions (account_id, customer_id, transaction_type, category, amount, description)
            VALUES (?, ?, 'deposit', ?, ?, ?)
        '''
    else:
        return False, "", "Unknown operation type for dual-run validation"
    
    # Simulate dual-run by validating the query structure
    # In a real system, this would generate the query twice using AI
    validation_passed = True 
    validation_message = "Dual-run validation passed (using pre-validated SQL templates)"
    
    return validation_passed, sql_query, validation_message

# Generate spending analytics
def generate_spending_analytics(customer_id: int) -> Dict:
    """Generate spending analytics with visualizations"""
    # Get transaction data
    query = '''
        SELECT 
            category,
            SUM(amount) as total_amount,
            COUNT(*) as transaction_count,
            DATE(transaction_date) as date
        FROM transactions
        WHERE customer_id = ? AND amount < 0
        GROUP BY category, DATE(transaction_date)
        ORDER BY date DESC
    '''
    
    result, error = execute_query(query, (customer_id,))
    
    if error:
        return {'error': error}
    
    if not result:
        return {'message': 'No spending data available'}
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(result)
    df['total_amount'] = df['total_amount'].abs()
    
    # Category breakdown
    category_totals = df.groupby('category')['total_amount'].sum().reset_index()
    
    # Create pie chart
    fig_pie = px.pie(category_totals, values='total_amount', names='category',
                     title='Spending by Category')
    pie_chart_html = fig_pie.to_html(full_html=False)
    
    # Create time series
    daily_spending = df.groupby('date')['total_amount'].sum().reset_index()
    fig_line = px.line(daily_spending, x='date', y='total_amount',
                       title='Daily Spending Trend')
    line_chart_html = fig_line.to_html(full_html=False)
    
    return {
        'category_breakdown': category_totals.to_dict('records'),
        'daily_spending': daily_spending.to_dict('records'),
        'pie_chart': pie_chart_html,
        'line_chart': line_chart_html,
        'total_spent': float(df['total_amount'].sum())
    }

# Structured JSON response builder
def build_response(customer_name: str, query_type: str, result_data: Any, 
                  success: bool = True, error: Optional[str] = None) -> Dict:
    """Build standardized JSON response"""
    return {
        'success': success,
        'customer_name': customer_name,
        'query_type': query_type,
        'result_data': result_data,
        'error': error,
        'compliance_disclaimer': COMPLIANCE_DISCLAIMER,
        'timestamp': datetime.utcnow().isoformat(),
        'bank': BANK_NAME
    }

# Routes
@app.route('/')
def home():
    """Serve React app"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_react_app(path):
    """Serve React app assets or fallback to index.html for client-side routing"""
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/balance', methods=['POST'])
def get_balance():
    """Get customer balance with data isolation"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    
    if not customer_id:
        return jsonify(build_response('Unknown', 'balance', None, False, 'Customer ID required')), 400
    
    # Secure parameterized query with customer isolation
    query = '''
        SELECT c.name, c.email, a.account_type, a.balance
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
        WHERE c.customer_id = ?
    '''
    
    expected_schema = {'name': 'str', 'email': 'str', 'account_type': 'str', 'balance': 'float'}
    result, error = execute_query(query, (customer_id,), customer_id, expected_schema)
    
    # Log to audit trail
    log_audit('balance_check', customer_id, 'Check balance', query, result, 
              {'model': 'direct_sql', 'version': '1.0'}, error)
    
    if error:
        return jsonify(build_response('Unknown', 'balance', None, False, error)), 500
    
    if not result:
        return jsonify(build_response('Unknown', 'balance', None, False, 'Customer not found')), 404
    
    customer_name = result[0]['name']
    return jsonify(build_response(customer_name, 'balance', result, True))

@app.route('/api/transactions', methods=['POST'])
def get_transactions():
    """Get customer transactions with data isolation"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    limit = data.get('limit', 10)
    
    if not customer_id:
        return jsonify(build_response('Unknown', 'transactions', None, False, 'Customer ID required')), 400
    
    query = '''
        SELECT t.transaction_id, t.transaction_type, t.category, t.amount, 
               t.description, t.transaction_date
        FROM transactions t
        WHERE t.customer_id = ?
        ORDER BY t.transaction_date DESC
        LIMIT ?
    '''
    
    result, error = execute_query(query, (customer_id, limit), customer_id)
    
    log_audit('transaction_history', customer_id, f'Get last {limit} transactions', 
              query, result, {'model': 'direct_sql', 'version': '1.0'}, error)
    
    if error:
        return jsonify(build_response('Unknown', 'transactions', None, False, error)), 500
    
    # Get customer name
    name_query = 'SELECT name FROM customers WHERE customer_id = ?'
    name_result, _ = execute_query(name_query, (customer_id,))
    customer_name = name_result[0]['name'] if name_result else 'Unknown'
    
    return jsonify(build_response(customer_name, 'transactions', result, True))

@app.route('/api/analytics', methods=['POST'])
def get_analytics():
    """Get spending analytics with visualizations"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    
    if not customer_id:
        return jsonify(build_response('Unknown', 'analytics', None, False, 'Customer ID required')), 400
    
    analytics_data = generate_spending_analytics(customer_id)
    
    log_audit('spending_analytics', customer_id, 'Generate spending analytics', 
              'Multiple aggregation queries', analytics_data, 
              {'model': 'analytics_engine', 'version': '1.0'})
    
    # Get customer name
    name_query = 'SELECT name FROM customers WHERE customer_id = ?'
    name_result, _ = execute_query(name_query, (customer_id,))
    customer_name = name_result[0]['name'] if name_result else 'Unknown'
    
    return jsonify(build_response(customer_name, 'analytics', analytics_data, True))

@app.route('/api/receive_transfer', methods=['POST'])
def receive_transfer():
    """Receive transfer from Investment Bank (Bank 2)"""
    try:
        data = request.json
        customer_id = data.get('customer_id')
        amount = data.get('amount')
        
        if not customer_id or not amount:
            return jsonify({'success': False, 'error': 'Missing customer_id or amount'}), 400
        
        amount = float(amount)
        if amount <= 0:
            return jsonify({'success': False, 'error': 'Amount must be positive'}), 400
        
        # Add to savings account
        query = 'UPDATE accounts SET balance = balance + ? WHERE customer_id = ?'
        result, error = execute_query(query, (amount, customer_id))
        
        if error:
            return jsonify({'success': False, 'error': error}), 500
        
        # Record deposit transaction
        tx_query = '''INSERT INTO transactions (customer_id, account_id, transaction_type, amount, category, description)
                      SELECT ?, account_id, 'deposit', ?, 'Transfer', 'Transfer from Investment Bank'
                      FROM accounts WHERE customer_id = ?'''
        execute_query(tx_query, (customer_id, amount, customer_id))
        
        # Get updated balance
        balance_query = 'SELECT balance FROM accounts WHERE customer_id = ?'
        balance_result, _ = execute_query(balance_query, (customer_id,))
        new_balance = balance_result[0]['balance'] if balance_result else 0
        
        return jsonify({
            'success': True,
            'message': f'Transfer received: ${amount:.2f}',
            'new_balance': new_balance
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transfer', methods=['POST'])
def transfer_funds():
    """Transfer funds from Savings to Investment Bank with dual-run validation"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    amount = data.get('amount')
    
    if not all([customer_id, amount]):
        return jsonify(build_response('Unknown', 'transfer', None, False,
                                     'Missing required fields')), 400
    
    if amount <= 0:
        return jsonify(build_response('Unknown', 'transfer', None, False,
                                     'Amount must be positive')), 400
    
    # Dual-run validation for high-stakes operation
    prompt = f"Transfer {amount} from customer {customer_id} savings to investment"
    is_valid, sql_query, message = dual_run_validation(prompt, customer_id)
    
    if not is_valid:
        log_audit('transfer_failed', customer_id, prompt, '', None,
                 {'model': 'template_based', 'dual_run': True}, message)
        return jsonify(build_response('Unknown', 'transfer', None, False, message)), 400
    
    # Check balance first
    balance_query = '''
        SELECT a.balance, c.name, a.account_id
        FROM accounts a
        JOIN customers c ON a.customer_id = c.customer_id
        WHERE a.customer_id = ?
    '''
    balance_result, error = execute_query(balance_query, (customer_id,), customer_id)
    
    if error or not balance_result:
        return jsonify(build_response('Unknown', 'transfer', None, False,
                                     'Could not verify balance')), 500
    
    customer_name = balance_result[0]['name']
    current_balance = balance_result[0]['balance']
    account_id = balance_result[0]['account_id']
    
    if current_balance < amount:
        return jsonify(build_response(customer_name, 'transfer', None, False,
                                     f'Insufficient funds. Balance: ${current_balance:.2f}')), 400
    
    # Deduct from Savings Bank
    update_query = '''
        UPDATE accounts
        SET balance = balance - ?
        WHERE customer_id = ? AND balance >= ?
    '''
    
    result, error = execute_query(update_query, (amount, customer_id, amount), customer_id)
    
    if error:
        log_audit('transfer_failed', customer_id, prompt, update_query, None,
                 {'model': 'template_based', 'dual_run': True}, error)
        return jsonify(build_response(customer_name, 'transfer', None, False, error)), 500
    
    # Record withdrawal transaction
    trans_query = '''
        INSERT INTO transactions (account_id, customer_id, transaction_type, category, amount, description)
        VALUES (?, ?, 'withdrawal', 'transfer', ?, 'Transfer to Investment Bank')
    '''
    execute_query(trans_query, (account_id, customer_id, -amount))
    
    # Send to Investment Bank (Bank 2)
    try:
        import requests
        response = requests.post(
            f'{BANK2_URL}/api/receive_transfer',
            json={'customer_id': customer_id, 'amount': amount},
            timeout=5
        )
        
        if response.status_code == 200:
            bank2_result = response.json()
            log_audit('transfer_completed', customer_id, prompt, update_query, result,
                     {'model': 'template_based', 'dual_run': True, 'validation': 'passed'})
            
            return jsonify(build_response(customer_name, 'transfer',
                                         {'amount': amount,
                                          'from': 'Savings Bank',
                                          'to': 'Investment Bank',
                                          'new_savings_balance': current_balance - amount,
                                          'bank2_response': bank2_result}, True))
        else:
            # Rollback on failure
            rollback_query = 'UPDATE accounts SET balance = balance + ? WHERE customer_id = ?'
            execute_query(rollback_query, (amount, customer_id))
            return jsonify(build_response(customer_name, 'transfer', None, False,
                                         'Transfer to Investment Bank failed - transaction rolled back')), 500
            
    except Exception as e:
        # Rollback on error
        rollback_query = 'UPDATE accounts SET balance = balance + ? WHERE customer_id = ?'
        execute_query(rollback_query, (amount, customer_id))
        log_audit('transfer_failed', customer_id, prompt, update_query, None,
                 {'model': 'template_based', 'dual_run': True}, str(e))
        return jsonify(build_response(customer_name, 'transfer', None, False,
                                     f'Could not connect to Investment Bank - transaction rolled back: {str(e)}')), 500

@app.route('/api/custom_query', methods=['POST'])
def custom_query():
    """Execute custom query using natural language parsing"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    query_description = data.get('query_description')
    
    if not all([customer_id, query_description]):
        return jsonify(build_response('Unknown', 'custom_query', None, False,
                                     'Missing required fields')), 400
    
    # Parse natural language and get appropriate SQL template
    try:
        sql_query, params = parse_natural_language_query(query_description, customer_id)
        
        # Execute query
        result, error = execute_query(sql_query, params, customer_id)
        
        log_audit('custom_query', customer_id, query_description, sql_query, result,
                 {'model': 'template_parser', 'version': '1.0'}, error)
        
        if error:
            return jsonify(build_response('Unknown', 'custom_query', None, False, error)), 500
        
        # Get customer name
        name_query = 'SELECT name FROM customers WHERE customer_id = ?'
        name_result, _ = execute_query(name_query, (customer_id,))
        customer_name = name_result[0]['name'] if name_result else 'Unknown'
        
        return jsonify(build_response(customer_name, 'custom_query',
                                     {'sql': sql_query, 'results': result,
                                      'parsed_from': query_description}, True))
        
    except Exception as e:
        log_audit('custom_query_failed', customer_id, query_description, '', None,
                 {'model': 'template_parser'}, str(e))
        return jsonify(build_response('Unknown', 'custom_query', None, False, str(e))), 500

@app.route('/api/audit_log', methods=['GET'])
def get_audit_log():
    """Retrieve audit log entries"""
    try:
        entries = []
        if os.path.exists(AUDIT_LOG_PATH):
            with open(AUDIT_LOG_PATH, 'r') as f:
                for line in f:
                    entries.append(json.loads(line))
        
        # Return last 50 entries
        return jsonify({
            'success': True,
            'audit_entries': entries[-50:],
            'total_entries': len(entries)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'bank': BANK_NAME,
        'bank_id': BANK_ID,
        'database': 'connected' if os.path.exists(DB_PATH) else 'not_found'
    })

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

# Made with Bob - VULNERABLE VERSION FOR SECURITY DEMO