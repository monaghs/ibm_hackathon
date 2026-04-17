"""
Strategist Agent
Identifies value pillars from public filings and company research
"""

from typing import Dict, List, Optional
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.scraper import CompanyResearcher


class StrategistAgent:
    """
    The Strategist Agent analyzes company data to identify strategic priorities
    and value pillars that align with IBM solutions
    """
    
    def __init__(self):
        self.researcher = CompanyResearcher()
        self.value_pillars = []
        
    def analyze_company(self, company_name: str, industry: str,
                       ticker: Optional[str] = None,
                       website: Optional[str] = None) -> Dict:
        """
        Perform comprehensive company analysis
        
        Returns:
            Dictionary containing strategic insights and value pillars
        """
        print("\n" + "="*60)
        print("🎯 STRATEGIST AGENT ACTIVATED")
        print("="*60)
        
        # Conduct comprehensive research
        research_results = self.researcher.comprehensive_research(
            company_name=company_name,
            industry=industry,
            ticker=ticker,
            website=website
        )
        
        # Extract and prioritize value pillars
        self.value_pillars = research_results.get('value_pillars', [])
        
        # Analyze strategic alignment
        strategic_analysis = self._analyze_strategic_alignment(research_results)
        
        # Identify friction points
        friction_points = self._identify_friction_points(research_results)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            research_results,
            strategic_analysis,
            friction_points
        )
        
        return {
            'research_results': research_results,
            'strategic_analysis': strategic_analysis,
            'friction_points': friction_points,
            'recommendations': recommendations,
            'value_pillars': self.value_pillars
        }
    
    def _analyze_strategic_alignment(self, research_data: Dict) -> Dict:
        """
        Analyze how IBM solutions align with company priorities
        """
        print("\n📊 Analyzing Strategic Alignment...")
        
        alignment = {
            'high_priority_areas': [],
            'medium_priority_areas': [],
            'alignment_score': 0.0,
            'key_opportunities': []
        }
        
        value_pillars = research_data.get('value_pillars', [])
        
        # Categorize by relevance score
        for pillar in value_pillars:
            score = pillar.get('relevance_score', 0)
            priority = pillar.get('priority', '')
            
            if score >= 0.8:
                alignment['high_priority_areas'].append(priority)
            elif score >= 0.6:
                alignment['medium_priority_areas'].append(priority)
        
        # Calculate overall alignment score
        if value_pillars:
            avg_score = sum(p.get('relevance_score', 0) for p in value_pillars) / len(value_pillars)
            alignment['alignment_score'] = round(avg_score, 2)
        
        # Identify key opportunities based on priorities
        ceo_priorities = research_data.get('sec_filings', {}).get('ceo_priorities', [])
        news_opportunities = research_data.get('news_sentiment', {}).get('opportunities_identified', [])
        
        alignment['key_opportunities'] = list(set(ceo_priorities + news_opportunities))[:5]
        
        return alignment
    
    def _identify_friction_points(self, research_data: Dict) -> List[Dict]:
        """
        Identify operational friction points that IBM solutions can address
        """
        print("🔍 Identifying Friction Points...")
        
        friction_points = []
        
        # Extract challenges from news sentiment
        challenges = research_data.get('news_sentiment', {}).get('challenges_mentioned', [])
        
        for challenge in challenges:
            friction_points.append({
                'friction_point': challenge,
                'severity': 'high',
                'source': 'Market Analysis',
                'addressable': True
            })
        
        # Extract pain points from industry benchmarks
        pain_points = research_data.get('industry_benchmarks', {}).get('common_pain_points', [])
        
        for pain in pain_points:
            friction_points.append({
                'friction_point': pain,
                'severity': 'medium',
                'source': 'Industry Benchmarks',
                'addressable': True
            })
        
        # Extract risk factors from SEC filings
        risk_factors = research_data.get('sec_filings', {}).get('risk_factors', [])
        
        for risk in risk_factors:
            friction_points.append({
                'friction_point': risk,
                'severity': 'high',
                'source': 'SEC Filings',
                'addressable': True
            })
        
        return friction_points[:10]  # Return top 10 friction points
    
    def _generate_recommendations(self, research_data: Dict,
                                 strategic_analysis: Dict,
                                 friction_points: List[Dict]) -> List[str]:
        """
        Generate strategic recommendations based on analysis
        """
        print("💡 Generating Strategic Recommendations...")
        
        recommendations = []
        
        # Recommendation based on alignment score
        alignment_score = strategic_analysis.get('alignment_score', 0)
        
        if alignment_score >= 0.8:
            recommendations.append(
                "Strong Strategic Alignment: Proceed with comprehensive solution implementation"
            )
        elif alignment_score >= 0.6:
            recommendations.append(
                "Moderate Alignment: Focus on high-priority areas first, then expand"
            )
        else:
            recommendations.append(
                "Limited Alignment: Conduct deeper discovery to identify specific use cases"
            )
        
        # Recommendations based on friction points
        high_severity_count = sum(1 for fp in friction_points if fp.get('severity') == 'high')
        
        if high_severity_count >= 3:
            recommendations.append(
                "Multiple High-Severity Issues: Prioritize quick wins to demonstrate value"
            )
        
        # Recommendations based on industry
        industry = research_data.get('industry', '').lower()
        
        if 'manufacturing' in industry:
            recommendations.append(
                "Manufacturing Focus: Emphasize supply chain optimization and quality control"
            )
        elif 'retail' in industry:
            recommendations.append(
                "Retail Focus: Highlight customer experience and inventory management"
            )
        elif 'financial' in industry:
            recommendations.append(
                "Financial Services Focus: Emphasize compliance, security, and fraud prevention"
            )
        
        # General recommendations
        recommendations.extend([
            "Establish Clear Success Metrics: Define KPIs aligned with CEO priorities",
            "Plan Phased Implementation: Start with pilot, then scale based on results",
            "Invest in Change Management: Ensure stakeholder buy-in and adoption"
        ])
        
        return recommendations
    
    def get_value_pillars_summary(self) -> str:
        """
        Generate a summary of identified value pillars
        """
        if not self.value_pillars:
            return "No value pillars identified yet."
        
        summary = "\n🎯 Identified Value Pillars:\n"
        summary += "="*60 + "\n"
        
        for i, pillar in enumerate(self.value_pillars, 1):
            summary += f"\n{i}. {pillar.get('priority', 'Unknown')}\n"
            summary += f"   Source: {pillar.get('source', 'N/A')}\n"
            summary += f"   Relevance: {pillar.get('relevance_score', 0):.0%}\n"
        
        return summary


def test_strategist():
    """Test the Strategist Agent"""
    agent = StrategistAgent()
    
    # Test analysis
    results = agent.analyze_company(
        company_name="Acme Corporation",
        industry="Manufacturing",
        ticker="ACME",
        website="https://www.acme.com"
    )
    
    print("\n" + "="*60)
    print("📋 STRATEGIST AGENT RESULTS")
    print("="*60)
    
    print("\n🎯 Strategic Alignment:")
    alignment = results['strategic_analysis']
    print(f"   Alignment Score: {alignment['alignment_score']:.0%}")
    print(f"   High Priority Areas: {len(alignment['high_priority_areas'])}")
    
    print("\n🔍 Friction Points Identified:")
    print(f"   Total: {len(results['friction_points'])}")
    
    print("\n💡 Recommendations:")
    for i, rec in enumerate(results['recommendations'], 1):
        print(f"   {i}. {rec}")
    
    print(agent.get_value_pillars_summary())


if __name__ == "__main__":
    test_strategist()

# Made with Bob
