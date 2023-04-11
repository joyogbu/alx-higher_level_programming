#!/usr/bin/python3
"""using utllib to frtch a url"""


import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
