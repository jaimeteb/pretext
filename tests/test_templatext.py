import unittest

from templatext import Templatext


class TestTemplatex(unittest.TestCase):
    """Test Templatext module"""

    def setUp(self):
        self.en = Templatext(language="en")
        self.es = Templatext(language="es")

    def test_preprocess_en(self):
        text = " <p> Hey music is good I'm loving it!! </p>"
        expected = ["hey", "music", "good", "love"]

        self.assertEqual(self.en.preprocess(text), expected)

    def test_preprocess_es(self):
        text = " <p> Está super interesante !! </p>"
        expected = ["super", "interesante"]

        self.assertEqual(self.es.preprocess(text), expected)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestTemplatex)
    )
    return suite


if __name__ == "__main__":
   unittest.TextTestRunner(verbosity=2).run(suite())
