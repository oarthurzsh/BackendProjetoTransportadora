# TransCarga - Backend

Este é o componente de servidor (API) do sistema **TransCarga**, responsável pelo gerenciamento de fretes, autenticação e regras de negócio da transportadora.

## 🚀 Tecnologias Utilizadas

O backend foi desenvolvido utilizando as seguintes tecnologias:

- **Linguagem:** Python 3.x
- **Framework:** FastAPI
- **Banco de Dados/ORM:** SQLAlchemy
- **Segurança:** Autenticação via JWT (JSON Web Tokens)
- **Documentação Automática:** Swagger/OpenAPI (acessível via `/docs`)

## 🛠️ Funcionalidades Principais

- Gerenciamento completo de fretes (CRUD).
- Sistema de autenticação administrativa.
- Configuração de CORS para integração com o frontend.
- Organização modular de rotas e lógica de negócio.

## ⚙️ Como Executar

1. Certifique-se de ter o Python instalado.
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/scripts/activate  # Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o servidor:
   ```bash
   uvicorn src.main:app --reload
   ```

---
Desenvolvido como parte do ecossistema TransCarga.
