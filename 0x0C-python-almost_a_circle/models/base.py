#!/usr/bin/python3
"""This module defines a class 'Base' which stands as the
    base-class or super-class or parent-class of all classes
    in this project
"""
import json


class Base:
    """The base-class / super-class / parent-class of all other classes
    in this project

    It defines the constructor method used to instantiate it with the
    following parameters:
        self: this is used to represent objects created from this class
        id: integer value (default: None) assigned to each object created

    It manages the id of all instances created from it or from its
    subclasses / derived-classes / child-classes

    It does this using a class attribute: *__nb_objects* which updates
    itself whenever an object is created

    Generally, it is used to manage id's and reduce repetition of code.
    """
    __nb_objects = 0

    # The constructor
    def __init__(self, id=None):
        """Instantiate object or subclass created from this class"""
        ID = id
        if ID is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation of a list of dictionaries"""
        if list_dictionaries is not None and list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """It saves to a file the list of objects who inherits
        from the Base class. Examples are:
                Objects made from class `Rectangle` or class `Square`
                who are subclass of the Base class
        It saves to a file named as: <Class name>.json of instances in list
        overwritting the file, if it already exist
        """
        # First of all getting the name of the file to save to
        file_name = cls.__name__

        list_of_obj_dict = []

        if list_objs is not None:
            for obj in list_objs:  # for every object in list
                # If object is a subclass of Base
                if issubclass(obj.__class__, Base):
                    # Append object dictionary representation to list
                    list_of_obj_dict.append(obj.to_dictionary())

        # Append json extension to file name
        file_name += ".json"

        # open file and save json string representation
        # of list-of-object-dictionaries
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_of_obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the Pythonic object orientation of *json_string*

        :param json_string: string representing a list of dictionaries

        Returns an empty list if *json_string* is empty or None, otherwise

        the Python list object as specified by *json_string*
        """
        return [] if json_string is None or \
            json_string == "" else json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """It returns a new instance with all it's attributes set

        :param dictionary: keyworded arguments used to set up instance
        attributes
        """
        from models.rectangle import Rectangle
        from models.square import Square

        # Used to know what class, the instance should be made as
        option = 'r'  # defaults to class Rectangle

        # Create and initialise instance with dummy values
        for key, value in dictionary.items():
            if key == "size":
                option = 's'  # change to square

        if option == 'r':
            instance = Rectangle(width=1, height=1)
        elif option == 's':
            instance = Square(size=1)

        # Update attributes with values stored in parameter dictionary
        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a json file

            Returns:
                the list of instances
        """
        list_of_real_obj = []

        # First of all get the file name
        file_name = cls.__name__ + ".json"

        # Then try to read file and store string
        try:
            with open(file_name, 'r') as file:
                string = file.read()
        # What if file doesn't exist
        except FileNotFoundError:
            string = None

        # Next, convert string back to Python object dict
        list_obj_dict = cls.from_json_string(string)

        # The output above comes out as a list containing dictionaries in it
        # Create real objects from those object dictionaries using`cls.create`
        for obj_dict in list_obj_dict:
            list_of_real_obj.append(cls.create(**obj_dict))

        # And lastly, return the list of real object
        return list_of_real_obj
