from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from app.models import Tarefa
from app.database import engine


router = APIRouter()

@router.post("/tarefas", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa):
    with Session(engine) as session:
        session.add(tarefa)
        session.commit()
        session.refresh(tarefa)
    return tarefa

@router.get("/tarefas", response_model=list[Tarefa])
def listar_tarefa():
    with Session(engine) as session:
        statement=select(Tarefa)
        resultado = session.exec(statement)
        tarefas = resultado.all()
    return tarefas