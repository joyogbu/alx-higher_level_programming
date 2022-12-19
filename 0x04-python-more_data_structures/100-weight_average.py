#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return(0)
    s = 0
    t = 0
    for sub in my_list:
        s += sub[0]*sub[1]
        t += sub[1]
    return(s / t)
