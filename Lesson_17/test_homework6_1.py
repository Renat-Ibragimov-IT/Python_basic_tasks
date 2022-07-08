import unittest
import Homework6_1


class HomeworkTest(unittest.TestCase):
    def test_merging_into_dict(self):
        self.assertEqual(Homework6_1.merging_into_dict((1, 2, 3),
                    ('one', 'two', 'three')), {1: 'one', 2: 'two', 3: 'three'})


if __name__ == '__main__':
    unittest.main()


