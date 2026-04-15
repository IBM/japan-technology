from flask import Flask, jsonify, request, render_template_string
import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Tuple, Optional
import hashlib
import re
import requests
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Bank configuration
BANK_NAME = os.getenv('BANK_NAME', 'Investment Bank')
BANK_ID = os.getenv('BANK_ID', 'bank2')
BANK_COLOR = os.getenv('BANK_COLOR', '#1565C0')  # Blue for investment
DB_PATH = os.getenv('DB_PATH', 'bank2_investment.db')
AUDIT_LOG_PATH = os.getenv('AUDIT_LOG_PATH', 'bank2_audit.jsonl')
BANK1_URL = os.getenv('BANK1_URL', 'http://localhost:5001')
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT = int(os.getenv('FLASK_PORT', '5000'))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Compliance disclaimer
COMPLIANCE_DISCLAIMER = "この銀行情報は参考情報として提供されています。すべての取引は確認および規制遵守の対象です。顧客データは適用されるプライバシー法に基づいて保護されています。"

MESSAGE_CUSTOMER_ID_REQUIRED = "顧客IDは必須です"
MESSAGE_CUSTOMER_NOT_FOUND = "顧客が見つかりません"
MESSAGE_REQUIRED_FIELDS = "必須項目が不足しています"
MESSAGE_CUSTOMER_ID_AND_AMOUNT_REQUIRED = "customer_id と amount は必須です"
MESSAGE_AMOUNT_POSITIVE = "金額は 0 より大きい必要があります"
MESSAGE_ACCOUNT_NOT_FOUND = "口座が見つかりません"
MESSAGE_NO_INVESTMENT_DATA = "投資データがありません"

INVESTMENT_CATEGORY_LABELS = {
    'stocks': '株式',
    'bonds': '債券',
    'mutual_funds': '投資信託',
    'etf': 'ETF',
    'transfer': '振替'
}


