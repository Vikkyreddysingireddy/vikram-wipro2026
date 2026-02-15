import unittest

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    unittest.main()
