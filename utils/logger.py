# utils/logger.py
import logging
import logging.handlers
import os

LOG_FILE = 'logs/automation.log'

def setup_logger(name):
    """Initializes and returns a robust, rotating file logger."""
    
    # Ensure log directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 1. Console Handler (for real-time feedback)
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)
        c_format = logging.Formatter('%(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)

    # 2. Rotating File Handler (for robust storage)
    if not any(isinstance(h, logging.handlers.RotatingFileHandler) for h in logger.handlers):
        # Rotates file at 10MB, keeping 5 backup copies
        f_handler = logging.handlers.RotatingFileHandler(
            LOG_FILE, maxBytes=10*1024*1024, backupCount=5
        )
        f_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)

    return logger