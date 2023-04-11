#!/usr/bin/python3
"""post an email"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    em = sys.argv[2]
    value = {"email": em}
    req = requests.post(url, data=value)
    print(req.text)
