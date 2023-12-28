#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers in matrix"""
    squared_matrix = []
    for row in matrix:
        squared_matrix.append(list(map(lambda x: x ** 2, row)))

    return squared_matrix
