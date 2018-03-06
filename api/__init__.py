from flask import Flask
from instance.config import app_config
from api.v1.auth import auth as auth_blueprint
from api.v1.business import business_blueprint

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(business_blueprint, url_prefix="/business")
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

