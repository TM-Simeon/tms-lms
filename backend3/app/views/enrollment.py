#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.enrollment import Enrollment
from datetime import datetime, timedelta

enrollment_blueprint = Blueprint('enrollment_views', __name__)


class EnrollmentViews(MethodView):
    @token_required
    def get(self):
        pass

    def post(self):
        pass

    def put(self, user_id):
        return "put request to student"

    def delete(self, user_id):
        return "delete request to student"


enrollment_views = EnrollmentViews.as_view('enrollment_views')

enrollment_blueprint.route('/enrollment', methods=['GET','POST'])(enrollment_views)
enrollment_blueprint.route('/enrollment/<int:user_id>', methods=['PUT','DELETE'])(enrollment_views)
