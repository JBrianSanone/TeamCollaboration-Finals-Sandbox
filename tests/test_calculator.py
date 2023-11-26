import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calculator.subtract(8, 3)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = self.calculator.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

        # Test division by zero
        result = self.calculator.divide(10, 0)
        self.assertEqual(result, "Error: Division by zero is not allowed")

    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)

    def test_square(self):
        result = self.calculator.square(4)
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.main()
