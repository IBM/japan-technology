#!/bin/bash
################################################################################
# Documentation Generation Script
#
# This script automatically generates comprehensive documentation for your
# codebase using Bob's AI capabilities.
#
# Usage:
#   ./generate-docs.sh [source-directory] [output-directory] [doc-type]
#
# Parameters:
#   source-directory  - Directory containing source code (default: .)
#   output-directory  - Directory for generated docs (default: ./docs)
#   doc-type         - Documentation format: markdown, html (default: markdown)
#
# Example:
#   ./generate-docs.sh ./src ./documentation markdown
#   ./generate-docs.sh . ./docs html
################################################################################

set -e  # Exit on error

# Configuration
SOURCE_DIR="${1:-.}"
OUTPUT_DIR="${2:-./docs}"
DOC_TYPE="${3:-markdown}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="./doc-generation-$TIMESTAMP.log"

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

# Validate parameters
if [ ! -d "$SOURCE_DIR" ]; then
    print_error "Source directory not found: $SOURCE_DIR"
    exit 1
fi

if [[ ! "$DOC_TYPE" =~ ^(markdown|html)$ ]]; then
    print_error "Invalid doc type: $DOC_TYPE (must be 'markdown' or 'html')"
    exit 1
fi

# Check if Bob CLI is installed
if ! command -v bob &> /dev/null; then
    print_error "Bob CLI is not installed"
    echo "Install it with: npm install -g @ibm/bob-cli"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Start logging
log_message "=== Documentation Generation Started ==="
log_message "Source Directory: $SOURCE_DIR"
log_message "Output Directory: $OUTPUT_DIR"
log_message "Documentation Type: $DOC_TYPE"

print_header "Documentation Generation"
echo "Source: $SOURCE_DIR"
echo "Output: $OUTPUT_DIR"
echo "Format: $DOC_TYPE"
echo "Log: $LOG_FILE"
echo ""

# Determine file extension
if [ "$DOC_TYPE" = "markdown" ]; then
    EXT="md"
else
    EXT="html"
fi

# Generate API Documentation
print_header "Generating API Documentation"
API_DOC="$OUTPUT_DIR/api.$EXT"
echo -n "Creating API documentation ... "
log_message "Generating API documentation"

if bob "Generate comprehensive API documentation for the code in $SOURCE_DIR in $DOC_TYPE format" > "$API_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: API documentation created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: API documentation failed"
fi
echo ""

# Generate Architecture Documentation
print_header "Generating Architecture Documentation"
ARCH_DOC="$OUTPUT_DIR/architecture.$EXT"
echo -n "Creating architecture documentation ... "
log_message "Generating architecture documentation"

if bob "Create architecture documentation for $SOURCE_DIR explaining the system design, components, and data flow in $DOC_TYPE format" > "$ARCH_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: Architecture documentation created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: Architecture documentation failed"
fi
echo ""

# Generate Usage Examples
print_header "Generating Usage Examples"
EXAMPLES_DOC="$OUTPUT_DIR/examples.$EXT"
echo -n "Creating usage examples ... "
log_message "Generating usage examples"

if bob "Create comprehensive usage examples for all public functions and classes in $SOURCE_DIR with code snippets and explanations" > "$EXAMPLES_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: Usage examples created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: Usage examples failed"
fi
echo ""

# Generate README
print_header "Generating README"
README_DOC="$OUTPUT_DIR/README.md"
echo -n "Creating README ... "
log_message "Generating README"

if bob "Create a comprehensive README for the project in $SOURCE_DIR including:
- Project overview and description
- Installation instructions
- Usage guide with examples
- API reference summary
- Configuration options
- Contributing guidelines
- License information
Format as professional GitHub README with badges and sections" > "$README_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: README created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: README failed"
fi
echo ""

# Generate Changelog (if git repository)
if [ -d ".git" ]; then
    print_header "Generating Changelog"
    CHANGELOG_DOC="$OUTPUT_DIR/CHANGELOG.md"
    echo -n "Creating changelog from git history ... "
    log_message "Generating changelog"
    
    if bob "Create a detailed changelog from git history following Keep a Changelog format with:
- Version numbers
- Release dates
- Added, Changed, Deprecated, Removed, Fixed, Security sections
- Commit messages organized by category" > "$CHANGELOG_DOC" 2>> "$LOG_FILE"; then
        print_success "Done"
        log_message "SUCCESS: Changelog created"
    else
        print_warning "Failed (continuing)"
        log_message "WARNING: Changelog failed"
    fi
    echo ""
