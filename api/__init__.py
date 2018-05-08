from flask import Flask
from instance.config import app_config
from api.v1.auth import auth as auth_blueprint
from api.v1.business import business_blueprint
from flask_sqlalchemy import SQLAlchemy
from api.global_functions import response_message


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(business_blueprint)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return response_message("Page not found", 404)

    @app.errorhandler(405)
    def method_not_allowed(e):
        return response_message("Method not allowed", 405)

    @app.errorhandler(400)
    def bad_request(e):
        return response_message("Bad request", 400)

    return app



