import unittest
from oda_rest.api import OdaProject

class MkdirTestCase(unittest.TestCase):

    def setUp(self):
        self.project = OdaProject("http://localhost:8000", 'mkdir', clone=True)
