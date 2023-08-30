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

    def size(self):
        """The getter
        Return:
            returns the value of the Square size
        """
        return self.__size

    def size(self, value):
        """The setter

        Description:
            resets the value of size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of square

        args:
            self: the instance or object created through class
        Return:
            returns the area
        """
        return (self.__size ** 2)
