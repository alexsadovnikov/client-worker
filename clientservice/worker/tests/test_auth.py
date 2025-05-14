import pytest
from worker.app.main import create_app  # ✅ корректный абсолютный импорт

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post("/auth/login", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data

def test_login_failure(client):
    response = client.post("/auth/login", json={"username": "admin", "password": "wrong"})
    assert response.status_code == 401

def test_protected_unauthorized(client):
    response = client.get("/auth/protected")
    assert response.status_code == 401

def test_protected_authorized(client):
    login = client.post("/auth/login", json={"username": "admin", "password": "admin"})
    token = login.get_json()["access_token"]
    response = client.get("/auth/protected", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.get_json()["logged_in_as"] == "admin"