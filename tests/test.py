import unittest
from api import create_app
from api.models import db
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
            "name": "Andela",
            "type": "Mentorship",
            "location":"Roysambu"
        }
        self.review = {
            "feedback": "feedback"
        }

    def tearDown(self):
        pass


        


