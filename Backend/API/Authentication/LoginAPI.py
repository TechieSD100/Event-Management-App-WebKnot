from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask_security import login_user
from flask_security.utils import verify_password
from models.models import User
from models.database import db
from config.validation import BusinessValidationError


class LoginAPI(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            raise BusinessValidationError(
                status_code=400,
                error_code="BE101",
                error_message="Email and password are required!"
            )

        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if not user:
            raise BusinessValidationError(
                status_code=401,
                error_code="BE104",
                error_message="Invalid email or password!"
            )

        # Verify password
        if not verify_password(password, user.password):
            raise BusinessValidationError(
                status_code=401,
                error_code="BE104",
                error_message="Invalid email or password!"
            )

        login_user(user)
        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Login successful!',
            'user': {
                'userid': user.userid,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        })
