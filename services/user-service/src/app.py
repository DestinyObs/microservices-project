from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis
import json

from config import SQLALCHEMY_DATABASE_URI
from models import db, User
from routes import user_routes
from utils import insert_default_data

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Ensure tables are created before handling requests
with app.app_context():
    db.create_all()
    insert_default_data(db)

print("Database migration completed successfully!")

# Register blueprints
app.register_blueprint(user_routes)

@app.route("/")
def home():
    return {"message": "User Service is running"}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# Cache user data
@app.route("/users", methods=["GET"])
def get_users():
    cached_users = redis_client.get("users")

    if cached_users:
        print("Serving users from cache")
        return jsonify(json.loads(cached_users))

    print("Fetching users from DB and caching")
    users = User.query.all()
    user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]

    redis_client.setex("users", 60, json.dumps(user_list))  # Cache for 60 sec
    return jsonify(user_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
