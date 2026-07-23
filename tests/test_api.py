

def test_api_appointments(client):
    response = client.get("/api/appointments")

    assert response.status_code == 200

    data = response.get_json()

    assert "data" in data
    assert isinstance(data["data"], list)

def test_404(client):
    response = client.get("/naoexiste")

    assert response.status_code == 404