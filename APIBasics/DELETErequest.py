import requests

response = requests.delete('https://reqres.in/api/users/2')

print(response.status_code)