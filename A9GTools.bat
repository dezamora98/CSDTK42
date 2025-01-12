@echo off
setlocal

REM Obtener el directorio del script
set "CSDTK42_PATH=%~dp0"

set VENV_PATH=%CSDTK42_PATH%A9GTools
set PYTHON_EXE=%VENV_PATH%\bin\python.exe
set SCRIPT_PATH=%VENV_PATH%\scripts\main.py

if exist "%VENV_PATH%" (
    "%PYTHON_EXE%" "%SCRIPT_PATH%" %*
) else (
    echo A9GTools not found.
)

endlocal
