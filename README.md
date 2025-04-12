 Task API – FastAPI 🐍🚀

API simples desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para fins de estudo e prática de backend com Python.

---

## ✨ Funcionalidades

- [x] FastAPI com estrutura modular
- [x] Uvicorn para desenvolvimento local com recarregamento automático
- [x] Ambiente virtual isolado com `venv`
- [x] Versionamento de dependências com `requirements.txt`

---

## 📁 Estrutura de Pastas

<pre> <code> task-api-fastapi/ ├── app/ │ └── main.py ├── .venv/ # Ambiente virtual (ignorado pelo Git) ├── requirements.txt # Dependências do projeto ├── README.md └── .gitignore </code> </pre>

## ✅ Requisitos

- Python 3.10+
- Git
- VS Code (opcional)
- Ubuntu, Linux ou WSL (recomendado)

---

## 🧪 Como Rodar Localmente

```bash
# Clonar o projeto
git clone git@github.com:leooliveira04/task-api-fastapi.git
cd task-api-fastapi

# Criar e ativar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
uvicorn app.main:app --reload