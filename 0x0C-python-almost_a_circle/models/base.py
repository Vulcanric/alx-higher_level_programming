#!/usr/bin/python3
"""This module defines a class 'Base' which stands as the
    base-class or super-class or parent-class of all classes
    in this project
"""


class Base:
    """The base-class / super-class / parent-class of all other classes
    in this project

    It defines the constructor method used to instantiate it with the
    following parameters:
        self: this is used to represents the object created
        id: integer value (default: None) assigned to each object created

    It manages the id of all instances created from it or from its
    sub-classes / derived-classes / child-classes

    It does this using a class attribute: *__nb_objects* which updates
    itself whenever an object is created

    Generally, it is used to manage id's and reduce repetition of code.
    """
    __nb_objects = 0

    # The constructor
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
