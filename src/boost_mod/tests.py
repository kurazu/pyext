import inspect

import base_tests


class BoostTest(base_tests.BaseTestCase):

    module_name = 'boost'

    def setUp(self):
        super().setUp()
        self.Native = self.module.Native
        self.assertTrue(inspect.isclass(self.Native))

    def test_has_letter(self):
        self.assertEqual(self.module.has_letter("zupa", "p"), True)
        self.assertEqual(self.module.has_letter("zupa", "x"), False)

    def test_init_exc(self):
        with self.assertRaisesArg(
            TypeError, """Python argument types in
    Native.__init__(Native)
did not match C++ signature:
    __init__(_object*, std::string, long, bool)"""
        ):
            self.Native()

        with self.assertRaisesArg(
            TypeError, """Python argument types in
    Native.__init__(Native, str)
did not match C++ signature:
    __init__(_object*, std::string, long, bool)"""
        ):
            self.Native('Geronimo')

        with self.assertRaisesArg(
            TypeError, """Python argument types in
    Native.__init__(Native, str, int)
did not match C++ signature:
    __init__(_object*, std::string, long, bool)"""
        ):
            self.Native('Geronimo', 1337)

        with self.assertRaisesArg(
            TypeError, """Python argument types in
    Native.__init__(Native, str, str, bool)
did not match C++ signature:
    __init__(_object*, std::string, long, bool)"""
        ):
            self.Native('Geronimo', "1337", True)

    def test_init_1(self):
        native = self.Native('Geronimo', 1337, True)
        self.assertEqual(native.name, 'Geronimo')
        self.assertEqual(native.number, 1337)
        self.assertEqual(native.pointer, 'YES')
        self.assertEqual(
            native.summary(), 'Native Geronimo number 1337 pointer YES'
        )
        del native

    def test_init_2(self):
        native = self.Native('Sitting Bull', 31337, False)
        self.assertEqual(native.name, 'Sitting Bull')
        self.assertEqual(native.number, 31337)
        self.assertEqual(native.pointer, 'NO')
        self.assertEqual(
            native.summary(), 'Native Sitting Bull number 31337 pointer NO'
        )
        del native

    def test_del(self):
        native = self.Native('Sitting Bull', 31337, False)
        with self.assertRaisesArg(
            AttributeError, "can't delete attribute"
        ):
            del native.number

        with self.assertRaisesArg(AttributeError, "can't delete attribute"):
            del native.pointer

        with self.assertRaisesArg(AttributeError, "can't delete attribute"):
            del native.name

        del native
