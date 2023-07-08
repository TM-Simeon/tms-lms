from .course import Course
from .dbobject import db
from datetime import datetime

class Content(db.Model):
    __tablename__ = 'content'

    c_id = db.Column(db.String(50), db.ForeignKey(Course.c_id))
    module_no = db.Column(db.Integer, nullable=False)
    part1 = db.Column(db.String(150), nullable=False)
    part2 = db.Column(db.String(150), nullable=False)
    part3 = db.Column(db.String(150), nullable=False)
    part4 = db.Column(db.String(150), nullable=False)
    part5 = db.Column(db.String(150))
    part6 = db.Column(db.String(150))
    part7 = db.Column(db.String(150))
    part8 = db.Column(db.String(150))
    part9 = db.Column(db.String(150))
    part10 = db.Column(db.String(150))
    quiz = db.Column(db.String(150))
    datecreated = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, c_id, module_no, part1, part2, part3, part4, part5, part6, part7, part8, part9, part10,quiz):
        self.c_id = c_id
        self.module_no = module_no
        self.part1 = part1
        self.part2 = part2
        self.part3 = part3
        self.part4 = part4
        self.part5 = part5
        self.part6 = part6
        self.part7 = part7
        self.part8 = part8
        self.part9 = part9
        self.part10 = part10
        self.quiz = quiz

# user = User(u_id=1,  email='john@gmail.com',dob=datetime.utcnow(), password='1234', status=True)
# print(user.dob)