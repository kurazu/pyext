import base_tests


class BasicTest(base_tests.BaseTestCase):

    module_name = 'basic'

    def test_basic(self):
        self.assertEqual(self.module.hello(), "Hello world")
