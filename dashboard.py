"""
BVA Generator Dashboard
Interactive web-based interface using Streamlit
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

# Import agents
from agents.strategist import StrategistAgent
from agents.quant import QuantAgent
from agents.creative import CreativeDirectorAgent

# Page configuration
st.set_page_config(
    page_title="BVA Generator Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #0F62FE;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #0F62FE;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
    }
    .info-box {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #17a2b8;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables"""
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'client_data' not in st.session_state:
        st.session_state.client_data = {}
    if 'strategic_results' not in st.session_state:
        st.session_state.strategic_results = None
    if 'bva_results' not in st.session_state:
        st.session_state.bva_results = None
    if 'synthesis' not in st.session_state:
        st.session_state.synthesis = None
    if 'report_paths' not in st.session_state:
        st.session_state.report_paths = None


def render_header():
    """Render dashboard header"""
    st.markdown('<h1 class="main-header">📊 BVA Generator Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("---")


def render_sidebar():
    """Render sidebar with navigation and progress"""
    with st.sidebar:
        st.image("https://www.ibm.com/brand/experience-guides/developer/b1db1ae501d522a1a4b49613fe07c9f1/01_8-bar-positive.svg", width=150)
        st.title("Navigation")
        
        # Progress indicator
        st.markdown("### Progress")
        progress_steps = [
            "Client Info",
            "Research",
            "Calculations",
            "Report"
        ]
        
        for i, step_name in enumerate(progress_steps, 1):
            if i < st.session_state.step:
                st.markdown(f"✅ {step_name}")
            elif i == st.session_state.step:
                st.markdown(f"🔵 **{step_name}**")
            else:
                st.markdown(f"⚪ {step_name}")
        
        st.markdown("---")
        
        # Quick actions
        st.markdown("### Quick Actions")
        if st.button("🔄 Start New BVA"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        if st.button("📚 View Documentation"):
            st.markdown("[README](README.md) | [Setup Guide](SETUP.md)")
        
        st.markdown("---")
        st.markdown("### About")
        st.info("**BVA Generator v1.0**\n\nPowered by Multi-Agent AI System")


def step1_client_info():
    """Step 1: Gather client information"""
    st.header("📝 Step 1: Client Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        company_name = st.text_input(
            "Company Name *",
            value=st.session_state.client_data.get('name', ''),
            placeholder="e.g., Acme Corporation"
        )
        
        industry = st.selectbox(
            "Industry *",
            options=[
                "Manufacturing",
                "Retail",
                "Financial Services",
                "Healthcare",
                "Technology",
                "Telecommunications",
                "Other"
            ],
            index=0 if not st.session_state.client_data.get('industry') else None
        )
        
        if industry == "Other":
            industry = st.text_input("Specify Industry", placeholder="Enter industry name")
    
    with col2:
        product = st.selectbox(
            "IBM Product/Solution *",
            options=[
                "IBM watsonx",
                "IBM Cloud",
                "IBM Security",
                "IBM Automation",
                "IBM Data & AI",
                "IBM Consulting",
                "Other IBM Solution"
            ]
        )
        
        if product == "Other IBM Solution":
            product = st.text_input("Specify Solution", placeholder="Enter solution name")
        
        ticker = st.text_input(
            "Stock Ticker (Optional)",
            value=st.session_state.client_data.get('ticker', ''),
            placeholder="e.g., ACME"
        )
        
        website = st.text_input(
            "Company Website (Optional)",
            value=st.session_state.client_data.get('website', ''),
            placeholder="https://www.example.com"
        )
    
    st.markdown("---")
    
    if st.button("Continue to Research →", type="primary", use_container_width=True):
        if company_name and industry and product:
            st.session_state.client_data = {
                'name': company_name,
                'industry': industry,
                'product': product,
                'ticker': ticker if ticker else None,
                'website': website if website else None
            }
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Please fill in all required fields (*)")


def step2_research():
    """Step 2: Conduct research"""
    st.header("🔍 Step 2: Company Research")
    
    # Display client info
    with st.expander("📋 Client Information", expanded=False):
        col1, col2, col3 = st.columns(3)
        col1.metric("Company", st.session_state.client_data['name'])
        col2.metric("Industry", st.session_state.client_data['industry'])
        col3.metric("Solution", st.session_state.client_data['product'])
    
    if st.session_state.strategic_results is None:
        if st.button("🚀 Start Research", type="primary", use_container_width=True):
            with st.spinner("🔍 Researching company and analyzing strategic priorities..."):
                strategist = StrategistAgent()
                
                # Progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("Searching company information...")
                progress_bar.progress(20)
                
                status_text.text("Analyzing SEC filings...")
                progress_bar.progress(40)
                
                status_text.text("Reviewing investor relations...")
                progress_bar.progress(60)
                
                status_text.text("Gathering industry benchmarks...")
                progress_bar.progress(80)
                
                # Perform research
                results = strategist.analyze_company(
                    company_name=st.session_state.client_data['name'],
                    industry=st.session_state.client_data['industry'],
                    ticker=st.session_state.client_data.get('ticker'),
                    website=st.session_state.client_data.get('website')
                )
                
                st.session_state.strategic_results = results
                
                status_text.text("Research complete!")
                progress_bar.progress(100)
                
                st.success("✅ Research completed successfully!")
                st.rerun()
    else:
        # Display research results
        results = st.session_state.strategic_results
        
        # Value Pillars
        st.subheader("🎯 Strategic Value Pillars")
        
        pillars_data = []
        for pillar in results['value_pillars'][:5]:
            pillars_data.append({
                'Priority': pillar['priority'],
                'Source': pillar['source'],
                'Relevance': f"{pillar['relevance_score']:.0%}"
            })
        
        df_pillars = pd.DataFrame(pillars_data)
        st.dataframe(df_pillars, use_container_width=True, hide_index=True)
        
        # Strategic Alignment
        col1, col2, col3 = st.columns(3)
        
        alignment = results['strategic_analysis']
        
        with col1:
            st.metric(
                "Strategic Alignment Score",
                f"{alignment['alignment_score']:.0%}",
                delta="High" if alignment['alignment_score'] > 0.7 else "Medium"
            )
        
        with col2:
            st.metric(
                "High Priority Areas",
                len(alignment['high_priority_areas'])
            )
        
        with col3:
            st.metric(
                "Friction Points Identified",
                len(results['friction_points'])
            )
        
        # Friction Points
        with st.expander("🔍 View Friction Points", expanded=False):
            for i, fp in enumerate(results['friction_points'][:10], 1):
                severity_color = "🔴" if fp['severity'] == 'high' else "🟡"
                st.markdown(f"{i}. {severity_color} **{fp['friction_point']}** ({fp['severity']} severity)")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Client Info"):
                st.session_state.step = 1
                st.rerun()
        
        with col2:
            if st.button("Continue to Calculations →", type="primary", use_container_width=True):
                st.session_state.step = 3
                st.rerun()


def step3_calculations():
    """Step 3: Perform BVA calculations"""
    st.header("🧮 Step 3: Value Calculations")
    
    # Project details input
    if st.session_state.bva_results is None:
        st.subheader("💼 Project Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            project_cost = st.number_input(
                "Estimated Project Cost (USD)",
                min_value=0,
                value=500000,
                step=50000,
                format="%d"
            )
        
        with col2:
            time_period = st.selectbox(
                "Analysis Time Period",
                options=[1, 3, 5],
                index=1,
                format_func=lambda x: f"{x} year{'s' if x > 1 else ''}"
            )
        
        st.markdown("---")
        
        if st.button("🧮 Calculate BVA", type="primary", use_container_width=True):
            with st.spinner("Calculating business value..."):
                quant = QuantAgent()
                
                # Progress
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("Calculating efficiency savings...")
                progress_bar.progress(33)
                
                status_text.text("Calculating risk mitigation value...")
                progress_bar.progress(66)
                
                status_text.text("Calculating growth enablement...")
                progress_bar.progress(90)
                
                # Perform calculations
                bva_results = quant.calculate_bva(
                    client_data=st.session_state.client_data,
                    friction_points=st.session_state.strategic_results['friction_points'],
                    project_cost=project_cost,
                    time_period_years=time_period
                )
                
                st.session_state.bva_results = bva_results
                
                status_text.text("Calculations complete!")
                progress_bar.progress(100)
                
                st.success("✅ BVA calculations completed!")
                st.rerun()
    else:
        # Display BVA results
        results = st.session_state.bva_results
        summary = results['summary']
        roi = results['roi']
        payback = results['payback']
        breakdown = results['value_breakdown']
        
        # Key Metrics
        st.subheader("💰 Key Financial Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Annual Value",
                f"${summary['total_annual_value']:,.0f}",
                delta="Projected"
            )
        
        with col2:
            st.metric(
                f"{summary['time_period_years']}-Year Value",
                f"${summary['total_value_over_period']:,.0f}"
            )
        
        with col3:
            st.metric(
                "ROI",
                f"{roi['roi_percentage']:.1f}%",
                delta="Strong" if roi['roi_percentage'] > 300 else "Good"
            )
        
        with col4:
            st.metric(
                "Payback Period",
                f"{payback['payback_months']:.1f} mo",
                delta="Fast" if payback['payback_months'] < 12 else "Moderate"
            )
        
        # Value Breakdown Chart
        st.subheader("📊 Value Breakdown")
        
        fig = go.Figure(data=[go.Pie(
            labels=['Efficiency Savings', 'Risk Mitigation', 'Growth Enablement'],
            values=[
                breakdown['efficiency_savings'],
                breakdown['risk_mitigation'],
                breakdown['growth_enablement']
            ],
            marker=dict(colors=['#0F62FE', '#24A148', '#FA4D56']),
            hole=0.4
        )])
        
        fig.update_layout(
            title="Annual Value Distribution",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # ROI Timeline
        st.subheader("📈 ROI Timeline")
        
        years = list(range(summary['time_period_years'] + 1))
        cumulative_value = [0] + [summary['total_annual_value'] * (i+1) for i in range(summary['time_period_years'])]
        cumulative_cost = [summary['project_cost']] * (summary['time_period_years'] + 1)
        net_value = [cv - cc for cv, cc in zip(cumulative_value, cumulative_cost)]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=years,
            y=cumulative_value,
            name='Cumulative Value',
            line=dict(color='#24A148', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=years,
            y=cumulative_cost,
            name='Project Cost',
            line=dict(color='#FA4D56', width=3, dash='dash')
        ))
        
        fig.add_trace(go.Scatter(
            x=years,
            y=net_value,
            name='Net Value',
            line=dict(color='#0F62FE', width=3)
        ))
        
        fig.update_layout(
            title="Value Accumulation Over Time",
            xaxis_title="Year",
            yaxis_title="Value (USD)",
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed Breakdown
        with st.expander("📋 Detailed Value Breakdown", expanded=False):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**💰 Efficiency Savings**")
                st.markdown(f"${breakdown['efficiency_savings']:,.0f}/year")
                st.markdown("- Time savings")
                st.markdown("- Labor cost reduction")
                st.markdown("- Process efficiency")
            
            with col2:
                st.markdown("**🛡️ Risk Mitigation**")
                st.markdown(f"${breakdown['risk_mitigation']:,.0f}/year")
                st.markdown("- Downtime avoidance")
                st.markdown("- Compliance risk")
                st.markdown("- Data breach prevention")
            
            with col3:
                st.markdown("**📈 Growth Enablement**")
                st.markdown(f"${breakdown['growth_enablement']:,.0f}/year")
                st.markdown("- Time-to-market")
                st.markdown("- Revenue enablement")
                st.markdown("- Market expansion")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Research"):
                st.session_state.step = 2
                st.rerun()
        
        with col2:
            if st.button("Generate Report →", type="primary", use_container_width=True):
                st.session_state.step = 4
                st.rerun()


def step4_report():
    """Step 4: Generate and download report"""
    st.header("📄 Step 4: Generate Report")
    
    if st.session_state.report_paths is None:
        st.subheader("📝 Report Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            include_pdf = st.checkbox("Generate PDF version", value=True)
        
        with col2:
            include_appendix = st.checkbox("Include detailed appendix", value=True)
        
        st.markdown("---")
        
        if st.button("🎨 Generate Report", type="primary", use_container_width=True):
            with st.spinner("Synthesizing findings and generating report..."):
                creative = CreativeDirectorAgent()
                
                # Progress
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("Synthesizing strategic insights...")
                progress_bar.progress(25)
                
                # Synthesize
                synthesis = creative.synthesize_bva(
                    client_data=st.session_state.client_data,
                    strategic_analysis=st.session_state.strategic_results,
                    bva_calculations=st.session_state.bva_results
                )
                
                st.session_state.synthesis = synthesis
                
                status_text.text("Generating Word document...")
                progress_bar.progress(50)
                
                # Generate report
                report_paths = creative.generate_report(
                    client_data=st.session_state.client_data,
                    research_data=st.session_state.strategic_results['research_results'],
                    calculations=st.session_state.bva_results,
                    synthesis=synthesis,
                    export_pdf=include_pdf
                )
                
                st.session_state.report_paths = report_paths
                
                status_text.text("Report generation complete!")
                progress_bar.progress(100)
                
                st.success("✅ Report generated successfully!")
                st.rerun()
    else:
        # Display completion
        st.success("🎉 BVA Report Generated Successfully!")
        
        # Summary
        st.subheader("📊 Executive Summary")
        
        synthesis = st.session_state.synthesis
        narrative = synthesis['executive_narrative']
        
        st.markdown(f"**{narrative['opening']}**")
        st.markdown(narrative['value_proposition'])
        
        # Recommendations
        st.subheader("💡 Key Recommendations")
        
        for i, rec in enumerate(synthesis['recommendations'][:5], 1):
            st.markdown(f"{i}. {rec}")
        
        st.markdown("---")
        
        # Download buttons
        st.subheader("📥 Download Reports")
        
        col1, col2 = st.columns(2)
        
        with col1:
            docx_path = st.session_state.report_paths['docx_path']
            if os.path.exists(docx_path):
                with open(docx_path, 'rb') as f:
                    st.download_button(
                        label="📄 Download Word Document",
                        data=f,
                        file_name=os.path.basename(docx_path),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )
        
        with col2:
            pdf_path = st.session_state.report_paths.get('pdf_path')
            if pdf_path and os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as f:
                    st.download_button(
                        label="📑 Download PDF",
                        data=f,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf",
                        use_container_width=True
                    )
        
        st.markdown("---")
        
        # Next steps
        st.info("""
        **📋 Next Steps:**
        1. Review the generated report
        2. Customize as needed for your client
        3. Share with stakeholders
        4. Track implementation progress
        """)
        
        if st.button("🔄 Start New BVA", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


def main():
    """Main dashboard application"""
    initialize_session_state()
    render_header()
    render_sidebar()
    
    # Route to appropriate step
    if st.session_state.step == 1:
        step1_client_info()
    elif st.session_state.step == 2:
        step2_research()
    elif st.session_state.step == 3:
        step3_calculations()
    elif st.session_state.step == 4:
        step4_report()


if __name__ == "__main__":
    main()

# Made with Bob
