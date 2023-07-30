# !/usr/bin/python
# -*- coding: utf-8 -*-

from utility.constants import KryptoPass as KP
from utility.locales import Translation
from utility.logger import logger
import os, sys

logger.debug("TEST")
translation = Translation(os.path.join(os.path.dirname(__file__), "locales"))
logger.debug("TEST")

def main():
    from libs.config import init

    Config = init({"language": "en"})

    logger.info(
        '%(name)s: v%(version)s  id: %(id)s' % {
        "name":  KP.NAME.value,
        "version": KP.VERSION.value,
        "id":KP.NAMESPACE.value
        })
    
    import cli

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)