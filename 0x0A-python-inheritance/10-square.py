#!/usr/python3
"""class square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """representing the class"""
    def __init__(self, size):
        """instantiating the class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    #def area(self):
        #return self.__size ** 2
