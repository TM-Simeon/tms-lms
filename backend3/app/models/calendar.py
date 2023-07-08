
from .dbobject import db
from datetime import datetime

class Calendar(db.Model):
    __tablename__ = 'calendar'

    # from the calendar scripts, a calendar is generated and the dates are passed to this table

    c_name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)


    def __init__(self, c_name, start_date, end_date):
        self.c_name = c_name
        self.start_date = start_date
        self.end_date = end_date