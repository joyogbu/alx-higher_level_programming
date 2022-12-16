#!/usr/bin/python3
def uniq_add(my_list=[]):
    arr = []
    for elem in my_list:
        if elem not in arr:
            arr.append(elem)
    su = sum(arr)
    return(su)