fi

# Generate Contributing Guide
print_header "Generating Contributing Guide"
CONTRIBUTING_DOC="$OUTPUT_DIR/CONTRIBUTING.md"
echo -n "Creating contributing guide ... "
log_message "Generating contributing guide"

if bob "Create a CONTRIBUTING.md file with:
- How to set up development environment
- Code style guidelines
- Testing requirements
- Pull request process
- Code review guidelines
- Community guidelines" > "$CONTRIBUTING_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: Contributing guide created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: Contributing guide failed"
fi
echo ""

# Generate Code of Conduct
print_header "Generating Code of Conduct"
CODE_OF_CONDUCT_DOC="$OUTPUT_DIR/CODE_OF_CONDUCT.md"
echo -n "Creating code of conduct ... "
log_message "Generating code of conduct"

if bob "Create a CODE_OF_CONDUCT.md following the Contributor Covenant standard" > "$CODE_OF_CONDUCT_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: Code of conduct created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: Code of conduct failed"
fi
echo ""

# Generate Troubleshooting Guide
print_header "Generating Troubleshooting Guide"
TROUBLESHOOTING_DOC="$OUTPUT_DIR/troubleshooting.$EXT"
echo -n "Creating troubleshooting guide ... "
log_message "Generating troubleshooting guide"

if bob "Analyze the code in $SOURCE_DIR and create a troubleshooting guide with:
- Common issues and solutions
- Error messages and fixes
- Configuration problems
- Performance issues
- Debugging tips" > "$TROUBLESHOOTING_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: Troubleshooting guide created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: Troubleshooting guide failed"
fi
echo ""

# Generate FAQ
print_header "Generating FAQ"
FAQ_DOC="$OUTPUT_DIR/faq.$EXT"
echo -n "Creating FAQ ... "
log_message "Generating FAQ"

if bob "Create a comprehensive FAQ for the project in $SOURCE_DIR covering:
- Installation questions
- Usage questions
- Configuration questions
- Common problems
- Best practices" > "$FAQ_DOC" 2>> "$LOG_FILE"; then
    print_success "Done"
    log_message "SUCCESS: FAQ created"
else
    print_warning "Failed (continuing)"
    log_message "WARNING: FAQ failed"
fi
echo ""

