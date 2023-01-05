#!/usr/bin/python3
"""defing magic class"""


class MagicClass:
    """representing the magic class"""

    def __init__(self):
        """initializing themagic class"""
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        return None    
        #self.__radius = None

    def area(self):
        """defining area"""
        return math.pi(self.__radius ** 2)

    def circumference(self):
        """defining circumference"""
        return 2 * (math.pi(self.__radius))

