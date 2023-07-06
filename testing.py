from fastapi import FastAPI
from fastapi.testclient import TestClient
from api.main import *

client=TestClient()

def test_main():
    response=client.get("/movie/1")
    assert response.status_code==200
    assert response.json()=={
                "id": 1,
                "title": "Mi película",
                "overview": "La pelicula estuvo buen",
                "year": 2022,
                "rating": 9.8,
                "category" : "Acción"
            }

def test_create_user_ok():
    user = {
        'email': 'test_create_user_ok@cosasdedevs.com',
        'username': 'test_create_user_ok',
        'password': 'admin123'
    }
    response = client.post(
        '/loging',
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data['email'] == user['email']
    assert data['username'] == user['username']