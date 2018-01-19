from oda_rest.api import Operation
from test.test_case import MkdirTestCase

class TestOperations(MkdirTestCase):

    def test_operations(self):
        expected = (
            Operation(datetime='2018-01-19T12:27:42.481440', user=None,
                      name='LoadOperation', desc='Loaded project'),
            Operation(datetime='2018-01-19T12:27:42.493382', user=None,
                      name='PassiveScanOperation', desc='Passive scan operation'),
        )

        actual = self.project.Operations()

        self.assertEqual(len(expected), len(actual))
