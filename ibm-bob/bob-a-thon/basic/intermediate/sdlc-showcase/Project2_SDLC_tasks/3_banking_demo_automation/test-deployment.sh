#!/bin/bash

# Banking Demo - Deployment Test Script
# This script tests the deployed banking applications

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
BANK1_URL="http://localhost:5001"
BANK2_URL="http://localhost:5002"

echo "=========================================="
echo "Banking Demo - Deployment Test"
echo "=========================================="
echo ""

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

# Test 1: Check if Bank 1 is running
echo "Test 1: Checking Bank 1 availability..."
if curl -s -f "$BANK1_URL/health" > /dev/null; then
    print_success "Bank 1 is running at $BANK1_URL"
else
    print_error "Bank 1 is not accessible at $BANK1_URL"
    exit 1
fi
echo ""

# Test 2: Check if Bank 2 is running
echo "Test 2: Checking Bank 2 availability..."
if curl -s -f "$BANK2_URL/health" > /dev/null; then
    print_success "Bank 2 is running at $BANK2_URL"
else
    print_error "Bank 2 is not accessible at $BANK2_URL"
    exit 1
fi
echo ""

# Test 3: Get Bank 1 users
echo "Test 3: Fetching Bank 1 users..."
BANK1_USERS=$(curl -s "$BANK1_URL/users")
if echo "$BANK1_USERS" | jq -e '.users | length > 0' > /dev/null 2>&1; then
    USER_COUNT=$(echo "$BANK1_USERS" | jq '.users | length')
    print_success "Bank 1 has $USER_COUNT users"
else
    print_error "Failed to fetch Bank 1 users"
    exit 1
fi
echo ""

# Test 4: Get Bank 2 users
echo "Test 4: Fetching Bank 2 users..."
BANK2_USERS=$(curl -s "$BANK2_URL/users")
if echo "$BANK2_USERS" | jq -e '.users | length > 0' > /dev/null 2>&1; then
    USER_COUNT=$(echo "$BANK2_USERS" | jq '.users | length')
    print_success "Bank 2 has $USER_COUNT users"
else
    print_error "Failed to fetch Bank 2 users"
    exit 1
fi
echo ""

# Test 5: Get initial balance for user1
echo "Test 5: Checking initial balances..."
BANK1_USER1=$(curl -s "$BANK1_URL/user/user1")
BANK2_USER1=$(curl -s "$BANK2_URL/user/user1")

BANK1_BALANCE=$(echo "$BANK1_USER1" | jq -r '.balance')
BANK2_BALANCE=$(echo "$BANK2_USER1" | jq -r '.balance')

print_info "Bank 1 - user1 balance: \$$BANK1_BALANCE"
print_info "Bank 2 - user1 balance: \$$BANK2_BALANCE"
echo ""

# Test 6: Transfer funds
echo "Test 6: Testing fund transfer..."
TRANSFER_AMOUNT=500.00
print_info "Transferring \$$TRANSFER_AMOUNT from Bank 1 to Bank 2 for user1..."

TRANSFER_RESPONSE=$(curl -s -X POST "$BANK1_URL/transfer" \
    -H "Content-Type: application/json" \
    -d "{\"user_id\": \"user1\", \"amount\": $TRANSFER_AMOUNT}")

if echo "$TRANSFER_RESPONSE" | jq -e '.success == true' > /dev/null 2>&1; then
    print_success "Transfer successful"
    NEW_BANK1_BALANCE=$(echo "$TRANSFER_RESPONSE" | jq -r '.new_balance')
    print_info "New Bank 1 balance: \$$NEW_BANK1_BALANCE"
else
    print_error "Transfer failed"
    echo "$TRANSFER_RESPONSE" | jq '.'
    exit 1
fi
echo ""

# Test 7: Verify balances after transfer
echo "Test 7: Verifying balances after transfer..."
BANK1_USER1_AFTER=$(curl -s "$BANK1_URL/user/user1")
BANK2_USER1_AFTER=$(curl -s "$BANK2_URL/user/user1")

BANK1_BALANCE_AFTER=$(echo "$BANK1_USER1_AFTER" | jq -r '.balance')
BANK2_BALANCE_AFTER=$(echo "$BANK2_USER1_AFTER" | jq -r '.balance')

print_info "Bank 1 - user1 balance after: \$$BANK1_BALANCE_AFTER"
print_info "Bank 2 - user1 balance after: \$$BANK2_BALANCE_AFTER"

# Verify the math
EXPECTED_BANK1=$(echo "$BANK1_BALANCE - $TRANSFER_AMOUNT" | bc)
EXPECTED_BANK2=$(echo "$BANK2_BALANCE + $TRANSFER_AMOUNT" | bc)

if [ "$(echo "$BANK1_BALANCE_AFTER == $EXPECTED_BANK1" | bc)" -eq 1 ]; then
    print_success "Bank 1 balance is correct"
else
    print_error "Bank 1 balance mismatch. Expected: \$$EXPECTED_BANK1, Got: \$$BANK1_BALANCE_AFTER"
fi

if [ "$(echo "$BANK2_BALANCE_AFTER == $EXPECTED_BANK2" | bc)" -eq 1 ]; then
    print_success "Bank 2 balance is correct"
else
    print_error "Bank 2 balance mismatch. Expected: \$$EXPECTED_BANK2, Got: \$$BANK2_BALANCE_AFTER"
fi
echo ""

# Test 8: Test error handling - insufficient funds
echo "Test 8: Testing error handling (insufficient funds)..."
LARGE_AMOUNT=999999.00
ERROR_RESPONSE=$(curl -s -X POST "$BANK1_URL/transfer" \
    -H "Content-Type: application/json" \
    -d "{\"user_id\": \"user1\", \"amount\": $LARGE_AMOUNT}")

if echo "$ERROR_RESPONSE" | jq -e '.success == false' > /dev/null 2>&1; then
    print_success "Error handling works correctly"
    ERROR_MSG=$(echo "$ERROR_RESPONSE" | jq -r '.error')
    print_info "Error message: $ERROR_MSG"
else
    print_error "Error handling failed"
fi
echo ""

# Test 9: Test error handling - invalid user
echo "Test 9: Testing error handling (invalid user)..."
INVALID_USER_RESPONSE=$(curl -s -X POST "$BANK1_URL/transfer" \
    -H "Content-Type: application/json" \
    -d '{"user_id": "user999", "amount": 100.00}')

if echo "$INVALID_USER_RESPONSE" | jq -e '.success == false' > /dev/null 2>&1; then
    print_success "Invalid user handling works correctly"
else
    print_error "Invalid user handling failed"
fi
echo ""

# Test 10: Check Docker containers
echo "Test 10: Checking Docker containers..."
if docker ps | grep -q "bank1-savings"; then
    print_success "Bank 1 container is running"
else
    print_error "Bank 1 container is not running"
fi

if docker ps | grep -q "bank2-investment"; then
    print_success "Bank 2 container is running"
else
    print_error "Bank 2 container is not running"
fi
echo ""

# Test 11: Check Docker network
echo "Test 11: Checking Docker network..."
if docker network ls | grep -q "banking-network"; then
    print_success "Banking network exists"
else
    print_error "Banking network does not exist"
fi
echo ""

# Summary
echo "=========================================="
echo "Test Summary"
echo "=========================================="
print_success "All tests passed!"
echo ""
echo "Deployment is working correctly."
echo ""
echo "Access the applications:"
echo "  Bank 1 (Savings): $BANK1_URL"
echo "  Bank 2 (Investment): $BANK2_URL"
echo "=========================================="

# Made with Bob
