# -*- coding: utf-8 -*-

from logging import DEBUG, ERROR, FATAL, INFO, WARN, getLogger
import logging, os

class SecondsFormatter(logging.Formatter):
    def format(self, record):
        record.relativeCreated /= 1000
        return super().format(record)

class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level
        self.name = "LevelFilter"

    def filter(self, record):
        return record.levelno >= self.level
    
    def setLevel(self, level: int):
        self.level = level

FORMAT = '%(relativeCreated)f | %(name)s | %(levelname)s | [%(message)s]'

logger = getLogger('KryptoPass')
_levelFilter = LevelFilter(ERROR)
_handler = logging.StreamHandler()
_handler.setFormatter(SecondsFormatter(FORMAT))
_handler.addFilter(_levelFilter)
logger.addHandler(_handler)
logger.setLevel(ERROR)

if os.environ.get("KRYPTOPASS_DEBUG"):
    logger.setLevel(DEBUG)
    _levelFilter.setLevel(DEBUG)

def setLevel(level: int):
    if level == 1:
        level = FATAL
    elif level == 2:
        level = ERROR
    elif level == 3:
        level = WARN
    elif level == 4:
        level = INFO
    else:
        level = ERROR

    logger.setLevel(level)
    _levelFilter.setLevel(level)

# from logging import DEBUG, ERROR, FATAL, INFO, WARN, getLogger
# import logging

# LEVELS = {
#     'DEBUG': DEBUG,
#     'INFO': INFO,
#     'WARN': WARN,
#     'ERROR': ERROR,
#     'FATAL': FATAL,
# }

# class SecondsFormatter(logging.Formatter):
#     def format(self, record):
#         record.relativeCreated /= 1000
#         return super().format(record)

# class LevelFilter(logging.Filter):
#     def __init__(self, level):
#         self.level = level

#     def filter(self, record):
#         return record.levelno >= self.level

# FORMAT = '%(relativeCreated)f | %(name)s | %(levelname)s | [%(message)s]'

# logger = getLogger('KryptoPass')
# handler = logging.StreamHandler()
# handler.setFormatter(SecondsFormatter(FORMAT))
# handler.addFilter(LevelFilter(DEBUG))
# logger.addHandler(handler)
# logger.setLevel(DEBUG)
