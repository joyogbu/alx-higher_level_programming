#!/usr/bin/python3
"""return an object represented by json string
"""


import json

def from_json_string(my_str):
    """defining the function
    """
    x = json.loads(my_str)
    return(x)
