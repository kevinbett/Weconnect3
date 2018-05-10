from flask import jsonify


def response_message(message, status_code=200):
    response = {
        "message": message
    }
    return jsonify(response), status_code

def get_user(auth_token):
    from api.models import User

    if auth_token:
        token = auth_token.split(" ")[1]
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