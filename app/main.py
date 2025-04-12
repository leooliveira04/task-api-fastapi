from fastapi import FastAPI
from app.routes import tarefas

app = FastAPI()

@app.get("/")
def home():
	return {"mensagem": "Api de Tarefas funcionando!"}

# Inclui as rotas
app.include_router(tarefas.router)