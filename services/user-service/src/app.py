from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from models import db, User
from routes import user_routes
from utils import insert_default_data

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
