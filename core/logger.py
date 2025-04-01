import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure the logs directory exists
log_dir = 'c:/Users/Thela/OneDrive/Desktop/HIDS-Windows/logs'
os.makedirs(log_dir, exist_ok=True)

# Configure logging to write to a rotating file
log_file = f"{log_dir}/detections.log"
handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=3)  # 5 MB per file, 3 backups
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger('detections_log')
logger.setLevel(logging.DEBUG)  # Set to DEBUG for development
logger.addHandler(handler)


# Example usage: Log flagged IPs
def log_flagged_ip(ip_address):
    """
    Logs a flagged IP address to the detections log file.  
    """
    logger.warning(f"Flagged IP detected: {ip_address}")

# Example: Call this function when a flagged IP is detected
# log_flagged_ip("192.168.1.1")