#!/usr/bin/python3
"""empty class BaseGeometry"""


class BaseGeometry:
    """representing the class"""
    pass

    def area(self):
        """defining area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

class Rectangle(BaseGeometry):
    """class rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantiating the class"""
        self.__width = width
        self.__height = height
        #BaseGeometry.__init__(self)
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

