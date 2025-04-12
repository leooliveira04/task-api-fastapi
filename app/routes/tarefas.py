from fastapi import APIRouter, HTTPException
from app.models import Tarefa
from app.database import tarefas_db

router = APIRouter()

@router.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    tarefas_db.append(tarefa)
    return {"mensagem": "Tarefa criada com sucesso", "tarefa": tarefa}

@router.get("/tarefas")
def listas_tarefas():
    return tarefas_db

@router.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    for tarefa in tarefas_db:
        if tarefa.id == id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@router.put("/tarefas/{id}")
def alterar_tarefa(id:int, nova_tarefa: Tarefa):
    for i, tarefa in enumerate(tarefas_db):
        if tarefa.id == id:
            tarefas_db[i] = nova_tarefa
            return {"mensagem": "Tarefa atualizada com sucesso", "tarefa": nova_tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@router.delete("/tarefas/{id}")
def deletar_tarefa(id:int):
    for tarefa in tarefas_db:
        if tarefa.id == id:
            tarefas_db.remove(tarefa)
            return {"mensagem": "Tarefa deletada com sucesso", "tarefa": tarefa}