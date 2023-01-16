#!/usr/bin/python3
"""class rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """representing the class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiating the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """use getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, val):
        """use setter to set the width"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """use getter to get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """use setter to set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """use getter to get x"""
        return self.__x

    @x.setter
    def x(self, val):
        """use setter to set x"""
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """use getter to get y"""
        return self.__y

    @y.setter
    def y(self, valu):
        """using setter to set the value"""
        if type(valu) != int:
            raise TypeError("y must be an integer")
        if valu < 0:
            raise ValueError("y must be >= 0")
        self.__y = valu

    def area(self):
        """defing the function for area of rectangle instance"""
        return self.__width * self.__height
