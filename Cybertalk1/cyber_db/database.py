# Cybertalk1/cyber_db/database.py
from Cybertalk1.cyber_db import db
from Cybertalk1.cyber_db.models import User
from flask_bcrypt import generate_password_hash

def seed_database():
    """Seed the database with initial data."""
    admin_password = generate_password_hash("admin123").decode("utf-8")
    user_password = generate_password_hash("user123").decode("utf-8")

    # Create default admin and user
    admin = User(username="admin", email="admin@example.com", password=admin_password, role="admin")
    user = User(username="user", email="user@example.com", password=user_password, role="user")

    # Add users to the database
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()

    print("Database seeded with initial data!")
