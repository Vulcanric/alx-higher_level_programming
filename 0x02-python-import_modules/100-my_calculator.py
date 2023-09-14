#!/usr/bin/python3
"""A program that performs basic calculations with
command line arguments
    Examples:

        $ ./100-my_calculator.py 2 + 3
        2 + 3 = 5

    When passed without or wrong number of arguments
        $ ./100-my_calculator.py
        Usage: ./100-my_calculator.py <a> <operator> <b>
        $ ./100-my_calculator.py 2 +
        Usage: ./100-my_calculator.py <a> <operator> <b>

    When passed with wrong operator
        $ ./100-my_calculator.py 2 H 3
        Unknown operator. Available operators: +, -, * and /
        $

    NOTE: When using the * operator, enclose it within qoutes: '*' or "*"
    So as to avoid the error: Usage: ./100-my_calculator.py <a> <operator> <b>
"""
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b = int(argv[1]), int(argv[3])

    if argv[2] == '+':
        print(f"{a} + {b} =", add(a, b))
    elif argv[2] == '-':
        print(f"{a} - {b} =", sub(a, b))
    elif argv[2] == '*':
        print(f"{a} * {b} =", mul(a, b))
    elif argv[2] == '/':
        print(f"{a} / {b} =", div(a, b))
