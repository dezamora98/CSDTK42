@echo off
set VENV_PATH=C:\CSDTK42\A9GTools
set PYTHON_EXE=%VENV_PATH%\bin\python.exe
set SCRIPT_PATH=C:\CSDTK42\A9GTools\scripts\main.py

if exist %VENV_PATH% (
    echo Activating virtual environment...
    %PYTHON_EXE% %SCRIPT_PATH% %*
) else (
    echo Virtual environment not found. Please create the virtual environment first.
)
