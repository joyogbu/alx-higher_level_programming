#!/usr/bin/python3
"""class rRectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantiating the class"""
        #self.__width = width
        #self.__height = height
        #super().area()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[" + str(self.__class__.__name__) + "]" + " " + str(self.__width) + "/" + str(self.__height)
