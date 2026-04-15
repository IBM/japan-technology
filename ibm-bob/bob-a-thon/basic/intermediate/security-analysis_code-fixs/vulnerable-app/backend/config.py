"""
Application Configuration - SECURE VERSION
Uses environment variables for sensitive data.
Secrets are loaded from .env file (not committed to version control).
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///todos.db')

# API Keys and Secrets
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

# Third-party credentials (optional)
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

# Email configuration (optional)
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# JWT configuration
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# Application settings
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
TESTING = os.getenv('TESTING', 'False').lower() == 'true'

# Validate required environment variables
REQUIRED_VARS = ['SECRET_KEY', 'API_KEY']
missing_vars = [var for var in REQUIRED_VARS if not os.getenv(var)]

if missing_vars:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing_vars)}\n"
        f"Please create a .env file based on .env.example"
    )

"""
SECURITY IMPROVEMENTS:
1. ✅ Secrets stored in environment variables, not in code
2. ✅ .env file excluded from version control
3. ✅ Easy credential rotation without code changes
4. ✅ Different credentials per environment
5. ✅ Validation of required variables
6. ✅ Clear error messages for missing configuration

USAGE:
1. Copy .env.example to .env
2. Update .env with your actual credentials
3. Never commit .env to version control
"""

# Made with Bob
