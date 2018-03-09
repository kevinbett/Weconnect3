import unittest
from flask import json
from api import create_app
from api.v1 import auth

class BusinessTestCase(unittest.TestCase):

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
            "type": "Mentorship"
        }

    def tearDown(self):
        auth.logout()

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
        self.assertEquals("The user name or password provided is wrong", json.loads(response.data)["message"])

    def test_register_business(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        response = self.client().post('/api/v1/businesses/',
                                      data=json.dumps(self.business),
                                      content_type="application/json")
        self.assertEquals("Business has been registered successfully", json.loads(response.data)["message"])

    def test_update_business(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/api/v1/businesses/',
                                      data=json.dumps(self.business),
                                      content_type="application/json")
        response = self.client().put("/api/v1/businesses/1",
                                      data=json.dumps(self.business),
                                      content_type="application/json")
        self.assertEquals("Business has been successfully edited", json.loads(response.data)["message"])

    def test_delete_business(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/api/v1/businesses/',
                                      data=json.dumps(self.business),
                                      content_type="application/json")
        response = self.client().delete("/api/v1/businesses/1")
        self.assertEquals("Business has been successfully deleted", json.loads(response.data)["message"])

    def test_cannot_get_business(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        response = self.client().get("/api/v1/businesses/29")
        self.assertEquals("The business you requested does not exist", json.loads(response.data)["message"])
        self.assertEquals(response.status_code, 404)

    def test_can_get_business(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/api/v1/businesses/', data=json.dumps(self.business), content_type="application/json")
        response = self.client().get("/api/v1/businesses/1")
        self.assertEquals(response.status_code, 200)

    def test_retrieve_all_businesses(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        response = self.client().get('/api/v1/businesses/')
        self.assertEquals(response.status_code, 200)
