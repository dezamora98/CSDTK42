@echo off
setlocal

set CSDTK42_PATH=%~dp0
set VENV_PY=%CSDTK42_PATH%A9GTools\bin\python.exe
set SCRIPT_PATH=%CSDTK42_PATH%A9GTools\scripts\A9GTools.py

where python >nul 2>&1
if %errorlevel%==0 (
    for /f "tokens=2 delims== " %%i in ('python --version 2^>nul') do set version=%%i
    echo %version% | findstr /C:"3.11" >nul
    if %errorlevel%==0 (
        set PYTHON_CMD=python
    )
) else (
    where py >nul 2>&1
    if %errorlevel%==0 (
        for /f "tokens=2 delims== " %%i in ('py --version 2^>nul') do set version=%%i
        echo %version% | findstr /C:"3.11" >nul
        if %errorlevel%==0 (
            set PYTHON_CMD=py
        )
    )
)

if defined PYTHON_CMD (
    %VENV_ACTIVATE%
    %VENV_PY% %SCRIPT_PATH% %*
    %VENV_DESACTIVATE%
) else (
    echo Python 3.11 is not installed.
)

endlocal
