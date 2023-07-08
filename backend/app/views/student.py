#!/usr/bin/env python

from flask import Blueprint
from flask.views import MethodView
from .auth import token_required
from flask import Flask, jsonify, request, redirect, make_response
import jwt
from functools import wraps
from app.models.dbobject import app, db
from app.models.student import Student
from datetime import datetime, timedelta

student_blueprint = Blueprint('student_views', __name__)


class StudentViews(MethodView):
    @token_required
    def get(self):
        try:
            student = Student.query.filter_by(u_id=1234).first()
        except Exception as e:
            print(e)
        return ({"message":"get request to student {}".format(student.s_id)})

    def post(self):
        u_id = 1234
        department = 'department'
        try:
            student = Student(department=department, status=True,u_id=u_id)
            db.session.add(student)
            db.session.commit()
        except Exception as e:
            print(e)
        return ({"message":"user with id: {} successfully enrolled as a student".format(u_id)})

    def put(self, user_id):
        return "put request to student"

    def delete(self, user_id):
        return "delete request to student"


student_views = StudentViews.as_view('student_views')

student_blueprint.route('/student', methods=['GET','POST'])(student_views)
student_blueprint.route('/student/<int:user_id>', methods=['PUT','DELETE'])(student_views)
