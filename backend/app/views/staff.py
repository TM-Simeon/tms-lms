#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.staff import Staff
from datetime import datetime, timedelta

staff_blueprint = Blueprint('staff_views', __name__)


class StaffViews(MethodView):
    @token_required
    def get(self):
        try:
            staff = Staff.query.filter_by(u_id=5678).first()
        except Exception as e:
            print(e)
        return "get request to staff"

    def post(self):
        u_id = 5678
        try:
            staff = Staff(u_id=u_id, status=True)
            db.session.add(staff)
            db.session.commit()
        except Exception as e:
            print(e)
        return "post request to staff"

    def put(self, user_id):
        return "put request to staff"

    def delete(self, user_id):
        return "delete request to staff"


staff_views = StaffViews.as_view('staff_views')
# student_blueprint.add_url_rule('/student', view_func=student_views, methods=['GET', 'POST'])
staff_blueprint.route('/staff', methods=['GET','POST'])(staff_views)
staff_blueprint.route('/staff/<int:user_id>', methods=['PUT','DELETE'])(staff_views)
