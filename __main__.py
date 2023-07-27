# !/usr/bin/python
# -*- coding: utf-8 -*-

from utility.locales import Translation
from utility.constants import KryptoPass
import os, sys

Translation(os.path.join(os.path.dirname(__file__), "locales"))

def main():
    from utility.logger import logger
    logger.info(
        '%(name)s: %(version)s id: %(id)s' % {
        "name":  KryptoPass.NAME.value,
        "version": KryptoPass.VERSION.value,
        "id":KryptoPass.NAMESPACE.value
        })
    import cli

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)