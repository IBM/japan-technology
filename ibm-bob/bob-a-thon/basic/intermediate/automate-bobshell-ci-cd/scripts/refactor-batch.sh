#!/bin/bash
################################################################################
# Batch Refactoring Script
#
# This script refactors multiple files based on specified criteria.
# It creates backups before making changes and provides detailed logging.
#
# Usage:
#   ./refactor-batch.sh [refactor-type] [target-directory]
#
# Refactor Types:
#   modernize  - Update code to use modern language features
#   optimize   - Optimize for performance
#   cleanup    - Remove dead code and fix style issues
#   security   - Fix security vulnerabilities
#
# Example:
#   ./refactor-batch.sh modernize ./src
#   ./refactor-batch.sh optimize ./lib
#   ./refactor-batch.sh cleanup .
################################################################################

set -e  # Exit on error

# Configuration
REFACTOR_TYPE="${1:-modernize}"
TARGET_DIR="${2:-.}"
BACKUP_DIR="./refactor-backups/$(date +%Y%m%d_%H%M%S)"
LOG_FILE="./refactor-log-$(date +%Y%m%d_%H%M%S).txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${CYAN}ℹ $1${NC}"
}

log_message() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Validate refactor type
VALID_TYPES=("modernize" "optimize" "cleanup" "security")
if [[ ! " ${VALID_TYPES[@]} " =~ " ${REFACTOR_TYPE} " ]]; then
    print_error "Invalid refactor type: $REFACTOR_TYPE"
    echo "Valid types: ${VALID_TYPES[*]}"
    exit 1
fi

# Check if Bob CLI is installed
if ! command -v bob &> /dev/null; then
    print_error "Bob CLI is not installed"
    echo "Install it with: npm install -g @ibm/bob-cli"
    exit 1
fi

# Check if target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    print_error "Directory not found: $TARGET_DIR"
    exit 1
fi

# Start logging
log_message "=== Batch Refactoring Started ==="
log_message "Refactor Type: $REFACTOR_TYPE"
log_message "Target Directory: $TARGET_DIR"
log_message "Backup Directory: $BACKUP_DIR"

print_header "Batch Refactoring"
echo "Refactor Type: $REFACTOR_TYPE"
echo "Target Directory: $TARGET_DIR"
echo "Backup Directory: $BACKUP_DIR"
echo "Log File: $LOG_FILE"
echo ""

# Create backup
print_header "Creating Backup"
mkdir -p "$BACKUP_DIR"

if cp -r "$TARGET_DIR" "$BACKUP_DIR/"; then
    print_success "Backup created successfully"
    log_message "Backup created: $BACKUP_DIR"
else
    print_error "Failed to create backup"
    log_message "ERROR: Backup failed"
    exit 1
fi
echo ""

# Find files to refactor
print_header "Finding Files"
FILES=$(find "$TARGET_DIR" -type f \( -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" -o -name "*.py" -o -name "*.java" \) 2>/dev/null || true)

if [ -z "$FILES" ]; then
    print_warning "No files found to refactor"
    log_message "No files found"
    exit 0
fi

FILE_COUNT=$(echo "$FILES" | wc -l)
print_success "Found $FILE_COUNT file(s) to refactor"
log_message "Files found: $FILE_COUNT"
echo ""

# Display files
print_info "Files to be refactored:"
echo "$FILES" | head -20 | while read -r file; do
    echo "  - $file"
done

if [ "$FILE_COUNT" -gt 20 ]; then
    echo "  ... and $((FILE_COUNT - 20)) more files"
fi
echo ""

# Confirm before proceeding
read -p "Proceed with refactoring? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_warning "Refactoring cancelled"
    log_message "Refactoring cancelled by user"
    exit 0
fi
echo ""

# Refactor each file
print_header "Refactoring Files"
SUCCESS_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0

echo "$FILES" | while read -r file; do
    if [ ! -f "$file" ]; then
        continue
    fi
    
    echo -n "Processing: $file ... "
    log_message "Processing: $file"
    
    # Determine refactoring command based on type
    case $REFACTOR_TYPE in
        modernize)
            REFACTOR_CMD="bob \"Refactor $file to use modern language features and best practices while preserving all functionality\""
            ;;
        optimize)
            REFACTOR_CMD="bob \"Refactor $file to optimize for performance while preserving all functionality\""
            ;;
        cleanup)
            REFACTOR_CMD="bob \"Refactor $file to remove dead code and fix style issues\""
            ;;
        security)
            REFACTOR_CMD="bob \"Refactor $file to fix security vulnerabilities while preserving all functionality\""
            ;;
        *)
            print_error "Unknown refactor type"
            exit 1
            ;;
    esac
    
    # Execute refactoring
    if eval "$REFACTOR_CMD" > "${file}.tmp" 2>> "$LOG_FILE" && mv "${file}.tmp" "$file"; then
        print_success "Done"
        log_message "SUCCESS: $file"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        print_error "Failed"
        log_message "FAILED: $file"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        
        # Restore from backup on failure
        BACKUP_FILE="$BACKUP_DIR/$(basename "$TARGET_DIR")/$file"
        if [ -f "$BACKUP_FILE" ]; then
            cp "$BACKUP_FILE" "$file"
            log_message "Restored from backup: $file"
        fi
    fi
