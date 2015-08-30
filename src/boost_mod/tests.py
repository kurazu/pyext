import base_tests


class GilTest(base_tests.BaseTestCase):

    module_name = 'boost'

    def test_has_letter(self):
        self.assertEqual(self.module.has_letter("zupa", "p"), True)
        self.assertEqual(self.module.has_letter("zupa", "x"), False)
