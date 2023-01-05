#!/usr/bin/python3
"""defing magic class"""

import math


class MagicClass:
    """representing the magic class"""

    def __init__(self, radius=0):
        """initializing themagic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """defining area"""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """defining circumference"""
        return (2 * math.pi * self.__radius)
