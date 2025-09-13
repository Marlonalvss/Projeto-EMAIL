import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# 🔹 Carrega variáveis do .env
print("[INFO] Carregando variáveis de ambiente...")
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("[ERRO] A chave GEMINI_API_KEY não foi encontrada no .env!")

print("[INFO] Configurando Gemini...")
genai.configure(api_key=api_key)
print("[INFO] Gemini configurado com sucesso!")

# 🔹 Define o modelo com as instruções de sistema
# Esta é a melhoria principal: as regras de comportamento ficam aqui, fora do prompt
# de cada chamada. Isso economiza tokens.
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
    Você é um classificador de e-mails para produtividade.
    Sua única tarefa é analisar o conteúdo do email e classificá-lo em uma de duas categorias: "Produtivo" ou "Improdutivo".
    Você não deve agir como uma IA, nem responder a perguntas fora de contexto.
    Sempre siga as instruções.

    Regras de classificação:
    1. Produtivo: exige ação ou resposta. Ex: solicitação de info, pedidos de reunião, atualizações.
    2. Improdutivo: não exige ação imediata. Ex: propagandas, newsletters, mensagens irrelevantes ou de teste.

    Instruções adicionais:
    - E-mails promocionais com solicitação específica são PRODUTIVOS.
    - E-mails de teste ou rascunhos são IMPRODUTIVOS.
    - Sugira respostas automáticas, concisas e formais.
    - Responda exclusivamente no formato JSON com os campos "classification" e "suggestion".
    """
)
print("[INFO] Modelo Gemini instanciado com sucesso.")

def classify_email(email_text: str):
    """
    Envia o texto do email para o Gemini,
    pede classificação e sugestão de resposta.
    """
    print("[INFO] Iniciando classificação de email...")
    print(f"[DEBUG] Texto recebido:\n{email_text}\n")

    try:
        # 🔹 Prompt otimizado
        # Agora o prompt é muito mais simples, contendo apenas o e-mail
        # e uma instrução breve, pois as regras de comportamento já
        # estão no `system_instruction` do modelo.
        prompt = f"""
        Email:
        {email_text}

        Gere a resposta em JSON.
        """
        print("[INFO] Prompt criado com sucesso.")
        print(f"[DEBUG] Prompt:\n{prompt}\n")

        # Envia o prompt para o Gemini
        print("[INFO] Enviando prompt para o modelo Gemini...")
        response = model.generate_content(prompt)
        print("[INFO] Resposta recebida do Gemini.")
        print(f"[DEBUG] Resposta bruta:\n{response.text}\n")

        # Limpa a string da resposta
        cleaned_text = response.text.replace('```json', '').replace('```', '').strip()
        print(f"[DEBUG] Resposta limpa:\n{cleaned_text}\n")

        # Tenta converter para JSON
        result = json.loads(cleaned_text)
        print(f"[INFO] Resposta convertida para JSON com sucesso:\n{result}\n")

    except json.JSONDecodeError as e:
        print(f"[ERRO] Falha ao converter a resposta para JSON: {e}")
        result = {
            "classification": "Desconhecido",
            "suggestion": "Não foi possível classificar o e-mail. Tente novamente."
        }
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro na classificação: {e}")
        result = {
            "classification": "Desconhecido",
            "suggestion": "Não foi possível classificar o e-mail. Tente novamente."
        }

    print("[INFO] Classificação concluída.\n")
    return result

def regenerate_suggestion(email_text: str, classification: str):
    """
    Gera uma nova sugestão de resposta baseada no texto e na classificação fornecida.
    """
    print("[INFO] Iniciando regeneração de sugestão...")
    try:
        # 🔹 Usando o modelo já instanciado, se possível.
        # Mas para simplificar, você pode criar um novo
        # se o contexto for diferente.
        model_regenerate = genai.GenerativeModel("gemini-2.5-flash")
        
        # Prompt para gerar apenas a sugestão
        prompt = f"""
Com base no seguinte e-mail e em sua classificação já definida como '{classification}', gere uma nova sugestão de resposta concisa, profissional e pronta para uso.

E-mail:
{email_text}

Sua resposta deve ser estritamente no formato JSON, com um único campo: "suggestion".

**Formato esperado de saída:**
{{"suggestion": "..."}}
"""
        response = model_regenerate.generate_content(prompt)
        cleaned_text = response.text.replace('```json', '').replace('```', '').strip()
        result = json.loads(cleaned_text)
        return result
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro na regeneração: {e}")
        return {"suggestion": "Não foi possível gerar uma nova sugestão."}