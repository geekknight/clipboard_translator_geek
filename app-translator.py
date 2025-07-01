#!/usr/bin/env python3
"""
Script para traduzir texto do clipboard automaticamente.
Traduz o texto copiado para português brasileiro.
O texto traduzido fica na memória de texto copiado do computador - clipboard.
Basta fazer um ctrl + v depois de rodar o script para colar a tradução.
"""

import pyperclip
from googletrans import Translator
import logging
import sys
from typing import Optional

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ClipboardTranslator:
    """Classe para gerenciar tradução de texto do clipboard."""
    
    def __init__(self, target_language: str = 'pt'):
        """
        Inicializa o tradutor.
        
        Args:
            target_language: Idioma de destino (padrão: 'pt' para português)
        """
        self.translator = Translator()
        self.target_language = target_language
    
    def get_clipboard_text(self) -> Optional[str]:
        """
        Obtém texto do clipboard.
        
        Returns:
            Texto do clipboard ou None se houver erro
        """
        try:
            text = pyperclip.paste()
            if not text or not text.strip():
                logger.warning("Clipboard está vazio ou contém apenas espaços em branco")
                return None
            return text.strip()
        except Exception as e:
            logger.error(f"Erro ao acessar clipboard: {e}")
            return None
    
    def translate_text(self, text: str) -> Optional[str]:
        """
        Traduz o texto para o idioma de destino.
        
        Args:
            text: Texto a ser traduzido
            
        Returns:
            Texto traduzido ou None se houver erro
        """
        try:
            # Detectar idioma do texto original
            detection = self.translator.detect(text)
            source_lang = detection.lang
            
            logger.info(f"Idioma detectado: {source_lang}")
            
            # Se o texto já está no idioma de destino, não traduzir
            if source_lang == self.target_language:
                logger.info("Texto já está no idioma de destino")
                return text
            
            # Realizar tradução
            result = self.translator.translate(text, dest=self.target_language, src=source_lang)
            return result.text
            
        except Exception as e:
            logger.error(f"Erro na tradução: {e}")
            return None
    
    def copy_to_clipboard(self, text: str) -> bool:
        """
        Copia texto para o clipboard.
        
        Args:
            text: Texto a ser copiado
            
        Returns:
            True se sucesso, False caso contrário
        """
        try:
            pyperclip.copy(text)
            logger.info("Texto traduzido copiado para o clipboard")
            return True
        except Exception as e:
            logger.error(f"Erro ao copiar para clipboard: {e}")
            return False
    
    def translate_clipboard(self, copy_result: bool = True) -> bool:
        """
        Função principal que traduz o conteúdo do clipboard.
        
        Args:
            copy_result: Se True, copia a tradução de volta para o clipboard
            
        Returns:
            True se a tradução foi bem-sucedida, False caso contrário
        """
        # Obter texto do clipboard
        original_text = self.get_clipboard_text()
        if not original_text:
            print("❌ Não foi possível obter texto do clipboard")
            return False
        
        print(f"📋 Texto original ({len(original_text)} caracteres):")
        print(f"   {original_text[:100]}{'...' if len(original_text) > 100 else ''}")
        print()
        
        # Traduzir texto
        translated_text = self.translate_text(original_text)
        if not translated_text:
            print("❌ Não foi possível traduzir o texto")
            return False
        
        print(f"🌐 Texto traduzido:")
        print(f"   {translated_text}")
        print()
        
        # Copiar resultado para clipboard se solicitado
        if copy_result:
            if self.copy_to_clipboard(translated_text):
                print("✅ Tradução copiada para o clipboard!")
            else:
                print("⚠️  Tradução realizada, mas não foi possível copiar para o clipboard")
        
        return True


def main():
    """Função principal do script."""
    print("🔤 Tradutor de Clipboard")
    print("=" * 50)
    
    try:
        # Criar instância do tradutor
        translator = ClipboardTranslator(target_language='pt')
        
        # Executar tradução
        success = translator.translate_clipboard(copy_result=True)
        
        if success:
            print("\n✨ Tradução concluída com sucesso!")
        else:
            print("\n❌ Falha na tradução")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Operação cancelada pelo usuário")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()