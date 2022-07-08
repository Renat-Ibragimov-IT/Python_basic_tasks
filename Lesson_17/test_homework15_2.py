import unittest
import Homework15_2


class HomeworkTest(unittest.TestCase):
    def test_change_user_number_true(self):
        self.assertEqual(Homework15_2.change_number_format("063-999-99-99"),
                         '(+38) 063 999-99-99')

    def test_change_user_number_false(self):
        self.assertEqual(Homework15_2.change_number_format("063-b999-99-99"),
                         'Failed to recognize number')


if __name__ == '__main__':
    unittest.main()
