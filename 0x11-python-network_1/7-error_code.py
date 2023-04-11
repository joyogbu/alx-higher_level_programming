#!/usr/bin/python3
"""printing error code from a url"""


import sys
import requests
import requests.exceptions


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = requests.get(url)
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print('Error code:', e.response.status_code)
