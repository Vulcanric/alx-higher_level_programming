#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list

    Returns a new list with True or False,
    depending on whether the integer at the same position of
    the original list is a multiple of 2
    """
    new_list = []

    if len(my_list) > 0:
        for number in my_list:
            if number % 2 == 0:  # If the number is a multiple of 2
                new_list.append(True)  # append True to the list
            else:                # Otherwise ...
                new_list.append(False)  # append False

    return new_list
