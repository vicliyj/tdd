"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""

from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app 

# we need to import the file that contains the status codes
from src import status 

from src import counter

class CounterTest(TestCase):
    """Counter tests"""

    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def setUp(self):
        self.client = app.test_client()

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        """Testing if counter is updated"""
        self.client = app.test_client()
        result = self.client.post('/counters/doo')
        currCount = result.json["doo"]
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result2 = self.client.put('/counters/doo')
        updatedCount = result2.json["doo"]
        self.assertEqual(result2.status_code, status.HTTP_200_OK)
        self.assertEqual(currCount + 1, updatedCount)
        
    def test_read_a_counter(self):
        """Testing if counter is read"""
        result2 = self.client.get('/counters/moo')
        self.assertEqual(result2.status_code, status.HTTP_200_OK)

    def test_delete_a_counter(self):
        """Testing if counter is deleted"""
        # client = app.test_client()
        # result = client.post('/counters/zoo')
        # self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.delete(self)
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)
