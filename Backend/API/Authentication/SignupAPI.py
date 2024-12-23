from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask_security.utils import hash_password
from models.models import User, Role
from models.database import db
def method_name():
    pass
from config.validation import *



class SignupAPI(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if user already exists
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            raise BusinessValidationError(status_code=400, error_code="BE103", error_message="The same registered email already exists!")

        # Create new user and save to database with the "attendee" role
        new_user = User(username=username, email=email, password=hash_password(password), role='attendee', removed=0)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'User registered successfully!',
        })
