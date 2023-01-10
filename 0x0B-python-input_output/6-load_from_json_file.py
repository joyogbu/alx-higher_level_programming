#!/usr/bin/python3
"""create an object from a json file
"""


import json


def load_from_json_file(filename):
    """defining the functionz"""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
