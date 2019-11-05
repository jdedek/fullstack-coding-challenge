#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines the Flask app instance, loads settings,
defines API URLs and initiates the database and migrations
"""

from logging.config import dictConfig

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from . import config


# logging settings
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def create_app(config_name):
    """
    Sets up the Flask app instance with settings etc.
    Uses the "Application Factory"-pattern here, which is described
    in detail inside the Flask docs:
    https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
    """
    app = Flask(__name__)

    # Flask extension for handling Cross Origin Resource Sharing (CORS)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # This makes sure that the operations are active in the right app context
    # in detail inside the Flask docs:
    # https://flask.palletsprojects.com/en/1.1.x/appcontext/
    with app.app_context():
        # loads the setting from the config.py
        app.config.from_object(config.app_config[config_name])
        app.config.from_pyfile('config.py')
        app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.Config.SQLALCHEMY_TRACK_MODIFICATIONS
        # defines the API ressource URLs
        from app.routes.api import TranslationRessource

        api = Api(app)
        api.add_resource(TranslationRessource, '/api/translations/',
                         '/api/translations/<string:uid>')

        # initiates the database and the migration
        from app.models import db, migrate
        db.init_app(app)
        migrate.init_app(app, db)

    return app
