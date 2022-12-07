#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    newl = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            newl.append(True)
        else:
            newl.append(False)
    return newl
