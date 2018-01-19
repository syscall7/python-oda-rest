from oda_rest.api import Comment
from test.test_case import MkdirTestCase

class TestComments(MkdirTestCase):

    def test_comments(self):
        expected = (
            Comment(vma = 4194900, comment = 'Comment at 4194900'),
            Comment(vma = 4194901, comment = 'Comment at 4194901'),
            Comment(vma = 4194902, comment = 'Comment at 4194902'),
            Comment(vma = 4194903, comment = 'Comment at 4194903'),
            Comment(vma = 4194904, comment = 'Comment at 4194904'),
        )

        for e in expected:
            self.project.CreateComment(e.vma, e.comment)

        actual = self.project.Comments()

        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)
