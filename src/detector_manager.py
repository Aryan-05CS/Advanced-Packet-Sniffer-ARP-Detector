"""
Detector Manager

Runs all enabled detection modules on every captured packet.
This makes it easy to add new detectors without modifying
the packet analyzer.
"""

from src.arp_detector import detect_arp
from src.logger import logger


def run_detectors(packet):
    """
    Execute all enabled detectors.
    """

    try:

        # ARP Spoofing Detection
        detect_arp(packet)

        # -----------------------------
        # Future Detection Modules
        # -----------------------------

        # detect_port_scan(packet)
        # detect_dns_spoofing(packet)
        # detect_syn_flood(packet)
        # detect_icmp_flood(packet)

    except Exception as e:

        logger.error(f"Detector Manager Error: {e}")