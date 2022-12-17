#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for ky, vl in a_dictionary.items():
        if key in a_dictionary:
            a_dictionary[ky] = value
        else:
            a_dictionary[key] = value
        return(a_dictionary)
