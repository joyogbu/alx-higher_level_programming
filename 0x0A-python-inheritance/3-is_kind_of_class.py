#!/usr/bin/python3
"""check8ng instance of an object"""


def is_kind_of_class(obj, a_class):
    """defining the functiom"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
