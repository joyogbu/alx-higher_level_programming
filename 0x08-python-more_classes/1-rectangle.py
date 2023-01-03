#!/usr/bin/python3
""" An empty class recrangle that defines a rectangle """


class Rectangle:
    """ defie the rectangle class
    """
    def __init__(self, width=0, height=0):
        """instatiating an object

        Args:
        width (int): width of the rectangle object
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """use getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """use setter to set the value

        Args:
        value (int): width value
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height

        Args:
        value (int): height
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
