from flask import Blueprint, request, jsonify
from api.models import User
from api.global_functions import response_message, get_user
from api.v1.validation import check_email, check_password, check_name

auth = Blueprint('auth', __name__)

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


    return response_message("User %s has been registered successfully" % (name),status_code=201)


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

@auth.route('/change-password', methods=['POST'])
def change_password():
    auth_token = request.headers.get("Authorization")
    user = get_user(auth_token)
    if not isinstance(user, User):
        return response_message(user, 401)

    requestData = request.get_json()
    try:
        new_password = check_password(requestData.get('new_password'))
    except Exception:
        return response_message("Enter a valid password", status_code=400)

    user.set_password(new_password)
    user.save()

    return response_message("Password has been succesfully changed", status_code=200)


@auth.route('/reset-password', methods=['POST'])
def reset_password():
    requestData = request.get_json()
    try:
        email = check_email(requestData.get('email'))
    except Exception:
        return response_message("Enter a valid email", status_code=400)

    user = User.query.filter_by(email=email).first()
    if user:
        auth_token = user.encode_auth_token(user.id)

        if auth_token:
            link = "http://127.0.0.1:5000/reset-password/{}".format(auth_token.decode())
            res = {
                "message": "Reset your password from the provided token",
                "link": link
            }
            return jsonify(res), 200


@auth.route('/reset-password/<token>', methods=['POST'])
def new_password(token):
    requestData = request.get_json()
    try:
        new_password = check_password(requestData.get('new_password'))
    except Exception:
        return response_message("Enter a valid password", status_code=400)
    user = get_user(token, split_token=False)
    if not isinstance(user, User):
        return response_message(user, 401)

    user.set_password(new_password)
    user.save()

    return response_message("Password has been successfully changed", status_code=200)

@auth.route('/logout', methods=['POST'])
def logout():
    auth_token = request.headers.get("Authorization")
    user = get_user(auth_token)
    if not isinstance(user, User):
        return response_message(user, 401)







