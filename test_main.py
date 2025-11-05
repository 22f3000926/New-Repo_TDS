from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sum_numbers():
    response = client.get("/sum")
    assert response.status_code == 200
    assert response.json() == {"sum": 15}
