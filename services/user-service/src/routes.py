from flask import Blueprint, jsonify

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})
