import requests
from utilities.configurations import get_configuration
from utilities.resources import APIResources

url = get_configuration()['API']['endpoint'] + APIResources.create_user

response = requests.post(url, json={
    "name": "Harry Potter",
    "job": "Wizard"
}, headers={"Content-Type": "application/json"})

data = response.json()
print(data)
print(data['id'])
print(data['name'])
print(data['job'])
print(data['createdAt'])
