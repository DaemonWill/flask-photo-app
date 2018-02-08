#!flask/bin/python
import os
import unittest
from app import app

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_make_successful_get_to_base_form_path(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/')
        # assert the status code of the response
        assert 200 == response.status_code

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
