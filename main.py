"""
BVA Generator Agent - Main Application
Interactive CLI for generating Business Value Assessments
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, Optional
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

# Import agents
from agents.strategist import StrategistAgent
from agents.quant import QuantAgent
from agents.creative import CreativeDirectorAgent

console = Console()


class BVAGeneratorApp:
    """Main application orchestrator for BVA generation"""
    
    def __init__(self):
        self.strategist = StrategistAgent()
        self.quant = QuantAgent()
        self.creative = CreativeDirectorAgent()
        self.client_data = {}
        self.config_path = Path("config/client_config.yaml")
        
    def run(self):
        """Run the BVA Generator application"""
        self._display_welcome()
        
        # Step 1: Gather client information
        self.client_data = self._gather_client_info()
        
        # Step 2: Conduct research
        console.print("\n[bold cyan]🔍 Initiating Company Research...[/bold cyan]")
        strategic_results = self.strategist.analyze_company(
            company_name=self.client_data['name'],
            industry=self.client_data['industry'],
            ticker=self.client_data.get('ticker'),
            website=self.client_data.get('website')
        )
        
        # Step 3: Review findings
        self._display_strategic_findings(strategic_results)
        
        if not self._confirm_continue("Proceed with value calculations?"):
            console.print("[yellow]Process cancelled by user.[/yellow]")
            return
        
        # Step 4: Gather project details
        project_details = self._gather_project_details()
        
        # Step 5: Calculate BVA
        console.print("\n[bold cyan]🧮 Calculating Business Value...[/bold cyan]")
        bva_results = self.quant.calculate_bva(
            client_data=self.client_data,
            friction_points=strategic_results['friction_points'],
            project_cost=project_details['project_cost'],
            time_period_years=project_details['time_period_years']
        )
        
        # Step 6: Display BVA results
        self._display_bva_results(bva_results)
        
        if not self._confirm_continue("Generate report?"):
            console.print("[yellow]Report generation cancelled.[/yellow]")
            return
        
        # Step 7: Synthesize and generate report
        console.print("\n[bold cyan]🎨 Synthesizing Findings...[/bold cyan]")
        synthesis = self.creative.synthesize_bva(
            client_data=self.client_data,
            strategic_analysis=strategic_results,
            bva_calculations=bva_results
        )
        
        # Step 8: Generate report documents
        export_pdf = questionary.confirm(
            "Export report as PDF? (requires additional setup)",
            default=False
        ).ask()
        
        report_paths = self.creative.generate_report(
            client_data=self.client_data,
            research_data=strategic_results['research_results'],
            calculations=bva_results,
            synthesis=synthesis,
            export_pdf=export_pdf
        )
        
        # Step 9: Display completion
        self._display_completion(report_paths)
        
        # Step 10: Save configuration
        self._save_configuration()
    
    def _display_welcome(self):
        """Display welcome message"""
        console.clear()
        welcome_text = """
[bold cyan]╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           BVA GENERATOR AGENT                             ║
║           Business Value Assessment System                ║
║                                                           ║
║           Powered by Multi-Agent Architecture             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝[/bold cyan]

[bold]Welcome to the BVA Generator![/bold]

This system will guide you through:
  1. 📝 Client information gathering
  2. 🔍 Automated company research
  3. 🎯 Business priority identification
  4. 🧮 ROI and value calculations
  5. 📄 Professional report generation

