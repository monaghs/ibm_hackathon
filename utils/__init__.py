"""
BVA Generator Utilities Package
Core utilities for scraping, calculations, and report generation
"""

from .scraper import CompanyResearcher
from .calculator import FormulaEngine
from .exporter import ReportGenerator

__all__ = [
    'CompanyResearcher',
    'FormulaEngine',
    'ReportGenerator'
]

# Made with Bob
