def test_get_expenses(client):
    response = client.get("/expenses/expenses")
    assert response.status_code in (200, 404)