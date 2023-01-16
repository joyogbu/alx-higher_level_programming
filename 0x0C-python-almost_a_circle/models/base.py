#!/usr/bin/python3
"""creating Base class module"""


class Base:
    """defining the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiating the class with id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
