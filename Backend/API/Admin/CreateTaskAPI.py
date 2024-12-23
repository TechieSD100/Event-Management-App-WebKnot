from flask_restful import Resource
from flask import request
from models.database import db
from models.models import Task, Event


class CreateTaskAPI(Resource):
    def post(self, event_id):
        """
        Create a new task associated with a specific event ID.
        """
        try:
            # Get the event from the database
            event = Event.query.get(event_id)
            if not event:
                return {"status": "error", "message": "Event not found"}, 404

            # Parse the request data
            data = request.get_json()
            task_name = data.get("task_name")
            description = data.get("description")

            if not task_name or not description:
                return {"status": "error", "message": "Task name and description are required"}, 400

            # Create a new Task
            new_task = Task(
                task_name=task_name,
                description=description,
                status=0,  # Default status: 0 (e.g., Pending)
                event_id=event_id
            )

            db.session.add(new_task)
            db.session.commit()

            return {
                "status": "success",
                "message": "Task created successfully",
                "task": {
                    "task_id": new_task.task_id,
                    "task_name": new_task.task_name,
                    "description": new_task.description,
                    "event_id": new_task.event_id,
                    "status": new_task.status
                }
            }, 201
        except Exception as e:
            db.session.rollback()
            return {"status": "error", "message": str(e)}, 500
