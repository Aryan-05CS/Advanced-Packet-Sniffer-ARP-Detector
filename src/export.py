"""
=========================================================
Export Manager
Mini Network IDS
=========================================================

Provides a simple interface for generating
all reports from the Report Generator.
"""

import os
from src.report_generator import ReportGenerator
from src.logger import logger


class ExportManager:
    """
    Handles report exporting.
    """

    def __init__(self):
        self.generator = ReportGenerator()

    def export_csv(self):
        """Generate CSV report."""
        return self.generator.export_csv()

    def export_json(self):
        """Generate JSON report."""
        return self.generator.export_json()

    def export_pdf(self):
        """Generate PDF report."""
        return self.generator.export_pdf()

    def export_all(self):
        """
        Generate all supported reports.
        """

        logger.info("Generating all reports...")

        reports = {
            "csv": self.export_csv(),
            "json": self.export_json(),
            "pdf": self.export_pdf()
        }

        logger.info("All reports generated successfully.")

        return reports


def export_reports():
    """
    Convenience function for exporting all reports.
    """

    manager = ExportManager()

    return manager.export_all()


if __name__ == "__main__":

    reports = export_reports()

    print("\nGenerated Reports:\n")

    for report_type, path in reports.items():
        print(f"{report_type.upper():5} : {os.path.abspath(path)}")