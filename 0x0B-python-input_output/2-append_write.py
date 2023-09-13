#!/usr/bin/python3
"""Defines a function that appends text to a file(UTF8)"""


def append_write(filename="", text=""):
    """Append text to a file (UTF8)
    :param filename: file to append @text to
    :param text: text to append
    :returns: the number of chars added
    """
    with open(filename, "a", encoding="utf-8") as file:
        chars_added = file.write(text)
        return chars_added
