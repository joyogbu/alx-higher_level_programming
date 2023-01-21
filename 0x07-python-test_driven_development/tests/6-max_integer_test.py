import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test2(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test3(self):
        self.assertEqual(max_integer([6]), 6)

    def test4(self):
        with self.assertRaises(TypeError):
            max_integer(["3", "3"])

    def test5(self):
        self.assertEqual(max_integer([2, 4, -6]), 4)

    def test6(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test7(self):
        with self.assertRaises(TypeError):
            max_integer([])

    def test7(self):
        self.assertEqual(max_integer([-2]), -2)

