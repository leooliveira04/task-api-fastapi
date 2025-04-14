from fastapi.testclient import TestClient
from app.main import app
from app.database import tarefas_db


client = TestClient(app)


def setup_function():
    tarefas_db.clear()


def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem" : "API de tarefas funcionando!"}


def test_post_tarefa():
    nova_tarefa = {
        "id": 1,
        "titulo": "Estudar pytest",
        "descricao": "Criar testes automatizados",
        "concluida": False
    }

    response = client.post("/tarefas", json=nova_tarefa)

    assert response.status_code == 200
    assert response.json()["mensagem"] == "Tarefa criada com sucesso"
    assert response.json()["tarefa"] == nova_tarefa

def test_get_tarefas():
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_tarefa_por_id():
    client.post("/tarefas", json={
        "id": 1,
        "titulo": "Estudar pytest",
        "descricao": "Criar testes automatizados",
        "concluida": False
    })
    response = client.get("/tarefas/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_tarefa_inexistente():
    response = client.get("/tarefas/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada"

def test_put_tarefa():
    client.post("/tarefas", json={
        "id": 1,
        "titulo": "Estudar pytest",
        "descricao": "Criar testes automatizados",
        "concluida": False
    })
    tarefa_atualizada = {
         "id": 1,
        "titulo": "Estudar FastAPI e Pytest",
        "descricao": "Atualizando tarefa via PUT",
        "concluida": True
    }
    
    response = client.put("/tarefas/1", json=tarefa_atualizada)
    assert response.status_code == 200
    assert response.json()["tarefa"] == tarefa_atualizada

def test_delete_tarefa():
    client.post("/tarefas", json={
        "id": 1,
        "titulo": "Estudar pytest",
        "descricao": "Criar testes automatizados",
        "concluida": False
    })
    response = client.delete("tarefas/1")
    assert response.status_code == 200
    assert response.json()["mensagem"] == "Tarefa deletada com sucesso"

def test_delete_inexistente():
    response = client.delete("tarefas/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada"