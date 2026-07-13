import sqlite3
import os

DATABASE = "database/packets.db"


def initialize_database():
    """Create the SQLite database and required tables."""

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # -----------------------------
    # Packets Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS packets (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        session_id INTEGER,

        timestamp TEXT,

        src_ip TEXT,

        dst_ip TEXT,

        src_mac TEXT,

        dst_mac TEXT,

        protocol TEXT,

        length INTEGER

    )
    """)

    # -----------------------------
    # Alerts Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        session_id INTEGER,

        timestamp TEXT,

        ip TEXT,

        old_mac TEXT,

        new_mac TEXT,

        severity TEXT,

        status TEXT

    )
    """)

    # -----------------------------
    # Monitoring Sessions
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        start_time TEXT,

        end_time TEXT,

        interface TEXT,

        packet_count INTEGER DEFAULT 0,

        alert_count INTEGER DEFAULT 0

    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()