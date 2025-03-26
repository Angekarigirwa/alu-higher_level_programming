#!/usr/bin/python3
"""function divides all elments of matrix"""


def matrix_divided(matrix, div):
    """divides elments of matrix"""
    if type(div) != float and type(div) != int:
        error1 = 'div must be a number'
        raise TypeError(error1)
    for i in matrix:
        if len(i) != len(matrix[0]):
            error2 = 'Each row of the matrix must have the same size'
            raise TypeError(error2)
    try:
        return [[round(k / div, 2) for k in j] for j in matrix]
    except TypeError:
        error3 = 'matrix must be a matrix (list of lists) of integers/floats'
        raise TypeError(error3)
    except ZeroDivisionError:
        raise ZeroDivisionError('division by zero')
