#!/usr/bin/python3
"""Define a function that serializes a python object to a
    json representation
"""
import json


def to_json_string(my_obj):
    """serializes my_obj into json representation"""
    try:
        return json.dumps(my_obj)
    except Exception:
        raise
