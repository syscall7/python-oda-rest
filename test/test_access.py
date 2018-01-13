import unittest
from oda_rest.api import OdaProject

class TestAccess(unittest.TestCase):

    def test_auth(self):

        with self.assertRaises(Exception):
            OdaProject("mkdir")

    def test_nonexistent(self):

        with self.assertRaises(Exception):
            OdaProject("does_not_exist")
