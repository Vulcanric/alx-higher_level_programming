#!/usr/bin/python3

"""Defined a class Square"""


class Square:
    """class Square:
        Defined class
    Initializes instances:
        set private attribute (size) to parameter (size)
    defined method Area:
        returns the area of size
    """
    def __init__(self, size=0):
        """Initializes a Square instance

        args:
            self: the instance or object created through class
            size (int): size of the square

        Return:
            returns nothing
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of square

        args:
            self: the instance or object created through class

        Return:
            returns the area
        """
        return (self.__size ** 2)
