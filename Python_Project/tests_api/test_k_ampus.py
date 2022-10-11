import requests
import pytest

def test_statuscode():
    response = requests.post("https://k-ampus.dev/api/v1/login",json={"password":"skhalipa@gmail.com","username":"skhalipa@gmail.com"})
    assert response.status_code ==200
    



    
def test_token():
    response = requests.post("https://k-ampus.dev/api/v1/login",json={"password":"skhalipa@gmail.com","username":"skhalipa@gmail.com"})
    assert response.json()["accessToken"]
    