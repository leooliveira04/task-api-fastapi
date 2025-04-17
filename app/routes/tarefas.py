from fastapi import APIRouter, HTTPException
from app.models import TarefaCriar, Tarefa, TarefaResposta
from app.database import tarefas_db

router = APIRouter()

@router.post("/tarefas", response_model=TarefaResposta)
def criar_tarefa(tarefa: TarefaCriar):
    tarefas_db.append(tarefa.model_dump())
    return tarefa

@router.get("/tarefas", response_model=list[TarefaResposta])
def listas_tarefas():
    return tarefas_db

@router.get("/tarefas/{id}", response_model=TarefaResposta)
def buscar_tarefa(id: int):
    for tarefa in tarefas_db:
        if tarefa["id"] == id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@router.put("/tarefas/{id}", response_model=TarefaResposta)
def alterar_tarefa(id:int, nova_tarefa: TarefaCriar):
    for i, tarefa in enumerate(tarefas_db):
        if tarefa["id"] == id:
            tarefas_db[i] = nova_tarefa.model_dump()
            return nova_tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@router.delete("/tarefas/{id}")
def deletar_tarefa(id:int):
    for tarefa in tarefas_db:
        if tarefa["id"] == id:
            tarefas_db.remove(tarefa)
            return {"mensagem": "Tarefa deletada com sucesso", "tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")