from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required
from models.models import Event
from models.database import db
# from API.Authentication.AdminLoginAPI import admin_required

class GetAllEventsAPI(Resource):
    # @jwt_required
    def get(self):
        # Fetch all events from the database
        events = Event.query.all()
        
        # Serialize the events to a list of dictionaries
        events_data = [
            {
                'event_id': event.event_id,
                'event_name': event.event_name,
                'description': event.description,
                'location': event.location,
                'event_date': event.event_date.strftime('%Y-%m-%d')  # Format the date as a string
            }
            for event in events
        ]
        
        # Return the events as a JSON response
        return jsonify({
            'status': 'success',
            'events': events_data
        })


