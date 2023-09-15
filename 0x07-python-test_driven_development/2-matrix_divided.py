#!/usr/bin/python3
"""
This module ``2-matrix_divided`` defines one function: ``matrix_divided()``

The function returns a new matrix containing factors of list elements & divisor
rounded to 2d.p (decimal places)
The function matrix_divided(matrix, div) takes two arguments:
    @ a list of lists containing integers or floats
    @ div - divisor of all numbers of elements in matrix(It divides all
    elements in each rows)

    >>> matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]

    the following prints the factors of |= 3 and matrix lists elements(int) =|
rounded to 2d.p
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix
    [[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """Returns a matrix(list of lists) contain factors(float) that resulted
    from dividing each row elements(int / float) of ``matrix`` by ``div``

    :param matrix: It must be a list of lists, otherwise TypeError is raised
    :param div (int / float): a non-zero number, the divisor
    """
    if not matrix or matrix[0] is None:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    new_matrix = []
    row = []
    row_size = len(matrix[0])

    # Handle zero division
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Handle type of divisor
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for rows in matrix:
        if type(rows) is not list:  # row might be a tuple, dict or string
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(rows) != row_size:  # If rows are not the same size
            raise TypeError("Each row of the matrix must have the same size")
        for num in rows:
            if type(num) not in [int, float]:  # row might be other types
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
            row.append(round(num / div, 2))
        new_matrix.append(row)
        row = []

    return new_matrix
