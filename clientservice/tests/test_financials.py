def test_get_financials(client):
    response = client.get("/financials/financials")
    assert response.status_code in (200, 404)