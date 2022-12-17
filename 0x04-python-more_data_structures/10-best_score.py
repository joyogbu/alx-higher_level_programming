#!/usr/bin/python3
def best_score(a_dictionary):
    #valu = a_dictionary.values()
    #max_val = max(valu)
    #print(valu)
    #print(max_val)
    if a_dictionary is not None:
        myk = {ky for ky, val in a_dictionary.items() if val == max(a_dictionary.values())}
        return(myk)
