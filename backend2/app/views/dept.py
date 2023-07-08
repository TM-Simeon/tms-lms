#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.dept import Dept
from datetime import datetime, timedelta

dept_blueprint = Blueprint('dept_views', __name__)


class DeptViews(MethodView):
    @token_required
    def get(self):
        pass

    def post(self):
        pass

    def put(self, user_id):
        return "put request to dept"

    def delete(self, user_id):
        return "delete request to dept"


dept_views = DeptViews.as_view('dept_views')

dept_blueprint.route('/dept', methods=['GET','POST'])(dept_views)
dept_blueprint.route('/dept/<int:user_id>', methods=['PUT','DELETE'])(dept_views)
