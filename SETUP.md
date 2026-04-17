# BVA Generator Agent - Setup Guide

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Navigate to the project directory:**
```bash
cd bva-generator-agent
```

2. **Create a virtual environment (recommended):**
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create necessary directories:**
```bash
mkdir -p reports templates
```

5. **Run the application:**
```bash
python main.py
```

## 📋 Configuration

### Client Configuration
Edit `config/client_config.yaml` to customize:
- Default report settings
- Brand colors and styling
- Export preferences
- Calculation parameters

### Formula Vault
Edit `config/formula_vault.yaml` to:
- Add custom formulas
- Update industry benchmarks
- Modify calculation methods

## 🔧 Advanced Setup

### Optional: PDF Export
For PDF export functionality, install additional dependencies:

**On macOS:**
```bash
pip install docx2pdf
```

**On Windows:**
```bash
pip install docx2pdf
```

**On Linux:**
```bash
# Install LibreOffice for conversion
sudo apt-get install libreoffice
pip install docx2pdf
```

### Optional: Enhanced Research
For enhanced company research capabilities, you can integrate:

1. **SEC EDGAR API** - For public company filings
2. **News APIs** - For sentiment analysis
   - NewsAPI: https://newsapi.org/
   - Google News API
3. **Company Data APIs**
   - Clearbit: https://clearbit.com/
   - Crunchbase: https://www.crunchbase.com/

Add API keys to a `.env` file:
```bash
NEWS_API_KEY=your_key_here
CLEARBIT_API_KEY=your_key_here
```

## 🎯 Usage

### Basic Workflow

1. **Start the application:**
```bash
python main.py
```

2. **Follow the interactive prompts:**
   - Enter client information (name, industry, product)
   - Provide optional details (ticker, website)
   - Review automated research findings
   - Enter project cost and timeline
   - Review calculated BVA results
   - Generate and export report

3. **Find your reports:**
   - Reports are saved in the `reports/` directory
   - Filename format: `BVA_CompanyName_YYYYMMDD_HHMMSS.docx`

### Testing Individual Components

**Test the Strategist Agent:**
```bash
python agents/strategist.py
```

**Test the Quant Agent:**
```bash
python agents/quant.py
```

**Test the Creative Director Agent:**
```bash
python agents/creative.py
```

**Test the Formula Engine:**
```bash
python utils/calculator.py
```

**Test the Report Generator:**
```bash
python utils/exporter.py
```

**Test the Web Scraper:**
```bash
python utils/scraper.py
```

## 🏗️ Project Structure

```
bva-generator-agent/
├── main.py                 # Main application entry point
├── config/
│   ├── client_config.yaml  # Client-specific configurations
│   └── formula_vault.yaml  # Industry formulas and benchmarks
├── agents/
│   ├── __init__.py
│   ├── strategist.py       # Company research and priority identification
│   ├── quant.py            # ROI calculations
│   └── creative.py         # Report generation and synthesis
├── utils/
│   ├── __init__.py
│   ├── scraper.py          # Web scraping utilities
│   ├── calculator.py       # Formula engine
│   └── exporter.py         # Word/PDF export
├── templates/              # Report templates (optional)
├── reports/                # Generated reports output
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── SETUP.md               # This file
```

## 🔍 Troubleshooting

### Import Errors
If you see import errors, ensure:
1. You're in the project root directory
2. Virtual environment is activated
3. All dependencies are installed: `pip install -r requirements.txt`

### PDF Conversion Issues
If PDF conversion fails:
1. Check if docx2pdf is installed: `pip list | grep docx2pdf`
2. On Linux, ensure LibreOffice is installed
3. Alternatively, manually convert the Word document to PDF

### Web Scraping Issues
If research fails:
1. Check your internet connection
2. Some sites may block automated requests
3. Consider adding API keys for enhanced research

### Missing Reports Directory
If reports aren't saving:
```bash
mkdir -p reports
```

## 🎨 Customization

### Adding Custom Industries
Edit `config/formula_vault.yaml` and add your industry:

```yaml
industry_benchmarks:
  your_industry:
    average_fte_hourly_rate: 60
    custom_metric: 1000
```

### Adding Custom Formulas
Add to the appropriate vault in `formula_vault.yaml`:

```yaml
efficiency_vault:
  your_custom_formula:
    name: "Your Formula Name"
    formula: "variable1 * variable2"
    variables:
      - variable1: "Description"
      - variable2: "Description"
    unit: "USD annually"
```

### Customizing Report Template
Modify the report generation in `utils/exporter.py`:
- Change colors in `_setup_styles()`
- Modify sections in `create_bva_report()`
- Add custom branding

## 📚 Additional Resources

- **IBM Value Engineering:** https://www.ibm.com/services/value-engineering
- **ROI Calculation Best Practices:** Industry-standard methodologies
- **Python Documentation:** https://docs.python.org/3/

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the README.md for architecture details
3. Test individual components to isolate issues
4. Check Python and dependency versions

## 🔄 Updates

To update the project:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## 📝 License

MIT License - See LICENSE file for details