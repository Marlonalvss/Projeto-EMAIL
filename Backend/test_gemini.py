import sys
import os

# Adiciona o diretório atual no path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gemini_client import classify_email

if __name__ == "__main__":
    email = """
   Olá Fernandoo! Boa tarde tudo bom? Agradeço o seu contato! Adorei o convite, vocês foram ótimos!
    """

    print("[TESTE] Enviando email para classificação...")
    result = classify_email(email)

    print("\n=== RESULTADO FINAL ===")
    print(result)
