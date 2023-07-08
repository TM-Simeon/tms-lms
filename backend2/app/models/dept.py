from .dbobject import db
from datetime import datetime, timedelta

class Dept(db.Model):
    __tablename__ = 'dept'

    d_id = db.Column(db.String(50), primary_key=True)
    core1 = db.Column(db.String(100),nullable=False)
    core2 = db.Column(db.String(100),nullable=False)
    core3 = db.Column(db.String(100))
    core4 = db.Column(db.String(100))
    core5 = db.Column(db.String(100))
    datecreated = db.Column(db.DateTime, default=datetime.utcnow())


    def __init__(self, d_id, core1, core2, core3, core4, core5):
        self.d_id = d_id
        self.core1 = core1
        self.core2 = core2
        self.core3 = core3
        self.core4 = core4
        self.core5 = core5
