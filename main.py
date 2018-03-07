import os

from api.__init__ import create_app

config_name = os.getenv('APP_ENV') # config_name = "development"
app = create_app("development")

if __name__ == '__main__':
    app.run()
