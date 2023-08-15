#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers
    """
    for row in matrix:
        for num in row:
            print("{}".format(num))
