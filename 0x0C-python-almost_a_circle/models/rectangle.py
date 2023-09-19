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
        """Instantiate objects made from this class"""
        # check for invalid parameter types
        Rectangle.validate_parameters(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """Returns string representation of rectangle object"""
        return "[Rectangle] ({0}) {1}/{2} - \
{3}/{4}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    # width getter
    @property
    def width(self):
        """returns the value of width to caller"""
        return self.__width

    # height getter
    @property
    def height(self):
        """returns the value of height to caller"""
        return self.__height

    # x getter
    @property
    def x(self):
        """returns the value of x to caller"""
        return self.__x

    # y getter
    @property
    def y(self):
        """returns the value of y to caller"""
        return self.__y

    # Setters
    @width.setter
    def width(self, width):
        """Sets the value of private attribute width"""
        Rectangle.validate_parameters(w=width)
        self.__width = width

    @height.setter
    def height(self, height):
        """Sets the value of private attribute height"""
        Rectangle.validate_parameters(h=height)
        self.__height = height

    @x.setter
    def x(self, x_value):
        """Sets the value of private attribute x"""
        Rectangle.validate_parameters(x=x_value)
        self.__x = x_value

    @y.setter
    def y(self, y_value):
        """Sets the value of private attribute y"""
        Rectangle.validate_parameters(y=y_value)
        self.__y = y_value

    def area(self):
        """Returns the area of the rectangular object"""
        return self.width * self.height

    def display(self):
        """displays 2D representation of a rectangular object"""
        print("\n" * self.y, end="")
        [print(' ' * self.x + '#' * self.width) \
for i in range(self.height)]

    def update(self, *args, **kwargs):
        """Updates instance private parameters using a variable
        number of arguments passed to it.
        """
        # If positional arguments passed is not empty, skip kwargs
        if args != ():
            # represents id, width, height, x, and y default values
            attributes = [self.id, self.width, self.height, self.x, self.y]

            # copy values of arguments passed, into attribute list
            for i in range(len(args)):
                attributes[i] = args[i]
            # get updated attribute-values updated
            self.id = attributes[0]
            self.width = attributes[1]
            self.height = attributes[2]
            self.x = attributes[3]
            self.y = attributes[4]
        else:  # otherwise use keyword argments: kwargs
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """It returns the dictionary representation of an instance
        created
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, \
'height': self.height, 'width': self.width}
