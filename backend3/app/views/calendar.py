#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.calendar import Calendar
from datetime import datetime, timedelta

calendar_blueprint = Blueprint('calendar_views', __name__)


class CalendarViews(MethodView):
    @token_required
    def get(self):
        pass

    def post(self):
        pass


calendar_views = StaffViews.as_view('calendar_views')
# student_blueprint.add_url_rule('/student', view_func=student_views, methods=['GET', 'POST'])
calendar_blueprint.route('/calendar', methods=['GET','POST'])(calendar_views)
calendar_blueprint.route('/calendar/<int:user_id>', methods=['PUT','DELETE'])(calendar_views)
