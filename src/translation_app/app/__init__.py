from flask import Flask
from flask_bootstrap import Bootstrap

from . import config

def create_app():
    # I'm using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
    app = Flask(__name__)
    
    # Create a bootstrap instance
    Bootstrap(app)

    # This makes sure that the operations are active in the right app context
    # in detail inside the Flask docs:
    # https://flask.palletsprojects.com/en/1.1.x/appcontext/
    with app.app_context():
        app.config.from_object(config.Config)
        app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.Config.SQLALCHEMY_TRACK_MODIFICATIONS
        from app.models import db, migrate
        db.init_app(app)
        migrate.init_app(app, db)

        #from app import routes, models
        from app.routes import home
        from app.models import translation
    
    return app