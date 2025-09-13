# 📧 Classificador de E-mail Inteligente

## 🚀 Visão Geral do Projeto

O **Classificador de E-mail Inteligente** é uma aplicação web interativa que utiliza o poder do modelo de linguagem **Gemini** para analisar e classificar e-mails em tempo real. O objetivo principal é ajudar os usuários a identificar rapidamente se um e-mail é **produtivo** (requer ação) ou **improdutivo** (não requer atenção imediata), além de sugerir uma resposta automática.

Este projeto demonstra a integração entre um frontend moderno em **Vue.js** e um backend em **FastAPI** para processamento de linguagem natural, aproveitando ao máximo as capacidades de IA do Google Gemini.

-----

## ✨ Funcionalidades

  * **Classificação Instantânea**: Analisa e classifica o conteúdo do e-mail em uma das duas categorias: "Produtivo" ou "Improdutivo".
  * **Sugestão de Resposta**: Gera uma sugestão de resposta concisa e formal para e-mails, otimizando o fluxo de trabalho.
  * **Múltiplos Formatos de Entrada**: Suporta a entrada de texto diretamente no campo de texto ou o upload de arquivos `.txt` e `.pdf`.
  * **Interface Intuitiva**: Interface de usuário moderna e responsiva, construída com **Vue.js** e **Tailwind CSS**.
  * **Suporte a Dark/Light Mode**: Inclui um seletor para alternar entre os temas claro e escuro.

-----

## 🛠️ Tecnologias Utilizadas

### Frontend

  * **Vue.js**: Framework JavaScript progressivo para a construção da interface do usuário.
  * **TypeScript**: Adiciona tipagem estática ao JavaScript para um código mais robusto.
  * **Tailwind CSS**: Framework CSS utilitário para estilização rápida e responsiva.

### Backend

  * **Python**: Linguagem de programação principal para o backend.
  * **FastAPI**: Framework web de alta performance para a construção da API.
  * **Gemini (Google Generative AI)**: Modelo de linguagem avançado do Google para análise e classificação do texto.
  * **`python-dotenv`**: Gerencia variáveis de ambiente.
  * **`PyPDF2`**: Biblioteca para extrair texto de arquivos PDF.
  * **`uvicorn`**: Servidor ASGI leve para rodar a aplicação FastAPI.

-----

## 📸 Fotos do Projeto

*Adicione aqui as fotos da aplicação em funcionamento, mostrando a interface, o tema claro/escuro e os resultados da classificação.*

**Foto 1: Interface Principal**
*![Interface Principal](./Docs/Screenshot%202025-09-12%20at%2022-06-36%20Classificador%20de%20E-mails.png)*

**Foto 2: Exemplo de Classificação**
*![Exemplo de Classificação](./Docs/Screenshot%202025-09-12%20at%2022-07-35%20Classificador%20de%20E-mails.png)*

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

## 🧑‍💻 Feito por: [Marlon Alves](https://github.com/Marlonalvss)
  * [LinkedIn](https://www.linkedin.com/in/marlon-alvss/)