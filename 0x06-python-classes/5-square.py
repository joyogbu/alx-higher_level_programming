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

    @property
    def size(self):
        """representing a getter"""
    @size.setter
    def size(self, value):
        """representing a setter
        Args:
        value (int): new size to ser
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """initializing area"""
        return self.__size**2

    def my_print(self):
        """representing a print method"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for v in range(self.__size):
                    print('#', end="")
                print()
