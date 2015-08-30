import base_tests


class KeyTest(base_tests.BaseTestCase):

    module_name = 'key'

    def setUp(self):
        super().setUp()
        self.mapping = {
            'fruit': ['Cherry', 'Apple'],
            'vegetable': ['Tomato', 'Cucumber']
        }

    def test_true(self):
        self.assertTrue(
            self.module.belongs(self.mapping, 'Cherry', 'fruit')
        )
        self.assertTrue(
            self.module.belongs(self.mapping, 'Cucumber', 'vegetable')
        )

    def test_kwargs(self):
        self.assertTrue(
            self.module.belongs(
                category='fruit',
                item='Cherry',
                mapping=self.mapping,
            )
        )
        self.assertFalse(
            self.module.belongs(
                item='Strawberry',
                category='fruit',
                mapping=self.mapping,
            )
        )

    def test_false(self):
        self.assertFalse(
            self.module.belongs(self.mapping, 'Strawberry', 'fruit')
        )
        self.assertFalse(
            self.module.belongs(self.mapping, 'Strawberry', 'vegetable')
        )

    def test_no_key(self):
        with self.assertRaisesArg(KeyError, 'candy'):
            self.module.belongs(self.mapping, 'Cookie', 'candy')

    def test_no_dict(self):
        with self.assertRaisesArg(
            TypeError, 'list indices must be integers, not str'
        ):
            self.module.belongs([], 'Cherry', 'fruit')
