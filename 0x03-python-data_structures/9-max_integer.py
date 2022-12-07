#!/usr/bin/python3
def max_integer(my_list=[]):
    le = len(my_list)
    for i in range(le):
        if le == 1:
            return my_list[i]
        if i == le - 1:
            i = le + 1
            return my_list[i]
        if my_list[i] > my_list[i-1]:
            return(my_list[i])
