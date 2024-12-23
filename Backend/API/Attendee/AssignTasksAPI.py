from flask_restful import Resource, reqparse
from flask import jsonify
from models.models import TaskMap, Task, Event
from models.database import db

class UserTasksAPI(Resource):
    def get(self, userid):
        try:
            # Query assigned tasks for the user
            task_mappings = TaskMap.query.filter_by(userid=int(userid)).all()

            tasks_data = []
            for mapping in task_mappings:
                task = Task.query.get(mapping.task_id)
                if not task:
                    continue
                event = Event.query.get(task.event_id)

                tasks_data.append({
                    'task_id': task.task_id,
                    'task_name': task.task_name,
                    'description': task.description,
                    'status': task.status,  # 1 for Pending, 2 for Completed
                    'event_name': event.event_name if event else "Unknown"
                })

            return jsonify({'status': 'success', 'tasks': tasks_data})
        except Exception as e:
            return jsonify({'status': 'fail', 'message': str(e)})





class UpdateUserTaskStatusAPI(Resource):
    def post(self):
        # Parse input data
        parser = reqparse.RequestParser()
        parser.add_argument('task_id', type=int, required=True, help="Task ID is required.")
        parser.add_argument('status', type=int, required=True, help="Status is required.")
        args = parser.parse_args()

        try:
            task = Task.query.get(args['task_id'])
            if not task:
                return jsonify({'status': 'fail', 'message': 'Task not found.'})

            # Update the status
            task.status = args['status']
            db.session.commit()

            return jsonify({'status': 'success', 'message': 'Task status updated successfully.'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'status': 'fail', 'message': str(e)})
