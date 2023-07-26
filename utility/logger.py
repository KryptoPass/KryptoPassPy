# -*- coding: utf-8 -*-

from logging import DEBUG, ERROR, FATAL, INFO, WARN, getLogger
import logging

__all__ = ['getLogger', 'INFO', 'WARN', 'DEBUG', 'TRACE', 'ERROR', 'FATAL', 'DEPRECATION']

TRACE = DEBUG - 5
logging.addLevelName(TRACE, 'TRACE')
DEPRECATION = WARN + 5
logging.addLevelName(DEPRECATION, 'DEPRECATION')
LEVELS = {
    'TRACE': TRACE,
    'DEBUG': DEBUG,
    'INFO': INFO,
    'WARN': WARN,
    'DEPRECATION': DEPRECATION,
    'ERROR': ERROR,
    'FATAL': FATAL,
}

class SecondsFormatter(logging.Formatter):
    def format(self, record):
        record.relativeCreated /= 1000
        return super().format(record)

FORMAT = '%(relativeCreated)s | %(name)s | %(levelname)s | [%(message)s]'
logger = getLogger('KryptoPass')
handler = logging.StreamHandler()
handler.setFormatter(SecondsFormatter(FORMAT))
logger.addHandler(handler)
logger.setLevel(DEBUG)
