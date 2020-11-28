import requests


def after_scenario(context, scenario):
    if 'library' in scenario.tags:
        url = 'https://reqres.in/api/users/' + context.user_id
        response = requests.delete(url)
        print(response.status_code)
        assert response.status_code == 204