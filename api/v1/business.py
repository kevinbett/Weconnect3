'''Imports'''
from flask import Blueprint, request, jsonify
from api.v1 import auth

business_blueprint = Blueprint("posts", __name__)

'''Initiating empty list'''
businesses = []

''''''
@business_blueprint.route("/businesses", methods=["POST", "GET"])
def register_business(request):
    name = request.args.get("name")
    content = request.args.get("type")

    if not name or not content:
        return "You must enter both name and Type of business"

    last_business_id = businesses[len(businesses) - 1]["id"] if len(businesses) > 0 else 0

    business = {
        "id": last_business_id + 1,
        "user_id": auth.logged_in_user["id"],
        "name": name,
        "type": content
    }
    businesses.append(business)

    return "Business with name %s has been registered succesfully"%(name)

def view_businesses():
    return jsonify(businesses)

@business_blueprint.route("businesses/<businessId>", methods=["PUT", "GET"])
def update_business(request, id):
    name = request.args.get("name")
    type = request.args.get("type")

    if not name and not type:
        return "You must to either the name or type of business to edit"

    for business in businesses:
        if business["id"] == int(id) and business["user_id"] == auth.logged_in_user["id"]:
            if len(name) > 0:
                business["name"] = name
            if len(type) > 0:
                business["type"] = type
            return "Business profile has been updated successfully"
    return "The business you entered does not exist"

@business_blueprint.route("//businesses/<businessId>", methods=["DELETE"])
def delete_business(id):
    global businesses
    for business in businesses:
        if business["id"] == int(id) and business["user_id"] == auth.logged_in_user["id"]:
            businesses = [business for business in businesses if business["id"] != id]
            return "Business has been deleted successfully"
    return "The business you entered does not exist"


@business_blueprint.route("/businesses/<businessId>", methods=["GET"])
def get_businesses():
    name = request.args.get("name")
    type = request.args.get("type")

    if not name and not type:
        return "You must to either the name or type of business to search"

    for business in businesses:
        if business["id"] == int(id) and business["user_id"] == auth.logged_in_user["id"]:
            if len(name) < 0:
                business["name"] = name
            if len(type) < 0:
                business["type"] = type
            return jsonify(businesses)
        return "The business you entered does not exist"

