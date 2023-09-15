#!/usr/bin/python3
"""This module defines a function ``say_my_name(first_name, last_name="")``

    The function prints "My name is <first_name> <last_name>" to stdout
"""
def say_my_name(first_name, last_name=""):
    """Prints the string "My name is <first_name> <last_name>" to stdout
    It raises a TypeError saying <first_name> or <last_name> must be a string
    if first_name or last_name was not passed as string objects

    Args:
        first_name: first argument
        last_name: last argument

    Returns: None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    try:
        print(f"My name is {first_name} {last_name}")
    except Exception as e:
        pass
