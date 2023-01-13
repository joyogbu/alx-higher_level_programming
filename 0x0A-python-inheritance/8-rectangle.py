#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """class rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantiating the class"""
        self.__width = width
        self.__height = height
        #super().integer(self)
        #BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
