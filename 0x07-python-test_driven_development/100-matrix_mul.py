#!/usr/bin/python3
"""multiply two matrices"""


def matrix_mul(m_a, m_b):
    """defining the function"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if not any(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not any(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elements, int) or isinstance(elements, float)) for elements in [item for row in m_b for item in row]):
        raise TypeError("m_b should contain only integers or floats")
    for rows in m_a:
        if len(rows) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for rows in m_b:
        if len(rows) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return(res)
