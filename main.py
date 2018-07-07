import os
from flask_cors import CORS, cross_origin
from api.__init__ import create_app

config_name = os.getenv('APP_ENV') # config_name = "development"
app = create_app("development")
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

