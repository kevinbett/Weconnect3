# Imports

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from api.v1.validation import check_review, check_business, check_update
from api.global_functions import response_message, get_user, format_reviews
from api.models import Business, User, Review


business_blueprint = Blueprint("business", __name__, url_prefix='/api/v1/businesses')


@business_blueprint.route('/', methods=["POST"])
def register_business():
    requestData = request.get_json()

    try:
        name = check_business(requestData.get("name"))
        type = check_business(requestData.get("type"))
        location = check_business(requestData.get("location"))
        category = check_business(requestData.get("category"))
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
    search_query = request.args.get('q', None)
    search_category = request.args.get('category', None)
    search_location = request.args.get('location', None)
    page = request.args.get('page', 1)
    limit = request.args.get('limit', 20)
    filtered_businesses = Business.query

    if search_query:
        # filtered_businesses = filtered_businesses.query.filter_by(name=search_query)
        search_parameter = '%{}%'.format(search_query)
        filtered_businesses = filtered_businesses.filter(Business.name.ilike(search_parameter))
    if search_category:
        filtered_businesses = filtered_businesses.filter_by(category = search_category)
    if search_location:
        filtered_businesses = filtered_businesses.filter_by(location = search_location)

    filtered_businesses = filtered_businesses.paginate(int(page), int(limit))

    businesses = [
        {
            "name" : business.name,
            "type" : business.type,
            "category": business.category,
            "id" : business.id,
            "location": business.location
        } for business in filtered_businesses.items
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
        return response_message(exception.args, status_code=500)

    auth_token = request.headers.get("Authorization")
    user = get_user(auth_token)
    if not isinstance(user, User):
        return response_message(user, 401)

    business = Business.query.filter_by(id=businessId).first()
    if not business:
        return response_message("The business you requested does not exist",
                                status_code=404)
    if business.name == name:
        return response_message("The entry/field you are trying to update is a duplicate", status_code=400)

    if business.user_id is not user.id:
        return response_message("You are not authorized to edit this business", status_code=401)

    try:
        if len(name) > 0:
            business.name = name
        if len(type) > 0:
            business.type = type
        if len(location) > 0:
            business.location = location
        if len(category) > 0:
            business.category = category
        business.save()

        return response_message("Business has been successfully edited", status_code=201)

    except IntegrityError:
        return response_message("Another business has a similar business name")

@business_blueprint.route("/<businessId>", methods=["DELETE"])
def delete_business(businessId):
    auth_token = request.headers.get("Authorization")
    user = get_user(auth_token)
    if not isinstance(user, User):
        return response_message(user, 401)

    business = Business.query.filter_by(id=businessId).first()
    if not business:
        return response_message("The business you requested does not exist", status_code=404)

    if user.id != business.user_id:
        return response_message("You are not authorised to delete this business!", status_code=401)

    business.delete()
    return response_message( "Business has been deleted successfully", status_code=200 )

@business_blueprint.route("/<businessId>", methods=["GET"])
def get_businesses(businessId):
    business = Business.query.filter_by(id=businessId).first()
    if not business:
        return response_message("The business you requested does not exist", status_code=404)

    business = {
        "name": business.name,
        "type": business.type,
        "category": business.category,
        "id": business.id,
        "location": business.location
    }

    return jsonify(business)

@business_blueprint.route("/<businessId>/reviews", methods=["POST"])
def add_review(businessId):
    requestData = request.get_json()

    try:
        feedback = check_review(requestData.get('feedback'))
    except Exception as exception:
        return response_message(exception.args, status_code=500)

    auth_token = request.headers.get("Authorization")
    user = get_user(auth_token)
    if not isinstance(user, User):
        return response_message(user, 401)

    business = Business.query.filter_by(id=businessId).first()
    if not business:
        return response_message("The business you requested does not exist", status_code=404)

    review = Review(feedback)
    review.user_id = user.id
    review.business_id = business.id
    review.save()
    return response_message("Your review has been added", 201)


@business_blueprint.route("/<businessId>/reviews", methods=["GET"])
def view_reviews(businessId):
    business = Business.query.filter_by(id=businessId).first()
    if not business:
        return response_message("The business you requested does not exist", status_code=404)

    business = {
        "name": business.name,
        "type": business.type,
        "category": business.category,
        "id": business.id,
        "location": business.location,
        "reviews": format_reviews(business.reviews)
    }

    return jsonify(business)




