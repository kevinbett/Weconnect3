import unittest
from api import create_app
from api.v1 import auth, business

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
        response = self.client().post('/register', data=self.user)
        self.assertEquals("User Test User has been registered successfully", str(response.data.decode("utf-8")))

    def test_login(self):
        self.client().post('/register', data=self.user)
        response = self.client().post('/login', data=self.user)
        self.assertEquals("You are now logged in", str(response.data.decode("utf-8")))

    def test_empty_login_details(self):
        self.client().post('/register', data=self.user)
        response = self.client().post('login', data={})
        self.assertEquals("You have not filled in either the email or password", str(response.data.decode("utf-8")))

    def test_invalid_login_details(self):
        self.client().post('/register', data=self.user)
        data = {
            "email": "user@example.com",
            "password": "wrongpassword"
        }
        response = self.client().post('login', data=data)
        self.assertEquals("Check Username or password", str(response.data.decode("utf-8")))


    # def test_details_not_provided_failure(self):
    #     self.client().post("/auth/register", data=self.user)
    #     self.client().post("/auth/login", data=self.user)
    #     response = self.client().post("/login/", data={})
    #     self.assertEquals(
    #         "You must enter both business name and type",
    #         str(response.data.decode("utf-8")))
    #
    def test_register_business(self):
        self.client().post('/register', data=self.user)
        self.client().post('/login', data=self.user)
        response = self.client().post('/api/v1/businesses/', data=self.business)
        self.assertEquals("Business has been registered successfully", str(response.data.decode("utf-8")))
    #
    def test_edit_business(self):
        self.client().post('/register', data=self.user)
        self.client().post('/login', data=self.user)
        self.client().post('/api/v1/businesses/', data=self.business)
        response = self.client().put("/api/v1/businesses/1", data=self.business)
        self.assertEquals("Business has been successfully edited", str(response.data.decode("utf-8")))

    def test_delete_business(self):
        self.client().post('/register', data=self.user)
        self.client().post('/login', data=self.user)
        self.client().post('/api/v1/businesses/', data=self.business)
        response= self.client().delete("/api/v1/businesses/1")
        self.assertEquals("Business has been successfully deleted", str(response.data.decode("utf-8")))
