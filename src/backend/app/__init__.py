from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from . import config

def create_app():
    # I'm using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
    app = Flask(__name__)

    # Flask extension for handling Cross Origin Resource Sharing (CORS)
    #CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # This makes sure that the operations are active in the right app context
    # in detail inside the Flask docs:
    # https://flask.palletsprojects.com/en/1.1.x/appcontext/
    with app.app_context():
        app.config.from_object(config.Config)
        app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.Config.SQLALCHEMY_TRACK_MODIFICATIONS
    

        from app.routes.home import TranslationRessource
        
        api = Api(app)
        api.add_resource(TranslationRessource, '/api/translations/', '/api/translations/<int:translation_id>')

        from app.models import db, migrate
        db.init_app(app)
        migrate.init_app(app, db)

    return app