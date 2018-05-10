# Imports

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from api.v1 import auth
from api.v1.validation import check_name, check_review, check_business, check_update
from api.global_functions import response_message, get_user
from api.models import Business, User


business_blueprint = Blueprint("business", __name__, url_prefix='/api/v1/businesses')
businesses = []
reviews = []


@business_blueprint.route('/', methods=["POST"])
def register_business():
    requestData = request.get_json()

    try:
        name = check_business(requestData.get("name"))
        type = check_business(requestData.get("type"))
        location = check_business(requestData.get("location"))
        category = check_business(requestData.get("location"))
    except Exception as exception:
        return response_message(exception.args, status_code=200)

    auth_token = request.headers.get("Authorization")
    user = get_user(auth_token)
    if not isinstance(user, User):
        return response_message(user, 401)

    try:
        business = Business(name, type, location, category)
        business.user_id = user.id
        business.save()
        return response_message("Business has been registered successfully", 201)
    except IntegrityError:
        return response_message("Duplicate business name", 400)


@business_blueprint.route('/', methods=["GET"])
def view_businesses():
    businessQuery = Business.query.all()
    businesses = [
        {
            "name" : business.name,
            "type" : business.type,
            "category": business.category,
            "id" : business.id,
            "location": business.location
        } for business in businessQuery
    ]
    response = {
        "businesses": list(businesses)
    }

    return jsonify(response)

@business_blueprint.route("/<businessId>", methods=["PUT"])
def update_business(businessId):
    requestData = request.get_json()
    try:
        name = check_update(requestData.get("name"))
        type = check_update(requestData.get("type"))
        location = check_update(requestData.get("location"))
        category = check_update(requestData.get("category"))
    except Exception as exception:
        return response_message(exception.args, status_code=201)

    auth_token = request.headers.get("Authorization")
    user = get_user(auth_token)
    if not isinstance(user, User):
        return response_message(user, 401)

    business = user.businesses.filter_by(id=id).first()

    if not business:
        return response_message("The business you requested does not exist", status_code=404)

    if len(name) > 0:
        business.name = name
    if len(type) > 0:
        business.type = type
    if len(location) > 0:
        business.location = location
    if len(category) > 0:
        business.category = category

    return response_message("Business has been successfully edited", status_code=201)

@business_blueprint.route("/<businessId>", methods=["DELETE"])
def delete_business(businessId):
    global businesses
    for index, business in enumerate(businesses):
        if business["id"] == int(businessId):
            if business["user_id"] != auth.logged_in_user["id"]:
                return response_message("You are not authorised to delete this business", status_code=401)
            del businesses[index]
            return response_message("Business has been successfully deleted", status_code=200)
    return response_message("The business you requested does not exist", status_code=404)


@business_blueprint.route("/<businessId>", methods=["GET"])
def get_businesses(businessId):
    for business in businesses:
        if business["id"] == int(businessId): #and business["user_id"] == auth.logged_in_user["id"]:
            return jsonify(business)
    else:
        return response_message("The business you requested does not exist", status_code=404)


@business_blueprint.route("/<businessId>/reviews", methods=["POST"])
def add_review(businessId):
    requestData = request.get_json()

    try:
        feedback = check_review(requestData.get('feedback'))
    except Exception as exception:
        return response_message(exception.args, status_code=200)

    if not auth.logged_in_user:
        return response_message("You must be logged in to review a business", 401)

    for business in businesses:
        if business["id"] == int(businessId):

            review = {
                "user_id": auth.logged_in_user["id"],
                "businessId": int(businessId),
                "feedback": feedback
            }
            reviews.append(review)

            return response_message("Your review has been posted", 201)

    return response_message("The business does not exist", status_code=404)


@business_blueprint.route("/<businessId>/reviews", methods=["GET"])
def view_reviews(businessId):
    if not auth.logged_in_user:
        return response_message("You must be logged in to view reviews", 401)

    for review in reviews:
        if review["businessId"] == int(businessId) and review["user_id"] == auth.logged_in_user["id"]:
            return jsonify(review)
    else:
        return response_message("This business has no review yet", status_code=404)
