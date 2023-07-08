from flask_sqlalchemy import SQLAlchemy
from app.models.dept import Dept
from app.models.course import Course
from app.models.content import Content
from app.models.dbobject import db
# from datetime import datetime

# db = SQLAlchemy()

def initialize_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'
    db.init_app(app)
    with app.app_context():
        db.create_all()

