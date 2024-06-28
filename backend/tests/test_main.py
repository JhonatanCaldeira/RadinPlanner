import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_user():
    user_id = 1
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "jhon"

def test_get_expense():
    user_id = 1
    response = client.get(f"/users/{user_id}/expenses/")
    assert response.status_code == 200
    #assert response.json()["amount"] == 100.0