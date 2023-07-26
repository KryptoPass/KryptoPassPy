@echo off
setlocal enabledelayedexpansion

for /r %%i in (kryptopass.po) do (
    if exist %%i (
        msgfmt "%%i" -o "%%~dpikryptopass.mo"
    )
)

echo Done! Press any key to exit.
pause > nul