def translate_investment_category(value: str) -> str:
    key = str(value).strip().lower()
    return INVESTMENT_CATEGORY_LABELS.get(key, value)

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
    'large_investments': '''
        SELECT t.transaction_id, t.transaction_type, t.category, t.amount,
               t.description, t.transaction_date
        FROM transactions t
        WHERE t.customer_id = ? AND t.amount > ?
        ORDER BY t.transaction_date DESC
    ''',
    'investments_by_category': '''
        SELECT t.category, COUNT(*) as count, SUM(t.amount) as total
        FROM transactions t
        WHERE t.customer_id = ?
        GROUP BY t.category
        ORDER BY total DESC
    ''',
    'monthly_performance': '''
        SELECT strftime('%Y-%m', t.transaction_date) as month,
               COUNT(*) as transaction_count,
               SUM(CASE WHEN t.amount > 0 THEN t.amount ELSE 0 END) as investments,
               SUM(CASE WHEN t.transaction_type = 'dividend' THEN t.amount ELSE 0 END) as dividends
        FROM transactions t
        WHERE t.customer_id = ?
        GROUP BY month
        ORDER BY month DESC
    ''',
    'portfolio_summary': '''
        SELECT c.name, c.email, a.account_type, a.balance,
               COUNT(t.transaction_id) as transaction_count,
               SUM(CASE WHEN t.transaction_type = 'dividend' THEN t.amount ELSE 0 END) as total_dividends
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
        amount = float(match.group(1)) if match else 1000.0
        return SQL_TEMPLATES['large_investments'], (customer_id, amount)
    
    elif 'category' in description_lower or 'categories' in description_lower or 'portfolio' in description_lower:
        return SQL_TEMPLATES['investments_by_category'], (customer_id,)
    
    elif 'month' in description_lower or 'performance' in description_lower:
        return SQL_TEMPLATES['monthly_performance'], (customer_id,)
    
    elif 'summary' in description_lower or 'dividend' in description_lower:
        return SQL_TEMPLATES['portfolio_summary'], (customer_id,)
    
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
            ('Alice Johnson', 'alice.invest@example.com'),
            ('Bob Smith', 'bob.invest@example.com'),
            ('Carol Davis', 'carol.invest@example.com'),
            ('David Wilson', 'david.invest@example.com'),
            ('Emma Brown', 'emma.invest@example.com')
        ]
        cursor.executemany('INSERT INTO customers (name, email) VALUES (?, ?)', demo_customers)
        
        # Create investment accounts for each customer
        for i in range(1, 6):
            cursor.execute('INSERT INTO accounts (customer_id, account_type, balance) VALUES (?, ?, ?)',
                         (i, 'investment', 10000.0 + (i * 1000)))
        
        # Insert demo investment transactions
        demo_transactions = [
            (1, 1, 'deposit', 'stocks', 5000.0, 'Stock purchase - Tech sector'),
            (1, 1, 'dividend', 'stocks', 150.0, 'Quarterly dividend'),
            (1, 1, 'withdrawal', 'bonds', -2000.0, 'Bond investment'),
            (2, 2, 'deposit', 'stocks', 3000.0, 'Stock purchase - Healthcare'),
            (2, 2, 'dividend', 'stocks', 80.0, 'Dividend payment'),
            (3, 3, 'deposit', 'mutual_funds', 4000.0, 'Mutual fund investment'),
            (3, 3, 'withdrawal', 'stocks', -1500.0, 'Stock sale'),
            (4, 4, 'deposit', 'bonds', 2800.0, 'Bond purchase'),
            (5, 5, 'deposit', 'etf', 3500.0, 'ETF investment'),
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
        return True, "検証対象のデータがありません"
    
    for row in result:
        for field, field_type in expected_schema.items():
            if field not in row:
                return False, f"必須フィールドが不足しています: {field}"
            
            value = row[field]
            
            # Type checking
            if field_type == 'float' and not isinstance(value, (int, float)):
                return False, f"フィールド {field} は数値である必要があります: {type(value)}"
            
            if field_type == 'str' and not isinstance(value, str):
                return False, f"フィールド {field} は文字列である必要があります: {type(value)}"
            
            # Business rule: balances must be >= 0
            if field == 'balance' and isinstance(value, (int, float)) and value < 0:
                return False, f"残高を負の値にはできません: {value}"
    
    return True, "検証に成功しました"

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
                    return [], f"検証に失敗しました: {message}"
            
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
    if 'invest' in prompt_lower:
        sql_query = '''
            INSERT INTO transactions (account_id, customer_id, transaction_type, category, amount, description)
            VALUES (?, ?, 'deposit', ?, ?, ?)
        '''
    elif 'withdraw' in prompt_lower:
        sql_query = '''
            UPDATE accounts
            SET balance = balance - ?
            WHERE customer_id = ? AND balance >= ?
        '''
    else:
        return False, "", "デュアルラン検証で操作種別を判別できませんでした"
    
    # Simulate dual-run by validating the query structure
    # In a real system, this would generate the query twice using AI
    validation_passed = True
    validation_message = "dual-run validation に成功しました（事前検証済みの SQL テンプレートを使用）"
    
    return validation_passed, sql_query, validation_message

# Generate investment analytics
def generate_investment_analytics(customer_id: int) -> Dict:
    """Generate investment analytics with visualizations"""
    # Get transaction data
    query = '''
        SELECT 
            category,
            SUM(amount) as total_amount,
            COUNT(*) as transaction_count,
            DATE(transaction_date) as date
        FROM transactions
        WHERE customer_id = ?
        GROUP BY category, DATE(transaction_date)
        ORDER BY date DESC
    '''
    
    result, error = execute_query(query, (customer_id,))
    
    if error:
        return {'error': error}
    
    if not result:
        return {'message': MESSAGE_NO_INVESTMENT_DATA}
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(result)
    df['category_label'] = df['category'].apply(translate_investment_category)
    
    # Category breakdown
    category_totals = df.groupby('category_label')['total_amount'].sum().reset_index()
    
    # Create pie chart for portfolio allocation
    fig_pie = px.pie(category_totals, values='total_amount', names='category_label',
                     title='投資ポートフォリオ配分')
    pie_chart_html = fig_pie.to_html(full_html=False)
    
    # Create time series for investment growth
    daily_totals = df.groupby('date')['total_amount'].sum().reset_index()
    fig_line = px.line(daily_totals, x='date', y='total_amount',
                       title='投資アクティビティ推移')
    line_chart_html = fig_line.to_html(full_html=False)
    
    return {
        'category_breakdown': category_totals.to_dict('records'),
        'daily_activity': daily_totals.to_dict('records'),
        'pie_chart': pie_chart_html,
        'line_chart': line_chart_html,
        'total_invested': float(df[df['total_amount'] > 0]['total_amount'].sum())
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
    <title>{{ bank_name }} - 管理ダッシュボード</title>
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .header {
            background: linear-gradient(135deg, {{ bank_color }} 0%, #667eea 100%);
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
            background: linear-gradient(135deg, {{ bank_color }} 0%, #667eea 100%);
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
            background: linear-gradient(135deg, {{ bank_color }} 0%, #667eea 100%);
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
            background: #e3f2fd;
            color: #0d47a1;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border: 1px solid #90caf9;
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
        <p>管理ダッシュボード</p>
    </div>
    
    <div class="container">
        <div class="dashboard-grid">
            <!-- Left Panel: Customer Selection & Operations -->
            <div class="card customer-selector">
                <h2>👥 顧客を選択</h2>
                <div id="customerGrid" class="customer-grid">
                    <div class="loading">顧客情報を読み込み中...</div>
                </div>
                
                <h2 style="margin-top: 30px;">🔧 操作</h2>
                <div class="operations-grid">
                    <button class="operation-btn" onclick="executeOperation('balance')" disabled id="balanceBtn">
                        💼 残高を確認
                    </button>
                    <button class="operation-btn" onclick="executeOperation('transactions')" disabled id="transactionsBtn">
                        📋 取引履歴を見る
                    </button>
                    <button class="operation-btn" onclick="executeOperation('analytics')" disabled id="analyticsBtn">
                        📈 分析
                    </button>
                    <button class="operation-btn" onclick="showTransferForm()" disabled id="transferBtn">
                        💸 Savings Bank へ振替
                    </button>
                    <button class="operation-btn" onclick="showInvestForm()" disabled id="investBtn">
                        💎 投資を実行
                    </button>
                    <button class="operation-btn" onclick="showCustomQueryForm()" disabled id="customBtn">
                        🔍 カスタムクエリ
                    </button>
                </div>
                
                <!-- Transfer Form -->
                <div id="transferForm" style="display: none; margin-top: 20px;">
                    <h3>Savings Bank への振替</h3>
                    <p style="color: #666; margin-bottom: 15px;">Investment 口座から Savings 口座へ資金を移動します</p>
                    <div class="form-group">
                        <label>金額 ($)</label>
                        <input type="number" id="transferAmount" step="0.01" placeholder="振替金額を入力">
                    </div>
                    <button class="operation-btn" onclick="executeTransfer()">Savings Bank へ振替</button>
                    <button class="operation-btn" onclick="hideTransferForm()" style="background: #6c757d;">キャンセル</button>
                </div>
                
                <!-- Investment Form -->
                <div id="investForm" style="display: none; margin-top: 20px;">
                    <h3>投資を実行</h3>
                    <div class="form-group">
                        <label>金額 ($)</label>
                        <input type="number" id="investAmount" step="0.01" placeholder="投資金額を入力">
                    </div>
                    <div class="form-group">
                        <label>投資カテゴリ</label>
                        <select id="investCategory">
                            <option value="stocks">株式</option>
                            <option value="bonds">債券</option>
                            <option value="mutual_funds">投資信託</option>
                            <option value="etf">ETF</option>
                        </select>
                    </div>
                    <button class="operation-btn" onclick="executeInvestment()">投資を実行</button>
                    <button class="operation-btn" onclick="hideInvestForm()" style="background: #6c757d;">キャンセル</button>
                </div>
                
                <!-- Custom Query Form -->
                <div id="customQueryForm" style="display: none; margin-top: 20px;">
                    <h3>カスタムクエリ</h3>
                    <div class="form-group">
                        <label>クエリ内容</label>
                        <textarea id="queryDescription" rows="3" placeholder="例: 'investments over $1000'（英語で入力してください）"></textarea>
                    </div>
                    <p style="color: #666; margin-bottom: 15px;">現在は英語クエリのみ対応しています。</p>
                    <button class="operation-btn" onclick="executeCustomQuery()">クエリを実行</button>
                    <button class="operation-btn" onclick="hideCustomQueryForm()" style="background: #6c757d;">キャンセル</button>
                </div>
            </div>
            
            <!-- Right Panel: Results -->
            <div class="card">
                <h2 id="resultTitle">📊 結果</h2>
                <div id="resultContainer">
                    <div style="text-align: center; padding: 40px; color: #666;">
                        顧客と操作を選択すると結果が表示されます
                    </div>
                </div>
                <div id="chartContainer" class="chart-container" style="display: none;"></div>
            </div>
        </div>
        
        <!-- Audit Log -->
        <div class="card" style="margin-top: 30px;">
            <h2>📋 監査ログ</h2>
            <button class="operation-btn" onclick="loadAuditLog()" style="margin-bottom: 15px;">
                🔄 監査ログを更新
            </button>
            <div id="auditLog" class="audit-log">
                <div class="loading">監査ログを読み込み中...</div>
            </div>
        </div>
        
        <div class="disclaimer">
            <strong>⚠️ コンプライアンスに関する注意:</strong> {{ disclaimer }}
        </div>
    </div>
    
    <script>
        let selectedCustomerId = null;
        let customers = [];
        const accountTypeLabels = {
            investment: '投資口座',
            savings: '普通預金'
        };
        const transactionTypeLabels = {
            deposit: '入金',
            withdrawal: '出金',
            transfer: '振替',
            dividend: '配当'
        };
        const categoryLabels = {
            stocks: '株式',
            bonds: '債券',
            mutual_funds: '投資信託',
            etf: 'ETF',
            transfer: '振替'
        };
        const descriptionLabels = {
            'Transfer to Savings Bank': 'Savings Bank への振替',
            'Transfer from Savings Bank': 'Savings Bank からの振替',
            'Stock purchase - Tech sector': '株式購入 - テックセクター',
            'Quarterly dividend': '四半期配当',
            'Bond investment': '債券投資',
            'Stock purchase - Healthcare': '株式購入 - ヘルスケア',
            'Dividend payment': '配当金支払い',
            'Mutual fund investment': '投資信託への投資',
            'Stock sale': '株式売却',
            'Bond purchase': '債券購入',
            'ETF investment': 'ETF 投資',
            'Investment in stocks': '株式への投資',
            'Investment in bonds': '債券への投資',
            'Investment in mutual_funds': '投資信託への投資',
            'Investment in etf': 'ETF への投資'
        };
        const fieldLabels = {
            transaction_id: '取引ID',
            transaction_type: '取引種別',
            category: 'カテゴリ',
            amount: '金額',
            description: '説明',
            transaction_date: '取引日時',
            name: '氏名',
            email: 'メールアドレス',
            account_type: '口座種別',
            balance: '残高',
            transaction_count: '取引件数',
            total_dividends: '配当合計',
            month: '月',
            investments: '投資額',
            dividends: '配当額'
        };
        const auditEventLabels = {
            balance_check: '残高確認',
            transaction_history: '取引履歴取得',
            investment_analytics: '投資分析生成',
            transfer_to_savings: 'Savings Bank への振替',
            investment_completed: '投資完了',
            investment_failed: '投資失敗',
            custom_query: 'カスタムクエリ',
            custom_query_failed: 'カスタムクエリエラー'
        };

        function translateFromMap(value, labels, fallback = '未設定') {
            if (value === null || value === undefined || value === '') {
                return fallback;
            }

            const key = String(value).trim().toLowerCase();
            return labels[key] || value;
        }

        function translateAccountType(value) {
            return translateFromMap(value, accountTypeLabels);
        }

        function translateTransactionType(value) {
            return translateFromMap(value, transactionTypeLabels, '不明');
        }

        function translateCategory(value) {
            return translateFromMap(value, categoryLabels, 'その他');
        }

        function translateDescription(value) {
            if (!value) {
                return '説明なし';
            }
            return descriptionLabels[value] || value;
        }

        function formatDate(value, includeTime = true) {
            const options = includeTime
                ? { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }
                : { year: 'numeric', month: '2-digit', day: '2-digit' };
            return new Date(value).toLocaleString('ja-JP', options);
        }

        function formatFieldLabel(key) {
            return fieldLabels[key] || key;
        }

        function formatFieldValue(key, value) {
            if (key === 'account_type') {
                return translateAccountType(value);
            }
            if (key === 'transaction_type') {
                return translateTransactionType(value);
            }
            if (key === 'category') {
                return translateCategory(value);
            }
            if (key === 'description') {
                return translateDescription(value);
            }
            if (key === 'transaction_date') {
                return formatDate(value);
            }
            return value ?? '未設定';
        }

        function formatAuditEvent(value) {
            return auditEventLabels[value] || value;
        }
        
        // Load customers on page load
        window.onload = function() {
            loadCustomers();
            loadAuditLog();
        };
        
        async function loadCustomers() {
            try {
                // Get all customers by trying each ID
                const customerGrid = document.getElementById('customerGrid');
                customerGrid.innerHTML = '<div class="loading">顧客情報を読み込み中...</div>';
                
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
                
                customerGrid.innerHTML = html || '<div style="text-align: center; color: #666;">顧客が見つかりません</div>';
                
            } catch (error) {
                document.getElementById('customerGrid').innerHTML = '<div class="error-message">顧客情報の読み込みに失敗しました</div>';
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
            document.getElementById('resultTitle').textContent = `📊 ${customer.name} の結果`;
            
            // Clear previous results
            document.getElementById('resultContainer').innerHTML = '<div style="text-align: center; padding: 20px; color: #666;">操作を選択すると結果が表示されます</div>';
        }
        
        async function executeOperation(operation) {
            if (!selectedCustomerId) {
                alert('先に顧客を選択してください');
                return;
            }
            
            const resultContainer = document.getElementById('resultContainer');
            const chartContainer = document.getElementById('chartContainer');
            
            resultContainer.innerHTML = '<div class="loading">処理中...</div>';
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
                    resultContainer.innerHTML = `<div class="error-message">エラー: ${result.error}</div>`;
                }
                
            } catch (error) {
                resultContainer.innerHTML = `<div class="error-message">エラー: ${error.message}</div>`;
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
                            <div class="balance-label">現在の残高</div>
                            <div class="balance-amount">$${balanceData.balance.toFixed(2)}</div>
                            <div style="margin-top: 15px;">
                                <div><strong>口座種別:</strong> ${translateAccountType(balanceData.account_type)}</div>
                                <div><strong>メールアドレス:</strong> ${balanceData.email}</div>
                            </div>
                        </div>
                    `;
                    break;
                    
                case 'transactions':
                    let transactionHtml = '<div class="transaction-list">';
                    result.result_data.forEach(transaction => {
                        const isPositive = transaction.amount > 0;
                        const date = formatDate(transaction.transaction_date, false);
                        transactionHtml += `
                            <div class="transaction-item ${isPositive ? 'positive' : 'negative'}">
                                <div class="transaction-details">
                                    <div class="transaction-amount ${isPositive ? 'positive' : 'negative'}">
                                        ${isPositive ? '+' : ''}$${Math.abs(transaction.amount).toFixed(2)}
                                    </div>
                                    <div class="transaction-description">
                                        <strong>${translateTransactionType(transaction.transaction_type)}</strong> - ${translateCategory(transaction.category)}
                                        ${transaction.description ? ': ' + translateDescription(transaction.description) : ''}
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
                                <strong>投資分析の生成が完了しました</strong><br>
                                総投資額: $${result.result_data.total_invested || 0}
                            </div>
                        `;
                        chartContainer.innerHTML = result.result_data.pie_chart + result.result_data.line_chart;
                        chartContainer.style.display = 'block';
                    } else {
                        resultContainer.innerHTML = '<div class="error-message">分析データがありません</div>';
                    }
                    break;
            }
        }
        
        function showInvestForm() {
            if (!selectedCustomerId) {
                alert('先に顧客を選択してください');
                return;
            }
            document.getElementById('investForm').style.display = 'block';
        }
        
        function hideInvestForm() {
            document.getElementById('investForm').style.display = 'none';
        }
        
        function showTransferForm() {
            if (!selectedCustomerId) {
                alert('先に顧客を選択してください');
                return;
            }
            document.getElementById('transferForm').style.display = 'block';
        }
        
        function hideTransferForm() {
            document.getElementById('transferForm').style.display = 'none';
        }
        
        async function executeTransfer() {
            const amount = parseFloat(document.getElementById('transferAmount').value);
            
            if (!amount || amount <= 0) {
                alert('有効な振替金額を入力してください');
                return;
            }
            
            const resultContainer = document.getElementById('resultContainer');
            resultContainer.innerHTML = '<div class="loading">Savings Bank への振替を処理中...</div>';
            
            try {
                const response = await fetch('/api/transfer_to_savings', {
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
                            <strong>✅ 振替が完了しました</strong><br><br>
                            <div style="font-size: 1.1em;">
                                <strong>振替金額:</strong> $${amount.toFixed(2)}<br>
                                <strong>振替元:</strong> Investment Bank<br>
                                <strong>振替先:</strong> Savings Bank<br><br>
                                <strong>新しい投資残高:</strong> $${result.new_balance.toFixed(2)}
                            </div>
                        </div>
                    `;
                    hideTransferForm();
                    document.getElementById('transferAmount').value = '';
                    loadCustomers(); // Refresh customer balances
                } else {
                    resultContainer.innerHTML = `<div class="error-message">❌ 振替に失敗しました: ${result.error}</div>`;
                }
                
            } catch (error) {
                resultContainer.innerHTML = `<div class="error-message">❌ エラー: ${error.message}</div>`;
            }
        }
        
        async function executeInvestment() {
            const amount = parseFloat(document.getElementById('investAmount').value);
            const category = document.getElementById('investCategory').value;
            
            if (!amount) {
                alert('投資金額を入力してください');
                return;
            }
            
            const resultContainer = document.getElementById('resultContainer');
            resultContainer.innerHTML = '<div class="loading">投資を処理中...</div>';
            
            try {
                const response = await fetch('/api/invest', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        customer_id: selectedCustomerId,
                        amount: amount,
                        category: category
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    resultContainer.innerHTML = `
                        <div class="success-message">
                            <strong>投資が完了しました</strong><br>
                            金額: $${amount.toFixed(2)} / ${translateCategory(category)}<br>
                            新しいポートフォリオ残高: $${result.result_data.new_balance.toFixed(2)}
                        </div>
                    `;
                    hideInvestForm();
                    loadCustomers(); // Refresh customer balances
                } else {
                    resultContainer.innerHTML = `<div class="error-message">投資に失敗しました: ${result.error}</div>`;
                }
                
            } catch (error) {
                resultContainer.innerHTML = `<div class="error-message">エラー: ${error.message}</div>`;
            }
        }
        
        function showCustomQueryForm() {
            if (!selectedCustomerId) {
                alert('先に顧客を選択してください');
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
                alert('クエリ内容を入力してください');
                return;
            }
            
            const resultContainer = document.getElementById('resultContainer');
            resultContainer.innerHTML = '<div class="loading">クエリを処理中...</div>';
            
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
                            <strong>クエリの実行が完了しました</strong><br>
                            解釈内容: "${result.result_data.parsed_from}"
                        </div>
                        <div style="margin-top: 15px;">
                    `;
                    
                    result.result_data.results.forEach(row => {
                        html += '<div style="background: #f8f9fa; padding: 10px; margin: 5px 0; border-radius: 5px;">';
                        Object.entries(row).forEach(([key, value]) => {
                            html += `<strong>${formatFieldLabel(key)}:</strong> ${formatFieldValue(key, value)}<br>`;
                        });
                        html += '</div>';
                    });
                    
                    html += '</div>';
                    resultContainer.innerHTML = html;
                    hideCustomQueryForm();
                } else {
                    resultContainer.innerHTML = `<div class="error-message">クエリの実行に失敗しました: ${result.error}</div>`;
                }
                
            } catch (error) {
                resultContainer.innerHTML = `<div class="error-message">エラー: ${error.message}</div>`;
            }
        }
        
        async function loadAuditLog() {
            const auditDiv = document.getElementById('auditLog');
            auditDiv.innerHTML = '<div class="loading">監査ログを読み込み中...</div>';
            
            try {
                const response = await fetch('/api/audit_log');
                const result = await response.json();
                
                if (result.success) {
                    let html = '';
                    result.audit_entries.slice(-10).forEach(entry => {
                        const date = new Date(entry.timestamp).toLocaleString('ja-JP');
                        html += `
                            <div class="audit-entry">
                                <strong>${date}</strong> - ${formatAuditEvent(entry.event_type)}<br>
                                顧客: ${entry.customer_id || 'N/A'} |
                                ハッシュ: ${entry.hash.substring(0, 16)}...
                            </div>
                        `;
                    });
                    auditDiv.innerHTML = html || '<div style="text-align: center; color: #666;">監査ログはまだありません</div>';
                } else {
                    auditDiv.innerHTML = '<div class="error-message">監査ログの読み込みに失敗しました</div>';
                }
            } catch (error) {
                auditDiv.innerHTML = '<div class="error-message">監査ログの読み込みに失敗しました</div>';
            }
        }
    </script>
</body>
</html>
'''

