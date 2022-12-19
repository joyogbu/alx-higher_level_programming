#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return(a_dictionary)
    y = {k: v for k, v in a_dictionary.items() if v == value}
    for ky, val in y.items():
        del a_dictionary[ky]
    return(a_dictionary)
