#!/usr/bin/python3
"""returns a list of lists representing paschal triangle
"""


def pascal_triangle(n):
    #my_list = []
    my_triangle = []
    index = 1
    if n <= 0:
        return my_list
    else:
        #first_term = 2
        last_term = 1
        #elem = first_term + last_term
        
        #my_list.insert(index, elem)
        #my_triangle.append(first_term)
        #my_triangle.insert(1, 2)
        my_triangle.append(last_term)
        for i in range(n):
            my_list = [1]
            #my_triangle.insert(index, my_list)
            my_list.extend(my_triangle)
            #index += 1
            
        #for i in range(n):
            #my_list.append(i)
        #return (my_list.append(i) * n for i in range(n))
            return (my_list)
