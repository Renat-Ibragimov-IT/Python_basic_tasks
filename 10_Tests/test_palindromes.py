import unittest
import palindromes


class TestPalindromes(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertEqual(palindromes.palindrome('12321'), 'Palindrome')

    def test_palindrome_false(self):
        self.assertEqual(palindromes.palindrome('123421'), 'Not Palindrome')


if __name__ == '__main__':
    unittest.main()
