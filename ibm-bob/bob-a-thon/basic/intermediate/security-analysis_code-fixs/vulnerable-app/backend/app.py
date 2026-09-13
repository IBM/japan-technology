"""
Todo Application - VULNERABLE VERSION
This code contains intentional security vulnerabilities for educational purposes.
DO NOT use this code in production!

Vulnerabilities included:
- SQL Injection
- Hardcoded secrets
- Missing input validation
- Insecure error handling
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Todo
from database import db, init_db
from config import DATABASE_URL, SECRET_KEY, API_KEY
from datetime import datetime

app = Flask(__name__)

# VULNERABILITY: Using hardcoded secret from config
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
init_db(app)


@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    try:
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return jsonify([todo.to_dict() for todo in todos]), 200
    except Exception as e:
        # VULNERABILITY: Exposing internal error details
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a specific todo"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404


@app.route('/api/todos', methods=['POST'])
def create_todo():
    """
    Create a new todo
    VULNERABILITY: No input validation
    """
    try:
        data = request.get_json()
        
        # VULNERABILITY: No validation of input data
        # Accepts any length, any characters, no sanitization
        todo = Todo(
            title=data.get('title', ''),
            description=data.get('description', ''),
            completed=False
        )
        
        db.session.add(todo)
        db.session.commit()
        
        return jsonify(todo.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        # VULNERABILITY: Exposing stack trace
        return jsonify({'error': str(e), 'trace': repr(e)}), 500


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Update a todo
    VULNERABILITY: No input validation
    """
    try:
        todo = Todo.query.get_or_404(todo_id)
        data = request.get_json()
        
        # VULNERABILITY: No validation, accepts any data
        if 'title' in data:
            todo.title = data['title']
        if 'description' in data:
            todo.description = data['description']
        if 'completed' in data:
            todo.completed = data['completed']
        
        db.session.commit()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'message': 'Todo deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/api/todos/search', methods=['GET'])
def search_todos():
    """
    Search todos by title
    CRITICAL VULNERABILITY: SQL Injection
    """
    query = request.args.get('q', '')
    
    try:
        # VULNERABILITY: Direct string formatting in SQL query
        # This allows SQL injection attacks!
        sql = f"SELECT * FROM todos WHERE title LIKE '%{query}%'"
        
        # Execute raw SQL (DANGEROUS!)
        result = db.session.execute(sql)
        
        # Convert results to list of dicts
        todos = []
        for row in result:
            todos.append({
                'id': row[0],
                'title': row[1],
                'description': row[2],
                'completed': bool(row[3]),
                'created_at': row[4]
            })
        
        return jsonify(todos), 200
    except Exception as e:
        # VULNERABILITY: Exposing SQL errors
        return jsonify({
            'error': str(e),
            'query': sql,  # Exposing the SQL query!
            'type': type(e).__name__
        }), 500


@app.route('/api/admin/config', methods=['GET'])
def get_config():
    """
    Admin endpoint to view configuration
    VULNERABILITY: Exposing sensitive configuration
    """
    # VULNERABILITY: Exposing secrets through API
    return jsonify({
        'database_url': DATABASE_URL,
        'api_key': API_KEY,
        'secret_key': SECRET_KEY,
        'debug': app.debug
    }), 200


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        # VULNERABILITY: Exposing version info
        'version': '1.0.0-vulnerable',
        'database': DATABASE_URL  # Exposing DB connection string
    }), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # VULNERABILITY: Running in debug mode in production
    app.run(debug=True, host='0.0.0.0', port=5000)

# Made with Bob
