from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__)

users = []
logged_in_user = None

'''Implementing Register, login and user'''

@auth.route('/register', methods=["POST"])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not name or not email or not password:
        return "You need to fill in the name, email and password"

    last_user_id = users[len(users) - 1]["id"] if len(users) > 0 else 0
    user = {
        "id": last_user_id + 1,
        "name": name,
        "email": email,
        "password": password
    }

    users.append(user)

    return "User %s has been registered successfully"%(name)

@auth.route('/login', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return "You have not filled in either the email or password"
    if len(users) <= 0:
        return "You are not registered. Please register before logged in"

    for user in users:
        if user["email"] == email and user["password"] == password:
            global logged_in_user
            logged_in_user = user
            return "You are now logged in"

    return "Check Username or password"

@auth.route('/logout', methods=["GET"])
def logout():
    global logged_in_user
    logged_in_user = None

