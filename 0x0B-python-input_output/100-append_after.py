#!/usr/bin/python3
"""inserts a line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """defining tje function"""
    text = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
