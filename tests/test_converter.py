# temp_converter/tests/test_converter.py

import unittest
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)

if __name__ == "__main__":
    unittest.main()

