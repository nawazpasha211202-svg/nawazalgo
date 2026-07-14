import logging
import json
import sys
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage(),
        }
        # Include extra fields if provided
        if hasattr(record, "user"):
            log_record["user"] = record.user
        if hasattr(record, "status"):
            log_record["status"] = record.status
        return json.dumps(log_record)

def setup_logger(name="app_logger", log_file="app.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JsonFormatter())

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(JsonFormatter())

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
