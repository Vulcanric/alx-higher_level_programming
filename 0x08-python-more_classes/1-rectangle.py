#!/usr/bin/python3
"""This module contains definition of a class ``Rectangle``"""


class Rectangle:
    """Creates an object or instance of type Rectangle
    class ``Rectangle`` has the following:
    private instance attribute called ``width``:
        getter method to retrieve it
        setter method to set it
    Private instance attribute ``height``:
        getter method to retrieve it
        setter method to set it
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
