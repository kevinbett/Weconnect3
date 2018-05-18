from tests.test import BaseTestCase
from flask import json

class ReviewTestCase(BaseTestCase):
    def test_add_review(self):
        authtoken = self.authenticate()
        self.client().post('/api/v1/businesses/',
                           data=json.dumps(self.business),
                           content_type="application/json",
                           headers={"Authorization": "Bearer " + authtoken})
        response = self.client().post('/api/v1/businesses/1/reviews',
                                      data=json.dumps(self.review),
                                      content_type="application/json",
                                      headers={"Authorization": "Bearer " + authtoken})
        self.assertEquals("Your review has been added", json.loads(response.data)["message"])
        self.assertEqual(response.status_code, 201)


    def test_view_reviews(self):
        authtoken = self.authenticate()
        self.client().post('/api/v1/businesses/',
                           data=json.dumps(self.business),
                           content_type="application/json",
                           headers={"Authorization": "Bearer " + authtoken})

        self.client().post('/api/v1/businesses/1/reviews',
                           data=json.dumps(self.review),
                           content_type="application/json",
                           headers={"Authorization": "Bearer " + authtoken})
        response = self.client().get('/api/v1/businesses/1/reviews')
        self.assertEqual(self.review,json.loads(response.data)["reviews"][0])
        self.assertEquals(response.status_code, 200)