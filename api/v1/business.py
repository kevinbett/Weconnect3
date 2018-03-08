'''Imports'''
from flask import Blueprint, request, jsonify
from api.v1 import auth

business_blueprint = Blueprint("business", __name__, url_prefix='/api/v1/businesses')
businesses = []

@business_blueprint.route('/', methods=["POST", "GET"])
def register_business():
    name = request.form.get("name")
    type = request.form.get("type")

    if not auth.logged_in_user:
        return 'You must be logged in to register business'

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

def view_businesses():
    return jsonify(businesses)

@business_blueprint.route("/<businessId>", methods=["PUT"])
def update_business(businessId):
    name = request.form.get("name")
    type = request.form.get("type")

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
            return business
    else:
        return "The business you entered does not exist"
