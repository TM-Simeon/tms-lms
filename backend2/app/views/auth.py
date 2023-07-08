from flask import Flask, jsonify, request, redirect, make_response, render_template
import jwt
from functools import wraps
from flask.views import MethodView
from flask import Blueprint
from app.models.dbobject import app
import os
from datetime import datetime, timedelta


auth_blueprint = Blueprint('auth_views', __name__, template_folder='../templates')
protected_blueprint = Blueprint('protected_views', __name__)
some_blueprint = Blueprint('some_views', __name__)

algorithms = ['HS256']

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.headers.get('Authorization')
		print("done")
		algoriths = ['HS256']
		if not token:
			return jsonify({'message':'Token is missing!'}), 401

		try:
			print("i tried token verify")
			data = jwt.decode(token, app.config['SECRET_KEY'], algoriths=algorithms, verify=False, options={'verify_signature': False})
		except jwt.InvalidTokenError as e:
			print("token bad")
			print(e)
			return jsonify({'message':'Invalid Token!'}), 401
		print(token)
		return f(*args, **kwargs)

	return decorated


#get user from database
registered_users = {
	'john@gmail.com': 'johnpass123',
	'jane@gmail.com': 'janepass123'
}

# expiration_time = datetime.utcnow() + timedelta(minutes=1)
# expiration_time2 = datetime.now()

# payload = {
# 	'email': 'john@gmail.com',
# 	'exp': expiration_time
# }

# user authentication
class UserAuthView(MethodView):
	def post(self):
		# email = request.json.get('email')
		# password = request.json.get('password')
		email = "john@gmail.com"
		password = "johnpass123"
		print("i reached here")

		expiration_time = datetime.utcnow() + timedelta(minutes=360)
		expiration_time2 = datetime.now()

		payload = {
			'email': email,
			'exp': expiration_time,
			'password': password
		}

		if email not in registered_users or registered_users[email] != password:
			return jsonify({'message': 'Invalid email or password'}), 401

		# generate JWT
		token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

		# create a response with the dashboard page
		response = make_response(redirect('/some'))

		# set the JWT token as a cookie in the response
		# response.set_cookie('token', token)

		# return render_template('dashboard.html')
		print(expiration_time)
		print(expiration_time2)
		return jsonify({'token':token})

	@token_required
	def get(self):
		current_user = jwt.decode(request.headers.get('Authorization'), app.config['SECRET_KEY'])
		return jsonify({'message': f'Hello, {current_user["email"]}! This is a protected route'}), 200


	@token_required
	def put(self):
		current_user = jwt.decode(request.headers.get('Authorization'), app.config['SECRET_KEY'])
		# implement the logic for updating user data
		return jsonify({'message': f'Hello, {current_user["email"]}! user data updated'}), 200

	@token_required
	def delete(self):
		current_user = jwt.decode(request.headers.get('Authorization'), app.config['SECRET_KEY'])
		# implement the logic for updating user data
		return jsonify({'message': f'Hello, {current_user["email"]}! user data deleted'}), 200




auth_views = UserAuthView.as_view('auth_views')

auth_blueprint.route('/login', methods=['GET', 'POST'])(auth_views)
