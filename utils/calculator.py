"""
Formula Engine for BVA Calculations
Handles all ROI, payback, and value calculations using the Formula Vault
"""

import yaml
from typing import Dict, List, Any, Optional
from pathlib import Path


class FormulaEngine:
    """Executes calculations using formulas from the Formula Vault"""
    
    def __init__(self, formula_vault_path: str = "config/formula_vault.yaml"):
        self.vault_path = Path(formula_vault_path)
        self.formulas = self._load_formulas()
        
    def _load_formulas(self) -> Dict:
        """Load formulas from YAML configuration"""
        try:
            with open(self.vault_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️  Error loading formula vault: {e}")
            return {}
    
    def calculate_efficiency_savings(self, formula_type: str, variables: Dict) -> Dict:
        """
        Calculate efficiency-based savings
        
        Args:
            formula_type: Type of efficiency calculation (time_savings, labor_cost_reduction, etc.)
            variables: Dictionary of variable values needed for calculation
            
        Returns:
            Dictionary with calculation results and details
        """
        if 'efficiency_vault' not in self.formulas:
            return {'error': 'Efficiency vault not found'}
            
        vault = self.formulas['efficiency_vault']
        
        if formula_type not in vault:
            return {'error': f'Formula type {formula_type} not found in efficiency vault'}
            
        formula_config = vault[formula_type]
        formula = formula_config['formula']
        
        try:
            # Execute the formula with provided variables
            result = eval(formula, {"__builtins__": {}}, variables)
            
            return {
                'formula_type': formula_type,
                'formula_name': formula_config['name'],
                'result': result,
                'unit': formula_config['unit'],
                'variables_used': variables,
                'formula': formula
            }
        except Exception as e:
            return {
                'error': f'Calculation error: {str(e)}',
                'formula': formula,
                'variables': variables
            }
    
    def calculate_risk_mitigation(self, formula_type: str, variables: Dict) -> Dict:
        """Calculate risk-based value"""
        if 'risk_vault' not in self.formulas:
            return {'error': 'Risk vault not found'}
            
        vault = self.formulas['risk_vault']
        
        if formula_type not in vault:
            return {'error': f'Formula type {formula_type} not found in risk vault'}
            
        formula_config = vault[formula_type]
        formula = formula_config['formula']
        
        try:
            result = eval(formula, {"__builtins__": {}}, variables)
            
            return {
                'formula_type': formula_type,
                'formula_name': formula_config['name'],
                'result': result,
                'unit': formula_config['unit'],
                'variables_used': variables,
                'formula': formula
            }
        except Exception as e:
            return {
                'error': f'Calculation error: {str(e)}',
                'formula': formula,
                'variables': variables
            }
    
    def calculate_growth_value(self, formula_type: str, variables: Dict) -> Dict:
        """Calculate growth-based value"""
        if 'growth_vault' not in self.formulas:
            return {'error': 'Growth vault not found'}
            
        vault = self.formulas['growth_vault']
        
        if formula_type not in vault:
            return {'error': f'Formula type {formula_type} not found in growth vault'}
            
        formula_config = vault[formula_type]
        formula = formula_config['formula']
        
        try:
            result = eval(formula, {"__builtins__": {}}, variables)
            
            return {
                'formula_type': formula_type,
                'formula_name': formula_config['name'],
                'result': result,
                'unit': formula_config['unit'],
                'variables_used': variables,
                'formula': formula
            }
        except Exception as e:
            return {
                'error': f'Calculation error: {str(e)}',
                'formula': formula,
                'variables': variables
            }
    
    def calculate_payback_period(self, total_project_cost: float, 
                                 monthly_value_generated: float) -> Dict:
        """Calculate payback period in months"""
        if monthly_value_generated <= 0:
            return {
                'error': 'Monthly value must be greater than 0',
                'payback_months': None
            }
            
        payback_months = total_project_cost / monthly_value_generated
        
        return {
            'payback_months': round(payback_months, 1),
            'payback_years': round(payback_months / 12, 2),
            'total_project_cost': total_project_cost,
            'monthly_value': monthly_value_generated,
            'annual_value': monthly_value_generated * 12
        }
    
    def calculate_roi(self, total_value: float, total_cost: float, 
                     time_period_years: int = 3) -> Dict:
        """Calculate Return on Investment"""
        if total_cost <= 0:
            return {
                'error': 'Total cost must be greater than 0',
                'roi_percentage': None
            }
            
        roi_percentage = ((total_value - total_cost) / total_cost) * 100
        
        return {
            'roi_percentage': round(roi_percentage, 2),
            'total_value': total_value,
            'total_cost': total_cost,
            'net_value': total_value - total_cost,
            'time_period_years': time_period_years,
            'annualized_roi': round(roi_percentage / time_period_years, 2)
        }
    
    def get_industry_benchmark(self, industry: str, metric: str) -> Optional[float]:
        """Retrieve industry benchmark value"""
        if 'industry_benchmarks' not in self.formulas:
            return None
            
        benchmarks = self.formulas['industry_benchmarks']
        
        # Normalize industry name
        industry_key = industry.lower().replace(' ', '_')
        
        if industry_key in benchmarks:
            return benchmarks[industry_key].get(metric)
        
        return None
    
    def get_all_industry_benchmarks(self, industry: str) -> Dict:
        """Get all benchmarks for a specific industry"""
        if 'industry_benchmarks' not in self.formulas:
            return {}
            
        benchmarks = self.formulas['industry_benchmarks']
        industry_key = industry.lower().replace(' ', '_')
        
        return benchmarks.get(industry_key, {})
    
    def calculate_comprehensive_bva(self, calculations: List[Dict], 
                                   project_cost: float,
                                   time_period_years: int = 3) -> Dict:
        """
        Calculate comprehensive BVA combining multiple value streams
        
        Args:
            calculations: List of calculation results from different vaults
            project_cost: Total project implementation cost
            time_period_years: Time period for ROI calculation
            
        Returns:
            Comprehensive BVA summary
        """
        total_annual_value = 0
        value_breakdown = {
            'efficiency': 0,
            'risk': 0,
            'growth': 0
        }
        
        calculation_details = []
        
        for calc in calculations:
            if 'error' in calc:
                continue
                
            annual_value = calc['result']
            
            # Categorize by vault type
            if 'efficiency' in calc.get('formula_type', ''):
                value_breakdown['efficiency'] += annual_value
            elif 'risk' in calc.get('formula_type', ''):
                value_breakdown['risk'] += annual_value
            elif 'growth' in calc.get('formula_type', ''):
                value_breakdown['growth'] += annual_value
                
            total_annual_value += annual_value
            calculation_details.append(calc)
        
        # Calculate total value over time period
        total_value = total_annual_value * time_period_years
        
        # Calculate ROI
        roi_result = self.calculate_roi(total_value, project_cost, time_period_years)
        
        # Calculate payback period
        monthly_value = total_annual_value / 12
        payback_result = self.calculate_payback_period(project_cost, monthly_value)
        
        return {
            'summary': {
                'total_annual_value': round(total_annual_value, 2),
                'total_value_over_period': round(total_value, 2),
                'project_cost': project_cost,
                'net_value': round(total_value - project_cost, 2),
                'time_period_years': time_period_years
            },
            'value_breakdown': {
                'efficiency_savings': round(value_breakdown['efficiency'], 2),
                'risk_mitigation': round(value_breakdown['risk'], 2),
                'growth_enablement': round(value_breakdown['growth'], 2)
            },
            'roi': roi_result,
            'payback': payback_result,
            'calculation_details': calculation_details
        }
    
    def list_available_formulas(self) -> Dict:
        """List all available formulas by vault"""
        available = {
            'efficiency_vault': [],
            'risk_vault': [],
            'growth_vault': []
        }
        
        for vault_name in available.keys():
            if vault_name in self.formulas:
                vault = self.formulas[vault_name]
                for formula_type, config in vault.items():
                    available[vault_name].append({
                        'type': formula_type,
                        'name': config['name'],
                        'variables': list(config.get('variables', [{}])[0].keys()) if config.get('variables') else []
                    })
        
        return available


def test_calculator():
    """Test the calculator functionality"""
    engine = FormulaEngine()
    
    print("🧮 Testing Formula Engine\n")
    
    # Test efficiency calculation
    print("1️⃣ Testing Time Savings Calculation:")
    efficiency_result = engine.calculate_efficiency_savings(
        'time_savings',
        {
            'manual_hours': 100,
            'automated_hours': 20,
            'hourly_rate': 50
        }
    )
    print(f"   Result: ${efficiency_result['result']:,.2f} {efficiency_result['unit']}")
    
    # Test risk calculation
    print("\n2️⃣ Testing Downtime Cost Avoidance:")
    risk_result = engine.calculate_risk_mitigation(
        'downtime_cost',
        {
            'probability_of_failure': 0.15,
            'downtime_hours': 24,
            'revenue_per_hour': 50000
        }
    )
    print(f"   Result: ${risk_result['result']:,.2f} {risk_result['unit']}")
    
    # Test growth calculation
    print("\n3️⃣ Testing Time-to-Market Value:")
    growth_result = engine.calculate_growth_value(
        'time_to_market',
        {
            'weeks_accelerated': 8,
            'weekly_revenue': 5000000
        }
    )
    print(f"   Result: ${growth_result['result']:,.2f} {growth_result['unit']}")
    
    # Test comprehensive BVA
    print("\n4️⃣ Testing Comprehensive BVA:")
    comprehensive = engine.calculate_comprehensive_bva(
        calculations=[efficiency_result, risk_result, growth_result],
        project_cost=500000,
        time_period_years=3
    )
    
    print(f"\n   📊 BVA Summary:")
    print(f"   Total Annual Value: ${comprehensive['summary']['total_annual_value']:,.2f}")
    print(f"   3-Year Total Value: ${comprehensive['summary']['total_value_over_period']:,.2f}")
    print(f"   Project Cost: ${comprehensive['summary']['project_cost']:,.2f}")
    print(f"   Net Value: ${comprehensive['summary']['net_value']:,.2f}")
    print(f"   ROI: {comprehensive['roi']['roi_percentage']}%")
    print(f"   Payback Period: {comprehensive['payback']['payback_months']} months")
    
    # Test industry benchmarks
    print("\n5️⃣ Testing Industry Benchmarks:")
    benchmarks = engine.get_all_industry_benchmarks('manufacturing')
    print(f"   Manufacturing Benchmarks:")
    for key, value in benchmarks.items():
        print(f"   - {key}: {value}")


if __name__ == "__main__":
    test_calculator()

# Made with Bob
