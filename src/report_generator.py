"""
=========================================================
Report Generator
Mini Network IDS
=========================================================

Generates CSV, JSON and PDF reports for
captured packets and detected alerts.
"""

import os
import csv
import json
import sqlite3
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors

from src.config import REPORT_FOLDER
from src.logger import logger


DATABASE = "database/packets.db"


class ReportGenerator:

    def __init__(self):

        os.makedirs(REPORT_FOLDER, exist_ok=True)

        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # -------------------------------------------------
    # Database
    # -------------------------------------------------

    def get_connection(self):

        return sqlite3.connect(DATABASE)

    # -------------------------------------------------
    # Packets
    # -------------------------------------------------

    def fetch_packets(self):

        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                timestamp,
                source_ip,
                destination_ip,
                protocol,
                packet_length
            FROM packets
            ORDER BY id DESC
        """)

        data = cursor.fetchall()

        conn.close()

        return data

    # -------------------------------------------------
    # Alerts
    # -------------------------------------------------

    def fetch_alerts(self):

        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                timestamp,
                ip_address,
                old_mac,
                new_mac,
                severity,
                status
            FROM alerts
            ORDER BY id DESC
        """)

        data = cursor.fetchall()

        conn.close()

        return data

    # -------------------------------------------------
    # CSV
    # -------------------------------------------------

    def export_csv(self):

        filename = os.path.join(
            REPORT_FOLDER,
            f"packets_{self.timestamp}.csv"
        )

        packets = self.fetch_packets()

        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Timestamp",
                "Source IP",
                "Destination IP",
                "Protocol",
                "Length"
            ])

            writer.writerows(packets)

        logger.info(f"CSV Report Saved : {filename}")

        return filename

    # -------------------------------------------------
    # JSON
    # -------------------------------------------------

    def export_json(self):

        filename = os.path.join(
            REPORT_FOLDER,
            f"packets_{self.timestamp}.json"
        )

        packets = self.fetch_packets()

        output = []

        for row in packets:

            output.append({

                "timestamp": row[0],
                "source_ip": row[1],
                "destination_ip": row[2],
                "protocol": row[3],
                "length": row[4]

            })

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(output, file, indent=4)

        logger.info(f"JSON Report Saved : {filename}")

        return filename

    # -------------------------------------------------
    # PDF
    # -------------------------------------------------

    def export_pdf(self):

        filename = os.path.join(
            REPORT_FOLDER,
            f"report_{self.timestamp}.pdf"
        )

        packets = self.fetch_packets()
        alerts = self.fetch_alerts()

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph("<b>Mini Network IDS Report</b>", styles["Title"])
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"Generated : {datetime.now()}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"Total Packets : {len(packets)}",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"Total Alerts : {len(alerts)}",
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 20))

        packet_table = [

            [
                "Time",
                "Source",
                "Destination",
                "Protocol",
                "Length"
            ]

        ]

        for row in packets[:30]:

            packet_table.append(list(row))

        table = Table(packet_table)

        table.setStyle(TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige)

        ]))

        story.append(table)

        story.append(Spacer(1, 20))

        story.append(
            Paragraph("<b>Detected Alerts</b>", styles["Heading1"])
        )

        alert_table = [[
            "Time",
            "IP",
            "Old MAC",
            "New MAC",
            "Severity"
        ]]

        for row in alerts[:20]:

            alert_table.append(row[:5])

        table = Table(alert_table)

        table.setStyle(TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.red),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke)

        ]))

        story.append(table)

        doc.build(story)

        logger.info(f"PDF Report Saved : {filename}")

        return filename

    # -------------------------------------------------
    # Export All
    # -------------------------------------------------

    def export_all(self):

        return {

            "csv": self.export_csv(),

            "json": self.export_json(),

            "pdf": self.export_pdf()

        }