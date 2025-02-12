@echo off

set CSDTK_PATH=%~dp0
set SCRIPT_PATH=%CSDTK_PATH%A9GTools\A9GTools.py

set PATH=%CSDTK_PATH%python;%PATH%

python %SCRIPT_PATH% %*

@echo on
