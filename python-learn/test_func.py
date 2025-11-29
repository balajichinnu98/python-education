# test_func.py
import unittest
from func import even_odd

class TestEvenOdd(unittest.TestCase):
    def test_even_odd(self):
        expected = ["0 is even", "1 is odd", "2 is even"]
        self.assertEqual(even_odd(3), expected)

if __name__ == "__main__":
    unittest.main()
