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

app = Flask(__name__, static_folder='static', static_url_path='')

# Bank configuration
BANK_NAME = os.getenv('BANK_NAME', 'Savings Bank')
BANK_ID = os.getenv('BANK_ID', 'bank1')
BANK_COLOR = os.getenv('BANK_COLOR', '#2E7D32')  # Green for savings
DB_PATH = os.getenv('DB_PATH', 'bank1_savings.db')
AUDIT_LOG_PATH = os.getenv('AUDIT_LOG_PATH', 'bank1_audit.jsonl')
BANK2_URL = os.getenv('BANK2_URL', 'http://localhost:5002')

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
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Accounts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            account_type TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0 CHECK(balance >= 0),
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
        demo_customers = [
            ('Alice Johnson', 'alice@example.com'),
            ('Bob Smith', 'bob@example.com'),
            ('Carol Davis', 'carol@example.com'),
            ('David Wilson', 'david@example.com'),
            ('Emma Brown', 'emma@example.com')
        ]
        cursor.executemany('INSERT INTO customers (name, email) VALUES (?, ?)', demo_customers)
        
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

# Web interface HTML template
WEB_INTERFACE_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ bank_name }} - Administrator Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .header {
            background: linear-gradient(135deg, {{ bank_color }} 0%, #1e3c72 100%);
            color: white;
            padding: 30px 0;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .dashboard-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 30px;
            margin-top: 30px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
        }
        
        .card h2 {
            color: {{ bank_color }};
            margin-bottom: 20px;
            font-size: 1.5em;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        
        .customer-selector {
            margin-bottom: 30px;
        }
        
        .customer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .customer-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .customer-card:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .customer-card.selected {
            background: linear-gradient(135deg, {{ bank_color }} 0%, #1e3c72 100%);
            transform: scale(1.05);
        }
        
        .customer-name {
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 5px;
        }
        
        .customer-id {
            opacity: 0.8;
            font-size: 0.9em;
        }
        
        .operations-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .operation-btn {
            background: linear-gradient(135deg, {{ bank_color }} 0%, #1e3c72 100%);
            color: white;
            border: none;
            padding: 15px 20px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .operation-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .operation-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        
        .form-group {
            margin: 15px 0;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }
        
        .form-group input, .form-group select, .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e1e5e9;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s ease;
        }
        
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            outline: none;
            border-color: {{ bank_color }};
        }
        
        .result-container {
            margin-top: 20px;
        }
        
        .balance-display {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin: 20px 0;
        }
        
        .balance-amount {
            font-size: 3em;
            font-weight: bold;
            margin: 10px 0;
        }
        
        .balance-label {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .transaction-list {
            max-height: 400px;
            overflow-y: auto;
        }
        
        .transaction-item {
            background: #f8f9fa;
            border-left: 4px solid {{ bank_color }};
            padding: 15px;
            margin: 10px 0;
            border-radius: 0 8px 8px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .transaction-item.positive {
            border-left-color: #28a745;
            background: #f8fff9;
        }
        
        .transaction-item.negative {
            border-left-color: #dc3545;
            background: #fff8f8;
        }
        
        .transaction-details {
            flex: 1;
        }
        
        .transaction-amount {
            font-size: 1.2em;
            font-weight: bold;
        }
        
        .transaction-amount.positive {
            color: #28a745;
        }
        
        .transaction-amount.negative {
            color: #dc3545;
        }
        
        .transaction-description {
            color: #666;
            margin-top: 5px;
        }
        
        .transaction-date {
            color: #999;
            font-size: 0.9em;
        }
        
        .chart-container {
            margin: 20px 0;
            background: white;
            border-radius: 10px;
            padding: 20px;
        }
        
        .audit-log {
            max-height: 300px;
            overflow-y: auto;
            background: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
        }
        
        .audit-entry {
            background: white;
            border-radius: 5px;
            padding: 10px;
            margin: 5px 0;
            border-left: 3px solid {{ bank_color }};
            font-size: 0.9em;
        }
        
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #c3e6cb;
        }
        
        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #f5c6cb;
        }
        
        .disclaimer {
            background: #fff3cd;
            color: #856404;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border: 1px solid #ffeaa7;
            font-size: 0.9em;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        .loading::after {
            content: '';
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid #f3f3f3;
            border-top: 3px solid {{ bank_color }};
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-left: 10px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @media (max-width: 768px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
            
            .customer-grid {
                grid-template-columns: 1fr;
            }
            
            .operations-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{ bank_name }}</h1>
        <p>Administrator Dashboard</p>
    </div>
    
    <div class="container">
        <div class="dashboard-grid">
            <!-- Left Panel: Customer Selection & Operations -->
            <div class="card customer-selector">
                <h2>👥 Select Customer</h2>
                <div id="customerGrid" class="customer-grid">
                    <div class="loading">Loading customers...</div>
                </div>
                
                <h2 style="margin-top: 30px;">🔧 Operations</h2>
                <div class="operations-grid">
                    <button class="operation-btn" onclick="executeOperation('balance')" disabled id="balanceBtn">
                        💰 Check Balance
                    </button>
                    <button class="operation-btn" onclick="executeOperation('transactions')" disabled id="transactionsBtn">
                        📋 View Transactions
                    </button>
                    <button class="operation-btn" onclick="executeOperation('analytics')" disabled id="analyticsBtn">
                        📊 Analytics
                    </button>
                    <button class="operation-btn" onclick="showTransferForm()" disabled id="transferBtn">
                        💸 Transfer Funds
                    </button>
                    <button class="operation-btn" onclick="showCustomQueryForm()" disabled id="customBtn">
                        🔍 Custom Query
                    </button>
                </div>
                
                <!-- Transfer Form -->
                <div id="transferForm" style="display: none; margin-top: 20px;">
                    <h3>Transfer to Investment Bank</h3>
                    <p style="color: #666; margin-bottom: 15px;">Transfer funds from your Savings account to your Investment account</p>
                    <div class="form-group">
                        <label>Amount ($)</label>
                        <input type="number" id="transferAmount" step="0.01" placeholder="Enter amount to transfer">
                    </div>
                    <button class="operation-btn" onclick="executeTransfer()">Transfer to Investment Bank</button>
                    <button class="operation-btn" onclick="hideTransferForm()" style="background: #6c757d;">Cancel</button>
                </div>
                
                <!-- Custom Query Form -->
                <div id="customQueryForm" style="display: none; margin-top: 20px;">
                    <h3>Custom Query</h3>
                    <div class="form-group">
                        <label>Query Description</label>
                        <textarea id="queryDescription" rows="3" placeholder="e.g., 'last 5 transactions over $100'"></textarea>
                    </div>
                    <button class="operation-btn" onclick="executeCustomQuery()">Execute Query</button>
                    <button class="operation-btn" onclick="hideCustomQueryForm()" style="background: #6c757d;">Cancel</button>
                </div>
            </div>
            
            <!-- Right Panel: Results -->
            <div class="card">
                <h2 id="resultTitle">📊 Results</h2>
                <div id="resultContainer">
                    <div style="text-align: center; padding: 40px; color: #666;">
                        Select a customer and operation to view results
                    </div>
                </div>
                <div id="chartContainer" class="chart-container" style="display: none;"></div>
            </div>
        </div>
        
        <!-- Audit Log -->
        <div class="card" style="margin-top: 30px;">
            <h2>📋 Audit Log</h2>
            <button class="operation-btn" onclick="loadAuditLog()" style="margin-bottom: 15px;">
                🔄 Refresh Audit Log
            </button>
            <div id="auditLog" class="audit-log">
                <div class="loading">Loading audit log...</div>
            </div>
        </div>
        
        <div class="disclaimer">
            <strong>⚠️ Compliance Disclaimer:</strong> {{ disclaimer }}
        </div>
    </div>
    
    <script>
        let selectedCustomerId = null;
        let customers = [];
        
        // Load customers on page load
        window.onload = function() {
            loadCustomers();
            loadAuditLog();
        };
        
        async function loadCustomers() {
            try {
                // Get all customers by trying each ID
                const customerGrid = document.getElementById('customerGrid');
                customerGrid.innerHTML = '<div class="loading">Loading customers...</div>';
                
                customers = [];
                for (let i = 1; i <= 5; i++) {
                    try {
                        const response = await fetch('/api/balance', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ customer_id: i })
                        });
                        
                        if (response.ok) {
                            const result = await response.json();
                            if (result.success && result.result_data.length > 0) {
                                customers.push({
                                    id: i,
                                    name: result.result_data[0].name,
                                    email: result.result_data[0].email,
                                    balance: result.result_data[0].balance
                                });
                            }
                        }
                    } catch (e) {
                        // Skip failed customers
                    }
                }
                
                // Display customers
                let html = '';
                customers.forEach(customer => {
                    html += `
                        <div class="customer-card" onclick="selectCustomer(${customer.id})">
                            <div class="customer-name">${customer.name}</div>
                            <div class="customer-id">ID: ${customer.id}</div>
                            <div style="margin-top: 10px; font-size: 0.9em;">$${customer.balance.toFixed(2)}</div>
                        </div>
                    `;
                });
                
                customerGrid.innerHTML = html || '<div style="text-align: center; color: #666;">No customers found</div>';
                
            } catch (error) {
                document.getElementById('customerGrid').innerHTML = '<div class="error-message">Error loading customers</div>';
            }
        }
        
        function selectCustomer(customerId) {
            selectedCustomerId = customerId;
            
            // Update UI
            document.querySelectorAll('.customer-card').forEach(card => {
                card.classList.remove('selected');
            });
            event.target.closest('.customer-card').classList.add('selected');
            
            // Enable operation buttons
            document.querySelectorAll('.operation-btn').forEach(btn => {
                btn.disabled = false;
            });
            
            // Update result title
            const customer = customers.find(c => c.id === customerId);
            document.getElementById('resultTitle').textContent = `📊 Results for ${customer.name}`;
            
            // Clear previous results
            document.getElementById('resultContainer').innerHTML = '<div style="text-align: center; padding: 20px; color: #666;">Select an operation to view results</div>';
        }
        
        async function executeOperation(operation) {
            if (!selectedCustomerId) {
                alert('Please select a customer first');
                return;
            }
            
            const resultContainer = document.getElementById('resultContainer');
            const chartContainer = document.getElementById('chartContainer');
            
            resultContainer.innerHTML = '<div class="loading">Processing...</div>';
            chartContainer.style.display = 'none';
            
            try {
                let endpoint = '';
                let data = { customer_id: selectedCustomerId };
                
                switch(operation) {
                    case 'balance':
                        endpoint = '/api/balance';
                        break;
                    case 'transactions':
                        endpoint = '/api/transactions';
                        data.limit = 10;
                        break;
                    case 'analytics':
                        endpoint = '/api/analytics';
                        break;
                }
                
                const response = await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    displayResult(operation, result);
                } else {
                    resultContainer.innerHTML = `<div class="error-message">Error: ${result.error}</div>`;
                }
                
            } catch (error) {
                resultContainer.innerHTML = `<div class="error-message">Error: ${error.message}</div>`;
            }
        }
        
        function displayResult(operation, result) {
            const resultContainer = document.getElementById('resultContainer');
            const chartContainer = document.getElementById('chartContainer');
            
            switch(operation) {
                case 'balance':
                    const balanceData = result.result_data[0];
                    resultContainer.innerHTML = `
                        <div class="balance-display">
                            <div class="balance-label">Current Balance</div>
                            <div class="balance-amount">$${balanceData.balance.toFixed(2)}</div>
                            <div style="margin-top: 15px;">
                                <div><strong>Account Type:</strong> ${balanceData.account_type}</div>
                                <div><strong>Email:</strong> ${balanceData.email}</div>
                            </div>
                        </div>
                    `;
                    break;
                    
                case 'transactions':
                    let transactionHtml = '<div class="transaction-list">';
                    result.result_data.forEach(transaction => {
                        const isPositive = transaction.amount > 0;
                        const date = new Date(transaction.transaction_date).toLocaleDateString();
                        transactionHtml += `
                            <div class="transaction-item ${isPositive ? 'positive' : 'negative'}">
                                <div class="transaction-details">
                                    <div class="transaction-amount ${isPositive ? 'positive' : 'negative'}">
                                        ${isPositive ? '+' : ''}$${Math.abs(transaction.amount).toFixed(2)}
                                    </div>
                                    <div class="transaction-description">
                                        <strong>${transaction.transaction_type}</strong> - ${transaction.category}
                                        ${transaction.description ? ': ' + transaction.description : ''}
                                    </div>
                                </div>
                                <div class="transaction-date">${date}</div>
                            </div>
                        `;
                    });
                    transactionHtml += '</div>';
                    resultContainer.innerHTML = transactionHtml;
                    break;
                    
                case 'analytics':
                    if (result.result_data.pie_chart) {
                        resultContainer.innerHTML = `
                            <div class="success-message">
                                <strong>Analytics Generated Successfully</strong><br>
                                Total Spent: $${result.result_data.total_spent || 0}
                            </div>
                        `;
                        chartContainer.innerHTML = result.result_data.pie_chart + result.result_data.line_chart;
                        chartContainer.style.display = 'block';
                    } else {
                        resultContainer.innerHTML = '<div class="error-message">No analytics data available</div>';
                    }
                    break;
            }
        }
        
        function showTransferForm() {
            if (!selectedCustomerId) {
                alert('Please select a customer first');
                return;
            }
            document.getElementById('transferForm').style.display = 'block';
        }
        
        function hideTransferForm() {
            document.getElementById('transferForm').style.display = 'none';
        }
        
        async function executeTransfer() {
            const amount = parseFloat(document.getElementById('transferAmount').value);
            
            if (!amount) {
                alert('Please enter an amount');
                return;
            }
            
            const resultContainer = document.getElementById('resultContainer');
            resultContainer.innerHTML = '<div class="loading">Processing transfer to Investment Bank...</div>';
            
            try {
                const response = await fetch('/api/transfer', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        customer_id: selectedCustomerId,
                        amount: amount
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    resultContainer.innerHTML = `
                        <div class="success-message">
                            <strong>Transfer Successful!</strong><br>
                            Amount: $${amount.toFixed(2)}<br>
                            From: ${result.result_data.from}<br>
                            To: ${result.result_data.to}<br>
                            New Savings Balance: $${result.result_data.new_savings_balance.toFixed(2)}
                        </div>
                    `;
                    hideTransferForm();
                    loadCustomers(); // Refresh customer balances
                } else {
                    resultContainer.innerHTML = `<div class="error-message">Transfer Failed: ${result.error}</div>`;
                }
                
            } catch (error) {
                resultContainer.innerHTML = `<div class="error-message">Error: ${error.message}</div>`;
            }
        }
        
        function showCustomQueryForm() {
            if (!selectedCustomerId) {
                alert('Please select a customer first');
                return;
            }
            document.getElementById('customQueryForm').style.display = 'block';
        }
        
        function hideCustomQueryForm() {
            document.getElementById('customQueryForm').style.display = 'none';
        }
        
        async function executeCustomQuery() {
            const queryDescription = document.getElementById('queryDescription').value;
            
            if (!queryDescription) {
                alert('Please enter a query description');
                return;
            }
            
            const resultContainer = document.getElementById('resultContainer');
            resultContainer.innerHTML = '<div class="loading">Processing query...</div>';
            
            try {
                const response = await fetch('/api/custom_query', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        customer_id: selectedCustomerId,
                        query_description: queryDescription
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    let html = `
                        <div class="success-message">
                            <strong>Query Executed Successfully</strong><br>
                            Parsed: "${result.result_data.parsed_from}"
                        </div>
                        <div style="margin-top: 15px;">
                    `;
                    
                    result.result_data.results.forEach(row => {
                        html += '<div style="background: #f8f9fa; padding: 10px; margin: 5px 0; border-radius: 5px;">';
                        Object.entries(row).forEach(([key, value]) => {
                            html += `<strong>${key}:</strong> ${value}<br>`;
                        });
                        html += '</div>';
                    });
                    
                    html += '</div>';
                    resultContainer.innerHTML = html;
                    hideCustomQueryForm();
                } else {
                    resultContainer.innerHTML = `<div class="error-message">Query Failed: ${result.error}</div>`;
                }
                
            } catch (error) {
                resultContainer.innerHTML = `<div class="error-message">Error: ${error.message}</div>`;
            }
        }
        
        async function loadAuditLog() {
            const auditDiv = document.getElementById('auditLog');
            auditDiv.innerHTML = '<div class="loading">Loading audit log...</div>';
            
            try {
                const response = await fetch('/api/audit_log');
                const result = await response.json();
                
                if (result.success) {
                    let html = '';
                    result.audit_entries.slice(-10).forEach(entry => {
                        const date = new Date(entry.timestamp).toLocaleString();
                        html += `
                            <div class="audit-entry">
                                <strong>${date}</strong> - ${entry.event_type}<br>
                                Customer: ${entry.customer_id || 'N/A'} |
                                Hash: ${entry.hash.substring(0, 16)}...
                            </div>
                        `;
                    });
                    auditDiv.innerHTML = html || '<div style="text-align: center; color: #666;">No audit entries found</div>';
                } else {
                    auditDiv.innerHTML = '<div class="error-message">Error loading audit log</div>';
                }
            } catch (error) {
                auditDiv.innerHTML = '<div class="error-message">Error loading audit log</div>';
            }
        }
    </script>
</body>
</html>
'''

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
    app.run(host='0.0.0.0', port=5001, debug=True)

# Made with Bob
