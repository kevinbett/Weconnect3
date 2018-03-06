from flask import Blueprint, request, jsonify
from api.v1 import auth
business_blueprint = Blueprint("posts", __name__)

businesses = []

@business_blueprint.route("/businesses", methods=["POST", "GET"])
def add_business():

    if request.method == "POST":
        return add_new_business(request)
    if request.method == "GET":
        return view_businesses()

def add_new_business(request):
    name = request.form.get("name")
    content = request.form.get("type")

    if not name or not content:
        return "You must enter both name and type"

    last_business_id = len(businesses)

    business = {
        "id": last_business_id + 1,
        "name": name,
        "type": content
    }
    businesses.append(business)

    return "Business with name %s has been added succesfully"%(name), 201


def view_businesses():
    return jsonify(businesses)
