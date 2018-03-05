
from flask import Blueprint, request, jsonify

business_blueprint = Blueprint("posts", __name__)

businesses = []

@business_blueprint.route("/", methods=["POST", "GET"])
def business_functionality():

    if request.method == "POST":
        return add_business(request)
    if request.method == "GET":
        return view_businesses()
    