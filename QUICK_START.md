# 🚀 Quick Start Guide

Get your BVA Generator up and running in 5 minutes!

## ⚡ Installation (2 minutes)

```bash
# 1. Navigate to project
cd bva-generator-agent

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 🎯 Run Your First BVA (3 minutes)

```bash
python main.py
```

Follow the prompts:
1. **Company Name:** Enter your client's name
2. **Industry:** Select from the list
3. **IBM Solution:** Choose the product
4. **Project Cost:** Enter estimated cost
5. **Review & Generate:** Confirm and generate report

## 📄 Find Your Report

Reports are saved in: `reports/BVA_CompanyName_YYYYMMDD_HHMMSS.docx`

## 🎨 Key Features

✅ **Automated Research** - Scrapes company data and industry benchmarks  
✅ **Dynamic Calculations** - Industry-specific ROI formulas  
✅ **Professional Reports** - Word & PDF export  
✅ **Multi-Agent System** - Strategist, Quant, and Creative Director agents  
✅ **Scalable Design** - Configuration-driven for easy customization  

## 🔧 Customization

### Add Your Industry
Edit `config/formula_vault.yaml`:
```yaml
industry_benchmarks:
  your_industry:
    average_fte_hourly_rate: 60
    custom_metric: 1000
```

### Modify Formulas
Add custom calculations to any vault in `formula_vault.yaml`

### Brand Your Reports
Edit colors and styling in `utils/exporter.py`

## 📚 Documentation

- **[README.md](README.md)** - Full architecture and features
- **[SETUP.md](SETUP.md)** - Detailed installation guide
- **[EXAMPLE_USAGE.md](EXAMPLE_USAGE.md)** - Complete walkthrough

## 🆘 Troubleshooting

**Import errors?**
```bash
pip install -r requirements.txt
```

**PDF conversion fails?**
```bash
pip install docx2pdf
```

**Missing reports directory?**
```bash
mkdir -p reports
```

## 💡 Pro Tips

1. Provide stock ticker for enhanced research
2. Use realistic project costs for accurate ROI
3. Review and customize generated reports
4. Save configurations for repeat clients
5. Test individual agents with their test functions

## 🎓 Learn More

Run individual agent tests:
```bash
python agents/strategist.py  # Test research
python agents/quant.py       # Test calculations
python agents/creative.py    # Test report generation
```

## 📞 Support

Check the troubleshooting section in [SETUP.md](SETUP.md) for common issues.

---

**Ready to generate your first BVA?** Run `python main.py` now! 🚀