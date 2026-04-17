# 📊 BVA Generator Dashboard Guide

## Overview

The BVA Generator Dashboard provides a modern, interactive web interface for generating Business Value Assessments. Built with Streamlit, it offers real-time visualizations, progress tracking, and an intuitive user experience.

## 🚀 Quick Start

### Installation

```bash
# Install dashboard dependencies
pip install streamlit plotly

# Or install all requirements
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open automatically in your default browser at `http://localhost:8501`

## 🎨 Dashboard Features

### 1. **Interactive Client Input**
- Form-based data entry
- Real-time validation
- Auto-save functionality
- Industry and product selection

### 2. **Live Research Progress**
- Real-time progress indicators
- Status updates during research
- Visual feedback for each research phase

### 3. **Interactive Visualizations**
- **Pie Chart**: Value breakdown by category
- **Line Chart**: ROI timeline projection
- **Metrics Cards**: Key financial indicators
- **Progress Bars**: Research and calculation status

### 4. **Multi-Step Workflow**
```
Step 1: Client Info → Step 2: Research → Step 3: Calculations → Step 4: Report
```

### 5. **Report Download**
- Direct download of Word documents
- PDF export (if configured)
- One-click report generation

## 📋 Dashboard Sections

### Sidebar Navigation
- **Progress Tracker**: Visual progress through workflow
- **Quick Actions**: Start new BVA, view documentation
- **About Section**: Version and system info

### Main Content Area

#### Step 1: Client Information
- Company name input
- Industry selection dropdown
- IBM product/solution selector
- Optional ticker and website fields
- Form validation

#### Step 2: Company Research
- Automated research initiation
- Real-time progress updates
- Strategic value pillars display
- Alignment score metrics
- Friction points analysis
- Expandable detailed views

#### Step 3: Value Calculations
- Project cost input
- Time period selection
- Real-time BVA calculations
- **Key Metrics Dashboard**:
  - Annual Value
  - Total Value
  - ROI Percentage
  - Payback Period
- **Interactive Charts**:
  - Value breakdown pie chart
  - ROI timeline projection
  - Cumulative value analysis
- Detailed breakdown by category

#### Step 4: Report Generation
- Report options configuration
- PDF export toggle
- Appendix inclusion option
- Executive summary preview
- Key recommendations display
- Download buttons for reports
- Next steps guidance

## 🎯 Using the Dashboard

### Complete Workflow Example

1. **Launch Dashboard**
   ```bash
   streamlit run dashboard.py
   ```

2. **Enter Client Information**
   - Fill in company name: "Acme Corporation"
   - Select industry: "Manufacturing"
   - Choose solution: "IBM watsonx"
   - Add ticker (optional): "ACME"
   - Click "Continue to Research"

3. **Conduct Research**
   - Click "Start Research"
   - Watch progress bar advance
   - Review strategic findings
   - Check alignment score
   - Click "Continue to Calculations"

4. **Calculate BVA**
   - Enter project cost: $500,000
   - Select time period: 3 years
   - Click "Calculate BVA"
   - Review metrics and charts
   - Click "Generate Report"

5. **Download Report**
   - Review executive summary
   - Check recommendations
   - Download Word document
   - Download PDF (if enabled)
   - Start new BVA or exit

## 📊 Visualization Details

### Value Breakdown Pie Chart
Shows distribution of value across three categories:
- **Blue**: Efficiency Savings
- **Green**: Risk Mitigation
- **Red**: Growth Enablement

### ROI Timeline Chart
Displays three lines:
- **Green Line**: Cumulative Value
- **Red Dashed Line**: Project Cost
- **Blue Line**: Net Value

Hover over chart for detailed values at each year.

### Metrics Cards
Color-coded indicators:
- **Green Delta**: Positive/Strong performance
- **Red Delta**: Needs attention
- **Gray**: Neutral/Informational

## 🎨 Customization

### Branding
Edit the CSS in `dashboard.py`:

