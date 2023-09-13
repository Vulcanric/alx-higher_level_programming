#!/usr/bin/python3

"""Defines a file io function that reads a file(utf-8) and
    print to stdout the content of the file
"""


def read_file(filename=""):
    """Reads the content of a file in encoding utf-8 and prints its
    content to stdout
    :param filename: file to read
    :returns: nothing
    """
    with open(filename, "r", encoding='utf-8') as file:
        chars = file.read()
        content = ""
        while chars != '':
            content += chars
            chars = file.read()
        print(content.rstrip(), end='')
