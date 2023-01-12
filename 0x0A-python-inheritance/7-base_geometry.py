#!/usr/bin/python3
"""empty class BaseGeometry"""


class BaseGeometry:
    """representing the class"""
    pass

    def area(self):
        """defining area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")

