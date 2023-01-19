#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """representing the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiating the class"""

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the rectangle object"""
        string = "[" + self.__class__.__name__ + "]" + " (" + \
            str(self.id) + ") " + str(self.x) + "/" + \
            str(self.y) + " - " + str(self.width)
        return (string)
