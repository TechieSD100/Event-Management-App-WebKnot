from flask_restful import Resource
from flask import jsonify, request
from models.models import Event
from models.database import db
import datetime

class GetEventDetailsAPI(Resource):
    def get(self, event_id):
        event = Event.query.get(event_id)
        if not event:
            return jsonify({"status": "error", "message": "Event not found"}), 404
        return jsonify({
            "status": "success",
            "event": {
                "event_id": event.event_id,
                "event_name": event.event_name,
                "description": event.description,
                "location": event.location,
                "event_date": str(event.event_date)
            }
        })



class UpdateEventAPI(Resource):
    def put(self, event_id):
        data = request.get_json()
        event = Event.query.get(event_id)
        if not event:
            return jsonify({"status": "error", "message": "Event not found"}), 404
        
        event.event_name = data.get('event_name', event.event_name)
        event.description = data.get('description', event.description)
        event.location = data.get('location', event.location)
        
        # Ensure the date is valid
        event_date = data.get('event_date', str(event.event_date))
        try:
            event.event_date = datetime.datetime.strptime(event_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"status": "error", "message": "Invalid date format. Use YYYY-MM-DD"}), 400

        db.session.commit()
        return jsonify({"status": "success", "message": "Event updated successfully"})