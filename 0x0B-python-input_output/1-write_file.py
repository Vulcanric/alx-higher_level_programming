#!/usr/bin/python3
"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    """Write the text - @text to file - @filename
    * Erases the former content of the file
    * Creates the file if it doesn't exist
    :param filename: file to write to
    :param text: content to write
    :returns: the number of characters written
    """
    with open(filename, "w", encoding='utf-8') as file:
        chars_read = file.write(text)
        return chars_read
