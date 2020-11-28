import requests

# creating session manager for authentication
request_session = requests.session()
request_session.auth = ('shashanksmaty', 'github_token')
github_response = request_session.get('https://api.github.com/user/repos')

# using auth as a parameter
# github_response = requests.get('https://api.github.com/user/repos', auth=('shashanksmaty', 'pass/token'))

print(github_response.status_code)
print(github_response.json())