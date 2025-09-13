from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
import io
import unicodedata
import re

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from gemini_client import classify_email, regenerate_suggestion

app = FastAPI()

# 🔹 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Pré-processamento de texto para NLP
def preprocess_text_nlp(text: str) -> str:
    # Normaliza Unicode (mantendo acentos)
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()

    # Remove caracteres indesejados, mantendo pontuação importante
    text = re.sub(r"[^a-z0-9áéíóúãõâêîôûçàèìòùü\s\.,;:!?()-]", " ", text)

    # Tokenização simples
    tokens = re.findall(r"\w+", text)

    # Remove stopwords
    stop_words = set(stopwords.words("portuguese"))
    tokens = [t for t in tokens if t not in stop_words]

    # Stemming
    stemmer = SnowballStemmer("portuguese")
    tokens = [stemmer.stem(t) for t in tokens]

    # Junta tokens de volta, mantendo espaços coerentes
    processed = " ".join(tokens)
    return processed

# 🔹 Função para extrair texto de arquivo
async def extract_text_from_file(file: UploadFile) -> str:
    if file.content_type == "application/pdf":
        pdf_reader = PdfReader(io.BytesIO(await file.read()))
        text = "".join([page.extract_text() or "" for page in pdf_reader.pages])
        return text
    elif file.content_type == "text/plain":
        text = (await file.read()).decode("utf-8")
        return text
    else:
        raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado (.txt ou .pdf)")

# 🔹 Classificação
@app.post("/classify")
async def classify(
    request: Request,
    file: UploadFile | None = File(None),
    text: str | None = Form(None)
):
    try:
        email_text = ""
        if file:
            email_text = await extract_text_from_file(file)
        elif request.headers.get("content-type", "").startswith("application/json"):
            body = await request.json()
            email_text = body.get("text", "")
        elif text:
            email_text = text
        else:
            raise HTTPException(status_code=400, detail="Nenhum texto ou arquivo enviado")

        if not email_text.strip():
            raise HTTPException(status_code=400, detail="Conteúdo vazio")

        # Pré-processamento NLP
        processed_text = preprocess_text_nlp(email_text)

        # Classificação
        result = classify_email(processed_text)

        return JSONResponse(content={"result": result})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔹 Regenerar sugestão
@app.post("/regenerate-suggestion")
async def regenerate_suggestion_endpoint(body: dict):
    email_text = body.get("text", "")
    classification = body.get("classification", "")

    if not email_text or not classification:
        raise HTTPException(status_code=400, detail="Texto e classificação são necessários para gerar uma nova sugestão.")

    try:
        # Pré-processamento leve para manter contexto e NLP
        processed_text = preprocess_text_nlp(email_text)

        result = regenerate_suggestion(processed_text, classification)
        return JSONResponse(content={"result": result})

    except Exception as e:
        return JSONResponse(content={"result": {"suggestion": "Não foi possível gerar uma nova sugestão."}})
