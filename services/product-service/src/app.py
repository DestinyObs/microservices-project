from flask import Flask, jsonify, request
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask_sqlalchemy import SQLAlchemy
import redis
import json

from config import SQLALCHEMY_DATABASE_URI
from models import db, Product
from routes import product_routes
from utils import insert_default_data

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db.init_app(app)

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Ensure tables are created before handling requests
with app.app_context():
    db.create_all()
    insert_default_data(db)

print("Database migration completed successfully!")

# Define Prometheus metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])

# Register Prometheus /metrics endpoint
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()  # Add the /metrics route
})

@app.before_request
def before_request():
    # Count incoming requests
    REQUESTS.labels(method=request.method, endpoint=request.endpoint).inc()

# Register blueprints
app.register_blueprint(product_routes)

# Application routes
@app.route("/")
def home():
    return {"message": "Product Service is running"}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# Cache product data
@app.route("/products", methods=["GET"])
def get_products():
    cached_products = redis_client.get("products")

    if cached_products:
        print("Serving products from cache")
        return jsonify(json.loads(cached_products))

    print("Fetching products from DB and caching")
    products = Product.query.all()
    product_list = [
        {"id": product.id, "name": product.name, "price": product.price, "stock": product.stock}
        for product in products
    ]

    redis_client.setex("products", 60, json.dumps(product_list))  # Cache for 60 sec
    return jsonify(product_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
