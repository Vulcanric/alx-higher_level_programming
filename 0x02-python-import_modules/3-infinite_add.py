#!/usr/bin/python3

from sys import argv

num_of_args = len(argv)
result = 0
index = 1
while index < num_of_args:
    num = int(argv[index])
    result += num
    index += 1

print(result)
