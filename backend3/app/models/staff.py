from .dbobject import db
from datetime import datetime
from .user import User

class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_id = db.Column(db.Integer,db.ForeignKey('users.u_id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    datecreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, u_id, status):
        # self.staff_id = staff_id
        self.u_id = u_id
        self.status = status
