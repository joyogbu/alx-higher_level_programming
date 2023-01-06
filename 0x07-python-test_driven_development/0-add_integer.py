#!/usr/bin/python3

"""we try to add two integers together"""


def add_integer(a, b=98):
    """function returns the sum of two integer

    Args:
    a(int): an integer
    b(int): anotjer integer

    Returns:
    sum of the integers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    return (a + b)
