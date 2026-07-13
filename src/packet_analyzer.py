from scapy.all import Ether, IP, IPv6, TCP, UDP, ICMP, ARP

from src.database import save_packet
from src.capture_manager import (
    increment_packet,
    get_session_id
)
from src.detector_manager import run_detectors
from src.logger import logger
from src.utils import current_time


def analyze_packet(packet):

    try:

        src_ip = "N/A"
        dst_ip = "N/A"

        src_mac = "N/A"
        dst_mac = "N/A"

        protocol = "UNKNOWN"

        if packet.haslayer(Ether):

            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst

        if packet.haslayer(IP):

            src_ip = packet[IP].src
            dst_ip = packet[IP].dst

        elif packet.haslayer(IPv6):

            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst

        if packet.haslayer(TCP):

            protocol = "TCP"

        elif packet.haslayer(UDP):

            protocol = "UDP"

        elif packet.haslayer(ICMP):

            protocol = "ICMP"

        elif packet.haslayer(ARP):

            protocol = "ARP"

            src_ip = packet[ARP].psrc
            dst_ip = packet[ARP].pdst

        elif packet.haslayer(IPv6):

            protocol = "IPv6"

        save_packet(

            get_session_id(),

            current_time(),

            src_ip,

            dst_ip,

            src_mac,

            dst_mac,

            protocol,

            len(packet)

        )

        increment_packet()

        run_detectors(packet)

        logger.info(
            f"{protocol} | {src_ip} -> {dst_ip}"
        )

    except Exception as e:

        logger.exception(e)