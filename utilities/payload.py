def user_payload(name, job):
    body = {
        "name": name,
        "job": job
    }
    return body


def create_user_payload(username, password):
    body = {
        "userName": username,
        "password": password
    }
    return body
