#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.content import Content
from datetime import datetime, timedelta


content_blueprint = Blueprint('content_views', __name__)

class ContentViews(MethodView):
    @token_required
    def get(self):
        pass

    @token_required
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

content_views = ContentViews.as_view('content_views')

content_blueprint.route('/content', methods=['GET','POST'])(content_views)
content_blueprint.route('/content/<int:user_id>', methods=['PUT','DELETE'])(content_views)