from flask import json
from tests.test import BaseTestCase

class BusinessTestCase(BaseTestCase):

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