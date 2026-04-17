"""
Quant Agent
Performs ROI calculations and financial modeling using the Formula Vault
"""

from typing import Dict, List, Optional
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.calculator import FormulaEngine


class QuantAgent:
    """
    The Quant Agent performs financial calculations and ROI modeling
    using industry-standard formulas and benchmarks
    """
    
    def __init__(self):
        self.engine = FormulaEngine()
        self.calculations = []
        
    def calculate_bva(self, 
                     client_data: Dict,
                     friction_points: List[Dict],
                     project_cost: float,
                     time_period_years: int = 3) -> Dict:
        """
        Calculate comprehensive Business Value Assessment
        
        Args:
            client_data: Client information including industry
            friction_points: List of identified friction points
            project_cost: Total project implementation cost
            time_period_years: Analysis time period
            
        Returns:
            Comprehensive BVA calculations
        """
        print("\n" + "="*60)
        print("🧮 QUANT AGENT ACTIVATED")
        print("="*60)
        
        # Get industry benchmarks
        industry = client_data.get('industry', '').lower().replace(' ', '_')
        benchmarks = self.engine.get_all_industry_benchmarks(industry)
        
        print(f"\n📊 Using {industry.title()} Industry Benchmarks")
        
        # Perform calculations based on friction points
        self.calculations = []
        
        # Efficiency calculations
        efficiency_calcs = self._calculate_efficiency_value(
            friction_points, 
            benchmarks,
            client_data
        )
        self.calculations.extend(efficiency_calcs)
        
        # Risk calculations
        risk_calcs = self._calculate_risk_value(
            friction_points,
            benchmarks,
            client_data
        )
        self.calculations.extend(risk_calcs)
        
        # Growth calculations
        growth_calcs = self._calculate_growth_value(
            friction_points,
            benchmarks,
            client_data
        )
        self.calculations.extend(growth_calcs)
        
        # Calculate comprehensive BVA
        comprehensive_bva = self.engine.calculate_comprehensive_bva(
            calculations=self.calculations,
            project_cost=project_cost,
            time_period_years=time_period_years
        )
        
        # Add industry context
        comprehensive_bva['industry_benchmarks'] = benchmarks
        comprehensive_bva['client_data'] = client_data
        
        self._print_summary(comprehensive_bva)
        
        return comprehensive_bva
    
    def _calculate_efficiency_value(self, friction_points: List[Dict],
                                   benchmarks: Dict,
                                   client_data: Dict) -> List[Dict]:
        """Calculate efficiency-based value"""
        print("\n💰 Calculating Efficiency Savings...")
        
        calculations = []
        
        # Time savings calculation
        # Assume automation reduces manual hours by 70%
        manual_hours_per_week = 40  # Default assumption
        automated_hours_per_week = manual_hours_per_week * 0.3
        hourly_rate = benchmarks.get('average_fte_hourly_rate', 50)
        weeks_per_year = 52
        
        time_savings = self.engine.calculate_efficiency_savings(
            'time_savings',
            {
                'manual_hours': manual_hours_per_week * weeks_per_year,
                'automated_hours': automated_hours_per_week * weeks_per_year,
                'hourly_rate': hourly_rate
            }
        )
        
        if 'error' not in time_savings:
            calculations.append(time_savings)
            print(f"   ✓ Time Savings: ${time_savings['result']:,.0f}/year")
        
        # Labor cost reduction
        # Assume 2 FTE reduction through automation
        current_fte = 10  # Default assumption
        future_fte = 8
        annual_salary = hourly_rate * 2080  # 2080 hours per year
        
        labor_reduction = self.engine.calculate_efficiency_savings(
            'labor_cost_reduction',
            {
                'current_fte_count': current_fte,
                'future_fte_count': future_fte,
                'annual_salary': annual_salary
            }
        )
        
        if 'error' not in labor_reduction:
            calculations.append(labor_reduction)
            print(f"   ✓ Labor Cost Reduction: ${labor_reduction['result']:,.0f}/year")
        
        # Process efficiency
        # Assume 40% cycle time reduction
        old_cycle_time = 100  # hours
        new_cycle_time = 60   # hours
        
        process_efficiency = self.engine.calculate_efficiency_savings(
            'process_efficiency',
            {
                'old_cycle_time': old_cycle_time,
                'new_cycle_time': new_cycle_time
            }
        )
        
        if 'error' not in process_efficiency:
            # Convert percentage to dollar value using hourly rate
            efficiency_gain = process_efficiency['result'] / 100
            dollar_value = efficiency_gain * old_cycle_time * hourly_rate * 52
            process_efficiency['result'] = dollar_value
            process_efficiency['unit'] = 'USD annually'
            calculations.append(process_efficiency)
            print(f"   ✓ Process Efficiency Gain: ${dollar_value:,.0f}/year")
        
        return calculations
    
    def _calculate_risk_value(self, friction_points: List[Dict],
                             benchmarks: Dict,
                             client_data: Dict) -> List[Dict]:
        """Calculate risk mitigation value"""
        print("\n🛡️  Calculating Risk Mitigation Value...")
        
        calculations = []
        
        # Downtime cost avoidance
        downtime_cost_per_hour = benchmarks.get('average_downtime_cost_per_hour', 10000)
        
        downtime_calc = self.engine.calculate_risk_mitigation(
            'downtime_cost',
            {
                'probability_of_failure': 0.15,  # 15% annual probability
                'downtime_hours': 24,
                'revenue_per_hour': downtime_cost_per_hour
            }
        )
        
        if 'error' not in downtime_calc:
            calculations.append(downtime_calc)
            print(f"   ✓ Downtime Cost Avoidance: ${downtime_calc['result']:,.0f}/year")
        
        # Compliance risk mitigation
        compliance_cost = benchmarks.get('compliance_cost_per_employee', 5000)
        employee_count = 100  # Default assumption
        
        compliance_calc = self.engine.calculate_risk_mitigation(
            'compliance_risk',
            {
                'probability_of_violation': 0.10,  # 10% probability
                'average_fine_amount': compliance_cost * employee_count
            }
        )
        
        if 'error' not in compliance_calc:
            calculations.append(compliance_calc)
            print(f"   ✓ Compliance Risk Mitigation: ${compliance_calc['result']:,.0f}/year")
        
        # Data breach prevention
        cost_per_record = benchmarks.get('cost_per_patient_record', 200)
        records_at_risk = 10000  # Default assumption
        
        breach_calc = self.engine.calculate_risk_mitigation(
            'data_breach_prevention',
            {
                'breach_probability': 0.08,  # 8% probability
                'records_at_risk': records_at_risk,
                'cost_per_record': cost_per_record
            }
        )
        
        if 'error' not in breach_calc:
            calculations.append(breach_calc)
            print(f"   ✓ Data Breach Prevention: ${breach_calc['result']:,.0f}/year")
        
        return calculations
    
    def _calculate_growth_value(self, friction_points: List[Dict],
                               benchmarks: Dict,
                               client_data: Dict) -> List[Dict]:
        """Calculate growth enablement value"""
        print("\n📈 Calculating Growth Enablement Value...")
        
        calculations = []
        
        # Time-to-market acceleration
        # Assume 8 weeks faster product launch
        annual_revenue = 5000000  # Default assumption
        
        ttm_calc = self.engine.calculate_growth_value(
            'time_to_market',
            {
                'weeks_accelerated': 8,
                'weekly_revenue': annual_revenue
            }
        )
        
        if 'error' not in ttm_calc:
            calculations.append(ttm_calc)
            print(f"   ✓ Time-to-Market Value: ${ttm_calc['result']:,.0f}")
        
        # Revenue enablement
        avg_deal_size = benchmarks.get('average_transaction_value', 1000)
        
        revenue_calc = self.engine.calculate_growth_value(
            'revenue_enablement',
            {
                'new_customers': 100,  # Additional customers reached
                'average_deal_size': avg_deal_size,
                'conversion_rate': 0.20  # 20% conversion
            }
        )
        
        if 'error' not in revenue_calc:
            calculations.append(revenue_calc)
            print(f"   ✓ Revenue Enablement: ${revenue_calc['result']:,.0f}/year")
        
        # Market expansion
        addressable_market = 10000000  # $10M TAM
        
        market_calc = self.engine.calculate_growth_value(
            'market_expansion',
            {
                'addressable_market_size': addressable_market,
                'market_share_gain': 0.05,  # 5% market share gain
                'profit_margin': 0.20  # 20% profit margin
            }
        )
        
        if 'error' not in market_calc:
            calculations.append(market_calc)
            print(f"   ✓ Market Expansion Value: ${market_calc['result']:,.0f}/year")
        
        return calculations
    
    def _print_summary(self, bva: Dict):
        """Print BVA summary"""
        print("\n" + "="*60)
        print("📊 BVA CALCULATION SUMMARY")
        print("="*60)
        
        summary = bva.get('summary', {})
        roi = bva.get('roi', {})
        payback = bva.get('payback', {})
        breakdown = bva.get('value_breakdown', {})
        
        print(f"\n💰 Financial Metrics:")
        print(f"   Total Annual Value: ${summary.get('total_annual_value', 0):,.0f}")
        print(f"   {summary.get('time_period_years', 3)}-Year Total Value: ${summary.get('total_value_over_period', 0):,.0f}")
        print(f"   Project Cost: ${summary.get('project_cost', 0):,.0f}")
        print(f"   Net Value: ${summary.get('net_value', 0):,.0f}")
        
        print(f"\n📈 Performance Metrics:")
        print(f"   ROI: {roi.get('roi_percentage', 0):.1f}%")
        print(f"   Payback Period: {payback.get('payback_months', 0):.1f} months")
        
        print(f"\n🎯 Value Breakdown:")
        print(f"   Efficiency Savings: ${breakdown.get('efficiency_savings', 0):,.0f}")
        print(f"   Risk Mitigation: ${breakdown.get('risk_mitigation', 0):,.0f}")
        print(f"   Growth Enablement: ${breakdown.get('growth_enablement', 0):,.0f}")
        
        print("\n" + "="*60)
    
    def get_calculation_details(self) -> List[Dict]:
        """Return detailed calculation results"""
        return self.calculations


def test_quant():
    """Test the Quant Agent"""
    agent = QuantAgent()
    
    # Sample data
    client_data = {
        'name': 'Acme Corporation',
        'industry': 'manufacturing',
        'product': 'IBM watsonx'
    }
    
    friction_points = [
        {'friction_point': 'Manual data entry', 'severity': 'high'},
        {'friction_point': 'System downtime', 'severity': 'high'},
        {'friction_point': 'Slow time-to-market', 'severity': 'medium'}
    ]
    
    # Calculate BVA
    bva_results = agent.calculate_bva(
        client_data=client_data,
        friction_points=friction_points,
        project_cost=500000,
        time_period_years=3
    )
    
    print("\n✅ Quant Agent test complete!")


if __name__ == "__main__":
    test_quant()

# Made with Bob
