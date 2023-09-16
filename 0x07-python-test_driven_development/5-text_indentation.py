#!/usr/bin/python3
"""This module defines a function called `text_indentation(text)`

The function indents strings after these characters: ".", "?" and ":"
"""


def text_indentation(text):
    """Prints indented version of string @text,
    printing 2 new lines after these characters: ".", "?" and ":"

    Arg:
        text: string to format

    Returns:
        Nothing

    Raises:
        A TypeError if @text is not a string object
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end='')
            print("\n")
        else:
            print(text[i], end='')
