"""
=========================================================
Database Manager
Mini Network IDS
=========================================================
"""

import os
import sqlite3
from contextlib import closing

from src.logger import logger

DATABASE_DIR = "database"
DATABASE_FILE = os.path.join(DATABASE_DIR, "packets.db")

os.makedirs(DATABASE_DIR, exist_ok=True)


def get_connection():
    return sqlite3.connect(DATABASE_FILE)


# =====================================================
# Database Initialization
# =====================================================

def initialize_database():

    with closing(get_connection()) as conn:

        cursor = conn.cursor()

        # ---------------- Sessions ----------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            start_time TEXT,

            end_time TEXT

        )
        """)

        # ---------------- Packets ----------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS packets(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            timestamp TEXT,

            source_ip TEXT,

            destination_ip TEXT,

            source_mac TEXT,

            destination_mac TEXT,

            protocol TEXT,

            packet_length INTEGER
        )
        """)

        # ---------------- Alerts ----------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            timestamp TEXT,

            ip_address TEXT,

            old_mac TEXT,

            new_mac TEXT,

            severity TEXT,

            status TEXT
        )
        """)

        conn.commit()

    logger.info("Database initialized.")


# =====================================================
# Session Management
# =====================================================

def create_session(start_time):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions(start_time)
        VALUES(?)
        """,
        (start_time,)
    )

    conn.commit()

    session = cursor.lastrowid

    conn.close()

    return session


def close_session(session_id, end_time):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE sessions
        SET end_time=?
        WHERE id=?
        """,
        (end_time, session_id)
    )

    conn.commit()

    conn.close()


# =====================================================
# Packet Storage
# =====================================================

def save_packet(

    session_id,

    timestamp,

    source_ip,

    destination_ip,

    source_mac,

    destination_mac,

    protocol,

    packet_length

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO packets(

            session_id,

            timestamp,

            source_ip,

            destination_ip,

            source_mac,

            destination_mac,

            protocol,

            packet_length

        )

        VALUES(?,?,?,?,?,?,?,?)

    """,

    (

        session_id,

        timestamp,

        source_ip,

        destination_ip,

        source_mac,

        destination_mac,

        protocol,

        packet_length

    ))

    conn.commit()

    conn.close()


# =====================================================
# Alert Storage
# =====================================================

def save_alert(

    session_id,

    timestamp,

    ip_address,

    old_mac,

    new_mac,

    severity,

    status

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO alerts(

            session_id,

            timestamp,

            ip_address,

            old_mac,

            new_mac,

            severity,

            status

        )

        VALUES(?,?,?,?,?,?,?)

    """,

    (

        session_id,

        timestamp,

        ip_address,

        old_mac,

        new_mac,

        severity,

        status

    ))

    conn.commit()

    conn.close()


# =====================================================
# Dashboard Statistics
# =====================================================

def total_packets():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM packets")

    value = cursor.fetchone()[0]

    conn.close()

    return value


def total_alerts():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM alerts")

    value = cursor.fetchone()[0]

    conn.close()

    return value


def protocol_count(protocol):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM packets WHERE protocol=?",

        (protocol,)

    )

    value = cursor.fetchone()[0]

    conn.close()

    return value


# =====================================================
# Report Queries
# =====================================================

def fetch_packets(limit=None):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
        SELECT
        timestamp,
        source_ip,
        destination_ip,
        protocol,
        packet_length
        FROM packets
        ORDER BY id DESC
    """

    if limit:
        query += f" LIMIT {limit}"

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    return rows


def fetch_alerts(limit=None):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
        SELECT
        timestamp,
        ip_address,
        old_mac,
        new_mac,
        severity,
        status
        FROM alerts
        ORDER BY id DESC
    """

    if limit:
        query += f" LIMIT {limit}"

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    return rows