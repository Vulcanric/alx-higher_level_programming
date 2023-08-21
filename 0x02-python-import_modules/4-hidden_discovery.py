#!/usr/bin/python3

from hidden_4 import *

if __name__ == "__main__":
    names = dir(hidden_4)  # getting all the names defined in the module
    names.sort()  # Making them to be in alphabetical order
    for name in names:  # Printing the names
        print(name)
