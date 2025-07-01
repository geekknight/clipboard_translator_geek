# 🎯 TL/DR - English
A Python script to automatically translate any text copied to the clipboard into another language chosen by the user.
The result is stored in the clipboard memory for you to paste wherever you want.<br>
**Nutshell: copy the text in one language and paste it into another.**

----------------

<br><br>

# 🔤 Tradutor de Clipboard

Um script Python simples e eficiente para traduzir automaticamente qualquer texto copiado no clipboard para português brasileiro.

## ✨ Características

- 🚀 **Tradução instantânea** de qualquer texto no clipboard
- 🌐 **Detecção automática** do idioma de origem
- 📋 **Cópia automática** da tradução de volta para o clipboard
- 🎯 **Interface amigável** com feedback visual colorido
- 🔍 **Sistema de logs** para debugging
- ⚡ **Leve e rápido** - execução em segundos

## 🛠️ Instalação

### Pré-requisitos

- Python 3.11 ou superior

### 1. Clone ou baixe o script

```bash
# Opção 1: Clone o repositório (se aplicável)
git clone https://github.com/geekknight/clipboard_translator_geek.git
cd clipboard_translator_geek

# Opção 2: Baixe apenas o arquivo clipboard_translator_geek.py
```

### 2. Instale as dependências

```bash
pip install pyperclip googletrans==4.0.0-rc1
```

**Nota importante**: Use especificamente a versão `4.0.0-rc1` da googletrans para evitar problemas de compatibilidade.

**ATENÇÃO:**: A biblioteca `googletrans` é uma API não oficial e gratuita para Python que implementa funcionalidades do Google Translate, permitindo detectar idiomas e traduzir textos de forma ilimitada e rápida, utilizando a API Ajax do Google Translate. Verificar a documentação em: [pypi.org/project/googletrans/](https://pypi.org/project/googletrans/)


### 3. (Opcional) Crie um ambiente virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências no ambiente virtual
pip install pyperclip googletrans==4.0.0-rc1
```

## 🚀 Como Usar

### Uso Básico

1. **Copie qualquer texto** para o clipboard (Ctrl+C / Cmd+C)
2. **Execute o script**:
   ```bash
   python clipboard_translator_geek.py
   ```
3. **Veja a tradução** na tela e ela será automaticamente copiada para o clipboard
4. **Cole onde quiser** (Ctrl+V / Cmd+V)

### Exemplo de Uso

```
🔤 Tradutor de Clipboard
==================================================
📋 Texto original (23 caracteres):
   Hello, how are you?

🌐 Texto traduzido:
   Olá, como você está?

✅ Tradução copiada para o clipboard!

✨ Tradução concluída com sucesso!
```

## 🎯 Funcionalidades Detalhadas

### Detecção Automática de Idioma
- O script detecta automaticamente o idioma do texto original
- Se o texto já estiver em português, não realiza tradução desnecessária

### Tratamento de Erros
- ✅ Clipboard vazio ou com apenas espaços
- ✅ Problemas de conexão com a internet
- ✅ Textos não traduzíveis
- ✅ Erros de acesso ao clipboard

### Sistema de Logs
- Logs detalhados para debugging
- Informações sobre idioma detectado
- Registro de erros para troubleshooting

## ⚙️ Configuração Avançada

### Mudando o Idioma de Destino

Para traduzir para outros idiomas, modifique a linha no código:

```python
translator = ClipboardTranslator(target_language='pt')  # Português
translator = ClipboardTranslator(target_language='en')  # Inglês
translator = ClipboardTranslator(target_language='es')  # Espanhol
translator = ClipboardTranslator(target_language='fr')  # Francês
```

### Códigos de Idioma Suportados

| Idioma | Código |
|--------|--------|
| Português | `pt` |
| Inglês | `en` |
| Espanhol | `es` |
| Francês | `fr` |
| Alemão | `de` |
| Italiano | `it` |
| Japonês | `ja` |
| Chinês | `zh` |
| Russo | `ru` |

[Lista completa de códigos de idioma](https://cloud.google.com/translate/docs/languages)

## 🔧 Automação

### Windows - Atalho de Teclado

1. Crie um arquivo `.bat`:
```batch
@echo off
cd /d "C:\caminho\para\seu\script"
python clipboard_translator_geek.py
pause
```

2. Crie um atalho e configure uma tecla de acesso rápido

----------------

### Windows - Atalho de Teclado e instalação das dependências em ambiente virtual

***Importante***: Desse modo instala as dependências de forma isolada e não global - melhor forma de usar.
<br>
Arquivos `.bat` para uso já pronto na pasta `./automation_bat`

1. Crie um arquivo `setup_clipboard_translator_geek.bat` para fazer o setup do ambiente virtual na pasta que tem o script:

```batch
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
```

2. Execute o setup_clipboard_translator_geek.bat - ***só precisa fazer isso uma única vez***

3. Crie um arquivo `clipboard_translator_geek.bat` com o script de traduzir:

```batch
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
```

4. Execute o script de traduzir sempre que precisar.

***Atenção: todos os arquivos devem estar na mesma pasta**

----------------

### Linux/Mac - Alias

Adicione ao seu `.bashrc` ou `.zshrc`:
```bash
alias translate="python /caminho/para/clipboard_translator_geek.py"
```

### Script de Execução Rápida

Crie um script `translate.sh` (Linux/Mac):
```bash
#!/bin/bash
cd "$(dirname "$0")"
python3 clipboard_translator_geek.py
```

----------------

## 🐛 Solução de Problemas

### Erro: "No module named 'pyperclip'"
```bash
pip install pyperclip
```

### Erro: "AttributeError: 'NoneType'"
- Verifique se há texto no clipboard
- Teste com um texto simples primeiro

### Erro de Conexão
- Verifique sua conexão com a internet
- Alguns firewalls podem bloquear o Google Translate

### Problema no Linux com Clipboard
```bash
# Instale xclip ou xsel
sudo apt-get install xclip
# ou
sudo apt-get install xsel
```

----------------

## 📝 Exemplos de Uso

### Tradução de Documentos
1. Copie parágrafo por parágrafo
2. Execute o script
3. Cole a tradução no documento de destino

### Tradução de E-mails
1. Copie o texto do e-mail
2. Execute o script
3. Use a tradução para responder

### Tradução de Código/Comentários
1. Copie comentários em outros idiomas
2. Execute o script
3. Substitua pelos comentários traduzidos

----------------

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ⭐ Suporte

Se este script foi útil para você, considere dar uma ⭐ no repositório!
[https://github.com/geekknight/clipboard_translator_geek/](https://github.com/geekknight/clipboard_translator_geek/

Para reportar bugs ou sugerir melhorias, abra uma [issue](https://github.com/geekknight/clipboard_translator_geek/issues).

---

**Desenvolvido por geekknight e claude para facilitar traduções rápidas e eficientes.** <br>
**Developed by geekknight and claude to facilitate fast and efficient translations.**