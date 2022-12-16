#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cop = my_list.copy()
    if search not in my_list:
        pass
    if len(cop) == 0:
        pass
    arr = []
    idx = 0
    for idx in range(len(cop)):
        for val in cop:
            #for idx, val in enumerate(cop):
            if val == search:
                arr.append(idx)
            idx += 1
        if arr == []:
            pass
        #print(arr)
        for v in arr:
            cop[v] = replace
            return(cop)
