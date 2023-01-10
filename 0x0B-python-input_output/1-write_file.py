#!/usr/bin/python3
"""writing to a text file
"""


def write_file(filename="", text=""):
    """defining the function
    """
    with open(filename, 'w', encoding="utf-8") as f:
        no_written = f.write(text)
        return(no_written)
