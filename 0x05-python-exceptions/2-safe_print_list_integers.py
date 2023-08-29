#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers
    """
    num_of_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_of_printed += 1

        except (TypeError, ValueError):
            continue

    print("")
    return num_of_printed
