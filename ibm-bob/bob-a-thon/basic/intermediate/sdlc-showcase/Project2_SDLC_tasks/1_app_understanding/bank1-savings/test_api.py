"""
Unit tests for Bank1-Savings API endpoints
Tests all major API endpoints with various scenarios
"""

import unittest
import json
import os
import tempfile
import sqlite3
from unittest.mock import patch, MagicMock
from app import app, init_db, execute_query, DB_PATH, AUDIT_LOG_PATH


class Bank1APITestCase(unittest.TestCase):
    """Test cases for Bank1-Savings API endpoints"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test database once for all tests"""
        # Create temporary database
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        cls.audit_fd, cls.audit_path = tempfile.mkstemp()
        
        # Override database paths
        os.environ['DB_PATH'] = cls.db_path
        os.environ['AUDIT_LOG_PATH'] = cls.audit_path
        
        # Initialize database with test data
        init_db()
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test database"""
        os.close(cls.db_fd)
        os.unlink(cls.db_path)
        os.close(cls.audit_fd)
        os.unlink(cls.audit_path)
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def tearDown(self):
        """Clean up after each test"""
        pass
    
    # ==================== Balance Endpoint Tests ====================
    
    def test_get_balance_success(self):
        """Test successful balance retrieval"""
        response = self.client.post('/api/balance',
                                   data=json.dumps({'customer_id': 1}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        self.assertEqual(data['query_type'], 'balance')
        self.assertIn('result_data', data)
        self.assertGreater(len(data['result_data']), 0)
        self.assertIn('balance', data['result_data'][0])
        self.assertIn('name', data['result_data'][0])
        self.assertIn('email', data['result_data'][0])
    
    def test_get_balance_missing_customer_id(self):
        """Test balance request without customer_id"""
        response = self.client.post('/api/balance',
                                   data=json.dumps({}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        
        self.assertFalse(data['success'])
        self.assertIn('error', data)
        self.assertIn('顧客IDは必須です', data['error'])
    
    def test_get_balance_invalid_customer(self):
        """Test balance request for non-existent customer"""
        response = self.client.post('/api/balance',
                                   data=json.dumps({'customer_id': 9999}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        
        self.assertFalse(data['success'])
        self.assertIn('顧客が見つかりません', data['error'])
    
    def test_get_balance_all_customers(self):
        """Test balance retrieval for all demo customers"""
        for customer_id in range(1, 6):
            response = self.client.post('/api/balance',
                                       data=json.dumps({'customer_id': customer_id}),
                                       content_type='application/json')
            
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data['success'])
            self.assertGreater(data['result_data'][0]['balance'], 0)
    
    # ==================== Transactions Endpoint Tests ====================
    
    def test_get_transactions_success(self):
        """Test successful transaction retrieval"""
        response = self.client.post('/api/transactions',
                                   data=json.dumps({'customer_id': 1, 'limit': 10}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        self.assertEqual(data['query_type'], 'transactions')
        self.assertIn('result_data', data)
        
        # Check transaction structure
        if len(data['result_data']) > 0:
            transaction = data['result_data'][0]
            self.assertIn('transaction_id', transaction)
            self.assertIn('transaction_type', transaction)
            self.assertIn('amount', transaction)
            self.assertIn('transaction_date', transaction)
    
    def test_get_transactions_with_limit(self):
        """Test transaction retrieval with custom limit"""
        response = self.client.post('/api/transactions',
                                   data=json.dumps({'customer_id': 1, 'limit': 5}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        self.assertLessEqual(len(data['result_data']), 5)
    
    def test_get_transactions_missing_customer_id(self):
        """Test transactions request without customer_id"""
        response = self.client.post('/api/transactions',
                                   data=json.dumps({'limit': 10}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        
        self.assertFalse(data['success'])
        self.assertIn('顧客IDは必須です', data['error'])
    
    def test_get_transactions_default_limit(self):
        """Test transactions with default limit"""
        response = self.client.post('/api/transactions',
                                   data=json.dumps({'customer_id': 1}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        # Default limit is 10
        self.assertLessEqual(len(data['result_data']), 10)
    
    # ==================== Analytics Endpoint Tests ====================
    
    def test_get_analytics_success(self):
        """Test successful analytics generation"""
        response = self.client.post('/api/analytics',
                                   data=json.dumps({'customer_id': 1}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        self.assertEqual(data['query_type'], 'analytics')
        self.assertIn('result_data', data)
    
    def test_get_analytics_missing_customer_id(self):
        """Test analytics request without customer_id"""
        response = self.client.post('/api/analytics',
                                   data=json.dumps({}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        
        self.assertFalse(data['success'])
        self.assertIn('顧客IDは必須です', data['error'])
    
    # ==================== Transfer Endpoint Tests ====================
    
    @patch('requests.post')
    def test_transfer_success(self, mock_post):
        """Test successful transfer to Bank2"""
        # Mock Bank2 response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'success': True, 'new_balance': 1000}
        mock_post.return_value = mock_response
        
        # Get initial balance
        balance_response = self.client.post('/api/balance',
                                           data=json.dumps({'customer_id': 1}),
                                           content_type='application/json')
        initial_balance = json.loads(balance_response.data)['result_data'][0]['balance']
        
        # Perform transfer
        transfer_amount = 100.0
        response = self.client.post('/api/transfer',
                                   data=json.dumps({
                                       'customer_id': 1,
                                       'amount': transfer_amount
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        self.assertIn('result_data', data)
        self.assertIn('new_savings_balance', data['result_data'])
        self.assertAlmostEqual(data['result_data']['new_savings_balance'], initial_balance - transfer_amount, places=2)
    
    def test_transfer_missing_parameters(self):
        """Test transfer with missing parameters"""
        # Missing amount
        response = self.client.post('/api/transfer',
                                   data=json.dumps({'customer_id': 1}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        
        # Missing customer_id
        response = self.client.post('/api/transfer',
                                   data=json.dumps({'amount': 100}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    def test_transfer_invalid_amount(self):
        """Test transfer with invalid amounts"""
        # Negative amount
        response = self.client.post('/api/transfer',
                                   data=json.dumps({
                                       'customer_id': 1,
                                       'amount': -100
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        
        # Zero amount
        response = self.client.post('/api/transfer',
                                   data=json.dumps({
                                       'customer_id': 1,
                                       'amount': 0
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    def test_transfer_insufficient_balance(self):
        """Test transfer with insufficient balance"""
        response = self.client.post('/api/transfer',
                                   data=json.dumps({
                                       'customer_id': 1,
                                       'amount': 999999.99
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertIn('残高不足です', data['error'])
    
    # ==================== Receive Transfer Endpoint Tests ====================
    
    def test_receive_transfer_success(self):
        """Test successful receipt of transfer from Bank2"""
        # Get initial balance
        balance_response = self.client.post('/api/balance',
                                           data=json.dumps({'customer_id': 1}),
                                           content_type='application/json')
        initial_balance = json.loads(balance_response.data)['result_data'][0]['balance']
        
        # Receive transfer
        transfer_amount = 200.0
        response = self.client.post('/api/receive_transfer',
                                   data=json.dumps({
                                       'customer_id': 1,
                                       'amount': transfer_amount
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        self.assertIn('new_balance', data)
        self.assertAlmostEqual(data['new_balance'], initial_balance + transfer_amount, places=2)
    
    def test_receive_transfer_missing_parameters(self):
        """Test receive transfer with missing parameters"""
        response = self.client.post('/api/receive_transfer',
                                   data=json.dumps({'customer_id': 1}),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    def test_receive_transfer_invalid_amount(self):
        """Test receive transfer with invalid amount"""
        response = self.client.post('/api/receive_transfer',
                                   data=json.dumps({
                                       'customer_id': 1,
                                       'amount': -100
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    # ==================== Audit Log Endpoint Tests ====================
    
    def test_get_audit_log(self):
        """Test audit log retrieval"""
        # First make some API calls to generate audit entries
        self.client.post('/api/balance',
                        data=json.dumps({'customer_id': 1}),
                        content_type='application/json')
        
        # Get audit log
        response = self.client.get('/api/audit_log')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertTrue(data['success'])
        self.assertIn('audit_entries', data)
        self.assertGreater(len(data['audit_entries']), 0)
        
        # Check audit entry structure
        entry = data['audit_entries'][0]
        self.assertIn('timestamp', entry)
        self.assertIn('event_type', entry)
        self.assertIn('hash', entry)
    
    # ==================== Health Check Tests ====================
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.client.get('/health')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('bank_id', data)
        self.assertIn('bank', data)
    
    # ==================== Integration Tests ====================
    
    @patch('requests.post')
    def test_full_transfer_workflow(self, mock_post):
        """Test complete transfer workflow"""
        # Mock Bank2 response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'success': True, 'new_balance': 1000}
        mock_post.return_value = mock_response
        
        customer_id = 1
        
        # 1. Check initial balance
        response = self.client.post('/api/balance',
                                   data=json.dumps({'customer_id': customer_id}),
                                   content_type='application/json')
        initial_balance = json.loads(response.data)['result_data'][0]['balance']
        
        # 2. Get initial transactions
        response = self.client.post('/api/transactions',
                                   data=json.dumps({'customer_id': customer_id, 'limit': 10}),
                                   content_type='application/json')
        initial_tx_count = len(json.loads(response.data)['result_data'])
        
        # 3. Perform transfer
        transfer_amount = 50.0
        response = self.client.post('/api/transfer',
                                   data=json.dumps({
                                       'customer_id': customer_id,
                                       'amount': transfer_amount
                                   }),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        # 4. Verify balance decreased
        response = self.client.post('/api/balance',
                                   data=json.dumps({'customer_id': customer_id}),
                                   content_type='application/json')
        new_balance = json.loads(response.data)['result_data'][0]['balance']
        self.assertAlmostEqual(new_balance, initial_balance - transfer_amount, places=2)
        
        # 5. Verify new transaction was recorded
        response = self.client.post('/api/transactions',
                                   data=json.dumps({'customer_id': customer_id, 'limit': 10}),
                                   content_type='application/json')
        new_tx_count = len(json.loads(response.data)['result_data'])
        self.assertEqual(new_tx_count, initial_tx_count + 1)
    
    def test_concurrent_balance_checks(self):
        """Test multiple concurrent balance checks"""
        customer_ids = [1, 2, 3]
        responses = []
        
        for customer_id in customer_ids:
            response = self.client.post('/api/balance',
                                       data=json.dumps({'customer_id': customer_id}),
                                       content_type='application/json')
            responses.append(response)
        
        # All should succeed
        for response in responses:
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data['success'])


class DatabaseFunctionTests(unittest.TestCase):
    """Test database utility functions"""
    
    def test_execute_query_select(self):
        """Test execute_query with SELECT statement"""
        query = "SELECT name FROM customers WHERE customer_id = ?"
        result, error = execute_query(query, (1,))
        
        self.assertIsNone(error)
        self.assertIsInstance(result, list)
        if len(result) > 0:
            self.assertIn('name', result[0])
    
    def test_execute_query_invalid_sql(self):
        """Test execute_query with invalid SQL"""
        query = "SELECT * FROM nonexistent_table"
        result, error = execute_query(query, ())
        
        self.assertIsNotNone(error)
        self.assertEqual(result, [])


def run_tests():
    """Run all tests and generate report"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(Bank1APITestCase))
    suite.addTests(loader.loadTestsFromTestCase(DatabaseFunctionTests))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)

# Made with Bob
