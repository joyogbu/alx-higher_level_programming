#!/usr/bin/python3
"""defining an empty square and instatiating with a size attribute """


class Square:
    """class that defines a square"""
    def __init__(self, size=None):
        """instatiating with private instance attribute

        Args:
        size (int): private instance attribute
        """
        self.__size = size
