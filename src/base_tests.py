import contextlib
import unittest


class BaseTestCase(unittest.TestCase):

    module_name = None

    def setUp(self):
        self.module = __import__(self.module_name)

    @contextlib.contextmanager
    def assertRaisesArg(self, exc_class, expected_arg):
        with self.assertRaises(TypeError) as ar:
            yield
        arg, = ar.exception.args
        self.assertEqual(arg, expected_arg)
