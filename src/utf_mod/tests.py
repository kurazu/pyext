import unittest


class UtfTest(unittest.TestCase):

    def setUp(self):
        import utf
        self.module = utf

    def test_utf(self):
        self.assertEqual(self.module.hello('żółw'), 'żółty')

    def test_different(self):
        self.assertEqual(self.module.hello('żółty'), 'ERROR')
