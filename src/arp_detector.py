"""
=========================================================
ARP Spoofing Detector
Mini Network IDS
=========================================================

Detects possible ARP Spoofing attacks by monitoring
changes in IP-to-MAC mappings.
"""

from scapy.all import ARP

from src.database import save_alert
from src.capture_manager import (
    increment_alert,
    get_session_id
)
from src.logger import logger
from src.utils import current_time

# --------------------------------------------------
# Known IP -> MAC Mapping
# --------------------------------------------------

arp_table = {}

# --------------------------------------------------
# Prevent Duplicate Alerts
# --------------------------------------------------

recent_alerts = set()


def detect_arp(packet):
    """
    Detect ARP Spoofing attacks.
    """

    try:

        if not packet.haslayer(ARP):
            return

        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        # First observation
        if ip not in arp_table:

            arp_table[ip] = mac
            return

        # MAC changed
        if arp_table[ip] != mac:

            old_mac = arp_table[ip]

            alert_key = (ip, old_mac, mac)

            # Avoid duplicate alerts
            if alert_key in recent_alerts:
                return

            recent_alerts.add(alert_key)

            timestamp = current_time()

            session_id = get_session_id()

            print("\n" + "=" * 70)
            print("⚠ POSSIBLE ARP SPOOFING DETECTED")
            print("=" * 70)
            print(f"Time     : {timestamp}")
            print(f"IP       : {ip}")
            print(f"Old MAC  : {old_mac}")
            print(f"New MAC  : {mac}")
            print("=" * 70)

            save_alert(
                session_id=session_id,
                timestamp=timestamp,
                ip_address=ip,
                old_mac=old_mac,
                new_mac=mac,
                severity="HIGH",
                status="Detected"
            )

            increment_alert()

            logger.warning(
                f"ARP Spoofing | {ip} | {old_mac} -> {mac}"
            )

        # Update mapping
        arp_table[ip] = mac

    except Exception as e:

        logger.exception(f"ARP Detector Error: {e}")