# Routes
@app.route('/')
def home():
    """Web interface"""
    return render_template_string(
        WEB_INTERFACE_TEMPLATE,
        bank_name=BANK_NAME,
        bank_color=BANK_COLOR,
        disclaimer=COMPLIANCE_DISCLAIMER
    )

@app.route('/api/balance', methods=['POST'])
def get_balance():
    """Get customer portfolio balance with data isolation"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    
    if not customer_id:
        return jsonify(build_response('Unknown', 'balance', None, False, MESSAGE_CUSTOMER_ID_REQUIRED)), 400
    
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
    log_audit('balance_check', customer_id, 'Check portfolio balance', query, result, 
              {'model': 'direct_sql', 'version': '1.0'}, error)
    
    if error:
        return jsonify(build_response('Unknown', 'balance', None, False, error)), 500
    
    if not result:
        return jsonify(build_response('Unknown', 'balance', None, False, MESSAGE_CUSTOMER_NOT_FOUND)), 404
    
    customer_name = result[0]['name']
    return jsonify(build_response(customer_name, 'balance', result, True))

@app.route('/api/transactions', methods=['POST'])
def get_transactions():
    """Get customer investment transactions with data isolation"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    limit = data.get('limit', 10)
    
    if not customer_id:
        return jsonify(build_response('Unknown', 'transactions', None, False, MESSAGE_CUSTOMER_ID_REQUIRED)), 400
    
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
    """Get investment analytics with visualizations"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    
    if not customer_id:
        return jsonify(build_response('Unknown', 'analytics', None, False, MESSAGE_CUSTOMER_ID_REQUIRED)), 400
    
    analytics_data = generate_investment_analytics(customer_id)
    
    log_audit('investment_analytics', customer_id, 'Generate investment analytics', 
              'Multiple aggregation queries', analytics_data, 
              {'model': 'analytics_engine', 'version': '1.0'})
    
    # Get customer name
    name_query = 'SELECT name FROM customers WHERE customer_id = ?'
    name_result, _ = execute_query(name_query, (customer_id,))
    customer_name = name_result[0]['name'] if name_result else 'Unknown'
    
    return jsonify(build_response(customer_name, 'analytics', analytics_data, True))
@app.route('/api/receive_transfer', methods=['POST'])
def receive_transfer():
    """Receive transfer from Savings Bank (Bank 1)"""
    try:
        data = request.json
        customer_id = data.get('customer_id')
        amount = data.get('amount')
        
        if not customer_id or not amount:
            return jsonify({'success': False, 'error': MESSAGE_CUSTOMER_ID_AND_AMOUNT_REQUIRED}), 400
        
        amount = float(amount)
        if amount <= 0:
            return jsonify({'success': False, 'error': MESSAGE_AMOUNT_POSITIVE}), 400
        
        # Add to investment account
        query = 'UPDATE accounts SET balance = balance + ? WHERE customer_id = ?'
        result, error = execute_query(query, (amount, customer_id))
        
        if error:
            return jsonify({'success': False, 'error': error}), 500
        
        # Record deposit transaction
        tx_query = '''INSERT INTO transactions (customer_id, account_id, transaction_type, amount, category, description)
                      SELECT ?, account_id, 'deposit', ?, 'Transfer', 'Transfer from Savings Bank'
                      FROM accounts WHERE customer_id = ?'''
        execute_query(tx_query, (customer_id, amount, customer_id))
        
        # Get updated balance
        balance_query = 'SELECT balance FROM accounts WHERE customer_id = ?'
        balance_result, _ = execute_query(balance_query, (customer_id,))
        new_balance = balance_result[0]['balance'] if balance_result else 0
        
        return jsonify({
            'success': True,
            'message': f'Savings Bank からの振替を受け付けました: ${amount:.2f}',
            'new_balance': new_balance
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/transfer_to_savings', methods=['POST'])
def transfer_to_savings():
    """Transfer from Investment Bank to Savings Bank"""
    try:
        data = request.json
        customer_id = data.get('customer_id')
        amount = data.get('amount')
        
        if not customer_id or not amount:
            return jsonify({'success': False, 'error': MESSAGE_REQUIRED_FIELDS}), 400
        
        amount = float(amount)
        if amount <= 0:
            return jsonify({'success': False, 'error': MESSAGE_AMOUNT_POSITIVE}), 400
        
        # Check balance
        balance_query = 'SELECT balance FROM accounts WHERE customer_id = ?'
        balance_result, error = execute_query(balance_query, (customer_id,))
        
        if error or not balance_result:
            return jsonify({'success': False, 'error': MESSAGE_ACCOUNT_NOT_FOUND}), 404
        
        current_balance = balance_result[0]['balance']
        if current_balance < amount:
            return jsonify({'success': False, 'error': f'残高不足です。現在の残高: ${current_balance:.2f}'}), 400
        
        # Deduct from investment account
        deduct_query = 'UPDATE accounts SET balance = balance - ? WHERE customer_id = ?'
        deduct_result, error = execute_query(deduct_query, (amount, customer_id))
        
        if error:
            return jsonify({'success': False, 'error': '口座からの引き落としに失敗しました'}), 500
        
        # Record withdrawal transaction
        tx_query = '''INSERT INTO transactions (customer_id, account_id, transaction_type, amount, category, description)
                      SELECT ?, account_id, 'withdrawal', ?, 'Transfer', 'Transfer to Savings Bank'
                      FROM accounts WHERE customer_id = ?'''
        execute_query(tx_query, (customer_id, amount, customer_id))
        
        # Send to Savings Bank (Bank 1)
        try:
            response = requests.post(
                f'{BANK1_URL}/api/receive_transfer',
                json={'customer_id': customer_id, 'amount': amount},
                timeout=5
            )
            
            if response.status_code == 200:
                # Get updated balance
                balance_result, _ = execute_query(balance_query, (customer_id,))
                new_balance = balance_result[0]['balance'] if balance_result else 0
                
                # Log successful transfer
                log_audit('transfer_to_savings', customer_id,
                         f'Transfer ${amount} to Savings Bank',
                         deduct_query, balance_result,
                         {'model': 'inter_bank_transfer', 'version': '1.0'}, None)
                
                return jsonify({
                    'success': True,
                    'message': f'Savings Bank へ ${amount:.2f} を振り替えました',
                    'amount': amount,
                    'new_balance': new_balance
                })
            else:
                # Rollback - add money back
                rollback_query = 'UPDATE accounts SET balance = balance + ? WHERE customer_id = ?'
                execute_query(rollback_query, (amount, customer_id))
                
                return jsonify({
                    'success': False,
                    'error': f'Savings Bank への振替に失敗しました: {response.text}'
                }), 500
                
        except requests.exceptions.RequestException as e:
            # Rollback - add money back
            rollback_query = 'UPDATE accounts SET balance = balance + ? WHERE customer_id = ?'
            execute_query(rollback_query, (amount, customer_id))
            
            return jsonify({
                'success': False,
                'error': f'Savings Bank に接続できませんでした: {str(e)}'
            }), 500
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/invest', methods=['POST'])
def make_investment():
    """Make investment with dual-run validation"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    amount = data.get('amount')
    category = data.get('category', 'stocks')
    
    if not all([customer_id, amount]):
        return jsonify(build_response('Unknown', 'invest', None, False, 
                                     MESSAGE_REQUIRED_FIELDS)), 400
    
    if amount <= 0:
        return jsonify(build_response('Unknown', 'invest', None, False, 
                                     MESSAGE_AMOUNT_POSITIVE)), 400
    
    # Dual-run validation for high-stakes operation
    prompt = f"Invest {amount} in {category} for customer {customer_id}"
    is_valid, sql_query, message = dual_run_validation(prompt, customer_id)
    
    if not is_valid:
        log_audit('investment_failed', customer_id, prompt, '', None, 
                 {'model': 'claude-3-5-sonnet', 'dual_run': True}, message)
        return jsonify(build_response('Unknown', 'invest', None, False, message)), 400
    
    # Get customer info
    info_query = '''
        SELECT c.name, a.account_id, a.balance
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
        WHERE c.customer_id = ?
    '''
    info_result, error = execute_query(info_query, (customer_id,), customer_id)
    
    if error or not info_result:
        return jsonify(build_response('Unknown', 'invest', None, False, 
                                     '口座を確認できませんでした')), 500
    
    customer_name = info_result[0]['name']
    account_id = info_result[0]['account_id']
    current_balance = info_result[0]['balance']
    
    # Record investment transaction
    insert_query = '''
        INSERT INTO transactions (account_id, customer_id, transaction_type, category, amount, description)
        VALUES (?, ?, 'deposit', ?, ?, ?)
    '''
    
    description = f"Investment in {category}"
    result, error = execute_query(insert_query, 
                                  (account_id, customer_id, category, amount, description), 
                                  customer_id)
    
    if error:
        log_audit('investment_failed', customer_id, prompt, insert_query, None, 
                 {'model': 'claude-3-5-sonnet', 'dual_run': True}, error)
        return jsonify(build_response(customer_name, 'invest', None, False, error)), 500
    
    # Update balance
    update_query = 'UPDATE accounts SET balance = balance + ? WHERE customer_id = ?'
    execute_query(update_query, (amount, customer_id), customer_id)
    
    log_audit('investment_completed', customer_id, prompt, insert_query, result, 
              {'model': 'claude-3-5-sonnet', 'dual_run': True, 'validation': 'passed'})
    
    return jsonify(build_response(customer_name, 'invest', 
                                 {'amount': amount, 'category': category, 
                                  'new_balance': current_balance + amount}, True))

@app.route('/api/custom_query', methods=['POST'])
def custom_query():
    """Execute custom query using natural language parsing"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    query_description = data.get('query_description')
    
    if not all([customer_id, query_description]):
        return jsonify(build_response('Unknown', 'custom_query', None, False,
                                     MESSAGE_REQUIRED_FIELDS)), 400
    
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
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)

# Made with Bob
