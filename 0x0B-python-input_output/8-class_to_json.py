#!/usr/bin/python3
"""return a dictionary of a data structure for json
serialization"""


def class_to_json(obj):
    """defining the function"""
    return (obj.__dict__)
