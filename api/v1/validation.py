import re

def check_name(username):
    if not re.match("^[a-zA-Z0-9_]*$", username):
        raise Exception("You have entered an invalid username")
    return username

def check_password(password):
    if len(password) < 6:
        raise Exception("Your password should have atleast 6 characters")
    return password

def check_email(email):
    if not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
        raise Exception("You have not entered a valid email")
    return email
