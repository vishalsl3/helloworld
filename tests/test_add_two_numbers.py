import unittest
from add_two_numbers import add_two_numbers

class TestAddTwoNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add_two_numbers(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_two_numbers(-1, 1), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add_two_numbers(1.5, 2.5), 4.0)

if __name__ == "__main__":
    unittest.main()
