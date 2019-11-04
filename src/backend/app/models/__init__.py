#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module creates the database object (SQLAlchemy),
migration helper (Migrate) and a helper for object serialization (Marschmallow)
To instanciate those helpers it uses the current_app proxy,
which points to the application handling the current activity

More Informations of the specific tools here:
https://flask-sqlalchemy.palletsprojects.com/
https://flask-migrate.readthedocs.io/
https://marshmallow.readthedocs.io/en/stable/
https://flask.palletsprojects.com/en/1.0.x/appcontext/
"""

from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# initialize database helper
db = SQLAlchemy(app)

# initialize migration helper
migrate = Migrate(app, db)

# initialize object serialization helper
ma = Marshmallow()
