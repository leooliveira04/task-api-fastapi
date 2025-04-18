import os
import json

def carregar_tarefas():
    if not os.path.exists('tarefas.json'):
        return []
    with open("tarefas.json", "r", encoding="utf-8") as f:
        return json.load(f)
    

def salvar_tarefas(tarefas: list):
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)






