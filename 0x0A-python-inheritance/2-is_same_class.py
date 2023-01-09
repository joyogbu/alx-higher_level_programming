#!/usr/bin/python3
"""check if an object is direcet instance of a type"""


def is_same_class(obj, a_class):
    """defining the function"""
    if type(obj) == a_class:
        return (True)
    return (False)
