#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_of_print = 0

    for i in range(0, x):
        try:
            print(my_list[i], end="")
            num_of_print += 1
        except IndexError:
            pass

    print("")
    return num_of_print
