#!/usr/bin/python3
"""demonstrate instance of a class
"""


def inherits_from(obj, a_class):
    """defining the function"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
