from behave import *
import requests
from utilities.configurations import get_configuration
from utilities.resources import APIResources
from utilities.payload import create_user_payload


@given(u'User data is available')
def step_impl(context):
    context.url = get_configuration()['API']['base_url'] + APIResources.create_account
    context.headers = {"Content-Type": "application/json"}
    context.payload = create_user_payload("tim", "Password@123")


@when(u'Post request is send to api url for account creation')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)


@then(u'User account is created')
def step_impl(context):
    data = context.response.json()
    print(data)
    print(data['userID'])
    print(data['username'])
    print(context.response.status_code)
    context.user_id = data['userID']
    context.username = data['username']
    assert context.response.status_code == 201


@then(u'Verify User account is not created')
def step_impl(context):
    data = context.response.json()
    print(context.response.status_code)
    assert context.response.status_code == 406
    assert data['code'] == "1204"
    assert data['message'] == 'User exists!'


@then(u'Verify the account username')
def step_impl(context):
    assert context.username == "tim"
