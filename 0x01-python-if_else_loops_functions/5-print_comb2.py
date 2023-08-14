#!/usr/bin/python3

# prints combination of two digits
i = 0
while i <= 99:
    if i != 99:
        print("{:02d},".format(i), end=' ')
    else:
        print("{:02d}".format(i))
    i += 1
