#!/usr/bin/python3
"""send github credentials and print id"""


import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    req = requests.get('https://api.github.com/user',
                       auth=(username, password))
    try:
        out = req.json()
        print(out['id'])
    except KeyError:
        print(None)
