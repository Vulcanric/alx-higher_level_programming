#!/usr/bin/python3

from sys import argv, stderr

if len(argv) != 3:
    stderr.write(f"Usage: {argv[0]} num_1 num_2\n")
    exit(1)

num1, num2 = int(argv[1]), int(argv[2])
prod = num1 * num2
print(f"{num1} * {num2} = {prod}")
