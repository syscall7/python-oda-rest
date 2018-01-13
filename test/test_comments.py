from test.test_case import MkdirTestCase

class TestComments(MkdirTestCase):

    def test_comments(self):
        expected = (
            {'offset': 4194900, 'comment': 'Comment at 4194900'},
            {'offset': 4194901, 'comment': 'Comment at 4194901'},
            {'offset': 4194902, 'comment': 'Comment at 4194902'},
            {'offset': 4194903, 'comment': 'Comment at 4194903'},
            {'offset': 4194904, 'comment': 'Comment at 4194904'},
        )

        for e in expected:
            self.project.CreateComment(e['offset'], e['comment'])

        actual = self.project.Comments()

        for e, a in zip(expected, actual):
            self.assertDictEqual(e, a)
