"""
Creative Director Agent
Synthesizes findings and generates executive-ready reports
"""

from typing import Dict, List
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.exporter import ReportGenerator


class CreativeDirectorAgent:
    """
    The Creative Director Agent synthesizes all findings and creates
    executive-ready reports that map technical value to business priorities
    """
    
    def __init__(self):
        self.generator = ReportGenerator()
        
    def synthesize_bva(self,
                      client_data: Dict,
                      strategic_analysis: Dict,
                      bva_calculations: Dict) -> Dict:
        """
        Synthesize all findings into executive narrative
        
        Args:
            client_data: Client information
            strategic_analysis: Results from Strategist Agent
            bva_calculations: Results from Quant Agent
            
        Returns:
            Synthesized report data ready for generation
        """
        print("\n" + "="*60)
        print("🎨 CREATIVE DIRECTOR AGENT ACTIVATED")
        print("="*60)
        
        # Map technical value to CEO priorities
        value_mapping = self._map_value_to_priorities(
            strategic_analysis,
            bva_calculations
        )
        
        # Create executive narrative
        executive_narrative = self._create_executive_narrative(
            client_data,
            strategic_analysis,
            bva_calculations,
            value_mapping
        )
        
        # Generate recommendations
        recommendations = self._synthesize_recommendations(
            strategic_analysis,
            bva_calculations
        )
        
        # Create visualizations data
        visualizations = self._prepare_visualizations(bva_calculations)
        
        synthesis = {
            'value_mapping': value_mapping,
            'executive_narrative': executive_narrative,
            'recommendations': recommendations,
            'visualizations': visualizations
        }
        
        self._print_synthesis_summary(synthesis)
        
        return synthesis
    
    def _map_value_to_priorities(self,
                                strategic_analysis: Dict,
                                bva_calculations: Dict) -> List[Dict]:
        """
        Map calculated value back to CEO priorities
        """
        print("\n🎯 Mapping Value to CEO Priorities...")
        
        value_pillars = strategic_analysis.get('value_pillars', [])
        value_breakdown = bva_calculations.get('value_breakdown', {})
        
        mappings = []
        
        for pillar in value_pillars[:3]:  # Top 3 priorities
            priority = pillar.get('priority', '')
            
            # Determine which value category aligns best
            mapping = {
                'ceo_priority': priority,
                'relevance_score': pillar.get('relevance_score', 0),
                'value_alignment': [],
                'total_aligned_value': 0
            }
            
            # Map efficiency savings
            if any(keyword in priority.lower() for keyword in ['efficiency', 'cost', 'operational', 'productivity']):
                efficiency_value = value_breakdown.get('efficiency_savings', 0)
                mapping['value_alignment'].append({
                    'category': 'Efficiency Savings',
                    'value': efficiency_value,
                    'description': 'Reduces operational costs and improves productivity'
                })
                mapping['total_aligned_value'] += efficiency_value
            
            # Map risk mitigation
            if any(keyword in priority.lower() for keyword in ['risk', 'compliance', 'security', 'reliability']):
                risk_value = value_breakdown.get('risk_mitigation', 0)
                mapping['value_alignment'].append({
                    'category': 'Risk Mitigation',
                    'value': risk_value,
                    'description': 'Reduces operational risks and ensures compliance'
                })
                mapping['total_aligned_value'] += risk_value
            
            # Map growth enablement
            if any(keyword in priority.lower() for keyword in ['growth', 'innovation', 'digital', 'transformation', 'market']):
                growth_value = value_breakdown.get('growth_enablement', 0)
                mapping['value_alignment'].append({
                    'category': 'Growth Enablement',
                    'value': growth_value,
                    'description': 'Accelerates growth and enables innovation'
                })
                mapping['total_aligned_value'] += growth_value
            
            # If no specific alignment, distribute value proportionally
            if not mapping['value_alignment']:
                total_value = sum(value_breakdown.values())
                mapping['value_alignment'].append({
                    'category': 'Overall Value',
                    'value': total_value,
                    'description': 'Supports strategic objectives'
                })
                mapping['total_aligned_value'] = total_value
            
            mappings.append(mapping)
            
            print(f"   ✓ {priority}: ${mapping['total_aligned_value']:,.0f} aligned value")
        
        return mappings
    
    def _create_executive_narrative(self,
                                   client_data: Dict,
                                   strategic_analysis: Dict,
                                   bva_calculations: Dict,
                                   value_mapping: List[Dict]) -> Dict:
        """
        Create compelling executive narrative
        """
        print("\n📝 Creating Executive Narrative...")
        
        company_name = client_data.get('name', 'the organization')
        product = client_data.get('product', 'the solution')
        
        summary = bva_calculations.get('summary', {})
        roi = bva_calculations.get('roi', {})
        payback = bva_calculations.get('payback', {})
        
        narrative = {
            'opening': f"{company_name} stands at a critical juncture. Our analysis reveals that "
                      f"implementing {product} will deliver ${summary.get('total_annual_value', 0):,.0f} "
                      f"in annual value, directly supporting the organization's strategic priorities.",
            
            'value_proposition': f"Over a {summary.get('time_period_years', 3)}-year period, "
                               f"{company_name} can expect to realize ${summary.get('total_value_over_period', 0):,.0f} "
                               f"in total value, representing a {roi.get('roi_percentage', 0):.0f}% return on investment "
                               f"with a payback period of just {payback.get('payback_months', 0):.1f} months.",
            
            'strategic_alignment': self._create_alignment_narrative(value_mapping),
            
            'competitive_advantage': f"By addressing key friction points and aligning with CEO priorities, "
                                   f"{company_name} will strengthen its competitive position and accelerate "
                                   f"its digital transformation journey.",
            
            'call_to_action': f"The compelling financial case, combined with strong strategic alignment, "
                            f"supports immediate action to capture this value opportunity."
        }
        
        return narrative
    
    def _create_alignment_narrative(self, value_mapping: List[Dict]) -> str:
        """Create narrative about strategic alignment"""
        if not value_mapping:
            return "The solution aligns with organizational priorities."
        
        narrative = "The solution directly supports key strategic priorities:\n\n"
        
        for mapping in value_mapping:
            priority = mapping['ceo_priority']
            value = mapping['total_aligned_value']
            
            narrative += f"• **{priority}**: Delivers ${value:,.0f} in aligned value through "
            
            alignments = mapping['value_alignment']
            if alignments:
                categories = [a['category'] for a in alignments]
                narrative += ", ".join(categories).lower()
            
            narrative += ".\n"
        
        return narrative
    
    def _synthesize_recommendations(self,
                                   strategic_analysis: Dict,
                                   bva_calculations: Dict) -> List[str]:
        """
        Synthesize actionable recommendations
        """
        print("\n💡 Synthesizing Recommendations...")
        
        recommendations = []
        
        # Get base recommendations from strategic analysis
        strategic_recs = strategic_analysis.get('recommendations', [])
        recommendations.extend(strategic_recs[:3])  # Top 3
        
        # Add financial-based recommendations
        roi = bva_calculations.get('roi', {})
        payback = bva_calculations.get('payback', {})
        
        if roi.get('roi_percentage', 0) > 300:
            recommendations.append(
                "Exceptional ROI: Fast-track approval and implementation"
            )
        
        if payback.get('payback_months', 0) < 12:
            recommendations.append(
                "Rapid Payback: Prioritize quick wins for immediate value realization"
            )
        
        # Add value-specific recommendations
        value_breakdown = bva_calculations.get('value_breakdown', {})
        
        max_category = max(value_breakdown.items(), key=lambda x: x[1])[0] if value_breakdown else None
        
        if max_category == 'efficiency_savings':
            recommendations.append(
                "Focus on Efficiency: Emphasize automation and process optimization in rollout"
            )
        elif max_category == 'risk_mitigation':
            recommendations.append(
                "Prioritize Risk Reduction: Highlight compliance and security benefits to stakeholders"
            )
        elif max_category == 'growth_enablement':
            recommendations.append(
                "Accelerate Growth: Position solution as growth enabler to executive team"
            )
        
        return recommendations[:6]  # Return top 6 recommendations
    
    def _prepare_visualizations(self, bva_calculations: Dict) -> Dict:
        """
        Prepare data for visualizations
        """
        value_breakdown = bva_calculations.get('value_breakdown', {})
        summary = bva_calculations.get('summary', {})
        
        return {
            'value_breakdown_chart': {
                'type': 'pie',
                'data': value_breakdown
            },
            'roi_timeline': {
                'type': 'line',
                'years': summary.get('time_period_years', 3),
                'annual_value': summary.get('total_annual_value', 0),
                'project_cost': summary.get('project_cost', 0)
            },
            'payback_chart': {
                'type': 'bar',
                'payback_months': bva_calculations.get('payback', {}).get('payback_months', 0)
            }
        }
    
    def _print_synthesis_summary(self, synthesis: Dict):
        """Print synthesis summary"""
        print("\n" + "="*60)
        print("📋 SYNTHESIS SUMMARY")
        print("="*60)
        
        narrative = synthesis.get('executive_narrative', {})
        
        print("\n📖 Executive Narrative:")
        print(f"   {narrative.get('opening', '')[:100]}...")
        
        print("\n🎯 Value Mappings:")
        for mapping in synthesis.get('value_mapping', [])[:3]:
            print(f"   • {mapping['ceo_priority']}: ${mapping['total_aligned_value']:,.0f}")
        
        print("\n💡 Key Recommendations:")
        for i, rec in enumerate(synthesis.get('recommendations', [])[:3], 1):
            print(f"   {i}. {rec}")
        
        print("\n" + "="*60)
    
    def generate_report(self,
                       client_data: Dict,
                       research_data: Dict,
                       calculations: Dict,
                       synthesis: Dict,
                       export_pdf: bool = True) -> Dict:
        """
        Generate final report documents
        
        Returns:
            Dictionary with paths to generated documents
        """
        print("\n📄 Generating Report Documents...")
        
        # Prepare report data
        recommendations = synthesis.get('recommendations', [])
        
        # Generate Word document
        docx_path = self.generator.create_bva_report(
            client_data=client_data,
            research_data=research_data,
            calculations=calculations,
            recommendations=recommendations
        )
        
        result = {
            'docx_path': docx_path,
            'pdf_path': None
        }
        
        # Convert to PDF if requested
        if export_pdf:
            print("\n📑 Converting to PDF...")
            pdf_path = self.generator.convert_to_pdf(docx_path)
            result['pdf_path'] = pdf_path
        
        return result


