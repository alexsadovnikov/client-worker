def test_get_time_entries(client):
    response = client.get("/time-entries/")
    assert response.status_code in (200, 404)