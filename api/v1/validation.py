import re


def check_name(name):
    if not re.match("^[a-zA-Z0-9_ ]*$", name):
        raise Exception("You have entered an invalid name")
    return name


def check_password(password):
    if len(password) < 6:
        raise Exception("Your password should have atleast 6 characters")
    return password


def check_email(email):
    if not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
        raise Exception("You have not entered a valid email")
    return email


def check_review(review):
    if re.match("^$", review.strip()):
        raise Exception("You have entered an invalid review")
    return review


