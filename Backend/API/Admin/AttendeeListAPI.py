from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required
from models.models import User, Task, Event, TaskMap
from models.database import db

class GetAttendeesAPI(Resource):
    def get(self):
        # Query users with role "attendee"
        attendees = User.query.filter_by(role="attendee").all()
        
        # Serialize the attendees to a list of dictionaries
        attendees_data = [
            {
                'userid': attendee.userid,
                'username': attendee.username,
                'email': attendee.email
            }
            for attendee in attendees
        ]
        
        return jsonify({
            'status': 'success',
            'attendees': attendees_data
        })



class GetTasksAPI(Resource):
    def get(self):
        # Query tasks with status = 0
        tasks = Task.query.filter_by(status=0).all()

        # Serialize the tasks to include event names
        tasks_data = [
            {
                'task_id': task.task_id,
                'task_name': task.task_name,
                'event_name': Event.query.get(task.event_id).event_name
            }
            for task in tasks
        ]

        return jsonify({
            'status': 'success',
            'tasks': tasks_data
        })
    


class AssignTaskAPI(Resource):
    def post(self):
        # Parse the input data
        parser = reqparse.RequestParser()
        parser.add_argument('task_id', type=int, required=True, help="Task ID is required.")
        parser.add_argument('userid', type=int, required=True, help="User ID is required.")
        args = parser.parse_args()

        task_id = args['task_id']
        userid = args['userid']

        try:
            # Check if the task is already assigned
            existing_mapping = TaskMap.query.filter_by(task_id=task_id, userid=userid).first()
            if existing_mapping:
                return jsonify({'status': 'fail', 'message': 'Task is already assigned to this user.'})

            # Create a new task map entry
            task_map = TaskMap(task_id=task_id, userid=userid)
            db.session.add(task_map)

            # Update task status
            task = Task.query.get(task_id)
            if task:
                task.status = 1  # Update status to indicate the task is assigned
                db.session.commit()

            return jsonify({'status': 'success', 'message': 'Task assigned successfully.'})

        except Exception as e:
            db.session.rollback()
            return jsonify({'status': 'fail', 'message': str(e)})



class RemoveUserAPI(Resource):
    def post(self):
        # Parse input data
        parser = reqparse.RequestParser()
        parser.add_argument('userid', type=int, required=True, help="User ID is required.")
        args = parser.parse_args()
        userid = args['userid']

        try:
            # Update user's removed status to 1
            user = User.query.get(userid)
            if not user:
                return jsonify({'status': 'fail', 'message': 'User not found.'})

            user.removed = 1
            db.session.commit()

            return jsonify({'status': 'success', 'message': 'User removed successfully.'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'status': 'fail', 'message': str(e)})

