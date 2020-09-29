import unittest

from templatext import Templatext


class TestTemplatex(unittest.TestCase):
    """Test Templatext module"""

    # def setUp(self):
    #     self.a = 10
    #     self.b = 5

    def test_preprocess(self):
        text = " <p> Hey music is good I'm loving it!! </p>"
        expected = ["hey", "music", "good", "love"]

        t = Templatext()
        self.assertEqual(t.preprocess(text), expected)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestTemplatex)
    )
    return suite


if __name__ == "__main__":
   unittest.TextTestRunner(verbosity=2).run(suite())
