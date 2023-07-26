# !/usr/bin/python
# -*- coding: utf-8 -*-

from utility.locales import Translation
import os, sys

Translation(os.path.join(os.path.dirname(__file__), "locales"))

def main():
    from utility.logger import logger
    logger.debug("")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)