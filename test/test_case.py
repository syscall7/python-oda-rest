import unittest
import requests

class MkdirTestCase(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()
        self.shortname = self.session.get(
            'http://localhost:8000/odaweb/api/masters/mkdir/clone/').json()
