import unittest
import phone_numbers_format


class TestPhoneNumbersFormat(unittest.TestCase):
    def test_change_user_number_true(self):
        self.assertEqual(phone_numbers_format.change_number_format
                         ("063-999-99-99"), '(+38) 063 999-99-99')

    def test_change_user_number_false(self):
        self.assertEqual(phone_numbers_format.change_number_format
                         ("063-b999-99-99"), 'Failed to recognize number')


if __name__ == '__main__':
    unittest.main()
