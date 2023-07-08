#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.result import Result
from datetime import datetime, timedelta


user_blueprint = Blueprint('user_views', __name__)


# algorithms = ['HS256']

class ResultViews(MethodView):
    @token_required
    def get(self):
        pass
        
    @token_required
    def post(self):
        pass

    def put(self, user_id):
        return "put request to user"

    def delete(self, user_id):
        return "delete request to user"


result_views = ResultViews.as_view('result_views')

result_blueprint.route('/result', methods=['GET','POST'])(result_views)
result_blueprint.route('/result/<int:user_id>', methods=['PUT','DELETE'])(result_views)