import re


def check_name(name):
    if re.match("^$", name.strip()):
        raise Exception("You have entered an invalid name")
    else:
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


def check_business(name):
    if re.match("^$", name.strip()):
        raise Exception("Business name or type cannot be blank")
    else:
        return name
