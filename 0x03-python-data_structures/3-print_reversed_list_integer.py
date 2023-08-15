#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list, in reverse order
    """
    if len(my_list) == 0:
        print("{}".format(''))
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
