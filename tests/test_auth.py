from tests.test import BaseTestCase
from flask import json

class AuthTestCase(BaseTestCase):

    def test_register(self):
        response = self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.assertEquals("User test_user has been registered successfully", json.loads(response.data)["message"])
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        response = self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        self.assertEquals("You are now logged in as test_user", json.loads(response.data)["message"])
        self.assertIsNotNone(json.loads(response.data)["auth_token"])
        self.assertEqual(response.status_code, 200)

    def test_invalid_login_details(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        user = {
            "email": "user@example.com",
            "password": "wrongpassword"
        }
        response = self.client().post('login', data=json.dumps(user), content_type="application/json")
        self.assertEquals("The email or password provided is wrong", json.loads(response.data)["message"])
        self.assertEqual(response.status_code, 401)