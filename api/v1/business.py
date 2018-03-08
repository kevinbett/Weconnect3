'''Imports'''
from flask import Blueprint, request, jsonify
from api.v1 import auth
from api.v1.validation import check_name

business_blueprint = Blueprint("business", __name__, url_prefix='/api/v1/businesses')
businesses = []

@business_blueprint.route('/', methods=["POST"])
def register_business():
    requestData = request.get_json()

    try:
        name = check_name(requestData.get('name'))
        type = check_name(requestData.get("type"))
    except Exception as exception:
        res = {
            "message": exception.args
        }
        return jsonify(res), 500

    if not auth.logged_in_user:
        return 'You must be logged in to register business', 401

    if not name or not type:
        return "You must enter both name and Type of business"

    last_business_id = businesses[len(businesses) - 1]["id"] if len(businesses) > 0 else 0

    business = {
        "id": last_business_id + 1,
        "user_id": auth.logged_in_user["id"],
        "name": name,
        "type": type
    }
    businesses.append(business)

    return "Business has been registered successfully"

@business_blueprint.route('/', methods=["GET"])
def view_businesses():
    res = {
        "businesses": businesses
    }
    return jsonify(res), 200

@business_blueprint.route("/<businessId>", methods=["PUT"])
def update_business(businessId):
    requestData = request.get_json()
    name = requestData.get("name")
    type = requestData.get("type")

    if not name and not type:
        return "You must to either the name or type of business to edit"

    for business in businesses:
        if business["id"] == int(businessId) and business["user_id"] == auth.logged_in_user["id"]:
            if len(name) > 0:
                business["name"] = name
            if len(type) > 0:
                business["type"] = type
            return "Business has been successfully edited"
    return "The business you entered does not exist"

@business_blueprint.route("/<businessId>", methods=["DELETE"])
def delete_business(businessId):
    global businesses
    for business in businesses:
        if business["id"] == int(businessId) and business["user_id"] == auth.logged_in_user["id"]:
            businesses = [business for business in businesses if business["id"] != businessId]
            return "Business has been successfully deleted"
    return "The business you entered does not exist"


@business_blueprint.route("/<businessId>", methods=["GET"])
def get_businesses(businessId):

    for business in businesses:
        if business["id"] == int(businessId) and business["user_id"] == auth.logged_in_user["id"]:
            return jsonify(business)
    else:
        return "The business you entered does not exist"
