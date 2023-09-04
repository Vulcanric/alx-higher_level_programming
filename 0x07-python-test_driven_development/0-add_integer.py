#!/usr/bin/python3
"""This module ``add_integer`` calls only one function: add_integer(a, b)
The function compute the sum of two integers or floats
"""


def add_integer(a, b=98):
    """returns the sum of a and b

    >>> add_integer(2, 5)
    7
    >>>

    """
    err_msg = "{param} must be an integer"

    # Making sure that arguments passed must be of type int or float
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    # If any parameter is of type float, typecast to int first
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
