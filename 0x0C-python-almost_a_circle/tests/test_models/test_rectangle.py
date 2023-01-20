import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """run tests for private instance attribute of rectangle
    """

    """testing with string value will raise Typeerror"""
    def test_instance_attr1(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")

    """testing with a negative width will raise a valueerror"""
    def test_instance_attr2(self):
        with self.assertRaises(ValueError) as er:
            r2 = Rectangle(-5, 4)
        self.assertEqual(str(er.exception), 'width must be > 0')

    """testing with a negative 'y' value will raise Valueerror"""
    def test_instance_attr3(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r3 = Rectangle(4, 3, 2, -1)

    """testing with a negative 'x' value will give Valueerror"""
    def test_instance_attr4(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r4 = Rectangle(3, 2, -1, 0)

    """testing with a float will raise typerror"""
    def test_instance_attr5(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r4 = Rectangle(3, 4, 2.3)

    """testing with a 0 width will raise valueerror"""
    def test_instance_0width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r_0 = Rectangle(0, 3)

    """testing with a 0 height will raise valueerror"""
    def teat_instance_0height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r_h = Rectangle(2, 0)

    """testing with a dictionary value for width will raise Typeerror"""
    def test_instance_attr6(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r4 = Rectangle({5}, 3)

    """testing with normal values"""
    def test_instance_attr7(self):
        self.assertEqual(Rectangle(3, 4).height, 4)

    def test_instance_attr8(self):
        self.assertEqual(Rectangle(2, 1, 6, 4, 2).x, 6)

    def test_instance_attr9(self):
        self.assertTrue(Rectangle(2, 4).width == 2)

    def test_instance_attr10(self):
        self.assertEqual(Rectangle(2, 4, 0, 0).y, 0)


class TestRectangleArea(unittest.TestCase):

    """testing normal values"""
    def test_area1(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)

    def test_area2(self):
        r2 = Rectangle(3, 5, 0, 0, 7)
        self.assertTrue(r2.area() == 15)

    """testing with a negative height will give valueerror"""
    def test_area3(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(3, -1).area()

    """testing with empty values"""
    def test_area4(self):
        with self.assertRaises(TypeError) as er:
            Rectangle().area()
        self.assertEqual(str(er.exception), "__init__() missing 2 required positional arguments: 'width' and 'height'")

    """testing with 0 width"""
    def test_area5(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 2).area()

    """testing with string value will return a Typeerror"""
    def test_area_string(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle("3", 2).area()

    """testing with float will give TypeError"""
    def test_area_float(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(2, 4.2).area()

    """testing with dictionary values"""
    def test_area_dict(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle({3, 2}, 4).area()


class TestRectangleStr(unittest.TestCase):
    
    def test_str1(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

    def test_str2(self):
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), '[Rectangle] (13) 1/0 - 5/5')

    def test_str3(self):
        with self.assertRaises(TypeError):
            r3 = Rectangle()
            print(r3)

    def test_str4(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            print(Rectangle(3, "3", 0, 0))

    def test_str5(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            print(Rectangle(2, 4, -1))
    


if __name__ == '__main__':
    unittest.main()
