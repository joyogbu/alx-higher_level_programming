#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mdic = {ky: val * 2 for ky, val in a_dictionary.items()}
    return(mdic)
