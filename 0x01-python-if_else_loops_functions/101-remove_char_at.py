#!/usr/bin/python3

def remove_char_at(str, n):
    """Creates a copy of the string str, removing the character at position n
    C array style
    """
    str_cpy = ""

    i = 0
    while i < len(str):
        if i != n:
            str_cpy += str[i]
        i += 1

    return str_cpy
