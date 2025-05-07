def test_get_users(client):
    response = client.get("/users/users")
    assert response.status_code in (200, 404)