"""
provides an example config class
"""

import logging

LOGGER = logging.getLogger(__name__)


class Config:

    def __init__(self):

        LOGGER.debug('Creating new config')

    debug = True
    log_dir = 'log'
    log_filename = 'app_log.log'
