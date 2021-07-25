from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_read_root():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World!"}
