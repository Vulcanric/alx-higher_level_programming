#!/usr/bin/python3

class Square:
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
