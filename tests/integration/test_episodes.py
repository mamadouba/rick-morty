from fastapi.testclient import TestClient


def test_get_episodes(client: TestClient, headers: dict):
    response = client.get("/episodes/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    fields = ["id", "name", "air_date", "episode", "characters"]
    for field in fields:
        assert field in data.get("data")[0]
