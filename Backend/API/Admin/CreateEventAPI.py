from flask_restful import Resource
from flask import request, make_response, jsonify
from models.models import Event
from models.database import db
from datetime import datetime

class CreateEventAPI(Resource):
    def post(self):
        data = request.get_json()
        event_name = data.get('event_name')
        description = data.get('description')
        location = data.get('location')
        event_date = data.get('event_date')

        # Ensure event_date is in the correct format
        try:
            event_date = datetime.strptime(event_date, '%Y-%m-%d').date()  # Convert string to date
        except ValueError:
            return {"status": "error", "message": "Invalid date format. Use YYYY-MM-DD"}, 400

        # Create a new Event object
        new_event = Event(
            event_name=event_name,
            description=description,
            location=location,
            event_date=event_date
        )

        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()

        return {
            'status': 'success',
            'message': 'Event created successfully!',
            'event': {
                'event_name': new_event.event_name,
                'description': new_event.description,
                'location': new_event.location,
                'event_date': str(new_event.event_date),  # Ensure event_date is a string
            }
        }, 201