```python
st.markdown("""
<style>
    .main-header {
        color: #YOUR_COLOR;  # Change header color
    }
    .metric-card {
        background-color: #YOUR_BG;  # Change card background
    }
</style>
""", unsafe_allow_html=True)
```

### Logo
Replace the IBM logo URL in the sidebar:

```python
st.image("YOUR_LOGO_URL", width=150)
```

### Color Scheme
Modify chart colors in the plotting functions:

```python
marker=dict(colors=['#COLOR1', '#COLOR2', '#COLOR3'])
```

## 🔧 Advanced Features

### Session State Management
The dashboard uses Streamlit's session state to maintain data across steps:
- `st.session_state.step`: Current workflow step
- `st.session_state.client_data`: Client information
- `st.session_state.strategic_results`: Research findings
- `st.session_state.bva_results`: Calculation results
- `st.session_state.synthesis`: Report synthesis
- `st.session_state.report_paths`: Generated report paths

### Progress Tracking
Visual progress indicator in sidebar shows:
- ✅ Completed steps
- 🔵 Current step
- ⚪ Pending steps

### Error Handling
Built-in validation:
- Required field checking
- Numeric input validation
- File existence verification
- Graceful error messages

## 🚀 Deployment Options

### Local Development
```bash
streamlit run dashboard.py
```

### Streamlit Cloud
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Deploy with one click
4. Share public URL

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "dashboard.py"]
```

### Custom Server
```bash
streamlit run dashboard.py --server.port 8080 --server.address 0.0.0.0
```

## 📱 Mobile Responsiveness

The dashboard is responsive and works on:
- Desktop browsers
- Tablets
- Mobile devices (limited functionality)

## 🔒 Security Considerations

For production deployment:

1. **Add Authentication**
   ```python
   import streamlit_authenticator as stauth
   # Add authentication layer
   ```

2. **Environment Variables**
   ```python
   import os
   API_KEY = os.getenv('API_KEY')
   ```

3. **HTTPS**
   - Use reverse proxy (nginx)
   - Enable SSL certificates

4. **Rate Limiting**
   - Implement request throttling
   - Add CAPTCHA for public access

## 🎯 Performance Tips

1. **Cache Data**
   ```python
   @st.cache_data
   def load_data():
       # Expensive operation
       return data
   ```

2. **Optimize Charts**
   - Limit data points
   - Use sampling for large datasets

3. **Lazy Loading**
   - Load components on demand
   - Use expanders for detailed views

## 🐛 Troubleshooting

### Dashboard Won't Start
```bash
# Check Streamlit installation
pip list | grep streamlit

# Reinstall if needed
pip install streamlit --upgrade
```

### Charts Not Displaying
```bash
# Install plotly
pip install plotly

# Clear cache
streamlit cache clear
```

### Import Errors
```bash
# Ensure you're in project root
cd bva-generator-agent

# Run from correct directory
streamlit run dashboard.py
```

### Port Already in Use
```bash
# Use different port
streamlit run dashboard.py --server.port 8502
```

## 📊 Dashboard vs CLI

| Feature | Dashboard | CLI (main.py) |
|---------|-----------|---------------|
| Interface | Web-based | Terminal |
| Visualizations | Interactive charts | Text-based |
| Progress | Real-time | Step-by-step |
| Multi-user | Yes (with deployment) | No |
| Accessibility | Browser required | Terminal only |
| Best For | Presentations, demos | Automation, scripts |

## 🎓 Tips for Best Experience

1. **Use Chrome or Firefox** for best compatibility
2. **Full screen mode** for better visualization
3. **Save configurations** before closing
4. **Review charts** before generating reports
5. **Download reports immediately** after generation

## 📚 Additional Resources

- **Streamlit Documentation**: https://docs.streamlit.io/
- **Plotly Documentation**: https://plotly.com/python/
- **Dashboard Examples**: https://streamlit.io/gallery

## 🆘 Support

For dashboard-specific issues:
1. Check browser console for errors
2. Clear browser cache
3. Restart Streamlit server
4. Review logs in terminal

---

**Ready to use the dashboard?** Run `streamlit run dashboard.py` now! 🚀