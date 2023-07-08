# from flask_sqlalchemy import SQLAlchemy
from .dbobject import db
from .user import User
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'student'

    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department = db.Column(db.String(100), nullable=False)
    datecreated = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, nullable=False)
    u_id = db.Column(db.Integer, db.ForeignKey(User.u_id), nullable=False)

    def __init__(self, department, status, u_id):
        # self.s_id = s_id
        self.department = department
        self.status = status
        self.u_id = u_id
