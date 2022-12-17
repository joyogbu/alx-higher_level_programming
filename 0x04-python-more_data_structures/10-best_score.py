#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    for ky, val in a_dictionary.items():
        if val == max(a_dictionary.values()):
            return(ky)
