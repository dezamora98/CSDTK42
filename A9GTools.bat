@echo off
REM Llama al script de Python pasando todos los argumentos

REM Cambiar la ruta al intérprete de Python si es necesario
set PYTHON_EXE=python

REM Cambiar la ruta al script de Python
set SCRIPT_PATH=C:\CSDTK42\A9GTools\main.py

REM Llama al script de Python pasando todos los argumentos
%PYTHON_EXE% %SCRIPT_PATH% %*
