import unittest


class BasicTest(unittest.TestCase):

    def setUp(self):
        import basic
        self.module = basic

    def test_basic(self):
        self.assertEqual(self.module.hello(), "Hello world")
