from flask import Blueprint, request, jsonify
from api.models import User
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

#Check if email is already used
    user = User.query.filter_by(email=email).first()
    if user:

            return response_message("email is already in use", status_code=400)
    user = User(name, email, password)
    user.save()


    return response_message("User %s has been registered successfully" % (name),status_code=200)


@auth.route('/login', methods=["POST"])
def login():
    requestData = request.get_json()

    try:
        email = check_email(requestData.get('email'))
        password = check_password(requestData.get('password'))
    except Exception as exception:
        return response_message(exception.args, status_code=500)

    user = User.query.filter_by(email=email).first()
    if not user:
        return response_message("You are not registered. Please register before logging in", status_code=400)

    if not user.is_correct_password(password):
        return response_message("The email or password provided is wrong", status_code=401)

    auth_token = user.encode_auth_token(user.id)
    if auth_token:
        res = {
            "message": "You are now logged in as {}".format(user.name),
            "auth_token": auth_token.decode()
        }
        return jsonify(res), 200

@auth.route('/reset-password', methods=['POST'])
def reset_password():
    requestData = request.get_json()
    global logged_in_user
    if logged_in_user is None:
        return response_message("Please login", status_code=401)
    try:
        new_password = check_password(requestData.get('new_password'))
        old_password = check_password(requestData.get('old_password'))
    except Exception:
        return response_message("Enter a valid password", status_code=400)

    if logged_in_user["password"] != old_password:
        return response_message("Please input your oldpassword", status_code=401)

    logged_in_user["password"] = new_password

    return response_message("Password has been successfully changed", status_code=200)


@auth.route('/logout', methods=["POST"])
def logout():
    global logged_in_user
    logged_in_user = None
    return "user has been logged out"


