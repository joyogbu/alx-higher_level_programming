#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cop = my_list.copy()
    ind = cop.index(search)
    cop[ind] = replace
    return(cop)
