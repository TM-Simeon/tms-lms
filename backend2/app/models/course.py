# from flask_sqlalchemy import SQLAlchemy
from .dbobject import db
from .dept import Dept
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'course'

    d_id = db.Column(db.String(50), db.ForeignKey(Dept.d_id), nullable=False)
    c_id = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    no_modules = db.Column(db.Integer, nullable=False)
    credit_load = db.Column(db.Integer, nullable=False)
    datecreated = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, d_id, c_id, title, description, icon, no_modules, credit_load):
        # self.s_id = s_id
        self.d_id = d_id
        self.c_id = c_id
        self.title = title
        self.description = description
        self.icon = icon
        self.no_modules = no_modules
        self.credit_load = credit_load
