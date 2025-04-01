from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from models import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Ensure tables are created before handling requests
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "User Service is running"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
