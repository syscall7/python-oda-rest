import unittest
from oda_rest.api import OdaProject
from test.test_case import MkdirTestCase

class TestFunctions(unittest.TestCase):

    def test_functions(self):
        project = OdaProject('mkdir', clone=True)
        funcs = project.Functions()
        for f in funcs:
            print(f)
