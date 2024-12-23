from flask_restful import Resource, reqparse
from models.models import Task, TaskMap, User, Event
from models.database import db

class GetTaskDetailsAPI(Resource):
    def get(self, task_id):
        try:
            # Fetch task details
            task = Task.query.get(task_id)
            if not task:
                return {"status": "error", "message": "Task not found"}, 404

            # Fetch assigned user (if any)
            task_map = TaskMap.query.filter_by(task_id=task_id).first()
            assigned_user = User.query.get(task_map.userid) if task_map else None

            # Fetch event details
            event = Event.query.get(task.event_id)

            return {
                "status": "success",
                "task": {
                    "task_id": task.task_id,
                    "task_name": task.task_name,
                    "description": task.description,
                    "status": task.status,
                    "event_id": task.event_id,
                },
                "assigned_user": {
                    "userid": assigned_user.userid,
                    "username": assigned_user.username,
                } if assigned_user else None,
                "event": {
                    "event_id": event.event_id,
                    "event_name": event.event_name,
                } if event else None,
            }, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500


class UpdateTaskDetailsAPI(Resource):
    def put(self, task_id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('task_name', required=True, help="Task name is required")
            parser.add_argument('description', required=True, help="Description is required")
            parser.add_argument('status', type=int, required=False)  # Updated to optional
            parser.add_argument('assigned_user_id', type=int, required=False)
            args = parser.parse_args()
            
            # Update task details
            task = Task.query.get(task_id)
            if not task:
                return {"status": "error", "message": "Task not found"}, 404
            
            task.task_name = args['task_name']
            task.description = args['description']

            # Determine and set task status based on assigned user
            if args['assigned_user_id']:
                task.status = 1  # Task is assigned
            else:
                task.status = 0  # Task is not assigned

            # Update task assignment
            if args['assigned_user_id']:
                task_map = TaskMap.query.filter_by(task_id=task_id).first()
                if task_map:
                    task_map.userid = args['assigned_user_id']
                else:
                    task_map = TaskMap(task_id=task_id, userid=args['assigned_user_id'])
                    db.session.add(task_map)
            else:
                # If no user is assigned, delete any existing mapping
                TaskMap.query.filter_by(task_id=task_id).delete()
            
            db.session.commit()
            return {"status": "success", "message": "Task updated successfully"}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500



class GetUsersAPI(Resource):
    def get(self):
        try:
            # Query users with the role "attendee"
            attendees = User.query.filter_by(role="attendee", removed=0).all()
            attendee_list = [{"userid": user.userid, "username": user.username} for user in attendees]
            
            return {"status": "success", "users": attendee_list}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500