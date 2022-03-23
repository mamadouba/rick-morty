from fastapi.testclient import TestClient

def test_create_comment(client: TestClient, headers: dict):
    payload = {
        "episode_id": 7,
        "comment": "Nice episode !"
    }
    response = client.post("/comments/", json=payload, headers=headers)
    assert response.status_code == 201
    data = response.json()    
    for field in payload:
        assert field in data
    assert "id" in data 
    assert type(data["id"]) == int

def test_unrelated_episode_character(client: TestClient, headers: dict):
    payload = {
        "episode_id": 7,
        "character_id": 100000,
        "comment": "Nice episode !"
    }
    response = client.post("/comments/", json=payload, headers=headers)
    assert response.status_code == 400
    data = response.json()    
    assert data["message"] == "episode and character are not associated"

def test_character_not_found(client: TestClient, headers: dict):
    payload = {
        "character_id": 1000,
        "comment": "Nice guy !"
    }
    response = client.post("/comments/", json=payload, headers=headers)
    assert response.status_code == 404
    data = response.json()    
    assert "character 1000 not found" == data["message"]

def test_episode_not_found(client: TestClient, headers: dict):
    payload = {
        "episode_id": 1000,
        "comment": "Nice guy !"
    }
    response = client.post("/comments/", json=payload, headers=headers)
    assert response.status_code == 404
    data = response.json()    
    assert "episode 1000 not found" == data["message"]

def test_get_comment(client: TestClient, headers: dict):
    response = client.get("/comments/1", headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()
    assert "comment" in response.json()
    assert "episode_id" in response.json()
    assert "character_id" in response.json()

def test_get_comments(client: TestClient, headers: dict):
    response = client.get("/comments/", headers=headers)
    assert response.status_code == 200
    data = response.json()

    for k in ["total", "current_page", "data"]:
        assert k in data 
    
    assert type(data["data"]) == list


def test_pagination(client: TestClient, headers: dict):
    response = client.get("/comments/?page=1&per_page=3", headers=headers)
    assert response.status_code == 200
    data = response.json()

    assert data["per_page"] == 3
    assert data["current_page"] == 1
    assert len(data["data"]) <= 3


