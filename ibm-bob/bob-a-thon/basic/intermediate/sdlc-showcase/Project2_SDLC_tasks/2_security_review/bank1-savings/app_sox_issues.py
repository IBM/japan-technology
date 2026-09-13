from flask import Flask, jsonify, request, render_template_string, send_from_directory
import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Tuple, Optional
import hashlib
import re

app = Flask(__name__, static_folder='static', static_url_path='')

# Bank configuration
BANK_NAME = os.getenv('BANK_NAME', 'Savings Bank')
BANK_ID = os.getenv('BANK_ID', 'bank1')
BANK_COLOR = os.getenv('BANK_COLOR', '#2E7D32')
DB_PATH = os.getenv('DB_PATH', 'bank1_savings.db')
AUDIT_LOG_PATH = os.getenv('AUDIT_LOG_PATH', 'bank1_audit.jsonl')
BANK2_URL = os.getenv('BANK2_URL', 'http://localhost:5002')

# SOX ISSUE 1: No segregation of duties - single admin can do everything
ADMIN_USER = "admin"
ADMIN_PASSWORD = "admin123"

# SOX ISSUE 2: No audit trail for configuration changes
# Missing: Who changed what, when, and why

# SOX ISSUE 3: No access controls - anyone can access any customer data
# Missing: Role-based access control (RBAC)

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
            balance REAL NOT NULL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Transactions table
    # SOX ISSUE 4: No immutability - transactions can be modified/deleted
    # Missing: Append-only design, no UPDATE/DELETE allowed
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
    
    # SOX ISSUE 5: No user activity logging table
    # Missing: Table to track who accessed what data and when
    
    # SOX ISSUE 6: No approval workflow table
    # Missing: Table for transaction approvals (maker-checker)
    
    # Insert demo data if tables are empty
    cursor.execute('SELECT COUNT(*) FROM customers')
    if cursor.fetchone()[0] == 0:
        demo_customers = [
            ('Alice Johnson', 'alice@example.com'),
            ('Bob Smith', 'bob@example.com'),
            ('Carol Davis', 'carol@example.com'),
        ]
        cursor.executemany('INSERT INTO customers (name, email) VALUES (?, ?)', demo_customers)
        
        for i in range(1, 4):
            cursor.execute('INSERT INTO accounts (customer_id, account_type, balance) VALUES (?, ?, ?)',
                         (i, 'savings', 5000.0 + (i * 500)))
        
        demo_transactions = [
            (1, 1, 'deposit', 'salary', 3000.0, 'Monthly salary'),
            (1, 1, 'withdrawal', 'groceries', -150.0, 'Supermarket'),
            (2, 2, 'deposit', 'salary', 2500.0, 'Monthly salary'),
        ]
        cursor.executemany(
            'INSERT INTO transactions (account_id, customer_id, transaction_type, category, amount, description) VALUES (?, ?, ?, ?, ?, ?)',
            demo_transactions
        )
    
    conn.commit()
    conn.close()

# SOX ISSUE 7: Incomplete audit logging - missing critical fields
def log_audit(event_type: str, customer_id: Optional[int], prompt: str, sql_query: str, 
              result: Any, model_config: Dict, error: Optional[str] = None):
    """Log interactions - INCOMPLETE for SOX compliance"""
    # Missing: user_id, ip_address, session_id, approval_status
    # Missing: data_before and data_after for changes
    # Missing: business justification
    audit_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'bank_id': BANK_ID,
        'event_type': event_type,
        'customer_id': customer_id,
        'prompt': prompt,
        'generated_sql': sql_query,
        'result': str(result)[:500],
        'model_config': model_config,
        'error': error,
        # SOX MISSING: user_id, ip_address, session_id
        # SOX MISSING: approval_required, approved_by, approval_date
        # SOX MISSING: data_before, data_after (for change tracking)
    }
    
    # SOX ISSUE 8: Audit log not tamper-proof
    # Missing: Digital signatures, blockchain, or write-once storage
    hash_input = json.dumps(audit_entry, sort_keys=True)
    audit_entry['hash'] = hashlib.sha256(hash_input.encode()).hexdigest()
    
    with open(AUDIT_LOG_PATH, 'a') as f:
        f.write(json.dumps(audit_entry) + '\n')

