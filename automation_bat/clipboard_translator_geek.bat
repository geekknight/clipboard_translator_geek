@echo off
title Tradutor de Clipboard
color 0A

REM Ativar ambiente virtual
if exist "translator_env\Scripts\activate" (
    call translator_env\Scripts\activate
)

REM Executar script
python clipboard_translator_geek.py

echo.
pause
