# -*- coding: utf-8 -*-

import subprocess
import platform
import gettext
import os

from utility.logger import logger

class Translation():
    def __init__(self, locales: str) -> None:
        languages = ["es", "en"]
        language = self.get_system_language()

        if language not in languages:
            language = "en"

        translation = gettext.translation("kryptopass", locales, [language])
        translation.install()
        gettext.gettext = translation.gettext

    def _get_system_language_windows(self):
        try:
            logger.debug("ESTO ESTÁ MUY LENTO HAY QUE OPTIMIZAR")

            command = [
                'powershell', 'Get-WinSystemLocale | Select-Object Name | Format-Table -HideTableHeaders']
            output = subprocess.check_output(command, text=True).strip()
            language_code = output.split()[0]
            return language_code.split("-")[0]
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None

    def _get_system_language_linux(self):
        try:
            lang_variable = os.environ.get('LANG')
            if lang_variable:
                language_code = lang_variable.split('.')[0]
                return language_code.split('_')[0]
            else:
                return None
        except (KeyError, ValueError):
            return None

    def _get_system_language_mac(self):
        try:
            output = subprocess.check_output(
                ['defaults', 'read', '-g', 'AppleLanguages'], text=True).strip()
            language_code = output.strip('"').split(',')[0]
            return language_code
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None

    def get_system_language(self):
        system_name = platform.system()

        if system_name == 'Windows':
            return self._get_system_language_windows()
        elif system_name == 'Linux':
            return self._get_system_language_linux()
        elif system_name == 'Darwin':  # macOS
            return self._get_system_language_mac()
        else:
            return None
