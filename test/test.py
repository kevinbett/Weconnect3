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
        self.client().post('/login', data=self.user)
        response = self.client().post('/login', data=self.user)
        self.assertEquals("You have not filled in either the email or password", str(response.data.decode("utf-8")))

    def test_details_not_provided_failure(self):
        self.client().post("/auth/register", data=self.user)
        self.client().post("/auth/login", data=self.user)
        response = self.client().post("/login/", data={})
        self.assertEquals(
            "You must enter both business name and type",
            str(response.data.decode("utf-8")))

    def test_register_business(self):
        response = self.client().post('/', data=self.business)
        self.assertEquals("Business has been registered successfully", str(response.data.decode("utf-8")))

    def test_edit_business(self):
        self.client().post("/<businessId>", data=self.user)
        self.client().post("/<businessId>", data=self.business)
        response = self.client().put("/<businessId>", data=self.business)
        self.assertEquals("Business has been successfully edited", str(response.data.decode("utf-8")))

    def test_delete_business(self):
        self.client().post("/<businessId>", data=self.user)
        self.client().post("/<businessId>", data=self.business)
        response = self.client().put("/<businessId>", data=self.business)
        self.assertEquals("Business has been successfully deleted", str(response.data.decode("utf-8")))
