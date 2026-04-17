# BVA Generator Agent

A modular, scalable Business Value Assessment (BVA) generator that works across IBM's entire portfolio. This system uses a multi-agent architecture to research companies, identify business priorities, calculate ROI, and generate professional reports.

## 🏗️ Architecture

The system is built on three distinct layers:

### 1. Input Layer (Agnostic Data Ingestion)
- **Company Context Scraper**: Analyzes 10-K filings and investor relations pages
- **Discovery Interface**: Interactive chat-based interview system
- **Value Vector Identification**: Identifies CEO's top 3 priorities

### 2. Logic Layer (Formula Vault)
- **Efficiency Vault**: Time and cost savings calculations
- **Risk Vault**: Risk mitigation and downtime cost analysis
- **Growth Vault**: Revenue acceleration and market expansion metrics

### 3. Synthesis Layer (Executive Translator)
- Maps technical savings to CEO priorities
- Generates board-ready executive summaries
- Customizes output to client's brand and tone

## 🤖 Multi-Agent System

| Agent | Function |
|-------|----------|
| **Strategist Agent** | Identifies value pillars from public filings |
| **Telemetry Agent** | Pulls friction metrics from connected systems |
| **Quant Agent** | Applies industry benchmarks and calculations |
| **Creative Director** | Packages output in client's brand style |

## 🚀 Features

- **Dynamic Research**: Automatically scrapes company data and industry benchmarks
- **Interactive Input**: Chat-based interface for gathering client information
- **Modular Calculations**: Industry-agnostic formula system
- **Professional Reports**: Export to Word (.docx) and PDF formats
- **Scalable Design**: Configuration-driven for easy expansion

## 📦 Installation

```bash
# Clone the repository
cd bva-generator-agent

# Install dependencies
pip install -r requirements.txt
```

## 🎯 Usage

### Option 1: Web Dashboard (Recommended)

```bash
# Launch interactive web dashboard
streamlit run dashboard.py
```

Features:
- 🎨 Modern web interface
- 📊 Interactive visualizations
- 📈 Real-time progress tracking
- 💾 One-click report download

### Option 2: Command Line Interface

```bash
# Run CLI version
python main.py
```

The system will guide you through:
1. Client information input (name, industry, product)
2. Automated company research
3. Business priority identification
4. KPI calculation
5. Report generation and export

## 📁 Project Structure

```
bva-generator-agent/
├── main.py                 # CLI application entry point
├── dashboard.py            # Web dashboard (Streamlit)
├── config/
│   ├── client_config.yaml  # Client-specific configurations
│   └── formula_vault.yaml  # Industry formulas and benchmarks
├── agents/
│   ├── strategist.py       # Company research and priority identification
│   ├── quant.py            # ROI calculations
│   └── creative.py         # Report generation and synthesis
├── utils/
│   ├── scraper.py          # Web scraping utilities
│   ├── calculator.py       # Formula engine
│   └── exporter.py         # Word/PDF export
├── reports/                # Generated reports output
├── README.md               # Project overview
├── SETUP.md                # Installation guide
├── DASHBOARD.md            # Dashboard documentation
├── EXAMPLE_USAGE.md        # Usage examples
└── QUICK_START.md          # Quick start guide
```

## 🔧 Configuration

Edit `config/client_config.yaml` to customize for different clients and industries.

## 📄 License

MIT License