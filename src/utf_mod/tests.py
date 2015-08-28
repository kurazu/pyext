import base_tests


class UtfTest(base_tests.BaseTestCase):

    module_name = 'utf'

    def test_utf(self):
        self.assertEqual(self.module.hello('żółw'), 'żółty')

    def test_different(self):
        self.assertEqual(self.module.hello('żółty'), 'ERROR')

    def test_len_ascii(self):
        self.assertEqual(self.module.len('Janusz'), 6)

    def test_len_unicode(self):
        self.assertEqual(self.module.len('żółw'), 7)

    def test_len_zero(self):
        with self.assertRaisesArg(
            TypeError, 'must be str without null characters, not str'
        ):
            self.module.len('zero\x00zero')
