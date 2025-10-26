import unittest
import math
from datetime import datetime

# Class to be tested
class Calculator:
    def __init__(self):
        self.calculation_history = []

    def add(self, a, b):
        result = a + b
        self.calculation_history.append(f"Add: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.calculation_history.append(f"Subtract: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.calculation_history.append(f"Multiply: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        self.calculation_history.append(f"Divide: {a} / {b} = {result}")
        return result

    def get_history(self):
        return self.calculation_history

# Test class with various test cases
class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a new Calculator instance before each test"""
        self.calc = Calculator()
        self.test_time = datetime.now()
        print(f"\nStarting test at {self.test_time}")

    def tearDown(self):
        """Clean up after each test"""
        print(f"Test completed at {datetime.now()}")
        del self.calc

    # Test cases for addition
    def test_add_positive_numbers(self):
        """Test addition with positive numbers"""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8, "Adding 5 + 3 should equal 8")

    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5, "Adding -2 + -3 should equal -5")

    def test_add_zero(self):
        """Test addition with zero"""
        result = self.calc.add(10, 0)
        self.assertEqual(result, 10, "Adding 10 + 0 should equal 10")

    # Test cases for subtraction
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers"""
        result = self.calc.subtract(5, 3)
        self.assert
