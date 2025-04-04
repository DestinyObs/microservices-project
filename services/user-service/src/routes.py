from flask import Blueprint, jsonify, request
from models import db, User
import redis
import json

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


user_routes = Blueprint("user_routes", __name__)
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@user_routes.route("/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(name=data["name"], email=data["email"])
    
    db.session.add(new_user)
    db.session.commit()

    # Invalidate cache
    redis_client.delete("users")

    return jsonify(new_user.to_dict()), 201


@user_routes.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200


@user_routes.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    db.session.commit()
    return jsonify(user.to_dict()), 200


@user_routes.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"message": "User deleted"}), 200
