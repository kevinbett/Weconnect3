import unittest
from api import create_app
from api.v1 import auth

class BusinessTestCase(unittest.TestCase):

    def setUp(self):
        self.api = create_app("testing")
        self.client = self.api.test_client
        self.user = {
            "id": 1,
            "name": "Test User",
            "email": "user@example.com",
            "password": "password"
        }
        self.business = {
            "name": "Andela",
            "type": "Mentorship"
        }

    def tearDown(self):
        auth.logout()

    def test_register(self):
        response = self.client().post("/auth/register", data=self.user)
        self.assertEquals("User Test User has been registered successfully", str(response.data.decode("utf-8")))

    def test_login(self):
        self.client().post("/auth/login", data=self.user)
        response = self.client().post("/auth/login", data=self.user)
        self.assertEquals("You have not filled in either the email or password", str(response.data.decode("utf-8")))


