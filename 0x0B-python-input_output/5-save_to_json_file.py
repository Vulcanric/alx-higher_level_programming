#!/usr/bin/python3
"""Defines a function that writes a Python object to a text file
    using JSON string representation"""


    import json

    def save_to_json_file(my_obj, filename):
        """Writes a Python object to a text file using JSON string
        representation
        :param my-obj: object to write
        :param filename: text file to write to
        :returns: nothing (None)
        """
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
