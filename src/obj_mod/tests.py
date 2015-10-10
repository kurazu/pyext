import base_tests
import inspect


class ObjTest(base_tests.BaseTestCase):

    module_name = 'obj'

    def setUp(self):
        super().setUp()
        self.Native = self.module.Native
        self.NativeError = self.module.NativeError
        self.assertTrue(inspect.isclass(self.Native))
        self.assertTrue(inspect.isclass(self.NativeError))
        self.assertTrue(issubclass(self.NativeError, ValueError))

    def test_init_exc(self):
        with self.assertRaisesArg(
            TypeError, "Required argument 'name' (pos 1) not found"
        ):
            self.Native()

        with self.assertRaisesArg(
            TypeError, "Required argument 'number' (pos 2) not found"
        ):
            self.Native('Geronimo')

        with self.assertRaisesArg(
            TypeError, "Required argument 'yes' (pos 3) not found"
        ):
            self.Native('Geronimo', 1337)

        with self.assertRaisesArg(
            TypeError, "an integer is required (got type str)"
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
        native = self.Native('Sitting Bull', 31337, [])
        self.assertEqual(native.name, 'Sitting Bull')
        self.assertEqual(native.number, 31337)
        self.assertEqual(native.pointer, 'NO')
        self.assertEqual(
            native.summary(), 'Native Sitting Bull number 31337 pointer NO'
        )
        del native

    def test_del(self):
        native = self.Native('Sitting Bull', 31337, [])
        with self.assertRaisesArg(
            TypeError, "can't delete numeric/char attribute"
        ):
            del native.number

        with self.assertRaisesArg(AttributeError, 'readonly attribute'):
            del native.pointer

        del native.name
        with self.assertRaisesArg(self.NativeError, 'name'):
            native.summary()

        del native

    def test_create(self):
        native = self.module.create()
        self.assertIsInstance(native, self.Native)
        self.assertEqual(native.name, 'Bill')
        self.assertEqual(native.number, 7)
        self.assertEqual(native.pointer, 'YES')
