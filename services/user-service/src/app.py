from flask import Flask, jsonify
from routes import user_routes

app = Flask(__name__)

# Register Blueprints (Routes)
app.register_blueprint(user_routes)

@app.route("/")
def home():
    return jsonify({"message": "User Service is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
