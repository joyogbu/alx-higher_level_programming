#!/usr/bin/python3
""" module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Representing the function"""

    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix \
                    (list of lists) of integers/floats')
    for row in matrix:
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return ([[round(item / div, 2) for item in row] for row in matrix])
