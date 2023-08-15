#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Function that replaces an element of a list at a specific index, idx
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    i = 0
    while i < len(my_list):
        if i == idx:
            my_list[i] = element
        i += 1

    return my_list
