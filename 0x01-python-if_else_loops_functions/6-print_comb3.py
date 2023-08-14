#!/usr/bin/python3

# Prints all possile different combinations of two-digits numbers
# The numbers are seperated by a ',' comma
# Digits must be different, 01 and 10 are considered the same combination
# two digits '1' and '0'

i = 0
while i < 9:
    j = i + 1
    while j <= 9:
        print("{}{}".format(i, j), end='')
        if i != 8 or j != 9:
            print(", ", end='')
        j += 1
    i += 1
print()
