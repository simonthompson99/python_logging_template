"""
creates the console and file handlers for logging
file handler is a timed rotating handler (rotating each day) and
keeping backups for a week
alternative would be rotatingfilehandler with some maxBytes so that we only
keep a certain size of log, not certain time
"""
import os
import logging
from logging.config import dictConfig
from config import Config

def setup_logger(c):
    """
    set up logging handlers and formatters
    :params c: a config object that contains something to say whether we are
    in debug mode (consoldHandler level will be set to debug), and log_dir and
    log_filenames
    """

    # set up log directory if it doesn't exist
    basedir = os.path.abspath(os.path.dirname(__file__))
    log_dir = os.path.join(basedir, c.log_dir)
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    # log config
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'fFormatter': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'cFormatter': {
                'class': 'logging.Formatter',
                'format': '%(name)s - %(levelname)s - %(message)s'
            }
        },
        'handlers': {
            'consoleHandler': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG' if c.debug else 'INFO',
                'formatter': 'cFormatter'
            },
            'fileHandler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(log_dir, c.log_filename),
                'formatter': 'fFormatter',
                'when': 'd',
                'interval': 1,
                'backupCount': 7
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['consoleHandler', 'fileHandler']
        }
    }

    # configure logging
    dictConfig(log_config)


if __name__ == "__main__":

    # need to set up the logger early on otherwise logging is lost
    # e.g. when creating a Config object we log but don't see it (as debug level
    # not present on console by default)
    c = Config()
    setup_logger(c)
    # but now we see it as we have configured the logging to print out debug
    d = Config()

    LOGGER = logging.getLogger(__name__)
    LOGGER.debug('Example debug msg')

    # other levels in descending order of seriousness:
    # critical
    # error
    # warning
    # info
