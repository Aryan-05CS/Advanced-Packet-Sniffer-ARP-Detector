import signal
import sys

from src.config import APP_NAME, APP_VERSION, DEFAULT_INTERFACE
from src.capture_manager import (
    start_capture,
    stop_capture,
    set_session_id
)
from src.database import (
    initialize_database,
    create_session,
    close_session
)
from src.logger import logger
from src.sniffer import start_sniffer
from src.utils import current_time


SESSION_ID = None


def shutdown(sig=None, frame=None):
    global SESSION_ID

    logger.info("Stopping Mini Network IDS...")

    stop_capture()

    if SESSION_ID:
        close_session(SESSION_ID, current_time())

    print("\nCapture Stopped Successfully")

    sys.exit(0)


def main():
    global SESSION_ID

    signal.signal(signal.SIGINT, shutdown)

    print("=" * 60)
    print(APP_NAME)
    print(APP_VERSION)
    print("=" * 60)

    initialize_database()

    SESSION_ID = create_session(current_time())

    set_session_id(SESSION_ID)

    start_capture()

    logger.info("Mini Network IDS Started")

    start_sniffer(interface=DEFAULT_INTERFACE)


if __name__ == "__main__":
    main()