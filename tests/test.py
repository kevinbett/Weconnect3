import unittest
from api import create_app
from api.models import db
from flask import json

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.api = create_app("testing")
        self.client = self.api.test_client
        app_context = self.api.app_context()
        app_context.push()
        db.create_all()

        self.user = {
            "id": 1,
            "name": "test_user",
            "email": "user@example.com",
            "password": "password"
        }
        self.business = {
            "name": "andela",
            "type": "mentorship",
            "location":"roysambu",
            "category":"food"
        }
        self.review = {
            "feedback": "feedback"
        }

    def authenticate(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        response = self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        authtoken = json.loads(response.data.decode())["auth_token"]
        return  authtoken


    def tearDown(self):
        with self.api.app_context():
            db.session.remove()
            db.drop_all()


