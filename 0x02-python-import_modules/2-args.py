#!/usr/bin/python3

from sys import argv

length = len(argv)
numArgs = length - 1

if __name__ == "__main__":
    if numArgs == 0:
        print(f"{numArgs} arguments.")
    elif numArgs == 1:
        print(f"{numArgs} argument:")
    else:
        print(f"{numArgs} arguments:")

    index = 1
    while index < length:
        arg = argv[index]
        print(f"{index}: {arg}")
        index += 1
