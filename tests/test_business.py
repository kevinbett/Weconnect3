from flask import json
from tests.test import BaseTestCase

class BusinessTestCase(BaseTestCase):

    def test_register_business(self):
        authtoken = self.authenticate()
        response = self.client().post('/api/v1/businesses/',data=json.dumps(self.business),content_type="application/json", headers = {"Authorization": "Bearer " + authtoken})
        self.assertEquals("Business has been registered successfully", json.loads(response.data)["message"])
        self.assertEquals(response.status_code, 201)


    def test_view_business(self):
        authtoken = self.authenticate()
        self.client().post('/api/v1/businesses/',
                           data=json.dumps(self.business),
                           content_type="application/json",
                           headers = {"Authorization": "Bearer " + authtoken})
        response = self.client().get('api/v1/businesses/')
        businesses = json.loads(response.data)["businesses"]
        self.assertEqual(self.business["name"], businesses[0]['name'])
        self.assertEqual(self.business["category"], businesses[0]['category'])
        self.assertEqual(self.business["type"], businesses[0]['type'])
        self.assertEqual(self.business["location"], businesses[0]['location'])
        self.assertEqual(response.status_code, 200)

    def test_update_business(self):
        authtoken = self.authenticate()
        self.client().post('/api/v1/businesses/',
                           data=json.dumps(self.business),
                           content_type="application/json",
                           headers={"Authorization": "Bearer " + authtoken})
        response = self.client().put('api/v1/businesses/1',
                          data=json.dumps({"name":"andela kenya"}),
                          content_type="application/json",
                          headers = {"Authorization": "Bearer " + authtoken})
        self.assertEquals("Business has been successfully edited", json.loads(response.data)["message"])
        self.assertEqual(response.status_code, 201)


    def test_delete_business(self):
        authtoken = self.authenticate()
        self.client().post('/api/v1/businesses/',
                           data=json.dumps(self.business),
                           content_type="application/json",
                           headers={"Authorization": "Bearer " + authtoken})
        response = self.client().delete('/api/v1/businesses/1',
                                        headers = {"Authorization": "Bearer " + authtoken})
        self.assertEqual("Business has been deleted successfully", json.loads(response.data)["message"])
        self.assertEqual(response.status_code,200)

    def test_can_get_business(self):
        authtoken = self.authenticate()
        self.client().post('/api/v1/businesses/',
                           data=json.dumps(self.business),
                           content_type="application/json",
                           headers={"Authorization": "Bearer " + authtoken})
        response = self.client().get('api/v1/businesses/1')
        business = json.loads(response.data)
        self.assertEqual(self.business["name"], business['name'])
        self.assertEqual(self.business["category"], business['category'])
        self.assertEqual(self.business["type"], business['type'])
        self.assertEqual(self.business["location"], business['location'])
        self.assertEqual(response.status_code, 200)



