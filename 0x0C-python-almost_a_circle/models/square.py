#!/usr/bin/python3
"""This module defines a class 'Square' which is a subclass
of class 'Rectangle'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class is defined as a subclass of class Rectangle

    It defines a square object, having all sides equal

    Every object created is instantiated as:
        Square(size, x=0, y=0, id=None)

    It uses all the attributes defined in Rectangle, only
    that both width and height are the same size and are
    represented as *size*

    When instances created from the class is printed, it displays
    the object as this:
            [Square] (<id>) <x>/<y> - <size>

    It performs activities related to a square object.
    """
    # The constructor
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates all object created from this class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints a string value that represents the object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, \
self.width)

    @property
    def size(self):
        """The getter of attribute size"""
        return self.width

    @size.setter
    def size(self, size):
        """The size setter method"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the attributes of a square instance"""
        # if positional argument passed is not empty, skip kwargs
        if args != ():
            # self.width a.k.a size
            attributes = [self.id, self.width, self.x, self.y]
            for i in range(len(args)):
                if i == 4:
                    break
                attributes[i] = args[i]
            self.id = attributes[0]
            self.width = attributes[1]
            self.x = attributes[2]
            self.y = attributes[3]
        else:  # otherwise use keyword arguments
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of instances"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
