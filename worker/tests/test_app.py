# worker/tests/test_app.py

from worker.worker import app  # ✅ правильно

def test_index_route_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
