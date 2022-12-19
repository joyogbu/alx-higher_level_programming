#!/usr/bin/python3
def weight_average(my_list=[]):
    #return(sum(x * y / sum(y) for x, y in my_list))
    #return(sum(x[0] * x[1]) / x[1] for x in my_list)
    s = 0
    t = 0
    for sub in my_list:
        s += sub[0]*sub[1]
        t += sub[1]
    return(s / t)
