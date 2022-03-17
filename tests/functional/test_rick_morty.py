from rick_morty import __version__
from httpx import AsyncClient

from rick_morty.main import app 


def test_version():
    assert __version__ == '0.1.0'

async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Rick & Morty API"}