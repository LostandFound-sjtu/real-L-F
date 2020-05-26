from django.test import TestCase

# Create your tests here.
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/login/')
        print('# ',response) 
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

