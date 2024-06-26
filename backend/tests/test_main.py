from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_create_expense():
    response = client.post("/expenses/", json={"amount": 100.0, "category": "food", "description": "groceries", "date": "2023-01-01", "user_id": 1})
    assert response.status_code == 200
    assert response.json()["amount"] == 100.0