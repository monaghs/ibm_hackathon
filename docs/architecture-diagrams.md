# BVA Agent Architecture Diagrams

This document contains Mermaid-based architecture diagrams for the BVA Generator Agent system.

## 1. System Context

```mermaid
flowchart LR
    User["User / IBM Seller / Consultant"]
    CLI["CLI App<br/>main.py"]
    Dashboard["Web Dashboard<br/>dashboard.py"]
    Strategist["Strategist Agent"]
    Quant["Quant Agent"]
    Creative["Creative Director Agent"]
    Scraper["CompanyResearcher<br/>utils/scraper.py"]
    Calculator["FormulaEngine<br/>utils/calculator.py"]
    Exporter["ReportGenerator<br/>utils/exporter.py"]
    ClientConfig["Client Config<br/>config/client_config.yaml"]
    FormulaVault["Formula Vault<br/>config/formula_vault.yaml"]
    Reports["Generated Reports<br/>reports/"]
    ExternalWeb["External Web Sources<br/>Google / SEC / IR / News"]

    User --> CLI
    User --> Dashboard

    CLI --> Strategist
    CLI --> Quant
    CLI --> Creative

    Dashboard --> Strategist
    Dashboard --> Quant
    Dashboard --> Creative

    Strategist --> Scraper
    Scraper --> ExternalWeb

    Quant --> Calculator
    Calculator --> FormulaVault

    Creative --> Exporter
    Exporter --> Reports

    CLI --> ClientConfig
    Dashboard --> ClientConfig
```

## 2. Agent Orchestration Flow

```mermaid
sequenceDiagram
    actor User
    participant Entry as CLI / Dashboard
    participant S as StrategistAgent
    participant R as CompanyResearcher
    participant Q as QuantAgent
    participant F as FormulaEngine
    participant C as CreativeDirectorAgent
    participant E as ReportGenerator

    User->>Entry: Enter client + solution details
    Entry->>S: analyze_company(company, industry, ticker, website)
    S->>R: comprehensive_research(...)
    R-->>S: research_results + value_pillars
    S-->>Entry: strategic_analysis + friction_points + recommendations

    Entry->>Q: calculate_bva(client_data, friction_points, project_cost, years)
    Q->>F: get_all_industry_benchmarks(industry)
    F-->>Q: industry benchmarks
    Q->>F: calculate efficiency/risk/growth formulas
    F-->>Q: calculation results
    Q->>F: calculate_comprehensive_bva(...)
    F-->>Q: ROI + payback + value breakdown
    Q-->>Entry: bva_results

    Entry->>C: synthesize_bva(client_data, strategic_analysis, bva_results)
    C-->>Entry: executive narrative + recommendations + visualizations

    Entry->>C: generate_report(...)
    C->>E: create_bva_report(...)
    E-->>C: report file paths
    C-->>Entry: generated report artifacts
    Entry-->>User: BVA outputs + downloadable reports
```

## 3. Layered Internal Architecture

```mermaid
flowchart TB
    subgraph Presentation["Presentation Layer"]
        CLI["CLI Experience<br/>main.py"]
        UI["Streamlit Dashboard<br/>dashboard.py"]
    end

    subgraph Orchestration["Application / Orchestration Layer"]
        App["BVAGeneratorApp"]
        Session["Streamlit Session State + Step Logic"]
    end

    subgraph Agents["Agent Layer"]
        Strategist["StrategistAgent"]
        Quant["QuantAgent"]
        Creative["CreativeDirectorAgent"]
    end

    subgraph Services["Service / Utility Layer"]
        Research["CompanyResearcher"]
        Formula["FormulaEngine"]
        Report["ReportGenerator"]
    end

    subgraph Config["Configuration Layer"]
        Client["client_config.yaml"]
        Vault["formula_vault.yaml"]
    end

    subgraph Outputs["Output Layer"]
        Docs["Word / PDF Reports"]
        Insights["Executive Narrative + KPI Tables + Charts"]
    end

    CLI --> App
    UI --> Session

    App --> Strategist
    App --> Quant
    App --> Creative

    Session --> Strategist
    Session --> Quant
    Session --> Creative

    Strategist --> Research
    Quant --> Formula
    Creative --> Report

    App --> Client
    Session --> Client
    Formula --> Vault

    Creative --> Insights
    Report --> Docs
```

## 4. Research and Value Pipeline

```mermaid
flowchart LR
    Input["Client Inputs<br/>company, industry, product, ticker, website"]
    Research["Research Aggregation<br/>CompanyResearcher.comprehensive_research()"]
    Sources["Source Modules<br/>company info / SEC filings / investor relations / benchmarks / news"]
    Pillars["Strategic Output<br/>value pillars, opportunities, friction points"]
    Calc["Quantification<br/>efficiency + risk + growth calculations"]
    BVA["BVA Summary<br/>annual value, ROI, payback, breakdown"]
    Synthesis["Executive Synthesis<br/>priority mapping + narrative + recommendations"]
    Report["Report Export<br/>.docx / optional PDF"]

    Input --> Research
    Research --> Sources
    Sources --> Pillars
    Pillars --> Calc
    Calc --> BVA
    BVA --> Synthesis
    Synthesis --> Report
```

## Notes

- The primary entry points are [`main.py`](../main.py) and [`dashboard.py`](../dashboard.py).
- The core agents are [`StrategistAgent`](../agents/strategist.py), [`QuantAgent`](../agents/quant.py), and [`CreativeDirectorAgent`](../agents/creative.py).
- Supporting services are [`CompanyResearcher`](../utils/scraper.py), [`FormulaEngine`](../utils/calculator.py), and [`ReportGenerator`](../utils/exporter.py).
- The formulas and benchmarks are loaded from [`formula_vault.yaml`](../config/formula_vault.yaml).