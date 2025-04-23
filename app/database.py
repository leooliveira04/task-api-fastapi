# from typing import List
from app.models import Tarefa
# from utils.arquivo import carregar_tarefas
from sqlmodel import SQLModel, create_engine

# tarefas_db = carregar_tarefas()

sqlite_file_name = "tarefas.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def criar_db():
    SQLModel.metadata.create_all(engine)