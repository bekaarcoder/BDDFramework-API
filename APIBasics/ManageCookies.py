import requests

cookie = {'visit-month': 'November'}
response = requests.get('https://httpbin.org/cookies', cookies=cookie)
print(response.history)
print(response.json())