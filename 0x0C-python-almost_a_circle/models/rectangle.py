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
    # The Constructor
    def __init__(self, width, height, x=0, y=0, id=None):
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
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y
