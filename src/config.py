import os

# -------------------------------------------------
# Application
# -------------------------------------------------

APP_NAME = "Mini Network Intrusion Detection System"

APP_VERSION = "1.0.0"

DEBUG = True


# -------------------------------------------------
# Database
# -------------------------------------------------

DATABASE = "database/packets.db"


# -------------------------------------------------
# Folders
# -------------------------------------------------

REPORT_FOLDER = "reports"

OUTPUT_FOLDER = "outputs"

LOG_FOLDER = "logs"

SCREENSHOT_FOLDER = "screenshots"

DOCS_FOLDER = "docs"


# -------------------------------------------------
# Packet Capture
# -------------------------------------------------

DEFAULT_INTERFACE = None

PACKET_LIMIT = 100

STORE_PACKETS = False

PROMISCUOUS_MODE = True


# -------------------------------------------------
# Dashboard
# -------------------------------------------------

AUTO_REFRESH_SECONDS = 3

RECENT_PACKET_LIMIT = 20

RECENT_ALERT_LIMIT = 20


# -------------------------------------------------
# Detection Settings
# -------------------------------------------------

ENABLE_ARP_DETECTION = True

ENABLE_PACKET_LOGGING = True


# -------------------------------------------------
# Report Settings
# -------------------------------------------------

EXPORT_CSV = True

EXPORT_JSON = True

EXPORT_PDF = True


# -------------------------------------------------
# Severity Levels
# -------------------------------------------------

LOW = "LOW"

MEDIUM = "MEDIUM"

HIGH = "HIGH"

CRITICAL = "CRITICAL"


# -------------------------------------------------
# Ensure Required Folders Exist
# -------------------------------------------------

for folder in [
    REPORT_FOLDER,
    OUTPUT_FOLDER,
    LOG_FOLDER,
    SCREENSHOT_FOLDER,
    DOCS_FOLDER
]:
    os.makedirs(folder, exist_ok=True)