# Frontend - Classificador de E-mails Inteligente

Este é o frontend do projeto **Classificador de E-mails Inteligente**, uma interface moderna e responsiva para análise e classificação automática de textos e e-mails.

## Tecnologias Utilizadas

- **Vue.js 3**: Framework JavaScript progressivo para construção de interfaces.
- **TypeScript**: Tipagem estática para maior segurança e produtividade.
- **Tailwind CSS**: Framework utilitário para estilização rápida e responsiva.
- **Vite**: Ferramenta de build e desenvolvimento rápido para projetos Vue.
- **Componentização**: Interface dividida em componentes reutilizáveis.

## Principais Componentes

- **HeroSection**: Cabeçalho com tema dinâmico e apresentação.
- **ThemeToggle**: Alternância entre tema claro e escuro (com ícones de sol/lua).
- **Classifier**: Área para inserir texto ou anexar arquivos (.txt/.pdf) e visualizar resultados.
- **ExamplesSection**: Exemplos prontos para testar a classificação.
- **InfoSection**: Informações sobre funcionamento e tecnologias do projeto.

## Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd Projeto-EMAIL/Frontend
   ```

2. **Instale as dependências:**
   ```bash
   npm install
   ```

3. **Inicie o servidor de desenvolvimento:**
   ```bash
   npm run dev
   ```
   O frontend estará disponível em `http://localhost:5173` (ou porta indicada pelo Vite).

4. **Configuração de ambiente:**
   - Certifique-se de que o backend está rodando em `http://localhost:8000` para integração correta.

## Funcionalidades

- **Classificação de texto ou arquivo**: Insira manualmente ou envie arquivos `.txt` ou `.pdf`.
- **Sugestão automática**: Receba sugestões de resposta/ação para o texto analisado.
- **Exemplos prontos**: Teste rapidamente com exemplos reais.
- **Tema dinâmico**: Alterne entre claro e escuro, com ícones visuais.
- **Interface responsiva**: Adaptada para desktop e dispositivos móveis.

## Estrutura dos arquivos

- `src/components/`: Componentes Vue organizados por funcionalidade.
- `src/App.vue`: Composição principal da interface.
- `index.html`: Arquivo base do projeto.

---

**Desenvolvido para fins educacionais e produtivos.**