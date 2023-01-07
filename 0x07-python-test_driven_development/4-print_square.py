#!/usr/bin/python3
"""this module prints a square based on size
"""


def print_square(size):
    """defining the print square function"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    string = ""
    for i in range(size):
        for v in range(size):
            string += "#"
        if i < size:
            string += '\n'
    print(string)
