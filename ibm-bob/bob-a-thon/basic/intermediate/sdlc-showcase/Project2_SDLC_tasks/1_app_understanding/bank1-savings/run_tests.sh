#!/bin/bash
# Convenience script to run Bank1-Savings tests

set -e

echo "=========================================="
echo "Bank1-Savings API Test Suite"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements-test.txt

echo ""
echo "=========================================="
echo "Running Tests"
echo "=========================================="
echo ""

# Run tests based on argument
case "${1:-unittest}" in
    unittest)
        echo "Running with unittest..."
        python test_api.py
        ;;
    pytest)
        echo "Running with pytest..."
        pytest test_api.py -v
        ;;
    coverage)
        echo "Running with coverage..."
        pytest test_api.py --cov=app --cov-report=term --cov-report=html
        echo ""
        echo "Coverage report generated in htmlcov/index.html"
        ;;
    quick)
        echo "Running quick tests (unittest, no verbose)..."
        python -m unittest test_api -q
        ;;
    *)
        echo "Usage: $0 [unittest|pytest|coverage|quick]"
        echo "  unittest  - Run with unittest (default)"
        echo "  pytest    - Run with pytest"
        echo "  coverage  - Run with coverage report"
        echo "  quick     - Quick run without verbose output"
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "Tests Complete!"
echo "=========================================="

# Made with Bob
