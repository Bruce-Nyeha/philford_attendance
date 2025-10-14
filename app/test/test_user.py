import pytest
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

test_user = {
    "email": "brucenyeha@gmail.com",
    "password": "sayless",
    "full_name": "Bruce Nyeha",
    "username": "brucehimselff",
    "country": "Ghana",
    "role": "student",
    "gender": "male",
    "created_at": "09-07-2025"
}

def test_user_registration():
    response = client.post("/auth/login", json=test_user)
    assert response.status_code ==201 or response.status_code==200
    assert "email" in response.json()

def test_login_user():
    response = client.post("/auth/login",data={
        "username": test_user["email"],
        "password": test_user["password"]
    })
    assert response.status_code == 200
    assert "access_token" in response.json()