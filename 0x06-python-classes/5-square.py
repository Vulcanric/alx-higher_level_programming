#!/usr/bin/python3

"""Defined a class Square"""


class Square:
    """Class Square:
        initialized instances with private attribute - size
        defined getter and setter methods to access attribute size:
            size: The getter:
                returns the value of size
            size: sets the value of size
        defined method area():
            returns the area of size
        defined method my_print():
            prints square with char '#' to stdout
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

    @property
    def size(self):
        """The getter
        Return:
            returns the value of the Square size
        """
        return self.__size

    @size.setter
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

    def my_print(self):
        """Prints the square of size with char '#' to stdout"""
        if self.__size == 0:
            print("")
        else:
            for x in range(1, self.__size + 1):
                print('#' * self.__size)
