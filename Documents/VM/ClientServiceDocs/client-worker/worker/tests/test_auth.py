import sys
from pathlib import Path
import pytest

# Добавляем путь к worker/ в PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.Main import app  # обычный импорт, теперь покрытие будет работать

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post("/login", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data

def test_login_failure(client):
    response = client.post("/login", json={"username": "admin", "password": "wrong"})
    assert response.status_code == 401

def test_protected_unauthorized(client):
    response = client.get("/protected")
    assert response.status_code == 401

def test_protected_authorized(client):
    login = client.post("/login", json={"username": "admin", "password": "admin"})
    token = login.get_json()["access_token"]
    response = client.get("/protected", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.get_json()["logged_in_as"] == "admin"
