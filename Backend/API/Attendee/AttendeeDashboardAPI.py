# from flask import jsonify, request
# from flask_restful import Resource
# from models.database import db
# from models.models import User


# class UserStatusAPI(Resource):
#     def get(self):
#         try:
#             # Get the user ID from request headers (or adjust as needed to extract from JWT/session)
#             user_id = request.headers.get('User-ID')  # Replace with your actual user identification logic
            
#             if not user_id:
#                 return jsonify({'status': 'fail', 'message': 'User ID is required'}), 400

#             # Query the User table for the provided user_id
#             user = User.query.filter_by(userid=user_id).first()

#             if not user:
#                 return jsonify({'status': 'fail', 'message': 'User not found'}), 404

#             return jsonify({
#                 'status': 'success',
#                 'removed': user.removed
#             }), 200
#         except Exception as e:
#             return jsonify({'status': 'fail', 'message': str(e)}), 500
