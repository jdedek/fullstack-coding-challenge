from enum import Enum
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class ValidEnvironments(Enum):
    """Enum to control valid environment config inputs"""
    Development = 'Development',
    Test = 'Test',
    Production = 'Production'


class Default:
    """Default Configuration that all environments will default to"""
    APP_NAME = "simple_translation_app"
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "A0Zr98jyX RHH!jmN]LWX/,?RT"
    ENV = os.environ.get("ENV") or ValidEnvironments.Development
    SERVER = os.environ.get("SERVER") or 'localhost'

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:temp@postgres:5432/master"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Default):
    """Development environment"""
    DEBUG = False
    TESTING = True
    ENV = os.environ.get("ENV") or ValidEnvironments.Development
    SERVER = os.environ.get("SERVER") or "jdk-cgn-dev-001"
   
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Test(Default):
    """Continuous Integration (CI) / User Acceptance"""
    DEBUG = False
    TESTING = True
    ENV = os.environ.get("ENV") or ValidEnvironments.Test
    SERVER = os.environ.get("SERVER") or "jdk-cgn-dev-001"

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Production(Default):
    """Production"""
    DEBUG = False
    TESTING = False
    ENV = os.environ.get("ENV") or ValidEnvironments.Production
    SERVER = os.environ.get("SERVER") or "jdk-cgn-prd-001"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = True