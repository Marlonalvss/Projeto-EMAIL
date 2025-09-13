from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
import io
from gemini_client import classify_email, regenerate_suggestion

app = FastAPI()

# 🔹 CORS: permite qualquer origem, método POST/OPTIONS e headers
# IMPORTANTE: Em produção, mude "*" para o domínio do seu frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos
    allow_headers=["*"],
)

@app.post("/classify")
async def classify(
    request: Request,
    file: UploadFile | None = File(None),
    text: str | None = Form(None)
):
    try:
        print("[LOG] Iniciando classificação de entrada...")
        email_text = ""

        # Caso 1: Se veio arquivo (FormData com file)
        if file:
            print(f"[LOG] Arquivo recebido: {file.filename} ({file.content_type})")
            if file.content_type == "application/pdf":
                pdf_reader = PdfReader(io.BytesIO(await file.read()))
                email_text = "".join([page.extract_text() or "" for page in pdf_reader.pages])
                print("[LOG] Texto extraído do PDF.")
            elif file.content_type == "text/plain":
                email_text = (await file.read()).decode("utf-8")
                print("[LOG] Texto extraído do TXT.")
            else:
                print("[ERRO] Tipo de arquivo não suportado.")
                raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado (.txt ou .pdf)")
        
        # Caso 2: Se veio JSON
        elif request.headers.get("content-type", "").startswith("application/json"):
            print("[LOG] Entrada recebida via JSON.")
            body = await request.json()
            email_text = body.get("text", "")
        
        # Caso 3: Se veio texto via Form sem arquivo
        elif text:
            print("[LOG] Entrada recebida via Form.")
            email_text = text

        else:
            print("[ERRO] Nenhum texto ou arquivo enviado.")
            raise HTTPException(status_code=400, detail="Nenhum texto ou arquivo enviado")

        if not email_text.strip():
            print("[ERRO] Conteúdo vazio.")
            raise HTTPException(status_code=400, detail="Conteúdo vazio")

        print(f"[LOG] Texto para classificar:\n{email_text[:200]}{'...' if len(email_text) > 200 else ''}")

        # 🚀 Chamando a função real de classificação do Gemini
        result = classify_email(email_text)
        print("[LOG] Classificação concluída.")

        return JSONResponse(content={"result": result})

    except Exception as e:
        print(f"[ERRO] Falha na classificação: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/regenerate-suggestion")
async def regenerate_suggestion_endpoint(body: dict):
    print("[LOG] Iniciando geração de nova sugestão...")
    email_text = body.get("text", "")
    classification = body.get("classification", "")

    if not email_text or not classification:
        print("[ERRO] Texto e classificação são necessários para gerar uma nova sugestão.")
        raise HTTPException(status_code=400, detail="Texto e classificação são necessários para gerar uma nova sugestão.")

    print(f"[LOG] Texto recebido para nova sugestão:\n{email_text[:200]}{'...' if len(email_text) > 200 else ''}")
    print(f"[LOG] Classificação recebida: {classification}")

    result = regenerate_suggestion(email_text, classification)
    print("[LOG] Nova sugestão gerada.")

    return JSONResponse(content={"result": result})