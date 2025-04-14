# Task API – FastAPI 🐍🚀

API simples desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para fins de estudo e prática de backend com Python.

---

## ✨ Funcionalidades

- [x] FastAPI com estrutura modular
- [x] Uvicorn para desenvolvimento local com recarregamento automático
- [x] Ambiente virtual isolado com `venv`
- [x] Versionamento de dependências com `requirements.txt`
- [x] Testes automatizados com `pytest` e `TestClient`
- [x] Isolamento de estado com `setup_function` para testes independentes

---

## 📁 Estrutura de Pastas

<pre><code>
task-api-fastapi/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes/
│       └── tarefas.py
├── tests/
│   └── test_tarefas.py
├── .venv/               # Ambiente virtual (ignorado pelo Git)
├── requirements.txt     # Dependências do projeto
├── README.md
└── .gitignore
</code></pre>

---

## ✅ Requisitos

- Python 3.10+
- Git
- VS Code (opcional)
- Ubuntu, Linux ou WSL (recomendado)

---

## 🧪 Como Rodar os Testes

O projeto utiliza `pytest` para validação automatizada de todas as rotas.  
A lista de tarefas é limpa automaticamente entre cada teste com `setup_function()`.

### Passos:

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar os testes
PYTHONPATH=. pytest

```

## Comentários
🔁 Rotas testadas

    GET /

    GET /tarefas

    GET /tarefas/{id}

    POST /tarefas

    PUT /tarefas/{id}

    DELETE /tarefas/{id}


📌 Status atual

    API funcional com rotas de CRUD completas

    Testes automatizados e independentes

    Estrutura pronta para evoluir com validações, autenticação e persistência real