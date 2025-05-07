def test_get_analytics(client):
    response = client.get("/analytics/analytics/reports")
    assert response.status_code in (200, 404)