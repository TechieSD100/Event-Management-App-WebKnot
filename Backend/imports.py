from models.models import *
from models.database import *

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

from config.security import *
from config.config import *

from flask_restful import Api
from API.Authentication.SignupAPI import *
from API.Authentication.LoginAPI import *
from API.Authentication.AdminLoginAPI import *
from API.Admin.CreateEventAPI import *
from API.Admin.DashboardAPI import *
from API.Admin.DeleteEventAPI import *
from API.Admin.EditEventAPI import *
from API.Admin.AttendeeListAPI import *
from API.Admin.EventDashboardAPI import *
from API.Admin.CreateTaskAPI import *
from API.Admin.EditTaskAPI import *
from API.Attendee.AssignTasksAPI import *
from API.Attendee.AttendeeDashboardAPI import *