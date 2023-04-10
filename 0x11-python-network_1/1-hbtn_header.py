#!/usr/bin/env python3
"""srnd a URL request and display the X-Request-Id data"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as req:
        out = req.headers['X-Request-Id']
        print(out)
