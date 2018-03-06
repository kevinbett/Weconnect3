import unittest
import os
import json

from api import create_app

class BusinessTestCase(unittest.TestCase):
    """Test case class"""

    def setUp(self):
        """Define test variables."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.business = {
        "name": "PACUNIVERSITY",
        "type": "MENTORSHIP"
        }

    def test_create_business(self):
        res = self.client().post('/businesses/', data=self.business)
        self.assertEqual(res.status_code, 201)
