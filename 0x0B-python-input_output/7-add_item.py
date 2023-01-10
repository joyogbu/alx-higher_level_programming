#!/usr/bin/python3
"""adds all arguments to a python list and save them to a file
"""


import json
import sys


index = 1
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = 'add_item.json'
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []
for arg in range(len(sys.argv[1:])):
    my_list.append(sys.argv[index])
    index += 1
save_to_json_file(my_list, filename)
