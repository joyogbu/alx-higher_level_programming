#!/usr/bin/python3
"""add attribute to an object"""


def add_attribute(obj, name, value):
    """defining the function"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
