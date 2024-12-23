from app import app  # Import your Flask app
from models.database import db
from models.models import User
from flask_security.utils import encrypt_password

# Ensure app context is set up for database access
with app.app_context():
    print("This script is specifically for Creating Admins.")
    username = input("Enter the username of the Admin:")
    email = input("Enter the email of the Admin:")
    password = input("Create a password:")

    # Create admin user
    new_admin = User(username=username, email=email, password=encrypt_password(password), role='admin')
    db.session.add(new_admin)
    db.session.commit()

    print("Admin user created successfully!")
