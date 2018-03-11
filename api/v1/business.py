'''Imports'''
from flask import Blueprint, request, jsonify
from api.v1 import auth
from api.v1.validation import check_name
from api.global_functions import response_message

business_blueprint = Blueprint("business", __name__, url_prefix='/api/v1/businesses')
businesses = []
reviews = []

@business_blueprint.route('/', methods=["POST"])
def register_business():
    requestData = request.get_json()

    try:
        name = check_name(requestData.get('name'))
        type = check_name(requestData.get("type"))
    except Exception as exception:
        return response_message(exception.args, status_code=200)

    if not auth.logged_in_user:
        return response_message("You must be logged in to register business", 401)

    last_business_id = businesses[len(businesses) - 1]["id"] if len(businesses) > 0 else 0

    business = {
        "id": last_business_id + 1,
        "user_id": auth.logged_in_user["id"],
        "name": name,
        "type": type
    }
    businesses.append(business)

    return response_message("Business has been registered successfully", 201)

@business_blueprint.route('/', methods=["GET"])
def view_businesses():
    res = {
        "businesses": businesses
    }
    return jsonify(res), 200

@business_blueprint.route("/<businessId>", methods=["PUT"])
def update_business(businessId):
    requestData = request.get_json()
    try:
        name = check_name(requestData.get('name'))
        type = check_name(requestData.get("type"))
    except Exception as exception:
        return response_message(exception.args, status_code=500)

    for business in businesses:
        if business["id"] == int(businessId) and business["user_id"] == auth.logged_in_user["id"]:
            if len(name) > 0:
                business["name"] = name
            if len(type) > 0:
                business["type"] = type
            return response_message("Business has been successfully edited", status_code=201)
    return response_message("The business you requested does not exist", status_code=404)

@business_blueprint.route("/<businessId>", methods=["DELETE"])
def delete_business(businessId):
    global businesses
    for business in businesses:
        if business["id"] == int(businessId) and business["user_id"] == auth.logged_in_user["id"]:
            businesses = [business for business in businesses if business["id"] != businessId]
            return response_message("Business has been successfully deleted", status_code=200)
    return response_message("The business you requested does not exist", status_code=404)


@business_blueprint.route("/<businessId>", methods=["GET"])
def get_businesses(businessId):

    for business in businesses:
        if business["id"] == int(businessId) and business["user_id"] == auth.logged_in_user["id"]:
            return jsonify(business)
    else:
        return response_message("The business you requested does not exist", status_code=404)

@business_blueprint.route("/<businessId>/reviews", methods=["POST"])
def add_review(self, business_id):
    requestData = request.get_json()
    try:
        name = check_name(requestData.get('name'))
        type = check_name(requestData.get("type"))
    except Exception as exception:
        return response_message(exception.args, status_code=200)

    for business in self.businesses:
        if business['business_id'] == business_id:

    return {'message': 'Check name of business'}

@business_blueprint.route("/<businessId>/reviews", methods=["GET"])
def view_reviews(self, business_id):
        for business in self.businesses:
            if business['business_id'] == business_id:
                for review in self.reviews:
                    if review['business_id'] == business_id:
                        return review
                return {'message': 'No reviews'}

