#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #my_tuple = [(x[0] + y[0], x[1] + y[1]) for x in tuple_a for y in tuple_b]
    #new_t = (0, 0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0)
    my_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return my_tuple
