"""
Database Configuration
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """Initialize the database with the Flask application"""
    db.init_app(app)
    
    with app.app_context():
        import models
        db.create_all()
        print("Database initialized!")

# Made with Bob
