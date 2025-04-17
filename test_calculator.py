# test_calculator.py

import unittest
import calculator  # importing the module to test

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
