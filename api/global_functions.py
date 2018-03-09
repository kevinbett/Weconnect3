from flask import jsonify

def response_message(message, status_code=200):
    response = {
        "message" : message
    }
    return jsonify(response), status_code