def execute_query(query: str, params: Tuple, customer_id: Optional[int] = None) -> Tuple[List[Dict], Optional[str]]:
    """Execute parameterized query"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(query, params)
        
        if query.strip().upper().startswith('SELECT'):
            rows = cursor.fetchall()
            result = [dict(row) for row in rows]
            conn.close()
            return result, None
        else:
            conn.commit()
            affected_rows = cursor.rowcount
            conn.close()
            return [{'affected_rows': affected_rows}], None
            
    except sqlite3.Error as e:
        return [], str(e)

# SOX ISSUE 9: No authentication/authorization on critical endpoints
@app.route('/api/balance', methods=['POST'])
def get_balance():
    """Get customer balance - NO ACCESS CONTROL"""
    # SOX MISSING: Authentication check
    # SOX MISSING: Authorization check (can user access this customer?)
    # SOX MISSING: Activity logging (who accessed what)
    
    data = request.get_json()
    customer_id = data.get('customer_id')
    
    if not customer_id:
        return jsonify({'success': False, 'error': 'Customer ID required'}), 400
    
    query = '''
        SELECT c.name, c.email, a.account_type, a.balance
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
        WHERE c.customer_id = ?
    '''
    
    result, error = execute_query(query, (customer_id,), customer_id)
    
    # SOX ISSUE 10: Audit log missing user context
    log_audit('balance_check', customer_id, 'Check balance', query, result, 
              {'model': 'direct_sql', 'version': '1.0'}, error)
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    if not result:
        return jsonify({'success': False, 'error': 'Customer not found'}), 404
    
    return jsonify({'success': True, 'result_data': result})

# SOX ISSUE 11: Direct balance modification without approval workflow
@app.route('/api/admin/modify_balance', methods=['POST'])
def modify_balance():
    """Modify account balance directly - NO MAKER-CHECKER"""
    # SOX MISSING: Maker-checker workflow (dual control)
    # SOX MISSING: Approval requirement for large changes
    # SOX MISSING: Business justification requirement
    # SOX MISSING: Supervisor approval
    
    data = request.get_json()
    customer_id = data.get('customer_id')
    new_balance = data.get('new_balance')
    reason = data.get('reason', 'No reason provided')  # Not enforced!
    
    # SOX ISSUE 12: No validation of balance changes
    # Missing: Threshold checks, reasonableness checks
    
    # SOX ISSUE 13: No retention of previous balance
    query = 'UPDATE accounts SET balance = ? WHERE customer_id = ?'
    result, error = execute_query(query, (new_balance, customer_id))
    
    # SOX ISSUE 14: Incomplete audit trail for critical changes
    log_audit('balance_modified', customer_id, f'Balance modified: {reason}', 
              query, result, {'model': 'admin', 'reason': reason}, error)
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    return jsonify({'success': True, 'message': 'Balance modified', 'new_balance': new_balance})

# SOX ISSUE 15: Transaction deletion allowed (violates immutability)
@app.route('/api/admin/delete_transaction', methods=['POST'])
def delete_transaction():
    """Delete transaction - VIOLATES SOX IMMUTABILITY"""
    # SOX VIOLATION: Financial transactions should NEVER be deleted
    # Should use: Reversal transactions instead
    
    data = request.get_json()
    transaction_id = data.get('transaction_id')
    
    # SOX ISSUE 16: No approval required for deletion
    # SOX ISSUE 17: No retention of deleted data
    query = 'DELETE FROM transactions WHERE transaction_id = ?'
    result, error = execute_query(query, (transaction_id,))
    
    # SOX ISSUE 18: Audit log doesn't capture deleted data
    log_audit('transaction_deleted', None, f'Deleted transaction {transaction_id}', 
              query, result, {'model': 'admin'}, error)
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    return jsonify({'success': True, 'message': f'Transaction {transaction_id} deleted'})

# SOX ISSUE 19: Transaction modification allowed
@app.route('/api/admin/modify_transaction', methods=['POST'])
def modify_transaction():
    """Modify existing transaction - VIOLATES SOX"""
    # SOX VIOLATION: Transactions should be immutable
    # Should use: Reversal + new transaction instead
    
    data = request.get_json()
    transaction_id = data.get('transaction_id')
    new_amount = data.get('new_amount')
    new_description = data.get('new_description')
    
    # SOX ISSUE 20: No record of original values
    query = '''
        UPDATE transactions 
        SET amount = ?, description = ? 
        WHERE transaction_id = ?
    '''
    result, error = execute_query(query, (new_amount, new_description, transaction_id))
    
    log_audit('transaction_modified', None, f'Modified transaction {transaction_id}', 
              query, result, {'model': 'admin'}, error)
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    return jsonify({'success': True, 'message': 'Transaction modified'})

# SOX ISSUE 21: No periodic reconciliation process
# Missing: Automated reconciliation reports
# Missing: Exception reporting
# Missing: Variance analysis

# SOX ISSUE 22: No data retention policy enforcement
# Missing: Automatic archival after retention period
# Missing: Legal hold capabilities
# Missing: Secure deletion after retention

# SOX ISSUE 23: No change management process
@app.route('/api/admin/update_config', methods=['POST'])
def update_config():
    """Update system configuration - NO CHANGE CONTROL"""
    # SOX MISSING: Change request documentation
    # SOX MISSING: Impact analysis
    # SOX MISSING: Approval workflow
    # SOX MISSING: Rollback plan
    # SOX MISSING: Testing evidence
    
    data = request.get_json()
    config_key = data.get('key')
    config_value = data.get('value')
    
    # SOX ISSUE 24: Configuration changes not tracked
    # Just updates without any approval or documentation
    
    return jsonify({'success': True, 'message': 'Configuration updated'})

# SOX ISSUE 25: No segregation of duties in code
# Same person can:
# - Create transactions
# - Approve transactions
# - Modify transactions
# - Delete transactions
# - Access all customer data
# - Modify system configuration

# SOX ISSUE 26: No automated controls
# Missing: Automated limit checks
# Missing: Automated reconciliation
# Missing: Automated exception detection
# Missing: Automated compliance reporting

# SOX ISSUE 27: No evidence of testing
# Missing: Test results documentation
# Missing: User acceptance testing sign-off
# Missing: Regression testing evidence

@app.route('/api/transactions', methods=['POST'])
def get_transactions():
    """Get customer transactions"""
    data = request.get_json()
    customer_id = data.get('customer_id')
    limit = data.get('limit', 10)
    
    if not customer_id:
        return jsonify({'success': False, 'error': 'Customer ID required'}), 400
    
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
        return jsonify({'success': False, 'error': error}), 500
    
    return jsonify({'success': True, 'result_data': result})

# SOX ISSUE 28: No backup verification process
# Missing: Regular backup testing
# Missing: Restore testing
# Missing: Backup integrity verification

# SOX ISSUE 29: No disaster recovery testing
# Missing: DR plan documentation
# Missing: DR testing schedule
# Missing: DR test results

# SOX ISSUE 30: No security monitoring
# Missing: Failed login attempt tracking
# Missing: Unusual activity detection
# Missing: Security incident response plan

@app.route('/api/audit_log', methods=['GET'])
def get_audit_log():
    """Retrieve audit log entries"""
    # SOX ISSUE 31: Audit log accessible without authentication
    # SOX ISSUE 32: No protection against audit log tampering
    
    try:
        entries = []
        if os.path.exists(AUDIT_LOG_PATH):
            with open(AUDIT_LOG_PATH, 'r') as f:
                for line in f:
                    entries.append(json.loads(line))
        
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

# SOX ISSUE 33: No documentation of internal controls
# Missing: Control documentation
# Missing: Control testing evidence
# Missing: Control effectiveness assessment

# SOX ISSUE 34: No management review process
# Missing: Periodic management review
# Missing: Control deficiency tracking
# Missing: Remediation tracking

# SOX ISSUE 35: No IT general controls
# Missing: Access provisioning/deprovisioning process
# Missing: Password policy enforcement
# Missing: Session timeout
# Missing: Encryption at rest
# Missing: Encryption in transit

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

# Made with Bob - SOX COMPLIANCE ISSUES FOR DEMO