Let's get started!
"""
        console.print(Panel(welcome_text, border_style="cyan"))
        input("\nPress Enter to continue...")
    
    def _gather_client_info(self) -> Dict:
        """Gather client information interactively"""
        console.print("\n[bold cyan]📝 Step 1: Client Information[/bold cyan]\n")
        
        client_data = {}
        
        # Company name
        client_data['name'] = questionary.text(
            "Company Name:",
            validate=lambda text: len(text) > 0 or "Company name is required"
        ).ask()
        
        # Industry
        industries = [
            "Manufacturing",
            "Retail",
            "Financial Services",
            "Healthcare",
            "Technology",
            "Telecommunications",
            "Other"
        ]
        
        client_data['industry'] = questionary.select(
            "Industry:",
            choices=industries
        ).ask()
        
        if client_data['industry'] == "Other":
            client_data['industry'] = questionary.text(
                "Please specify industry:"
            ).ask()
        
        # IBM Product/Solution
        products = [
            "IBM watsonx",
            "IBM Cloud",
            "IBM Security",
            "IBM Automation",
            "IBM Data & AI",
            "IBM Consulting",
            "Other IBM Solution"
        ]
        
        client_data['product'] = questionary.select(
            "IBM Product/Solution:",
            choices=products
        ).ask()
        
        if client_data['product'] == "Other IBM Solution":
            client_data['product'] = questionary.text(
                "Please specify solution:"
            ).ask()
        
        # Optional: Stock ticker
        has_ticker = questionary.confirm(
            "Is this a publicly traded company?",
            default=False
        ).ask()
        
        if has_ticker:
            client_data['ticker'] = questionary.text(
                "Stock Ticker Symbol (optional):",
                default=""
            ).ask()
        
        # Optional: Website
        client_data['website'] = questionary.text(
            "Company Website (optional):",
            default=""
        ).ask()
        
        # Display summary
        self._display_client_summary(client_data)
        
        return client_data
    
    def _display_client_summary(self, client_data: Dict):
        """Display client information summary"""
        table = Table(title="Client Information Summary", show_header=False)
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="white")
        
        table.add_row("Company", client_data['name'])
        table.add_row("Industry", client_data['industry'])
        table.add_row("Solution", client_data['product'])
        
        if client_data.get('ticker'):
            table.add_row("Ticker", client_data['ticker'])
        if client_data.get('website'):
            table.add_row("Website", client_data['website'])
        
        console.print("\n")
        console.print(table)
    
    def _display_strategic_findings(self, results: Dict):
        """Display strategic analysis findings"""
        console.print("\n[bold cyan]📊 Strategic Analysis Results[/bold cyan]\n")
        
        # Value Pillars
        console.print("[bold]🎯 Identified Value Pillars:[/bold]")
        for i, pillar in enumerate(results['value_pillars'][:5], 1):
            console.print(
                f"  {i}. [green]{pillar['priority']}[/green] "
                f"(Relevance: {pillar['relevance_score']:.0%})"
            )
        
        # Strategic Alignment
        alignment = results['strategic_analysis']
        console.print(f"\n[bold]📈 Strategic Alignment Score:[/bold] {alignment['alignment_score']:.0%}")
        
        # Friction Points
        console.print(f"\n[bold]🔍 Friction Points Identified:[/bold] {len(results['friction_points'])}")
        for i, fp in enumerate(results['friction_points'][:5], 1):
            console.print(f"  {i}. {fp['friction_point']} ({fp['severity']} severity)")
        
        console.print()
    
    def _gather_project_details(self) -> Dict:
        """Gather project-specific details"""
        console.print("\n[bold cyan]💼 Step 2: Project Details[/bold cyan]\n")
        
        project_details = {}
        
        # Project cost
        cost_str = questionary.text(
            "Estimated Project Cost (USD):",
            validate=lambda text: text.replace(',', '').replace('.', '').isdigit() or "Please enter a valid number"
        ).ask()
        
        project_details['project_cost'] = float(cost_str.replace(',', ''))
        
        # Time period
        project_details['time_period_years'] = int(questionary.select(
            "Analysis Time Period:",
            choices=["1 year", "3 years", "5 years"],
            default="3 years"
        ).ask().split()[0])
        
        return project_details
    
    def _display_bva_results(self, bva: Dict):
        """Display BVA calculation results"""
        console.print("\n[bold cyan]💰 Business Value Assessment Results[/bold cyan]\n")
        
        summary = bva['summary']
        roi = bva['roi']
        payback = bva['payback']
        breakdown = bva['value_breakdown']
        
        # Create results table
        table = Table(title="Financial Metrics", show_header=True)
        table.add_column("Metric", style="cyan", width=30)
        table.add_column("Value", style="green", justify="right")
        
        table.add_row("Total Annual Value", f"${summary['total_annual_value']:,.0f}")
        table.add_row(
            f"{summary['time_period_years']}-Year Total Value",
            f"${summary['total_value_over_period']:,.0f}"
        )
        table.add_row("Project Investment", f"${summary['project_cost']:,.0f}")
        table.add_row("Net Value", f"${summary['net_value']:,.0f}")
        table.add_row("Return on Investment", f"{roi['roi_percentage']:.1f}%")
        table.add_row("Payback Period", f"{payback['payback_months']:.1f} months")
        
        console.print(table)
        
        # Value breakdown
        console.print("\n[bold]🎯 Value Breakdown:[/bold]")
        console.print(f"  • Efficiency Savings: ${breakdown['efficiency_savings']:,.0f}")
        console.print(f"  • Risk Mitigation: ${breakdown['risk_mitigation']:,.0f}")
        console.print(f"  • Growth Enablement: ${breakdown['growth_enablement']:,.0f}")
        console.print()
    
    def _display_completion(self, report_paths: Dict):
        """Display completion message"""
        completion_text = f"""
[bold green]✅ BVA Generation Complete![/bold green]

[bold]📄 Generated Reports:[/bold]
  • Word Document: {report_paths['docx_path']}
"""
        
        if report_paths.get('pdf_path'):
            completion_text += f"  • PDF Document: {report_paths['pdf_path']}\n"
        
        completion_text += """
[bold]Next Steps:[/bold]
  1. Review the generated report
  2. Customize as needed for your client
  3. Share with stakeholders
  4. Track implementation progress

Thank you for using the BVA Generator!
"""
        
        console.print(Panel(completion_text, border_style="green"))
    
    def _confirm_continue(self, message: str) -> bool:
        """Ask user to confirm continuation"""
        return questionary.confirm(message, default=True).ask()
    
    def _save_configuration(self):
        """Save configuration for future use"""
        save = questionary.confirm(
            "Save this configuration for future use?",
            default=True
        ).ask()
        
        if save:
            try:
                # Update config file
                config = {
                    'client_info': self.client_data,
                    'last_updated': str(Path.cwd())
                }
                
                with open(self.config_path, 'w') as f:
                    yaml.dump(config, f, default_flow_style=False)
                
                console.print("[green]✓ Configuration saved successfully![/green]")
            except Exception as e:
                console.print(f"[yellow]⚠ Could not save configuration: {e}[/yellow]")


def main():
    """Main entry point"""
    try:
        app = BVAGeneratorApp()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Process interrupted by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        console.print("[yellow]Please check your inputs and try again.[/yellow]")
        sys.exit(1)


if __name__ == "__main__":
    main()

# Made with Bob
