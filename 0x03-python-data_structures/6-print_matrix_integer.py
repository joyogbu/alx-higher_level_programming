#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
       for val in row:
           if row.index(val) != (len(matrix) - 1):
               print("{:d}".format(val), end=" ")
           else:
               print("{:d}".format(val), end = "")
       print()