done

echo ""

# Generate refactoring report
print_header "Generating Report"
REPORT_FILE="./refactor-report-$(date +%Y%m%d_%H%M%S).md"

cat > "$REPORT_FILE" << EOF
# Batch Refactoring Report

**Date:** $(date)
**Refactor Type:** $REFACTOR_TYPE
**Target Directory:** $TARGET_DIR
**Backup Location:** $BACKUP_DIR

## Summary

- **Total Files:** $FILE_COUNT
- **Successfully Refactored:** $SUCCESS_COUNT
- **Failed:** $FAILED_COUNT
- **Skipped:** $SKIPPED_COUNT

## Refactoring Details

### Type: $REFACTOR_TYPE

EOF

case $REFACTOR_TYPE in
    modernize)
        cat >> "$REPORT_FILE" << EOF
**Modernization includes:**
- Updated to modern language features
- Converted callbacks to async/await
- Updated deprecated APIs
- Improved code structure
EOF
        ;;
    optimize)
        cat >> "$REPORT_FILE" << EOF
**Optimizations include:**
- Performance improvements
- Reduced complexity
- Optimized algorithms
- Better resource usage
EOF
        ;;
    cleanup)
        cat >> "$REPORT_FILE" << EOF
**Cleanup includes:**
- Removed dead code
- Fixed style issues
- Removed unused imports
- Improved code organization
EOF
        ;;
    security)
        cat >> "$REPORT_FILE" << EOF
**Security fixes include:**
- Fixed vulnerabilities
- Improved input validation
- Updated security practices
- Removed security risks
EOF
        ;;
esac

cat >> "$REPORT_FILE" << EOF

## Files Processed

EOF

echo "$FILES" | while read -r file; do
    echo "- $file" >> "$REPORT_FILE"
done

cat >> "$REPORT_FILE" << EOF

## Next Steps

1. **Review Changes:** Carefully review all refactored files
2. **Run Tests:** Execute your test suite to verify functionality
3. **Manual Testing:** Perform manual testing of critical features
4. **Code Review:** Have team members review the changes
5. **Commit Changes:** If everything looks good, commit the changes

## Backup Information

A complete backup of the original code is available at:
\`$BACKUP_DIR\`

To restore from backup if needed:
\`\`\`bash
cp -r $BACKUP_DIR/$(basename "$TARGET_DIR")/* $TARGET_DIR/
\`\`\`

## Logs

Detailed logs are available at: \`$LOG_FILE\`

---

*Generated by Bob Batch Refactoring Script*
EOF

print_success "Report generated: $REPORT_FILE"
log_message "Report generated: $REPORT_FILE"
echo ""

# Final summary
print_header "Refactoring Complete"
echo "Summary:"
echo "  Total Files: $FILE_COUNT"
echo "  Successful: $SUCCESS_COUNT"
echo "  Failed: $FAILED_COUNT"
echo ""
echo "Backup: $BACKUP_DIR"
echo "Report: $REPORT_FILE"
echo "Log: $LOG_FILE"
echo ""

if [ "$FAILED_COUNT" -gt 0 ]; then
    print_warning "$FAILED_COUNT file(s) failed refactoring"
    print_info "Failed files have been restored from backup"
    echo ""
fi

print_header "Important Next Steps"
echo "1. Review the changes in your code editor"
echo "2. Run your test suite:"
echo "   npm test  # or your test command"
echo "3. Manually test critical functionality"
echo "4. Review the report: $REPORT_FILE"
echo ""

if [ "$SUCCESS_COUNT" -gt 0 ]; then
    print_success "Refactoring completed successfully!"
    log_message "=== Batch Refactoring Completed Successfully ==="
    exit 0
else
    print_error "No files were successfully refactored"
    log_message "=== Batch Refactoring Failed ==="
    exit 1
fi

# Made with Bob
