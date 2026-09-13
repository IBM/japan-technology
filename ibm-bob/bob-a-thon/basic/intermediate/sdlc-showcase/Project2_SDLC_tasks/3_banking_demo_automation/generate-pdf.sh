#!/bin/bash

# Script to generate PDF from Azure Architecture markdown
# Requires: pandoc and texlive (for PDF generation)

set -e

echo "🔄 Generating PDF from AZURE_ARCHITECTURE.md..."

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "❌ Error: pandoc is not installed"
    echo ""
    echo "Install pandoc:"
    echo "  macOS:   brew install pandoc"
    echo "  Ubuntu:  sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended"
    echo "  Windows: choco install pandoc miktex"
    exit 1
fi

# Check if pdflatex is available (for better PDF output)
if command -v pdflatex &> /dev/null; then
    echo "✅ Using pdflatex engine for high-quality PDF"
    ENGINE="--pdf-engine=pdflatex"
else
    echo "⚠️  pdflatex not found, using default engine"
    echo "   For better output, install: brew install basictex (macOS) or texlive (Linux)"
    ENGINE=""
fi

# Generate PDF
pandoc AZURE_ARCHITECTURE.md \
    -o AZURE_ARCHITECTURE.pdf \
    $ENGINE \
    --variable geometry:margin=1in \
    --variable fontsize=11pt \
    --variable colorlinks=true \
    --variable linkcolor=blue \
    --variable urlcolor=blue \
    --toc \
    --toc-depth=2 \
    --highlight-style=tango \
    --metadata title="Azure Deployment Architecture" \
    --metadata subtitle="Banking Demo Application" \
    --metadata author="Banking Demo Team" \
    --metadata date="$(date +%Y-%m-%d)" \
    2>/dev/null || {
        echo "❌ PDF generation failed"
        echo ""
        echo "Trying alternative method with wkhtmltopdf..."
        
        if command -v wkhtmltopdf &> /dev/null; then
            # Convert markdown to HTML first, then to PDF
            pandoc AZURE_ARCHITECTURE.md -o AZURE_ARCHITECTURE.html
            wkhtmltopdf AZURE_ARCHITECTURE.html AZURE_ARCHITECTURE.pdf
            rm AZURE_ARCHITECTURE.html
            echo "✅ PDF generated using wkhtmltopdf"
        else
            echo "❌ wkhtmltopdf also not available"
            echo ""
            echo "Alternative: Use online converter"
            echo "  1. Visit: https://www.markdowntopdf.com/"
            echo "  2. Upload: AZURE_ARCHITECTURE.md"
            echo "  3. Download the PDF"
            exit 1
        fi
    }

if [ -f "AZURE_ARCHITECTURE.pdf" ]; then
    echo "✅ PDF generated successfully: AZURE_ARCHITECTURE.pdf"
    echo ""
    echo "📄 File size: $(du -h AZURE_ARCHITECTURE.pdf | cut -f1)"
    echo "📍 Location: $(pwd)/AZURE_ARCHITECTURE.pdf"
    echo ""
    echo "To view: open AZURE_ARCHITECTURE.pdf"
else
    echo "❌ PDF generation failed"
    exit 1
fi

# Made with Bob
