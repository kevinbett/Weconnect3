from tests.test import BaseTestCase
from flask import json

class ReviewTestCase(BaseTestCase):
    def test_add_review(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/api/v1/businesses/1/reviews', data=json.dumps(self.user), content_type="application/json")
        response = self.client().post('/api/v1/businesses/1/reviews',
                                      data=json.dumps(self.review),
                                      content_type="application/json")
        self.assertEquals("Your review has been posted", json.loads(response.data)["message"])


    def test_view_reviews(self):
        self.client().post('/register', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/login', data=json.dumps(self.user), content_type="application/json")
        self.client().post('/api/v1/businesses/',
                           data=json.dumps(self.business),
                           content_type="application/json")
        self.client().post('/api/v1/businesses/1/reviews', data=json.dumps(self.user), content_type="application/json")
        response = self.client().get('/api/v1/businesses/1/reviews')
        self.assertEquals(response.status_code, 200)