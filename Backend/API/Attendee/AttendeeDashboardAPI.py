from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.database import db
from models.models import User  # Assuming User is your user model

class UserStatusAPI(Resource):
    # @jwt_required()
    def get(self, user_id):
        try:
            # Fetch the user details from the database
            user = User.query.filter_by(userid = user_id).first()
            if user.removed == 1:
                return {"status": "success"}, 200

        except Exception as e:
            # Ensure all errors are handled and return JSON
            return {"status": "error", "message": str(e)}, 500
