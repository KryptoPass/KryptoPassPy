@echo off
setlocal enabledelayedexpansion

for /r %%i in (kryptopass.po) do (
    if exist %%i (
        set "kryptopass=%%i"
        msgfmt "%%i" -o "!kryptopass:~0,-2!mo"
    )
)

echo Done! Press any key to exit.
