import unittest
import Homework7_2


class HomeworkTest(unittest.TestCase):
    def test_temp_conv(self):
        self.assertEqual(Homework7_2.temp_conv(50, 'C', 'F'), 122)


if __name__ == '__main__':
    unittest.main()
