#!/usr/bin/python3
"""write object to a text file using json"""


import json


def save_to_json_file(my_obj, filename):
    """defining the function"""
    with open(filename, 'w', encoding="utf-8") as f:
        written = f.write(json.dumps(my_obj))
        return (written)
