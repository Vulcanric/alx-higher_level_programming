#!/usr/bin/python3
"""Defines a class: 'Rectangle' that inherits from the: 'Base' class
defined in the: 'base.py' module
"""
from models.base import Base


class Rectangle(Base):
    """This class is a subclass / child-class of the: 'Base' class

    It has its own instance attributes, which are private,
    that defines a rectangular object, along with their
    getters and setters methods
    These attributes are:
        width, height, x, y, including the inherited *id*

    Every object created from this class inherits its id from the
    'Base' class
    """
    def validate_parameters(w=1, h=1, x=0, y=0):
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    # The Constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        # check for invalid parameter types
        Rectangle.validate_parameters(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # width getter
    @property
    def width(self):
        return self.__width

    # height getter
    @property
    def height(self):
        return self.__height

    # x getter
    @property
    def x(self):
        return self.__x

    # y getter
    @property
    def y(self):
        return self.__y

    # Setters
    @width.setter
    def width(self, width):
        Rectangle.validate_parameters(w=width)
        self.__width = width

    @height.setter
    def height(self, height):
        Rectangle.validate_parameters(h=height)
        self.__height = height

    @x.setter
    def x(self, x_value):
        Rectangle.validate_parameters(x=x_value)
        self.__x = x_value

    @y.setter
    def y(self, y_value):
        Rectangle.validate_parameters(y=y_value)
        self.__y = y_value
