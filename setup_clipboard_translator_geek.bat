@echo off
title Setup Tradutor de Clipboard
color 0B

echo =================================================
echo      CONFIGURACAO - TRADUTOR DE CLIPBOARD
echo =================================================
echo.

REM Criar ambiente virtual se não existir
if not exist "translator_env" (
    echo 🔧 Criando ambiente virtual...
    python -m venv translator_env
    echo ✅ Ambiente virtual criado!
    echo.
)

REM Ativar ambiente virtual
echo 🔄 Ativando ambiente virtual...
call translator_env\Scripts\activate

REM Atualizar pip
echo 📦 Atualizando pip...
python -m pip install --upgrade pip

REM Instalar dependências
echo 📚 Instalando dependencias...
pip install pyperclip googletrans==4.0.0-rc1

echo.
echo ✅ Configuracao concluida!
echo.
echo Para usar o tradutor, execute: clipboard_translator_geek.bat
echo.
pause
