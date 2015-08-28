import unittest
import contextlib


class ParamTest(unittest.TestCase):

    def setUp(self):
        import param
        self.module = param

    def test_basic(self):
        self.assertEqual(
            self.module.hello("Janusz", 45),
            "Hello Janusz age 45!"
        )

    def test_outside_unsigned(self):
        self.assertEqual(
            self.module.hello("Grzegorz", -3), "Hello Grzegorz age -3"
        )

    def test_long_unsigned(self):
        self.assertEqual(
            self.module.hello(
                "Roksana",
                999999999999999999999999999999999999999999999999999999999999999
            ),
            "Hello Roksana "
            "999999999999999999999999999999999999999999999999999999999999999"
        )

    @contextlib.contextmanager
    def assertRaisesArg(self, exc_class, expected_arg):
        with self.assertRaises(TypeError) as ar:
            yield
        arg, = ar.exception.args
        self.assertEqual(arg, expected_arg)

    def test_wrong_params_1(self):
        with self.assertRaisesArg(
            TypeError, "function takes exactly 2 arguments (1 given)"
        ):
            self.module.hello("Seba")

    def test_wrong_params_2(self):
        with self.assertRaisesArg(
            TypeError, "must be str, not int"
        ):
            self.module.hello(16, "Seba")

    def test_wrong_params_3(self):
        with self.assertRaisesArg(
            TypeError, "function takes exactly 2 arguments (3 given)"
        ):
            self.module.hello("Seba", 16, "GRUBY")
