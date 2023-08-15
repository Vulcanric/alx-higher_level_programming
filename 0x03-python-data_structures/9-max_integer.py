#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list
    """
    # If the list is empty
    if len(my_list) == 0:
        return None

    max_num = my_list[0]

    for number in my_list:
        if max_num < number:
            max_num = number

    return max_num
