#!/usr/bin/python3
"""send a query string via post"""


import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        val = ""
    else:
        val = sys.argv[1]
    payload = {'q': val}
    req = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    if req.json():
        print("[{}] {}".format(req.json()['id'], req.json()['name']))
    else:
        print("No result")
        print(req.status_code)
