#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.course import Course
from datetime import datetime, timedelta

course_blueprint = Blueprint('course_views', __name__)


class CourseViews(MethodView):
    @token_required
    def get(self):
        pass

    @token_required
    def post(self):
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass


course_views = CourseViews.as_view('course_views')

course_blueprint.route('/course', methods=['GET','POST'])(course_views)
course_blueprint.route('/course/<int:user_id>', methods=['PUT','DELETE'])(course_views)
