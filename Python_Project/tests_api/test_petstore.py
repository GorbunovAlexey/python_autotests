import requests
import pytest

def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/385")
    assert response.status_code ==200
    
def test_string_reply():
    response = requests.get("https://petstore.swagger.io/v2/pet/385")
    assert response.json()['name'] == 'Sparky'    