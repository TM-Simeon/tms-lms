#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.user import User
from datetime import datetime, timedelta


user_blueprint = Blueprint('user_views', __name__)


# algorithms = ['HS256']

class UserViews(MethodView):
    @token_required
    def get(self):
        try:
            user = User.query.filter_by(username='john doe').first()
        except Exception as e:
            print(e)
        return jsonify({'message':'its all fine: {}'.format(user.email)})
        
    # @token_required
    def post(self):
        email = "john@gmail.com"
        try:
            user = User(username='tm simeon', email=email, dob=datetime.utcnow(), password='1234', status=True)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
        return ({"message":"post request to user with email: {}".format(email) })

    def put(self, user_id):
        return "put request to user"

    def delete(self, user_id):
        return "delete request to user"


user_views = UserViews.as_view('user_views')

user_blueprint.route('/user', methods=['GET','POST'])(user_views)
user_blueprint.route('/user/<int:user_id>', methods=['PUT','DELETE'])(user_views)