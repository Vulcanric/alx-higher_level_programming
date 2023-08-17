#!/usr/bin/python3

# Program that prints the ascii alphabet in reverse order,
# alternating between lowercase and uppercase

ch, i = 0, 90  # ch = 0, i = 90
while (i >= 65):
    if i % 2 == 0:
        ch = i + 32
    else:
        ch = i
    print("{:s}".format(chr(ch)), end='')
    i -= 1
