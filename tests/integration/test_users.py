from fastapi.testclient import TestClient

def test_list_users(client: TestClient, headers: dict):
    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
    data = response.json()   
    fields = [
        "id",
        "firstname",
        "lastname",
        "email"
    ]
    for field in fields:
        assert field in data.get("data")[0]
    assert "password_hash" not in data.get("data")[0]