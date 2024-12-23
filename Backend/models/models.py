from models.database import db
from flask_security import UserMixin, RoleMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)
    removed = db.Column(db.Integer)

    @property
    def id(self):
        return self.userid
    
    def get_id(self):
        return str(self.userid)


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)


class Event(db.Model):
    __tablename__ = 'event'
    event_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    event_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(350))
    location = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)


class Task(db.Model):
    __tablename__ = 'task'
    task_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    task_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(300))
    status = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)



class TaskMap(db.Model):
    __tablename__ = 'task-map'
    map_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False)