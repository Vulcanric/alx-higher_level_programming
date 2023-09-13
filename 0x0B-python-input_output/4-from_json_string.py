#!/usr/bin/python3
"""Defines a function that deserialize a JSON string
into a Python object"""
import json


def from_json_string(my_str):
    """Deserialize a JSON string into a Python object
    :param my_str: JSON string to deserialize
    :returns: Python Object representation
    """
    return json.loads(my_str)
