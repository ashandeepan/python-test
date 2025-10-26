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
        self.assertEqual(result, 2, "Subtracting 5 - 3 should equal 2")

    def test_subtract_negative_result(self):
        """Test subtraction yielding negative result"""
        result = self.calc.subtract(3, 5)
        self.assertEqual(result, -2, "Subtracting 3 - 5 should equal -2")

    # Test cases for multiplication
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers"""
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12, "Multiplying 4 * 3 should equal 12")

    def test_multiply_by_zero(self):
        """Test multiplication by zero"""
        result = self.calc.multiply(10, 0)
        self.assertEqual(result, 0, "Multiplying 10 * 0 should equal 0")

    # Test cases for division
    def test_divide_positive_numbers(self):
        """Test division with positive numbers"""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0, "Dividing 10 / 2 should equal 5.0")

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Division by zero is not allowed")

    # Test history functionality
    def test_calculation_history(self):
        """Test if calculation history is maintained correctly"""
        self.calc.add(5, 3)
        self.calc.subtract(5, 3)
        self.calc.multiply(4, 3)
        history = self.calc.get_history()
        self.assertEqual(len(history), 3, "History should contain 3 entries")
        self.assertIn("Add: 5 + 3 = 8", history)
        self.assertIn("Subtract: 5 - 3 = 2", history)
        self.assertIn("Multiply: 4 * 3 = 12", history)

    # Test floating point precision
    def test_floating_point_precision(self):
        """Test floating point calculations"""
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result, 0.3333333333333333, places=7)

    # Test type checking
    def test_invalid_input_types(self):
        """Test that invalid input types raise TypeError"""
        with self.assertRaises(TypeError):
            self.calc.add("5", 3)
        with self.assertRaises(TypeError):
            self.calc.add(5, "3")

    # Test class instance
    def test_calculator_instance(self):
        """Test if calculator is proper instance"""
        self.assertIsInstance(self.calc, Calculator)

    @unittest.skip("Demonstrating skipping test")
    def test_skipped_test(self):
        """This test will be skipped"""
        self.fail("This should not run")

    @unittest.expectedFailure
    def test_expected_failure(self):
        """Test that's expected to fail"""
        result = self.calc.add(2, 2)
        self.assertEqual(result, 22, "This is expected to fail")

# Run specific tests with custom conditions
class TestCalculatorConditional(unittest.TestCase):
    @unittest.skipIf(math.sqrt(16) != 4, "Skipping because math.sqrt is broken")
    def test_conditional_skip(self):
        """Test that will be skipped if condition is met"""
        result = self.calc.add(2, 2)
        self.assertEqual(result, 4)

# Custom test suite runner
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_add_positive_numbers'))
    suite.addTest(TestCalculator('test_divide_by_zero'))
    suite.addTest(TestCalculator('test_calculation_history'))
    return suite

if __name__ == '__main__':
    # Create test runner
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Run all tests
    print("Running all tests...")
    unittest.main(verbosity=2, exit=False)
    
    # Run custom test suite
    print("\nRunning custom test suite...")
    runner.run(suite())
