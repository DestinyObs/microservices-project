from models import Product  # Import the Product model
from flask_sqlalchemy import SQLAlchemy
from random import choice, randint

def insert_default_data(db: SQLAlchemy):
    if Product.query.count() == 0:
        sample_products = [
            {"name": "Laptop", "price": 1200, "stock": 15},
            {"name": "Smartphone", "price": 800, "stock": 30},
            {"name": "Headphones", "price": 150, "stock": 50},
            {"name": "Keyboard", "price": 100, "stock": 25},
            {"name": "Monitor", "price": 300, "stock": 10},
            {"name": "Mouse", "price": 50, "stock": 40},
            {"name": "Smartwatch", "price": 200, "stock": 20},
            {"name": "Tablet", "price": 600, "stock": 18},
            {"name": "External SSD", "price": 250, "stock": 12},
            {"name": "Gaming Chair", "price": 350, "stock": 8},
        ]

        for product in sample_products:
            new_product = Product(
                name=product["name"],
                price=product["price"],
                stock=product["stock"]
            )
            db.session.add(new_product)

        db.session.commit()
        print("Inserted default products.")



def format_response(message, status=200):
    return {"message": message, "status": status}

