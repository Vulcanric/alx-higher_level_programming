#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list, in reverse order
    """
    i = -1
    while my_list is not None:
        print("{:d}".format(my_list[i]))
        i -= 1
