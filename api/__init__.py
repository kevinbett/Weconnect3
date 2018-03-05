from flask import Flask
from api.v1.business import business_blueprint

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    return app
