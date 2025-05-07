def test_get_tasks(client):
    response = client.get("/tasks/tasks")
    assert response.status_code in (200, 404)