#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app
from .auth import token_required


index_blueprint = Blueprint('index_views', __name__)


class IndexViews(MethodView):
    @token_required
    def get(self):
        return "get request to index"

    def post(self):
        return "post request to index"

    def put(self, user_id):
        return "put request to index"

    def delete(self, user_id):
        return "delete request to index"


index_views = IndexViews.as_view('index_views')
index_blueprint.route('/', methods=['GET','POST'])(index_views)
