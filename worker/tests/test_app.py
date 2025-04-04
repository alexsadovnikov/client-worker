from worker.worker import app
from unittest.mock import patch, MagicMock

client = app.test_client()

@patch("worker.worker.producer")
def test_send_route(mock_producer):
    mock_producer.send = MagicMock()
    mock_producer.flush = MagicMock()
    response = client.post("/send", json={"event": "test", "data": "demo"})
    assert response.status_code == 200
    assert response.json["status"] == "ok"

@patch("worker.worker.requests.get")
def test_get_contacts(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": []}
    response = client.get("/crm/contacts")
    assert response.status_code == 200
    assert response.json == {"data": []}

@patch("worker.worker.requests.post")
def test_create_contact(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"result": "ok"}
    response = client.post("/crm/contact", json={"entity": "ContactCc"})
    assert response.status_code == 200
    assert response.json == {"result": "ok"}
