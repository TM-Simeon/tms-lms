from flask_sqlalchemy import SQLAlchemy
from app.models.user import User
from app.models.student import Student
from app.models.staff import Staff
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


# # to connect many different flask apps

# # Create the SQLAlchemy instance
# db = SQLAlchemy()

# # Define the User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

# # Create the first Flask application
# app1 = Flask(__name__)
# app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app1_database.db'
# db.init_app(app1)

# # Create the second Flask application
# app2 = Flask(__name__)
# app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app2_database.db'
# db.init_app(app2)

# # Create the third Flask application
# app3 = Flask(__name__)
# app3.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app3_database.db'
# db.init_app(app3)

# # Define routes and interact with the databases
# with app1.app_context():
#     db.create_all()  # Create tables if they don't exist

#     # Perform database operations
#     user1 = User(username='user1', email='user1@example.com')
#     db.session.add(user1)
#     db.session.commit()

# with app2.app_context():
#     db.create_all()  # Create tables if they don't exist

#     # Perform database operations
#     user2 = User(username='user2', email='user2@example.com')
#     db.session.add(user2)
#     db.session.commit()

# with app3.app_context():
#     db.create_all()  # Create tables if they don't exist

#     # Perform database operations
#     user3 = User(username='user3', email='user3@example.com')
#     db.session.add(user3)
#     db.session.commit()
