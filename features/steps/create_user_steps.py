from behave import *
import requests
from utilities.configurations import get_configuration
from utilities.resources import APIResources
from utilities.payload import user_payload


@given('User details is available which needs to be added')
def step_impl(context):
    context.url = get_configuration()['API']['endpoint'] + APIResources.create_user
    context.headers = {"Content-Type": "application/json"}
    context.payload = user_payload("Harry Potter", "Wizard")


@when('Add User Post API method is executed')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)


@then('New user is successfully created')
def step_impl(context):
    data = context.response.json()
    print(data)
    print(data['id'])
    print(data['name'])
    print(data['job'])
    print(data['createdAt'])
    context.user_id = data['id']
    assert context.response.status_code == 201


@given("User {name} and {job} is available")
def step_impl(context, name, job):
    context.url = get_configuration()['API']['endpoint'] + APIResources.create_user
    context.headers = {"Content-Type": "application/json"}
    context.payload = user_payload(name, job)


@given("request url and user credentials are available")
def step_impl(context):
    context.request_session = requests.session()
    context.request_session.auth = (get_configuration()['GITHUB']['user'], get_configuration()['GITHUB']['token'])


@when("I send the request to github api")
def step_impl(context):
    context.response = context.request_session.get(APIResources.github_url)


@then('User repos are return successfully and status code is {status_code:d}')
def step_impl(context, status_code):
    print(context.response.status_code)
    print(context.response.json())
    assert context.response.status_code == status_code
