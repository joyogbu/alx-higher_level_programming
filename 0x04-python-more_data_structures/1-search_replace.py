#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cop = my_list.copy()
    if search not in my_list:
        return
    idx = 0
    for idx in cop:
        if idx == search:
            ind = cop.index(search)
            cop[ind] = replace
            idx = idx + 1
            return(cop)
