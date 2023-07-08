from .dbobject import db
from datetime import datetime

class Result(db.Model):
    __tablename__ = 'result'

    # before the result is recorded, the student data will be retrived from the user app
    # before assigning the graded score, check if deadline is past already, and mark over 50% if so
    
    s_id = db.Column(db.Integer, nullable=False)
    c_id = db.Column(db.String(50), nullable=False)
    module_no = db.Column(db.Integer, nullable=False)
    assess_type = db.Column(db.String(25), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_due = db.Column(db.Date, nullable=False)
    date_taken = db.Column(db.DateTime, default=datetime.utcnow())
    graded_score = db.Column(db.Integer)

    def __init__(self, s_id, c_id, module_no, assess_type, score, date_due):
        self.s_id = s_id
        self.c_id = c_id
        self.module_no = module_no
        self.assess_type = assess_type
        self.score = score
        self.date_due = date_due

        today = datetime.utcnow().date()
        date1 = datetime.strptime(date_due, '%Y-%m-%d').date()
        date2 = datetime.strptime(today, '%Y-%m-%d').date()

        date_diff = date2 - date1
        if date_diff.days > 0:
            self.graded_score = 0.5 * score
        else:
            self.graded_score = score