def test_creative():
    """Test the Creative Director Agent"""
    agent = CreativeDirectorAgent()
    
    # Sample data
    client_data = {
        'name': 'Acme Corporation',
        'industry': 'Manufacturing',
        'product': 'IBM watsonx'
    }
    
    strategic_analysis = {
        'value_pillars': [
            {'priority': 'Digital Transformation', 'relevance_score': 0.9, 'source': 'CEO Letter'},
            {'priority': 'Operational Efficiency', 'relevance_score': 0.85, 'source': 'SEC Filings'}
        ],
        'recommendations': [
            'Strong strategic alignment',
            'Focus on quick wins'
        ]
    }
    
    bva_calculations = {
        'summary': {
            'total_annual_value': 1500000,
            'total_value_over_period': 4500000,
            'project_cost': 500000,
            'time_period_years': 3
        },
        'value_breakdown': {
            'efficiency_savings': 800000,
            'risk_mitigation': 400000,
            'growth_enablement': 300000
        },
        'roi': {
            'roi_percentage': 800
        },
        'payback': {
            'payback_months': 4.0
        }
    }
    
    # Synthesize
    synthesis = agent.synthesize_bva(
        client_data=client_data,
        strategic_analysis=strategic_analysis,
        bva_calculations=bva_calculations
    )
    
    print("\n✅ Creative Director Agent test complete!")


if __name__ == "__main__":
    test_creative()

# Made with Bob
