#!/usr/bin/env python

from flask import Flask
# from flask import Blueprint
from .db import initialize_db
from app.models.dbobject import app
from flask import Flask, make_response

# from datetime import datetime



def create_app(app):
    # Create the Flask application object

    # Set up any extensions or additional configurations
    initialize_db(app)
    # For example, initializing a database or registering blueprints
    @app.after_request
    def add_cache_control(response):
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    # Import and register blueprints
    from .views.calendar import calendar_blueprint
    from .views.enrollment import enrollment_blueprint
    from .views.result import result_blueprint
    from .views.auth import auth_blueprint

    app.register_blueprint(calendar_blueprint)
    app.register_blueprint(enrollment_blueprint)
    app.register_blueprint(result_blueprint)
    app.register_blueprint(auth_blueprint)

    # Return the configured application object
    return app