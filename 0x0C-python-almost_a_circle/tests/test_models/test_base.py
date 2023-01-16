import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """test base class"""

    def test_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_public_id(self):
        b3 = Base()
        b3.id = 10
        self.assertEqual(b3.id, 10)

    """test number of instances after unique id"""
    def test_id2(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id3(self):
        self.assertEqual(Base(15).id, 15)
    """check for None value"""
    def test_id4(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 5)

    """test id for instance of a subclass rectangle"""
    def test_id5(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 6)

    def test_id6(self):
        r2 = Rectangle(3, 10)
        self.assertEqual(r2.id, 7)

    def test_id7(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_id8(self):
        with self.assertRaises(TypeError) as er:
            r4 = Rectangle()
        print(str(er.exception))
        self.assertEqual(str(er.exception), "__init__() missing 2 "
                                            "required positional arguments: "
                                            "'width' and 'height'")


if __name__ == '__main__':
    unittest.main()
