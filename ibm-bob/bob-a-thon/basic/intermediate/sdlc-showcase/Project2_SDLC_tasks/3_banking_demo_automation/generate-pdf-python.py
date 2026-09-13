#!/usr/bin/env python3
"""
Generate PDF from AZURE_ARCHITECTURE.md using Python libraries
Requires: pip install markdown reportlab
"""

import sys
import os
from pathlib import Path

try:
    import markdown
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    from reportlab.pdfgen import canvas
except ImportError as e:
    print("❌ Error: Required Python packages not installed")
    print("")
    print("Install required packages:")
    print("  pip install markdown reportlab")
    print("")
    print(f"Missing: {e.name}")
    sys.exit(1)

def create_pdf():
    """Generate PDF from markdown file"""
    
    # Read markdown file
    md_file = Path("AZURE_ARCHITECTURE.md")
    if not md_file.exists():
        print(f"❌ Error: {md_file} not found")
        sys.exit(1)
    
    print(f"🔄 Reading {md_file}...")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Create PDF
    pdf_file = "AZURE_ARCHITECTURE.pdf"
    print(f"🔄 Generating {pdf_file}...")
    
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#1565C0',
        spaceAfter=30,
        alignment=TA_CENTER,
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor='#1565C0',
        spaceAfter=12,
        spaceBefore=12,
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='#2E7D32',
        spaceAfter=10,
        spaceBefore=10,
    )
    
    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor='#424242',
        spaceAfter=8,
        spaceBefore=8,
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        leftIndent=20,
        rightIndent=20,
        spaceAfter=10,
        spaceBefore=10,
        backColor='#f5f5f5',
    )
    
    # Add title
    elements.append(Paragraph("Azure Deployment Architecture", title_style))
    elements.append(Paragraph("Banking Demo Application", styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Process markdown content
    lines = md_content.split('\n')
    in_code_block = False
    code_lines = []
    
    for line in lines:
        # Handle code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                # End of code block
                if code_lines:
                    code_text = '\n'.join(code_lines)
                    elements.append(Preformatted(code_text, code_style))
                code_lines = []
                in_code_block = False
            else:
                # Start of code block
                in_code_block = True
            continue
        
        if in_code_block:
            code_lines.append(line)
            continue
        
        # Skip empty lines
        if not line.strip():
            elements.append(Spacer(1, 0.1*inch))
            continue
        
        # Handle headings
        if line.startswith('# '):
            text = line[2:].strip()
            elements.append(Paragraph(text, heading1_style))
        elif line.startswith('## '):
            text = line[3:].strip()
            elements.append(Paragraph(text, heading2_style))
        elif line.startswith('### '):
            text = line[4:].strip()
            elements.append(Paragraph(text, heading3_style))
        elif line.startswith('#### '):
            text = line[5:].strip()
            elements.append(Paragraph(text, styles['Heading4']))
        # Handle lists
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            elements.append(Paragraph(f"• {text}", styles['Normal']))
        elif line.strip().startswith('1. ') or line.strip().startswith('2. '):
            text = line.strip()[3:]
            elements.append(Paragraph(f"  {text}", styles['Normal']))
        # Handle tables (simplified)
        elif '|' in line and not line.strip().startswith('|---'):
            # Simple table row
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            row_text = ' | '.join(cells)
            elements.append(Paragraph(row_text, styles['Normal']))
        # Regular paragraphs
        else:
            # Clean up markdown formatting
            text = line.strip()
            text = text.replace('**', '<b>').replace('**', '</b>')
            text = text.replace('`', '<font face="Courier">')
            text = text.replace('`', '</font>')
            
            if text:
                elements.append(Paragraph(text, styles['Normal']))
    
    # Build PDF
    print("🔄 Building PDF...")
    doc.build(elements)
    
    # Check if file was created
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file)
        print(f"✅ PDF generated successfully: {pdf_file}")
        print(f"📄 File size: {file_size / 1024:.1f} KB")
        print(f"📍 Location: {os.path.abspath(pdf_file)}")
        print("")
        print(f"To view: open {pdf_file}")
    else:
        print("❌ PDF generation failed")
        sys.exit(1)

if __name__ == "__main__":
    try:
        create_pdf()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

# Made with Bob
