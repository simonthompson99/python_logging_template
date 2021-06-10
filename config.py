"""
provides an example config class
"""

import logging

LOGGER = logging.getLogger(__name__)

class Config:

    LOGGER.critical('Creating new config')

    debug = True
    log_dir = 'log'
    log_filename = 'app_log.log'
