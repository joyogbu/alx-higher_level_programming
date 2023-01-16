import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """run tests for private instance attribute of rectangle
    """
    def test_instance_attr1(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")
            #self.assertEqual(str(er.exception), 'height must be an integer')

    def test_instance_attr2(self):
        with self.assertRaises(ValueError) as er:
            r2 = Rectangle(-5, 4)
        self.assertEqual(str(er.exception), 'width must be > 0')

    def test_instance_attr3(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r3 = Rectangle(4, 3, 2, -1)

    def test_instance_attr4(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r4 = Rectangle(3, 2, -1, 0)

    def test_instance_attr4(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r4 = Rectangle(3, 4, 2.3)
    def test_instance_attr5(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r4 = Rectangle({5}, 3)

    def test_instance_attr6(self):
        self.assertEqual(Rectangle(3, 4).height, 4)

    def test_instance_attr7(self):
        self.assertEqual(Rectangle(2, 1, 6, 4, 2).x, 6)

if __name__ == '__main__':
    unittest.main()
