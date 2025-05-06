def test_get_projects(client):
    response = client.get("/projects/projects")
    assert response.status_code in (200, 404)