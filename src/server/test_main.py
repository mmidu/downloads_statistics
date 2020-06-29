from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
	response = client.get("/api")
	assert response.status_code == 200
	assert response.json() == {"app": {"version": "0.01"}}

def test_get_downloads():
	response = client.get("/downloads")
	assert response.status_code == 200
	assert isinstance(response.json(), dict)
	assert isinstance(response.json()["downloads"], list)