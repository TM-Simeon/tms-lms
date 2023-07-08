
from .dbobject import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    datecreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, username, dob, password, status):
        # self.u_id = u_id
        self.username = username
        self.email = email
        self.dob = dob
        self.password = password
        self.status = status


# user = User(u_id=1,  email='john@gmail.com',dob=datetime.utcnow(), password='1234', status=True)
# print(user.dob)