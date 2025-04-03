from models import User  # Import the User model
from flask_sqlalchemy import SQLAlchemy
from random import choice

def insert_default_data(db: SQLAlchemy):
    if User.query.count() == 0:
        sample_users = [
            {"name": "John Doe", "email": "john.doe@example.com"},
            {"name": "Jane Smith", "email": "jane.smith@example.com"},
            {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
            {"name": "Bob Williams", "email": "bob.williams@example.com"},
            {"name": "Charlie Brown", "email": "charlie.brown@example.com"},
            {"name": "David Miller", "email": "david.miller@example.com"},
            {"name": "Emma Wilson", "email": "emma.wilson@example.com"},
            {"name": "Frank Thomas", "email": "frank.thomas@example.com"},
            {"name": "Grace Lee", "email": "grace.lee@example.com"},
            {"name": "Henry White", "email": "henry.white@example.com"},
        ]

        for user in sample_users:
            new_user = User(
                name=user["name"],
                email=user["email"]
            )
            db.session.add(new_user)

        db.session.commit()
        print("Inserted default users.")


def format_response(message, status=200):
    return {"message": message, "status": status}




