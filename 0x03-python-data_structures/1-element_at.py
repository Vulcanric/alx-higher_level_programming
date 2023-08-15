#!/usr/bin/python3

def element_at(my_list, idx):
    """Function that retrieves an element from a list
    at a particuliar index idx
    """
    if idx < 0 or idx >= len(my_list):  # if idx is negative or out of range
        return None
    i = 0
    while i < len(my_list):
        if i == idx:
            return my_list[i]
        i += 1
