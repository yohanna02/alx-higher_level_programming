#!/usr/bin/python3
"""
This module divides each
item in the matrix
"""

def matrix_divided(matrix, div):
    """
    divides the value of the matrix
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    new_matrix = []
    max_size = 0
    for index, i in enumerate(matrix):
        if index == 0:
            max_size = len(i)
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif index > 0 and len(i) != max_size:
            raise TypeError("Each row of the matrix must have the same size")
        
        temp = []
        for j in range(max_size):
            temp.append(round(i[j] / div, 2))
        new_matrix.append(temp)
    
    return new_matrix