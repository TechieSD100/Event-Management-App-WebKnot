from imports import *

def create_app():
    app_create = Flask(__name__)
    if os.getenv('ENV', "development") == "production":
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting Local Development")
        app_create.config.from_object(LocalDevelopmentConfig)
 
    # Adjust CORS to allow all methods from any origin for now
    CORS(app_create, resources={r"/api/*": {"origins": "*"}})
    
    db.init_app(app_create)
    api_create = Api(app_create)
    JWTManager(app_create)
    security.init_app(app_create, user_datastore)
    app_create.app_context().push()
    
    return app_create, api_create

app, api = create_app()

api.add_resource(SignupAPI, '/api/signup')
api.add_resource(LoginAPI, '/api/login')
api.add_resource(AdminLoginAPI, '/api/admin-login')
api.add_resource(CreateEventAPI, '/api/create-event')
api.add_resource(GetAllEventsAPI, '/api/events')
api.add_resource(DeleteEventAPI, '/api/delete-event/<int:event_id>')
api.add_resource(UpdateEventAPI, '/api/edit-event/<int:event_id>')
api.add_resource(GetEventDetailsAPI, '/api/event-details/<int:event_id>')
api.add_resource(GetAttendeesAPI, '/api/attendees')
api.add_resource(GetEventDashboardAPI, '/api/event-dashboard/<int:event_id>')
api.add_resource(CreateTaskAPI, '/api/event-dashboard/<int:event_id>/create-task')
api.add_resource(DeleteTaskAPI, '/api/task/<int:task_id>/delete')
api.add_resource(UpdateTaskStatusAPI, '/api/task/<int:task_id>/complete')
api.add_resource(GetTasksAPI, '/api/fetch-tasks')
api.add_resource(AssignTaskAPI, '/api/assign-task')
api.add_resource(GetTaskDetailsAPI, '/api/task/<int:task_id>')
api.add_resource(UpdateTaskDetailsAPI, '/api/task/<int:task_id>/update')
api.add_resource(GetUsersAPI, '/api/get-users')
api.add_resource(RemoveUserAPI, '/api/remove-user')
api.add_resource(UserTasksAPI, '/api/user-tasks/<int:userid>')
api.add_resource(UpdateUserTaskStatusAPI, '/api/update-task-status')
# api.add_resource(UserStatusAPI, '/api/user-status')



if __name__ == "__main__":
    app.run(debug=True)