from fastapi.testclient import TestClient
from rick_morty.main import app

client = TestClient(app)

def test_get_episodes():
    response = client.get("/episodes/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    
    fields = [
        "id",
        "name",
        "air_date",
        "episode",
        "characters"
    ]
    for field in fields:
        assert field in data[0]