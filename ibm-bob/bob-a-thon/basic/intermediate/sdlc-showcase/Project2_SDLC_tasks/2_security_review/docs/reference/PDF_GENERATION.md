# PDF Generation Guide

This guide explains how to generate a PDF from the Azure Architecture documentation.

## Option 1: Using Pandoc (Recommended)

### Install Pandoc

**macOS:**
```bash
brew install pandoc basictex
```

**Ubuntu/Debian:**
```bash
sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended
```

**Windows:**
```bash
choco install pandoc miktex
```

### Generate PDF

```bash
cd banking-demo
./generate-pdf.sh
```

This will create `AZURE_ARCHITECTURE.pdf` with:
- Table of contents
- Syntax highlighting
- Clickable links
- Professional formatting

---

## Option 2: Using Python (Alternative)

### Install Python Dependencies

```bash
pip install markdown reportlab
```

### Generate PDF

```bash
cd banking-demo
python3 generate-pdf-python.py
```

---

## Option 3: Online Converters (No Installation)

### Method A: Markdown to PDF
1. Visit: https://www.markdowntopdf.com/
2. Upload: `AZURE_ARCHITECTURE.md`
3. Click "Convert"
4. Download the PDF

### Method B: GitHub + Print to PDF
1. Push `AZURE_ARCHITECTURE.md` to GitHub
2. View the file on GitHub (it renders markdown)
3. Use browser's "Print to PDF" feature

### Method C: VS Code Extension
1. Install "Markdown PDF" extension in VS Code
2. Open `AZURE_ARCHITECTURE.md`
3. Right-click → "Markdown PDF: Export (pdf)"

---

## Option 4: Using Docker (No Local Installation)

```bash
cd banking-demo

# Run pandoc in Docker container
docker run --rm \
  -v "$(pwd):/data" \
  pandoc/latex:latest \
  AZURE_ARCHITECTURE.md \
  -o AZURE_ARCHITECTURE.pdf \
  --toc \
  --variable geometry:margin=1in
```

---

## Option 5: Manual Export from Markdown Viewer

### Using Typora (Recommended for Best Results)
1. Download Typora: https://typora.io/
2. Open `AZURE_ARCHITECTURE.md`
3. File → Export → PDF
4. Choose export settings
5. Save as `AZURE_ARCHITECTURE.pdf`

### Using Marked 2 (macOS)
1. Download Marked 2: https://marked2app.com/
2. Open `AZURE_ARCHITECTURE.md`
3. File → Print → Save as PDF

---

## Troubleshooting

### Pandoc: "pdflatex not found"
Install LaTeX distribution:
- **macOS**: `brew install basictex`
- **Ubuntu**: `sudo apt-get install texlive-latex-base`
- **Windows**: Install MiKTeX from https://miktex.org/

### Python: "No module named 'reportlab'"
```bash
pip install reportlab markdown
```

### Docker: Permission denied
```bash
# On Linux/macOS, add user permissions
docker run --rm \
  -v "$(pwd):/data" \
  -u $(id -u):$(id -g) \
  pandoc/latex:latest \
  AZURE_ARCHITECTURE.md \
  -o AZURE_ARCHITECTURE.pdf
```

---

## Quick Comparison

| Method | Quality | Speed | Installation |
|--------|---------|-------|--------------|
| Pandoc + LaTeX | ⭐⭐⭐⭐⭐ | Fast | Medium |
| Python Script | ⭐⭐⭐ | Fast | Easy |
| Online Converter | ⭐⭐⭐⭐ | Medium | None |
| VS Code Extension | ⭐⭐⭐⭐ | Fast | Easy |
| Docker | ⭐⭐⭐⭐⭐ | Medium | Easy |
| Typora | ⭐⭐⭐⭐⭐ | Fast | Medium |

---

## Recommended Workflow

**For Development:**
```bash
# Quick preview
./generate-pdf.sh
```

**For Production/Presentation:**
1. Use Typora or Pandoc with LaTeX
2. Customize styling if needed
3. Review output carefully
4. Share PDF with stakeholders

---

## Custom Styling (Advanced)

### Pandoc with Custom CSS

Create `custom.css`:
```css
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
}

h1 {
    color: #1565C0;
    border-bottom: 2px solid #1565C0;
}

h2 {
    color: #2E7D32;
}

code {
    background-color: #f5f5f5;
    padding: 2px 4px;
    border-radius: 3px;
}
```

Generate with custom styling:
```bash
pandoc AZURE_ARCHITECTURE.md \
  -o AZURE_ARCHITECTURE.pdf \
  --css=custom.css \
  --toc \
  --variable geometry:margin=1in
```

---

## Files

- **AZURE_ARCHITECTURE.md** - Source markdown file (368 lines)
- **generate-pdf.sh** - Bash script for pandoc
- **generate-pdf-python.py** - Python script alternative
- **AZURE_ARCHITECTURE.pdf** - Generated PDF (created after running script)

---

## Support

If you encounter issues:
1. Check that the markdown file exists
2. Verify tool installation: `pandoc --version` or `python3 --version`
3. Try alternative methods listed above
4. Check file permissions

For best results, use **Pandoc with LaTeX** or **Typora**.