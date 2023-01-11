#!/usr/bin/python3
"""returns a list of lists representing paschal triangle
"""


def pascal_triangle(n):
    my_list = [[]]
    if n <= 0:
        return my_list
    else:
        #for i in range(n):
            #my_list.append(i)
        return (my_list.append(i) * n for i in range(n))