# Generate Index Page (if HTML)
if [ "$DOC_TYPE" = "html" ]; then
    print_header "Generating Index Page"
    INDEX_DOC="$OUTPUT_DIR/index.html"
    echo -n "Creating index page ... "
    log_message "Generating index page"
    
    cat > "$INDEX_DOC" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Documentation</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        header {
            background: #2c3e50;
            color: white;
            padding: 2rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }
        h1 { margin: 0; }
        .subtitle { opacity: 0.8; margin-top: 0.5rem; }
        .docs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .doc-card {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .doc-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        .doc-card h2 {
            margin-top: 0;
            color: #2c3e50;
        }
        .doc-card p {
            color: #666;
            margin-bottom: 1rem;
        }
        .doc-card a {
            color: #3498db;
            text-decoration: none;
            font-weight: 500;
        }
        .doc-card a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 3rem;
            text-align: center;
            color: #666;
            padding: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>📚 Project Documentation</h1>
        <p class="subtitle">Comprehensive documentation generated by Bob AI</p>
    </header>
    
    <div class="docs-grid">
        <div class="doc-card">
            <h2>🚀 Getting Started</h2>
            <p>Learn how to install and set up the project</p>
            <a href="README.md">Read README →</a>
        </div>
        
        <div class="doc-card">
            <h2>📖 API Reference</h2>
            <p>Complete API documentation with examples</p>
            <a href="api.html">View API Docs →</a>
        </div>
        
        <div class="doc-card">
            <h2>🏗️ Architecture</h2>
            <p>System architecture and design decisions</p>
            <a href="architecture.html">View Architecture →</a>
        </div>
        
        <div class="doc-card">
            <h2>💡 Examples</h2>
            <p>Usage examples and code snippets</p>
            <a href="examples.html">View Examples →</a>
        </div>
        
        <div class="doc-card">
            <h2>🔧 Troubleshooting</h2>
            <p>Common issues and solutions</p>
            <a href="troubleshooting.html">View Guide →</a>
        </div>
        
        <div class="doc-card">
            <h2>❓ FAQ</h2>
            <p>Frequently asked questions</p>
            <a href="faq.html">View FAQ →</a>
        </div>
        
        <div class="doc-card">
            <h2>🤝 Contributing</h2>
            <p>How to contribute to the project</p>
            <a href="CONTRIBUTING.md">Contributing Guide →</a>
        </div>
        
        <div class="doc-card">
            <h2>📝 Changelog</h2>
            <p>Version history and changes</p>
            <a href="CHANGELOG.md">View Changelog →</a>
        </div>
    </div>
    
    <footer>
        <p>Generated on $(date) by Bob Documentation Generator</p>
    </footer>
</body>
</html>
EOF
    
    print_success "Done"
    log_message "SUCCESS: Index page created"
    echo ""
fi

# Generate Documentation Summary
print_header "Generating Summary"
SUMMARY_FILE="$OUTPUT_DIR/documentation-summary.md"

cat > "$SUMMARY_FILE" << EOF
# Documentation Generation Summary

**Generated:** $(date)
**Source Directory:** $SOURCE_DIR
**Output Directory:** $OUTPUT_DIR
**Format:** $DOC_TYPE

## Generated Documents

EOF

# List all generated files
for doc in "$OUTPUT_DIR"/*; do
    if [ -f "$doc" ]; then
        filename=$(basename "$doc")
        filesize=$(du -h "$doc" | cut -f1)
        echo "- [$filename](./$filename) ($filesize)" >> "$SUMMARY_FILE"
    fi
done

cat >> "$SUMMARY_FILE" << EOF

## Documentation Structure

\`\`\`
$OUTPUT_DIR/
├── README.md              # Project overview and getting started
├── api.$EXT               # API reference documentation
├── architecture.$EXT      # System architecture
├── examples.$EXT          # Usage examples
├── troubleshooting.$EXT   # Troubleshooting guide
├── faq.$EXT              # Frequently asked questions
├── CONTRIBUTING.md        # Contributing guidelines
├── CODE_OF_CONDUCT.md     # Code of conduct
└── CHANGELOG.md           # Version history
EOF

if [ "$DOC_TYPE" = "html" ]; then
    echo "└── index.html             # Documentation homepage" >> "$SUMMARY_FILE"
fi

cat >> "$SUMMARY_FILE" << EOF
\`\`\`

## Next Steps

1. **Review Documentation:** Check all generated files for accuracy
2. **Customize Content:** Add project-specific details where needed
3. **Add Images:** Include diagrams and screenshots
4. **Update Links:** Ensure all internal links work correctly
5. **Publish:** Deploy documentation to your hosting platform

## Viewing Documentation

EOF

if [ "$DOC_TYPE" = "html" ]; then
    cat >> "$SUMMARY_FILE" << EOF
Open \`index.html\` in your browser:
\`\`\`bash
open $OUTPUT_DIR/index.html
# or
python -m http.server 8000 --directory $OUTPUT_DIR
# Then visit http://localhost:8000
\`\`\`
EOF
else
    cat >> "$SUMMARY_FILE" << EOF
View markdown files in your editor or use a markdown viewer:
\`\`\`bash
# Using grip (GitHub-flavored markdown viewer)
grip $OUTPUT_DIR/README.md

# Or open in VS Code
code $OUTPUT_DIR
\`\`\`
EOF
fi

cat >> "$SUMMARY_FILE" << EOF

## Maintenance

Keep documentation up to date by:
- Running this script after major changes
- Updating examples when APIs change
- Reviewing and updating troubleshooting guides
- Maintaining the changelog

---

*Generated by Bob Documentation Generator*
*Log file: $LOG_FILE*
EOF

print_success "Summary created: $SUMMARY_FILE"
log_message "Summary created"
echo ""

# Final summary
print_header "Documentation Generation Complete"
echo "Output directory: $OUTPUT_DIR"
echo "Summary: $SUMMARY_FILE"
echo "Log: $LOG_FILE"
echo ""

# Count generated files
DOC_COUNT=$(find "$OUTPUT_DIR" -type f | wc -l)
print_success "Generated $DOC_COUNT documentation file(s)"
echo ""

if [ "$DOC_TYPE" = "html" ]; then
    print_info "To view documentation, open: $OUTPUT_DIR/index.html"
else
    print_info "To view documentation, open: $OUTPUT_DIR/README.md"
fi

log_message "=== Documentation Generation Completed ==="
log_message "Generated $DOC_COUNT files"

exit 0

# Made with Bob
