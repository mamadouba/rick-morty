import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from rick_morty.main import create_app
from rick_morty.settings import settings
from rick_morty.dependencies import get_db

# settings.db_name = "test1"

# @pytest.fixture(scope="session", autouse=True)
# def testdb():
#     db = get_db()
#     db.create_database()
#     yield
#     db.drop_database()


@pytest.fixture(scope="session")
def client() -> TestClient:
    app: FastAPI = create_app()
    client = TestClient(app)
    yield client


@pytest.fixture()
def headers(client: TestClient) -> dict:
    payload = {
        "firstname": "test",
        "lastname": "test",
        "email": "test@example.com",
        "password": "test",
    }
    response = client.post("/users/", json=payload)
    assert response.status_code in [201, 409]

    payload = {"email": "test@example.com", "password": "test"}

    response = client.post("/users/login", json=payload)
    assert response.status_code == 200

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}
