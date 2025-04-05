from worker.worker import app
from unittest.mock import patch, MagicMock

client = app.test_client()

# --- /send
@patch("worker.worker.producer")
def test_send_route(mock_producer):
    mock_producer.send = MagicMock()
    mock_producer.flush = MagicMock()
    response = client.post("/send", json={"event": "test", "data": "demo"})
    assert response.status_code == 200
    assert response.json["status"] == "ok"

# --- /crm/contacts
@patch("worker.worker.requests.get")
def test_get_contacts(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": []}
    response = client.get("/crm/contacts")
    assert response.status_code == 200
    assert response.json == {"data": []}

# --- /crm/contact
@patch("worker.worker.requests.post")
def test_create_contact(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"result": "ok"}
    response = client.post("/crm/contact", json={"entity": "ContactCc"})
    assert response.status_code == 200
    assert response.json == {"result": "ok"}

# --- /crm/cases
@patch("worker.worker.requests.get")
def test_get_cases(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"cases": []}
    response = client.get("/crm/cases")
    assert response.status_code == 200
    assert response.json == {"cases": []}

# --- /crm/contacts/search
@patch("worker.worker.requests.post")
def test_search_contacts(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"results": []}
    response = client.post("/crm/contacts/search", json={"fieldFilters": []})
    assert response.status_code == 200
    assert response.json == {"results": []}

# --- /crm/contact/<contact_id>/cases
@patch("worker.worker.requests.get")
def test_get_contact_cases(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"linkedCases": []}
    response = client.get("/crm/contact/123/cases")
    assert response.status_code == 200
    assert response.json == {"linkedCases": []}

# --- /crm/entity/<entity>
@patch("worker.worker.requests.post")
def test_create_entity(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"created": True}
    response = client.post("/crm/entity/ContactCc", json={"name": "Alex"})
    assert response.status_code == 200
    assert response.json == {"created": True}

# --- /crm/entity/<entity>/<entity_id>
@patch("worker.worker.requests.put")
def test_update_entity(mock_put):
    mock_put.return_value.status_code = 200
    mock_put.return_value.json.return_value = {"updated": True}
    response = client.put("/crm/entity/ContactCc/456", json={"name": "Updated"})
    assert response.status_code == 200
    assert response.json == {"updated": True}
    from worker.worker import app

def test_index_route_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
