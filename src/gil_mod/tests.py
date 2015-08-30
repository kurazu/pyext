import base_tests


class ParamTest(base_tests.BaseTestCase):

    module_name = 'gil'

    def setUp(self):
        super().setUp()
        from . import fibo
        self.py_module = fibo

        self.expected = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55),
            (11, 89),
            (12, 144),
            (13, 233),
            (14, 377),
            (15, 610),
            (16, 987),
            (17, 1597),
            (18, 2584),
            (19, 4181),
            (20, 6765),
            (21, 10946),
            (22, 17711),
            (23, 28657),
            (24, 46368),
            (25, 75025),
            (26, 121393),
            (27, 196418),
            (28, 317811),
            (29, 514229),
            (30, 832040),
            (31, 1346269),
            (32, 2178309),
            (33, 3524578),
            (34, 5702887),
            (35, 9227465),
            (36, 14930352),
            (37, 24157817),
            (38, 39088169),
            (39, 63245986),
            (40, 102334155)
        ]

    def check_fun(self, func):
        for n, expected in self.expected:
            actual = func(n)
            self.assertEqual(actual, expected)

    def test_calc(self):
        self.check_fun(self.module.calc)

    def test_calc_release(self):
        self.check_fun(self.module.calc_release)

    def test_py(self):
        self.check_fun(self.py_module.fibonacci)