#!/usr/bin/python3
"""read and print a text file
"""


def read_file(filename=""):
    """defining the function"""
    with open(filename, encoding="utf-8") as f:
        my_txt = f.read()
        print(my_txt, end='')
