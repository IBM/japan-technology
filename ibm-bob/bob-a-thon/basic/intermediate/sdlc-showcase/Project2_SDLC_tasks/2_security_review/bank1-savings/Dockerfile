# Multi-stage build for Bank 1 with React frontend

# Stage 1: Build React frontend
FROM node:18-alpine AS frontend-builder

WORKDIR /frontend

# Copy package files
COPY frontend/package*.json ./

# Install dependencies
RUN npm ci

# Copy frontend source
COPY frontend/ ./

# Build the React app
RUN npm run build

# Stage 2: Python Flask application with React frontend
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Copy built React frontend from stage 1
COPY --from=frontend-builder /frontend/dist ./static

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
ENV BANK_NAME="Savings Bank"
ENV BANK_ID="bank1"

# Expose port 5000
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/health')" || exit 1

# Run the application
CMD ["python", "app.py"]