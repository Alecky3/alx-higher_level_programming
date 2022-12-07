#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""

    return (list(map(lambda x: [i**2 for i in x], matrix)))
