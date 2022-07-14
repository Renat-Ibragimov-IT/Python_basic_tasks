import unittest
import dict_iterating


class TestDictIterating(unittest.TestCase):
    def test_merging_into_dict(self):
        self.assertEqual(dict_iterating.merging_into_dict((1, 2, 3),
                    ('one', 'two', 'three')), {1: 'one', 2: 'two', 3: 'three'})


if __name__ == '__main__':
    unittest.main()
