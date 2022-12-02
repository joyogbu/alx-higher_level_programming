#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    list_names = names.sort
    for i in list_names:
        if names[0:2] != '__':
             print(list_names)
