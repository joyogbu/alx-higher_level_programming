#!/usr/bin/python3
"""appending to a text file
"""


def append_write(filename="", text=""):
    """defining the function
    """
    with open(filename, 'a', encoding="utf-8") as f:
        appended = f.write(text)
        return(appended)
