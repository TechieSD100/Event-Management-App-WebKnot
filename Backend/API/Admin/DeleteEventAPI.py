from flask_restful import Resource
from flask import jsonify
from models.models import Event
from models.database import db

class DeleteEventAPI(Resource):
    def delete(self, event_id):
        try:
            event = Event.query.get(event_id)
            if not event:
                return jsonify({
                    "status": "error",
                    "message": "Event not found"
                }), 404

            # Delete the event
            db.session.delete(event)
            db.session.commit()

            return jsonify({
                "status": "success",
                "message": "Event deleted successfully"
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                "status": "error",
                "message": f"An error occurred: {str(e)}"
            }), 500
