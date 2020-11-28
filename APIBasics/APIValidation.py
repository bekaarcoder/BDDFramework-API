import requests
import json

response = requests.get('https://reqres.in/api/users', params={'page': 2}, )

# print(response.text)
# print(type(response.text))
#
# data = json.loads(response.text)
# print(type(data))

# retrieve the json response
json_res = response.json()
print(type(json_res))
print(json_res)

# get the response status code
print(response.status_code)

# get response headers
print(response.headers)

# get response cookies
print(response.cookies)