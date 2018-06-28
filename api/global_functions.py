from flask import jsonify
from api.models import Blacklist

def response_message(message, status_code=200):
    response = {
        "message": message
    }
    return jsonify(response), status_code

def get_user(token, split_token=True):
    from api.models import User

    check_token = Blacklist.query.filter_by(token=token).first()

    if check_token:
        return "Expired Token"


    if token:
        if split_token:
            token = token.split(" ")[1]

        user_id = User.decode_auth_token(token)

        if not isinstance(user_id, str):
            user = User.query.filter_by(id=user_id).first()
            return user
        return {
            'message': user_id
        }

    return {
        'message':'provide a valid token'
    }

def format_reviews(reviews):
    formatted_reviews = []
    for review in reviews:
        rev = {

            "feedback":review.feedback
        }

        formatted_reviews.append(rev)

    return formatted_reviews


