"""
Application Configuration - VULNERABLE VERSION
This file contains hardcoded secrets for educational purposes.
DO NOT use this pattern in production!

VULNERABILITY: Hardcoded Secrets
All sensitive credentials are stored directly in the source code.
"""

# VULNERABILITY: Hardcoded database credentials
# Anyone with access to the code can see the password
DATABASE_URL = "postgresql://admin:SuperSecret123@localhost:5432/todos_db"

# VULNERABILITY: Hardcoded API key
# This key should be in environment variables or a secrets manager
API_KEY = "sk_live_abc123xyz789_this_is_a_secret_key"

# VULNERABILITY: Hardcoded secret key
# Used for session management and should be randomly generated
SECRET_KEY = "my-super-secret-key-12345"

# VULNERABILITY: Hardcoded third-party credentials
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VULNERABILITY: Hardcoded email credentials
EMAIL_USERNAME = "admin@example.com"
EMAIL_PASSWORD = "EmailPassword123!"

# Additional configuration
DEBUG = True  # VULNERABILITY: Debug mode enabled
TESTING = False

# VULNERABILITY: Hardcoded JWT secret
JWT_SECRET_KEY = "jwt-secret-key-not-secure"

"""
WHY THIS IS DANGEROUS:
1. Credentials are visible in version control history
2. Anyone with code access has full system access
3. Credentials can't be rotated without code changes
4. Same credentials used across all environments
5. Secrets may be exposed in logs or error messages
6. No audit trail of who accessed what

PROPER SOLUTION:
Use environment variables or a secrets management service like:
- AWS Secrets Manager
- Azure Key Vault
- HashiCorp Vault
- Environment variables with .env files (not committed)
"""

# Made with Bob
