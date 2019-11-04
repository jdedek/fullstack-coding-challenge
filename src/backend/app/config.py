#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module contains the different setting configurations
of the API. Sentitive informations are stored in the .env
file and get imported here.
"""

import os


class Config(object):
    """ Base class for configurations """

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ["SECRET_KEY"]
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    database = os.environ['POSTGRES_DB']
    port = os.environ['POSTGRES_PORT']
    DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """ Class for production configuration """
    DEBUG = False


class DevelopmentConfig(Config):
    """ Class for development configuration """
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """ Class for test configuration """
    TESTING = True
