#!/usr/bin/env python

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.create_app import create_app
from app.models.dbobject import db, app
# from app.db import *

# Create Flask app instance
app1 = create_app(app)
manager = Manager(app1)

# Database migration commands
migrate = Migrate(app1, db)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    # app1.debug = False
    # manager.run()
    app1.run()



