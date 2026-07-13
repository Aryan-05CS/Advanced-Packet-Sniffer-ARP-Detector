"""
=========================================================
Statistics Manager
Mini Network IDS
=========================================================
"""

import sqlite3
from collections import Counter

DATABASE = "database/packets.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def _count(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    value = cursor.fetchone()[0]
    conn.close()
    return value


def dashboard_stats():
    return {
        "packets": _count("SELECT COUNT(*) FROM packets"),
        "alerts": _count("SELECT COUNT(*) FROM alerts"),
        "tcp": _count("SELECT COUNT(*) FROM packets WHERE protocol='TCP'"),
        "udp": _count("SELECT COUNT(*) FROM packets WHERE protocol='UDP'"),
        "icmp": _count("SELECT COUNT(*) FROM packets WHERE protocol='ICMP'"),
        "arp": _count("SELECT COUNT(*) FROM packets WHERE protocol='ARP'"),
        "ipv6": _count("SELECT COUNT(*) FROM packets WHERE protocol='IPv6'")
    }


def top_source_ips(limit=10):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT source_ip, COUNT(*)
        FROM packets
        GROUP BY source_ip
        ORDER BY COUNT(*) DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def top_destination_ips(limit=10):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT destination_ip, COUNT(*)
        FROM packets
        GROUP BY destination_ip
        ORDER BY COUNT(*) DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def protocol_distribution():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT protocol
        FROM packets
    """)

    rows = cursor.fetchall()

    conn.close()

    counter = Counter()

    for row in rows:
        counter[row[0]] += 1

    return dict(counter)


def recent_packets(limit=20):

    conn = get_connection()

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
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def recent_alerts(limit=20):

    conn = get_connection()

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
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def traffic_history(limit=50):
    """
    Returns packet timestamps for a live traffic chart.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp
        FROM packets
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows