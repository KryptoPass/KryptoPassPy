# -*- coding: utf-8 -*-

import gettext

class Translation():
    def __init__(self, locales: str) -> None:
        self._translation = gettext.translation("kryptopass", locales, ["es"])
        self._translation.install()
        gettext.gettext  = self._translation.gettext