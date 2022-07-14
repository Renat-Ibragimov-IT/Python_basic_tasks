import unittest
import temperature_conversion


class TestTemperatureConversion(unittest.TestCase):
    def test_temp_conv(self):
        self.assertEqual(temperature_conversion.temperature_converter(50, 'C',
                                                                      'F'),
                         122)


if __name__ == '__main__':
    unittest.main()
