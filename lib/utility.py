""" lib/utility.py
This module holds functions that are very commonly used in different modules.
"""

import logging
from datetime import datetime

from configs.config import LOG_MESSAGES


def display_log(message) -> None:
    """
    This is a utility function which print the required message to
    logs and also append it log list to render it to user's UI.
    
    Args:
        message: The incoming message to log.

    Returns:
        None
    """
    logging.info(message)
    current_time = datetime.now().replace(microsecond=0)
    log_message = f"{current_time} - {message}"
    LOG_MESSAGES.append(log_message)
    
