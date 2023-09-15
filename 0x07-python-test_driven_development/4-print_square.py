#!/usr/bin/python3
"""This module defines a function ``print_square(size)`` that prints
    a square of size :param size: with the character '#'
"""


def print_square(size):
    """prints a square of size :param size: with the character '#' to stdout

    Arg:
        size: size of the square
    Returns:
        Nothing (None)
    Raises:
        * A TypeError, if size is not passed as an integer or is a
        float less than 0
        * A ValueError, if the size passed is less than 0
    """
    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    while i < size:
        print('#' * size)
        i += 1
