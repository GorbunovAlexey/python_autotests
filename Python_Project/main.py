import requests
response = requests.post("https://petstore.swagger.io/v2/pet",json={
  "id": 385,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Ronnie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.put("https://petstore.swagger.io/v2/pet",json={
  "id": 385,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Sparky",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)
response = requests.get("https://petstore.swagger.io/v2/pet/385")
print(response.text)