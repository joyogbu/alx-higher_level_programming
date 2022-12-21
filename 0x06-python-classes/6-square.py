#!/usr/bin/python3
"""defining a empty square class"""


class Square():
    """Represents a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing with data
        Args:
        size (int): size of the square
        position (tuple): position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """representing a getter"""
        return self.__size
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

    @property
    def position(self):
        """Represent a getter"""
        return self.__position
    @position.setter
    def position(self, value):
        """representing a position setter
        Args:
        value (int): new position to set
        """
        if (len(value) != 2 or type(value) != tuple or not
                all(isinstance(i, int) for i in value) or not
                all(i >= 0 for i in value)):
            raise TypeError('position \
                    must be a tuple of two positive integers')
        else:
            self.__position = value

    def area(self):
        """initializing area"""
        return self.__size**2

    def my_print(self):
        """representing a print method"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for v in range(self.__size):
                    print('#', end="")
                print()
