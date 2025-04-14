from fastapi import FastAPI
from app.routes import tarefas

app = FastAPI()

@app.get("/")
def home():
	return {"mensagem": "API de tarefas funcionando!"}

# Inclui as rotas
app.include_router(tarefas.router)