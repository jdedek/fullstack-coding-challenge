from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from . import config

app = Flask(__name__)
app.config.from_object(config.Config)
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.Config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#from app import routes, models
from app.routes import home
from app.models import translation
