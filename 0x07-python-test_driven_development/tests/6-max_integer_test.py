import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """defining the class"""
    def test_max1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_test2(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max3(self):
        self.assertEqual(max_integer([6]), 6)

    def test_max5(self):
        self.assertEqual(max_integer([2, 4, -6]), 4)

    def test_max6(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max7(self):
        with self.assertRaises(TypeError):
            max_integer([])

    def test_max7(self):
        self.assertEqual(max_integer([-2]), -2)
