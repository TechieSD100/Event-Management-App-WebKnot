from flask_restful import Resource
from flask import jsonify
from models.models import Event, Task, TaskMap, User
from models.database import db

class GetEventDashboardAPI(Resource):
    def get(self, event_id):
        try:
            event = Event.query.get(event_id)
            if not event:
                return {"status": "error", "message": "Event not found"}, 404

            # Fetch tasks associated with the event
            tasks = Task.query.filter_by(event_id=event_id).all()
            task_list = []

            for task in tasks:
                # Fetch user assignment for the task
                task_map = TaskMap.query.filter_by(task_id=task.task_id).first()
                if task_map:
                    user = User.query.get(task_map.userid)
                    assigned_to = user.username if user else "(Not assigned yet)"
                else:
                    assigned_to = "(Not assigned yet)"

                task_list.append({
                    "task_id": task.task_id,
                    "task_name": task.task_name,
                    "description": task.description,
                    "status": task.status,
                    "assigned_to": assigned_to
                })

            return {
                "status": "success",
                "event": {
                    "event_id": event.event_id,
                    "event_name": event.event_name,
                    "description": event.description,
                    "location": event.location,
                    "event_date": str(event.event_date),
                },
                "tasks": task_list,
            }, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500



class DeleteTaskAPI(Resource):
    def delete(self, task_id):
        try:
            task = Task.query.get(task_id)
            if not task:
                return {"status": "error", "message": "Task not found"}, 404

            db.session.delete(task)
            db.session.commit()
            return {"status": "success", "message": "Task deleted successfully"}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500


class UpdateTaskStatusAPI(Resource):
    def put(self, task_id):
        try:
            task = Task.query.get(task_id)
            if not task:
                return {"status": "error", "message": "Task not found"}, 404

            task.status = 2  # Mark as completed
            db.session.commit()
            return {"status": "success", "message": "Task marked as completed"}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
        

class GetUsersAPI(Resource):
    def get(self):
        try:
            users = User.query.all()
            user_list = [{"userid": user.userid, "username": user.username} for user in users]
            return {"status": "success", "users": user_list}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500