from fastapi.testclient import TestClient

def test_get_characters(client: TestClient, headers: dict):
    response = client.get("/characters/", headers=headers)
    assert response.status_code == 200
    data = response.json()    
    fields = [
        "id",
        "name",
        "status",
        "species",
        "type",
        "gender",
        "episodes"
    ]
    for field in fields:
        assert field in data.get("data")[0]

