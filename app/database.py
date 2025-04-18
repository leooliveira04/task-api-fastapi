from typing import List
from app.models import Tarefa
from utils.arquivo import carregar_tarefas

tarefas_db = carregar_tarefas()

