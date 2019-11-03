from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow()
