from .dbobject import db
from datetime import datetime

class Enrollment(db.Model):
    __tablename__ = 'enrollment'

    # one cannot enroll for a course except he is first a user
    # so before creating a record in the enrollment table, the u_id is checked for from the user app
    # the u_id is passed to the enrollment table

    e_id = db.Column(db.Integer, autoincrement=True)
    u_id = db.Column(db.String(50), nullable=False)
    d_id = db.Column(db.String(50), primary_key=True, nullable=False)
    elective1 = db.Column(db.String(100), nullable=False)
    elective2 = db.Column(db.String(100), nullable=False)
    elective3 = db.Column(db.String(100))
    elective4 = db.Column(db.String(100))
    elective5 = db.Column(db.String(100))
    datecreated = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, u_id, d_id, elective1, elective2, elective3=None, elective4=None, elective5=None):
        self.u_id = u_id
        self.d_id = d_id
        self.elective1 = elective1
        self.elective2 = elective2
        self.elective3 = elective3
        self.elective4 = elective4
        self.elective5 = elective5

