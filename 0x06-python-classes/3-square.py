#!/usr/bin/python3
"""defining a empty square class"""


class Square():
    """Represents a class Square"""
    def __init__(self, size=0):
        """Initializing with data
        Args:
        size (int): size of the square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """initializing area"""
        return self.__size**2
