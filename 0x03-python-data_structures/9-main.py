#!/usr/bin/python3

max_integer = __import__("9-max_integer").max_integer

# List with both positive and negative numbers
my_list = [1, 90, 2, 13, 34, 5, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Empty list
empty_list = []
max_value = max_integer(empty_list)
print("Max: {}".format(max_value))

# List with negative integers
neg_list = [-10, -1, -20, -50, -5, -1024]
max_value = max_integer(neg_list)
print("Max: {}".format(max_value))
