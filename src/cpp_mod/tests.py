import base_tests


class CppTest(base_tests.BaseTestCase):

    module_name = 'cpp'

    def test_cpp(self):
        self.assertEqual(
            self.module.format("Mary", 21),
            "Mary is 21 years old."
        )
        self.assertEqual(
            self.module.format("George", 34),
            "George is 34 years old."
        )
        with self.assertRaises(TypeError):
            # must be str without null characters, not str
            self.module.format("Zero\x00zero", 0)
