from scapy.all import sniff

import src.capture_manager as manager

from src.packet_analyzer import analyze_packet
from src.logger import logger


def start_sniffer(interface=None, packet_filter=None):

    logger.info("Packet Sniffer Started")

    while manager.capture_running:

        sniff(
            iface=interface,
            filter=packet_filter,
            prn=analyze_packet,
            store=False,
            timeout=2
        )

    logger.info("Packet Sniffer Stopped")