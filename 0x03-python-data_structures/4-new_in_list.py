#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list,
    at a specific position without modifying the original list
    """
    # Getting a copy of the list
    new_list = []
    for elem in my_list:
        new_list.append(elem)

    # Modifying the copy

    # If the index given is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return new_list
    i = 0
    while i < len(new_list):
        if i == idx:
            new_list[i] = element
        i += 1

    return new_list
