"""
Capture Manager

Manages packet capture sessions, runtime statistics,
packet counters, alert counters, and application state.
"""

from threading import Lock
from datetime import datetime

from src.logger import logger


# =====================================================
# Global Capture State
# =====================================================

capture_running = False

_capture_lock = Lock()


# =====================================================
# Session Information
# =====================================================

_session_id = 1

_start_time = None

_stop_time = None


# =====================================================
# Runtime Counters
# =====================================================

_packet_count = 0

_alert_count = 0


# =====================================================
# Capture Control
# =====================================================

def start_capture():
    """
    Start a new packet capture session.
    """

    global capture_running
    global _packet_count
    global _alert_count
    global _start_time
    global _stop_time

    with _capture_lock:

        capture_running = True

        _packet_count = 0
        _alert_count = 0

        _start_time = datetime.now()
        _stop_time = None

    logger.info("Capture Started")


def stop_capture():
    """
    Stop packet capture.
    """

    global capture_running
    global _stop_time

    with _capture_lock:

        capture_running = False
        _stop_time = datetime.now()

    logger.info("Capture Stopped")


# =====================================================
# Session Management
# =====================================================

def get_session_id():
    """
    Return current capture session ID.
    """

    return _session_id


def set_session_id(session_id):
    """
    Set session ID from database.
    """

    global _session_id

    _session_id = session_id


# =====================================================
# Packet Counter
# =====================================================

def increment_packet():

    global _packet_count

    with _capture_lock:

        _packet_count += 1


def get_packet_count():

    return _packet_count


# =====================================================
# Alert Counter
# =====================================================

def increment_alert():

    global _alert_count

    with _capture_lock:

        _alert_count += 1


def get_alert_count():

    return _alert_count


# =====================================================
# Runtime Information
# =====================================================

def get_runtime():

    if _start_time is None:
        return 0

    end = _stop_time if _stop_time else datetime.now()

    return round((end - _start_time).total_seconds(), 2)


def get_statistics():
    """
    Return live capture statistics.
    """

    return {

        "session_id": _session_id,

        "capture_running": capture_running,

        "packets": _packet_count,

        "alerts": _alert_count,

        "runtime_seconds": get_runtime(),

        "started_at": (
            _start_time.strftime("%Y-%m-%d %H:%M:%S")
            if _start_time else None
        ),

        "stopped_at": (
            _stop_time.strftime("%Y-%m-%d %H:%M:%S")
            if _stop_time else None
        )

    }


# =====================================================
# Reset Session
# =====================================================

def reset_statistics():
    """
    Reset counters without affecting session ID.
    """

    global _packet_count
    global _alert_count

    with _capture_lock:

        _packet_count = 0
        _alert_count = 0

    logger.info("Capture statistics reset")