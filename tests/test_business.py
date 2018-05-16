from flask import json
from tests.test import BaseTestCase

class BusinessTestCase(BaseTestCase):

    def test_register_business(self):
        authtoken = self.authenticate()
        response = self.client().post('/api/v1/businesses/',data=json.dumps(self.business),content_type="application/json", headers = {"Authorization": "Bearer " + authtoken})
        self.assertEquals("Business has been registered successfully", json.loads(response.data)["message"])