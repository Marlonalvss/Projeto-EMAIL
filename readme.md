# 📧 Classificador de E-mail Inteligente

## 🚀 Visão Geral do Projeto

O **Classificador de E-mail Inteligente** é uma aplicação web interativa que utiliza o poder do modelo de linguagem **Gemini** para analisar e classificar e-mails em tempo real. O objetivo principal é ajudar os usuários a identificar rapidamente se um e-mail é **produtivo** (requer ação) ou **improdutivo** (não requer atenção imediata), além de sugerir uma resposta automática.

Este projeto demonstra a integração entre um frontend moderno em **Vue.js** e um backend em **FastAPI** para processamento de linguagem natural, aproveitando ao máximo as capacidades de IA do Google Gemini.

🌍 **Teste agora:** <a href="https://projeto-email-front.onrender.com/" target="_blank" rel="noopener noreferrer">Clique aqui para acessar o site 🚀</a>


-----

## ✨ Funcionalidades

  * **Classificação Instantânea**: Analisa e classifica o conteúdo do e-mail em uma das duas categorias: "Produtivo" ou "Improdutivo".
  * **Sugestão de Resposta**: Gera uma sugestão de resposta concisa e formal para e-mails, otimizando o fluxo de trabalho.
  * **Gerar Nova Resposta**: Permite gerar uma nova sugestão de resposta mantendo a classificação original do e-mail.
  * **Múltiplos Formatos de Entrada**: Suporta a entrada de texto diretamente no campo de texto ou o upload de arquivos `.txt` e `.pdf`.
  * **Interface Intuitiva**: Interface de usuário moderna e responsiva, construída com **Vue.js** e **Tailwind CSS**.
  * **Suporte a Dark/Light Mode**: Inclui um seletor para alternar entre os temas claro e escuro.

-----

## 🛠️ Tecnologias Utilizadas  

### Frontend  
- **Vue.js**  
- **TypeScript**  
- **Tailwind CSS**  

### Backend  
- **Python + FastAPI**  
- **Gemini (Google Generative AI)**  
- **python-dotenv**  
- **PyPDF2**  
- **uvicorn**  
- **nltk** (incluindo `stopwords`, baixadas no deploy)  

> 💡 Todo o **requirements.txt** já inclui as dependências necessárias para rodar o projeto sem dor de cabeça.  

### Deploy  
🚀 O **Frontend** e o **Backend** foram hospedados no 🌍 **Render** <a href="https://render.com/" target="_blank" rel="noopener noreferrer">Clique aqui para acessar o site 🚀</a>.  

-----

## 📸 Fotos do Projeto

**Foto 1: Interface Principal**
*![Interface Principal](./Docs/Screenshot%202025-09-12%20at%2022-06-36%20Classificador%20de%20E-mails.png)*

**Foto 2: Exemplo de Classificação**
*![Exemplo de Classificação](./Docs/Screenshot%202025-09-13%20at%2012-53-02%20Classificador%20de%20E-mails.png)*

**Foto 3: Tema Escuro**
*![Tema Escuro](./Docs/Screenshot%202025-09-12%20at%2022-06-44%20Classificador%20de%20E-mails.png)*

-----

## ⚙️ Como Utilizar

Siga os passos abaixo para configurar e rodar o projeto em sua máquina.

### 1\. Pré-requisitos

Certifique-se de ter o **Node.js** e o **Python 3.8+** instalados.

### 2\. Configuração do Backend

1.  Clone o repositório:

    ```bash
    git clone [https://github.com/Marlonalvss/Projeto-EMAIL.git]
    cd [Backed ou Frontend]
    ```

2.  Crie um ambiente virtual e instale as dependências do Python:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  Obtenha uma chave de API do Gemini no [Google AI Studio](https://aistudio.google.com/).

4.  Crie um arquivo `.env` na raiz do projeto e adicione sua chave:

    ```
    GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
    ```

5.  Inicie o servidor backend:

    ```bash
    uvicorn app:app --reload
    ```

    O servidor estará disponível em `http://localhost:8000`.

### 3\. Configuração do Frontend

1.  Navegue até o diretório do frontend (geralmente a raiz do projeto, a menos que esteja em um subdiretório).

2.  Instale as dependências do Node.js:

    ```bash
    npm install
    ```

3.  Inicie a aplicação Vue.js:

    ```bash
    npm run dev
    ```

    A aplicação estará disponível em `http://localhost:5173`.

-----

## 🧑‍💻 Feito por :

<p align="center">
  <img src="https://avatars.githubusercontent.com/u/86992904?v=4" alt="Foto do Marlon" width="200" style="border-radius:50%"/>
</p>

<h3 align="center">Marlon Alves</h3>
<p align="center">A arte move a criatividade.</p>

<p align="center">
  <a href="https://github.com/Marlonalvss">🌐 GitHub</a> • 
  <a href="https://www.linkedin.com/in/marlon-alvss/">💼 LinkedIn</a>
</p>

  