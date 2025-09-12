from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
import io

app = FastAPI()

# 🔹 CORS: permite qualquer origem, método POST/OPTIONS e headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/classify")
async def classify(
    request: Request,
    file: UploadFile | None = File(None),
    text: str | None = Form(None)
):
    try:
        email_text = ""

        # Caso 1: Se veio arquivo (FormData com file)
        if file:
            if file.content_type == "application/pdf":
                pdf_reader = PdfReader(io.BytesIO(await file.read()))
                email_text = "".join([page.extract_text() or "" for page in pdf_reader.pages])
            elif file.content_type == "text/plain":
                email_text = (await file.read()).decode("utf-8")
            else:
                raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado (.txt ou .pdf)")
        
        # Caso 2: Se veio JSON
        elif request.headers.get("content-type", "").startswith("application/json"):
            body = await request.json()
            email_text = body.get("text", "")
        
        # Caso 3: Se veio texto via Form sem arquivo
        elif text:
            email_text = text

        else:
            raise HTTPException(status_code=400, detail="Nenhum texto ou arquivo enviado")

        if not email_text.strip():
            raise HTTPException(status_code=400, detail="Conteúdo vazio")

       
         # 🚀 Chamando a função real de classificação do Gemini
        from gemini_client import classify_email
        result = classify_email(email_text)

        return JSONResponse(content={"result": result})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
