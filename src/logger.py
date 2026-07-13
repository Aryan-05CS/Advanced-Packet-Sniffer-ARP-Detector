import logging
import os
from logging.handlers import RotatingFileHandler

# ------------------------------------
# Create Logs Folder
# ------------------------------------

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")


# ------------------------------------
# Logger Configuration
# ------------------------------------

logger = logging.getLogger("MiniNIDS")

logger.setLevel(logging.INFO)

# Avoid duplicate handlers
if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File Logger
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=2 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    # Console Logger
    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)