#!/usr/bin/python3
"""read and print a text file
"""


def read_file(filename=""):
    """defining the function"""
    with open(filename, encoding="utf-8") as my_file:
        my_txt = my_file.read()
        print(my_txt)
