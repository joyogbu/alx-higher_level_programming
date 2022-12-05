#!/usr/bin/python3
def no_c(my_string):
    str_cpy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(str_cpy))
