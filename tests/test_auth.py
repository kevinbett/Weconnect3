from tests.test import BaseTestCase
from flask import json

class AuthTestCase(BaseTestCase):

    def test_register(self):
        response = self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.assertEquals("User test_user has been registered successfully", json.loads(response.data)["message"])

    def test_login(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        response = self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        self.assertEquals("You are now logged in as test_user", json.loads(response.data)["message"])


    def test_empty_login_details(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        user = self.user
        user["password"] = ""
        response = self.client().post('login', data=json.dumps(user), content_type="application/json")
        self.assertEquals(["Your password should have atleast 6 characters"], json.loads(response.data)["message"])


    def test_invalid_login_details(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        user = {
            "email": "user@example.com",
            "password": "wrongpassword"
        }
        response = self.client().post('login', data=json.dumps(user), content_type="application/json")
        self.assertEquals("The email or password provided is wrong", json.loads(response.data)["message"])