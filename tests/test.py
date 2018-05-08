import unittest
from flask import json
from api import create_app
from api.v1 import auth


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.api = create_app("testing")
        self.client = self.api.test_client
        self.user = {
            "id": 1,
            "name": "test_user",
            "email": "user@example.com",
            "password": "password"
        }
        self.business = {
            "name": "Andela",
            "type": "Mentorship",
            "location":"Roysambu"
        }
        self.review = {
            "feedback": "feedback"
        }

    def tearDown(self):
        auth.logout()


        


