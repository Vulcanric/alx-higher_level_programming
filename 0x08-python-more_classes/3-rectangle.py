#!/usr/bin/python3
"""This module contains more updated definition of a class ``Rectangle``
than other previous modules"""


class Rectangle:
    """Creates an object or instance of type Rectangle
    class ``Rectangle`` has the following:
    Private instance attribute called ``width``:
        getter method to retrieve it
        setter method to set it
    Private instance attribute ``height``:
        getter method to retrieve it
        setter method to set it
    Public instance method area():
        Returns the area of Rectangle
    Public instance method perimeter():
        Returns the perimeter of Rectangle
    Public instance __str__() method that prints the rectangle
    """

    def __init__(self, width=0, height=0):
        """Instantiate Object/instances created from this class
        :param width (int): private attribute, width of a Rectangle
        :param height (int): private attribute,height of a Rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def __str__(self):
        """Prints out the string representation of a Rectangle
        in shape using the '#' character
        :returns: the shape
        """
        rect_rep = []
        for i in range(self.__height):
            rect_rep.append('#' * self.__width + '\n')
        str_rep = ''.join(rect_rep)
        return str_rep.rstrip()

    @property
    def height(self):
        """Property (height) getter
        :returns: the value of private attribute ``height``
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property (height) setter
        Sets/resets the value of private attribute ``height``
        :returns: nothing
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Property (width) getter
        :returns: the value of private attribute ``width``
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property (width) setter
        Sets/resets the value of private attribute ``width``
        :returns: nothing
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the sum of the total sides of the rectangle"""
        length = self.__height
        breadth = self.__width
        perim = 2 * (length + breadth)
        return perim
