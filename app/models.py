from pydantic import BaseModel, Field, field_validator
from typing import Optional

class Tarefa(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=50)
    descricao: str = Field(..., min_length=5, max_length=200)
    prioridade: Optional[int] | None = Field(default=None, ge=1, le=5)
    concluida: bool = False

    @field_validator("titulo")
    def checar_titulo(cls, v):
        if"teste" in v.lower():
            raise ValueError("O título não pode conter a palavras 'teste'")
        if not v[0].isupper():
            raise ValueError("O título deve começar com letra maiúscula")
        return v

    @field_validator('descricao')
    def checar_descricao(cls, v):
        if "http://" in v or "https://" in v or "www." in v:
            raise ValueError("Não é permitido o uso de links")
        return v

class TarefaCriar(Tarefa):
   id: int

class TarefaResposta(TarefaCriar):
    pass