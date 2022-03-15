from fastapi.testclient import TestClient
from rick_morty.main import app

client = TestClient(app)

def test_get_characters():
    response = client.get("/characters/")
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

