#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Function that deletes the item at a given position(idx) in the list
    """
    list_len = len(my_list)

    if idx < 0 or idx >= list_len:  # If idx is negative or out of range
        return my_list

    i = 0
    while i < list_len:
        if i == idx:
            del my_list[i]
        i += 1

    return my_list
