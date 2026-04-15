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


def validate_todo_input(data):
    """
    Validate todo input data - SECURE VERSION
    
    Returns:
        tuple: (errors_list, validated_data_dict)
    """
    errors = []
    
    # Validate title
    title = data.get('title', '').strip()
    if not title:
        errors.append('Title is required and cannot be empty')
    elif len(title) < 1:
        errors.append('Title must be at least 1 character long')
    elif len(title) > 200:
        errors.append('Title must be 200 characters or less')
    
    # Validate description
    description = data.get('description', '').strip()
    if len(description) > 1000:
        errors.append('Description must be 1000 characters or less')
    
    # Validate completed (if provided)
    completed = data.get('completed', False)
    if not isinstance(completed, bool):
        errors.append('Completed must be a boolean value')
    
    return errors, {
        'title': title,
        'description': description,
        'completed': completed
    }


@app.route('/api/todos', methods=['POST'])
def create_todo():
    """
    Create a new todo - SECURE VERSION
    Includes comprehensive input validation
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        # SECURE: Validate input data
        errors, validated_data = validate_todo_input(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Create todo with validated data
        todo = Todo(
            title=validated_data['title'],
            description=validated_data['description'],
            completed=False
        )
        
        db.session.add(todo)
        db.session.commit()
        
        return jsonify(todo.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        # SECURE: Generic error message without exposing internal details
        app.logger.error(f"Error creating todo: {str(e)}")
        return jsonify({'error': 'Failed to create todo'}), 500


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Update a todo - SECURE VERSION
    Includes input validation
    """
    try:
        todo = Todo.query.get_or_404(todo_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        # SECURE: Validate input data
        errors, validated_data = validate_todo_input(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Update only provided fields with validated data
        if 'title' in data:
            todo.title = validated_data['title']
        if 'description' in data:
            todo.description = validated_data['description']
        if 'completed' in data:
            todo.completed = validated_data['completed']
        
        db.session.commit()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        # SECURE: Generic error message
        app.logger.error(f"Error updating todo {todo_id}: {str(e)}")
        return jsonify({'error': 'Failed to update todo'}), 500


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
    Search todos by title - SECURE VERSION
    Uses SQLAlchemy ORM to prevent SQL injection
    """
    query = request.args.get('q', '')
    
    try:
        # SECURE: Using SQLAlchemy ORM with parameterized query
        # The ORM automatically escapes user input, preventing SQL injection
        todos = Todo.query.filter(
            Todo.title.like(f'%{query}%')
        ).order_by(Todo.created_at.desc()).all()
        
        # Convert to list of dicts using the model's to_dict method
        return jsonify([todo.to_dict() for todo in todos]), 200
    except Exception as e:
        # SECURE: Generic error message without exposing internal details
        app.logger.error(f"Search error: {str(e)}")
        return jsonify({'error': 'Search failed'}), 500


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
#    app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug=True, host='0.0.0.0', port=5001)

# Made with Bob
