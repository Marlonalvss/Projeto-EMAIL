# Backend - Classificador de E-mails

Este projeto é o backend do **Classificador de E-mails Inteligente**, responsável por receber textos ou arquivos, filtrar entradas, classificar o conteúdo usando o Gemini API e sugerir respostas automáticas.

## Principais Tecnologias e Bibliotecas

- **Python 3.10+**
- **FastAPI**: Framework web rápido para APIs.
- **Uvicorn**: Servidor ASGI para FastAPI.
- **python-dotenv**: Carregamento de variáveis de ambiente.
- **google-generativeai**: Integração com Gemini API.
- **PyPDF2**: Leitura e extração de texto de arquivos PDF.
- **typing-extensions**: Tipagem avançada e compatibilidade.
- **nltk**: Biblioteca de processamento de linguagem natural (stopwords, stemming, etc.).
- **python-multipart**: Suporte a upload de arquivos via FormData.


## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd Projeto-EMAIL/Backend
   ```

2. **Crie e ative um ambiente virtual (opcional):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   Se não houver um arquivo `requirements.txt`, instale manualmente:
   ```bash
   pip install fastapi uvicorn PyPDF2 python-dotenv google-generativeai typing-extensions nltk python-multipart
   ```

4. **Configure a chave da API Gemini:**
   - Crie um arquivo `.env` na pasta `Backend` com o conteúdo:
     ```
     GEMINI_API_KEY=seu_token_aqui
     ```

## Como rodar localmente

1. **Inicie o servidor FastAPI:**
   ```bash
   uvicorn app:app --reload
   ```
   O backend estará disponível em `http://localhost:8000`.

2. **Testes rápidos:**
   - Execute o script de teste:
     ```bash
     python test_gemini.py
     ```

## Endpoints

- `POST /classify`: Recebe texto ou arquivo (`.txt` ou `.pdf`), filtra entradas ofensivas ou tentativas de manipulação, classifica e retorna sugestão de resposta.

## Observações

- O backend está levemente protegido contra perguntas diretas para IA.
- Apenas textos relevantes para classificação de e-mails são aceitos.

## Estrutura dos arquivos

- `app.py`: API principal FastAPI.
- `gemini_client.py`: Integração e lógica de classificação com Gemini.
- `test_gemini.py`: Teste unitário da classificação.

---

**Desenvolvido para fins educacionais e produtivos.**