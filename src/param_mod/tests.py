import base_tests


class ParamTest(base_tests.BaseTestCase):

    module_name = 'param'

    def test_basic(self):
        self.assertEqual(
            self.module.hello("Janusz", 45),
            "Hello Janusz age 45!"
        )

    def test_outside_unsigned(self):
        self.assertEqual(
            self.module.hello("Grzegorz", -3), "Hello Grzegorz age 4294967293!"
        )

    def test_long_unsigned(self):
        self.assertEqual(
            self.module.hello(
                "Roksana",
                999999999999999999999999999999999999999999999999999999999999999
            ),
            "Hello Roksana age 4294967295!"
        )

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
