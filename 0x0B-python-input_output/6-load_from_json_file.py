#!/usr/bin/python3
"""Defines a function that creates a Pyton object from a 'JSON file'"""
from json import load


def load_from_json_file(filename):
    """Creates a Python object from a "JSON file"
    :param filename: file to read obj-str representation from
    :returns: the object created
    """
    with open(filename) as file:
        return load(file)
