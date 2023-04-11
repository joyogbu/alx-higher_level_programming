#!/usr/bin/python3
"""printing error code from a url"""


import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as req:
            print(req.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)

