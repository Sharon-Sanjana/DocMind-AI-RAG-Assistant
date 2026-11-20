"""
Logger Utility

Provides a reusable logger for all modules.
"""

import logging

from config.logging_config import *

def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Args:
        name: Usually __name__

    Returns:
        logging.Logger
    """
    return logging.getLogger(name)