from flask import Blueprint, request

from api.global_functions import response_message
from api.v1.validation import check_email, check_password, check_name

auth = Blueprint('auth', __name__)

users = []
logged_in_user = None

'''Implementing Register, login and user'''


@auth.route('/register', methods=["POST"])
def register():
    requestData = request.get_json()

    try:
        name = check_name(requestData.get('name'))
        email = check_email(requestData.get('email'))
        password = check_password(requestData.get('password'))
    except Exception as exception:
        return response_message(exception.args, status_code=500)

    last_user_id = users[len(users) - 1]["id"] if len(users) > 0 else 0
    user = {
        "id": last_user_id + 1,
        "name": name,
        "email": email,
        "password": password
    }

    users.append(user)
    return response_message(
        "User %s has been registered successfully" % (name),
        status_code=200)


@auth.route('/login', methods=["POST"])
def login():
    requestData = request.get_json()

    try:
        email = check_email(requestData.get('email'))
        password = check_password(requestData.get('password'))
    except Exception as exception:
        return response_message(exception.args, status_code=500)

    if len(users) <= 0:
        return response_message(
            "You are not registered. Please register before logging in",
            status_code=400)

    for user in users:
        if user["email"] == email and user["password"] == password:
            global logged_in_user
            logged_in_user = user
            return response_message(
                "You are now logged in as %s" % (user["name"]),
                status_code=200)

    return response_message(
        "The user name or password provided is wrong",
        status_code=400)


@auth.route('/logout', methods=["POST"])
def logout():
    global logged_in_user
    logged_in_user = None
    return "user has been logged out"
