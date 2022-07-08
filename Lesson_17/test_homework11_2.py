import unittest
import Homework11_2


class HomeworkTest(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertEqual(Homework11_2.palindrome('12321'), 'Palindrome')

    def test_palindrome_false(self):
        self.assertEqual(Homework11_2.palindrome('123421'), 'Not Palindrome')


if __name__ == '__main__':
    unittest.main()
