#!/usr/bin/python3
"""post an email"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'Your email is' : email}
    # data = urllib.parse.urlencode(value)
    # data = data.encode()
    req = urllib.request.Request(url, data) 
    with urllib.request.urlopen(req) as response:
        out = response.headers
        print(out)
