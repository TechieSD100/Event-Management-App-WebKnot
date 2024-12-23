from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask_security import login_user
from flask_security.utils import verify_password
from models.models import User  # Assuming a unified User model for admin and attendees
from models.database import db
from config.validation import BusinessValidationError
from functools import wraps
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity
from datetime import timedelta

class AdminLoginAPI(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            raise BusinessValidationError(
                status_code=400,
                error_code="BE101",
                error_message="Username and password are required!"
            )

        # Check if user exists
        user = User.query.filter_by(username=username).first()
        if not user:
            raise BusinessValidationError(
                status_code=401,
                error_code="BE104",
                error_message="Invalid username or password!"
            )

        # Check if the user is an admin
        if user.role != 'admin':
            raise BusinessValidationError(
                status_code=403,
                error_code="BE105",
                error_message="Access denied! This user is not an admin."
            )

        # Verify password
        if not verify_password(password, user.password):
            raise BusinessValidationError(
                status_code=401,
                error_code="BE104",
                error_message="Invalid username or password!"
            )


        access_token = create_access_token(identity=user.userid)
        login_user(user)
        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Admin login successful!',
            'admin': {
                'user_id': user.userid,
                'username': user.username,
                'role': user.role
            }
        })

